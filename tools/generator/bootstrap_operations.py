#!/usr/bin/env python3
"""Bootstrap operations.json from existing hand-written service implementations."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
SERVICES_ROOT = REPO_ROOT / "prime_sdk" / "services"
OUTPUT = Path(__file__).resolve().parent / "config" / "operations.json"


def load_spec_ops() -> dict[tuple[str, str], str]:
    spec_path = REPO_ROOT / "apiSpec" / "prime-public-api-spec.yaml"
    spec = yaml.safe_load(open(spec_path))
    ops: dict[tuple[str, str], str] = {}
    for path, methods in spec.get("paths", {}).items():
        for method, op in methods.items():
            if method in ("get", "post", "put", "patch", "delete") and "operationId" in op:
                norm = path
                if norm.startswith("/v1"):
                    norm = norm[3:]
                elif norm.startswith("/v2"):
                    norm = norm[3:]
                ops[(method.upper(), norm)] = op["operationId"]
                ops[(method.upper(), path)] = op["operationId"]
    return ops


def parse_service_method(body: str) -> dict:
    path_m = re.search(r'path\s*=\s*(f?"[^"]+"|"/[^"]+")', body, re.DOTALL)
    http_m = re.search(r'self\.client\.request\("(\w+)"', body)
    version_m = re.search(r'version="(v\d+)"', body)
    method_body = body.strip()

    path_expr = path_m.group(1) if path_m else ""
    if path_expr.startswith('f"'):
        path_template = path_expr[2:-1]
    elif path_expr.startswith('"'):
        path_template = path_expr[1:-1]
    else:
        path_template = ""

    return {
        "http_method": http_m.group(1) if http_m else "GET",
        "path_template": path_template,
        "api_version": version_m.group(1) if version_m else "v1",
        "method_body": method_body,
    }


def get_request_class(ep_file: Path) -> str | None:
    if not ep_file.exists():
        return None
    content = ep_file.read_text()
    m = re.search(r"class (\w+Request):", content)
    return m.group(1) if m else None


def main() -> int:
    spec_ops = load_spec_ops()
    operations: dict[str, dict] = {}
    missing: list[str] = []

    for domain_dir in sorted(SERVICES_ROOT.iterdir()):
        if not domain_dir.is_dir():
            continue
        service_py = domain_dir / "service.py"
        if not service_py.exists():
            continue

        content = service_py.read_text()
        tree = ast.parse(content)
        method_nodes: list[ast.FunctionDef] = []
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                for item in node.body:
                    if isinstance(item, ast.FunctionDef) and item.name != "__init__":
                        method_nodes.append(item)
        for node in method_nodes:
            if not node.args.args or node.args.args[0].arg != "self":
                continue
            if len(node.args.args) < 2 or node.args.args[1].arg != "request":
                continue

            method_name = node.name
            body_lines = ast.get_source_segment(content, node) or ""
            meta = parse_service_method(body_lines)

            ep_file = domain_dir / f"{method_name}.py"
            req_class = get_request_class(ep_file)
            if not req_class:
                req_class = "".join(w.capitalize() for w in method_name.split("_")) + "Request"

            # Match to spec operationId
            path_for_match = meta["path_template"]
            path_for_match = re.sub(r"\{request\.(\w+)\}", r"{\1}", path_for_match)
            key = (meta["http_method"], path_for_match)
            op_id = spec_ops.get(key)

            if not op_id:
                # try v2 path
                key2 = (meta["http_method"], f"/v2{path_for_match}" if meta["api_version"] == "v2" else path_for_match)
                op_id = spec_ops.get(key2)

            if not op_id:
                missing.append(f"{domain_dir.name}.{method_name}: {meta['http_method']} {path_for_match}")
                continue

            operations[op_id] = {
                "domain": domain_dir.name,
                "method_name": method_name,
                "request_class": req_class,
                "response_class": req_class.replace("Request", "Response"),
                "http_method": meta["http_method"],
                "path_template": meta["path_template"],
                "api_version": meta["api_version"],
            }

    if missing:
        print(f"Warning: {len(missing)} methods could not be matched to spec:", file=sys.stderr)
        for m in missing:
            print(f"  {m}", file=sys.stderr)

    overrides_path = OUTPUT.parent / "operations-overrides.json"
    if overrides_path.exists():
        with open(overrides_path) as f:
            overrides = json.load(f)
        operations.update(overrides)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w") as f:
        json.dump({"operations": operations}, f, indent=2, sort_keys=True)
        f.write("\n")

    print(f"Wrote {len(operations)} operations to {OUTPUT}")
    return 0 if len(operations) >= 100 else 1


if __name__ == "__main__":
    raise SystemExit(main())
