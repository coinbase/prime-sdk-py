from __future__ import annotations

import json
import re
import shutil
import textwrap
from pathlib import Path

from tools.generator.phases.spec_parser import SpecParser
from tools.generator.utils.copyright import apply_copyright


def _reindent_method(method: str) -> str:
    return textwrap.indent(textwrap.dedent(method), "    ")


def _fix_known_long_lines(content: str) -> str:
    content = content.replace(
        'query_params = f"product_id={request.product_id}&granularity={request.granularity}'
        '&start_time={request.start_time}&end_time={request.end_time}"',
        "query_params = (\n"
        '            f"product_id={request.product_id}&granularity={request.granularity}"\n'
        '            f"&start_time={request.start_time}&end_time={request.end_time}"\n'
        "        )",
    )
    content = content.replace(
        'warn("The \'leg_id\' field is deprecated and will be removed in a future version. '
        'Use \'allocation_leg_id\' instead.", DeprecationWarning)',
        "warn(\n"
        '                "The \'leg_id\' field is deprecated and will be removed in a future "\n'
        '                "version. Use \'allocation_leg_id\' instead.",\n'
        "                DeprecationWarning,\n"
        "            )",
    )
    return content


def _transform_imports(content: str) -> str:
    if "Pagination" in content and "from ...common import Pagination" not in content:
        content = content.replace(
            "from ...model import Pagination",
            "from ...common import Pagination",
        )
    return content


def _load_operations(config_dir: Path) -> dict[str, dict]:
    with open(config_dir / "operations.json") as f:
        return json.load(f)["operations"]


def _validate_operations(spec_path: Path, operations: dict[str, dict]) -> None:
    parser = SpecParser(spec_path)
    spec_ops = {op.operation_id for op in parser.load_operations()}
    mapped = set(operations.keys())
    missing = spec_ops - mapped
    if missing:
        raise ValueError(f"operations.json missing {len(missing)} operations: {sorted(missing)[:5]}...")


def _generate_service_method(op_meta: dict, source_content: str | None) -> str:
    if source_content:
        return source_content

    method_name = op_meta["method_name"]
    req_class = op_meta["request_class"]
    resp_class = op_meta["response_class"]
    http_method = op_meta["http_method"]
    path_template = op_meta["path_template"]
    api_version = op_meta.get("api_version", "v1")

    lines = [f"    def {method_name}(self, request: {req_class}) -> {resp_class}:"]
    lines.append(f'        path = f"{path_template}"')

    has_body = http_method in ("POST", "PUT", "PATCH")
    if has_body:
        lines.append("        body = to_body_dict(request)")
        if api_version != "v1":
            lines.append(
                f'        response = self.client.request("{http_method}", path, body=body, '
                f'version="{api_version}", allowed_status_codes=request.allowed_status_codes)'
            )
        else:
            lines.append(
                f'        response = self.client.request("{http_method}", path, body=body, '
                f"allowed_status_codes=request.allowed_status_codes)"
            )
    else:
        if api_version != "v1":
            lines.append(
                f'        response = self.client.request("{http_method}", path, '
                f'version="{api_version}", allowed_status_codes=request.allowed_status_codes)'
            )
        else:
            lines.append(
                f'        response = self.client.request("{http_method}", path, '
                f"allowed_status_codes=request.allowed_status_codes)"
            )
    lines.append(f"        return {resp_class}.from_response(response.json())")
    return "\n".join(lines)


def run_client_surface_phase(
    spec_path: Path,
    repo_root: Path,
    config_dir: Path,
    naming_config: dict,
    source_services_dir: Path | None = None,
    dry_run: bool = False,
) -> dict[str, list[str]]:
    operations = _load_operations(config_dir)
    _validate_operations(spec_path, operations)

    services_output = repo_root / "prime_sdk" / "services"
    source_services = source_services_dir or services_output
    backup_services = repo_root / "tools" / "generator" / ".source_services_backup"

    if not backup_services.exists() and source_services.exists():
        shutil.copytree(source_services, backup_services)

    if not dry_run:
        if services_output.exists():
            shutil.rmtree(services_output)
        services_output.mkdir(parents=True)

    domains: dict[str, list[dict]] = {}
    for op_id, meta in operations.items():
        domain = meta["domain"]
        domains.setdefault(domain, []).append(meta)

    domain_exports: dict[str, list[str]] = {}

    for domain, ops in sorted(domains.items()):
        domain_dir = services_output / domain
        if not dry_run:
            domain_dir.mkdir(parents=True, exist_ok=True)

        endpoint_exports: list[str] = []
        service_imports: list[str] = []
        method_bodies: list[str] = []

        for meta in sorted(ops, key=lambda x: x["method_name"]):
            method_name = meta["method_name"]
            req_class = meta["request_class"]
            resp_class = meta["response_class"]

            endpoint_exports.extend([req_class, resp_class])
            service_imports.append(f"from .{method_name} import (\n    {req_class},\n    {resp_class}\n)")

            source_ep = backup_services / domain / f"{method_name}.py"
            if source_ep.exists():
                ep_content = _fix_known_long_lines(_transform_imports(source_ep.read_text()))
                if not ep_content.startswith("# Copyright"):
                    ep_content = apply_copyright(ep_content)
            else:
                ep_content = apply_copyright(
                    f"from dataclasses import dataclass\n\n"
                    f"from ...base_response import BaseResponse\n\n\n"
                    f"@dataclass\nclass {req_class}:\n    pass\n\n\n"
                    f"@dataclass\nclass {resp_class}(BaseResponse):\n    pass\n"
                )

            source_svc = backup_services / domain / "service.py"
            method_source = None
            if source_svc.exists():
                svc_content = source_svc.read_text()
                m = re.search(
                    rf"def {method_name}\(self, request:.*?(?=\n    def |\nclass |\Z)",
                    svc_content,
                    re.DOTALL,
                )
                if m:
                    method_source = _reindent_method(m.group(0).rstrip())

            method_bodies.append(_generate_service_method(meta, method_source))

            if not dry_run:
                (domain_dir / f"{method_name}.py").write_text(ep_content)

        service_class = naming_config["domain_to_service_class"][domain]
        needs_asdict = any("asdict(" in b for b in method_bodies)
        asdict_import = "from dataclasses import asdict\n" if needs_asdict else ""
        service_content = _fix_known_long_lines(
            apply_copyright(
                "from ...client import Client\n"
                "from ...utils import append_query_param, append_pagination_params, to_body_dict\n"
                + asdict_import
                + "\n".join(service_imports)
                + f"\n\n\nclass {service_class}:\n"
                "    def __init__(self, client: Client):\n"
                "        self.client = client\n\n" + "\n\n".join(method_bodies) + "\n"
            )
        )

        init_content = apply_copyright(
            f"from .service import {service_class}\n"
            + "\n".join(
                f"from .{meta['method_name']} import {meta['request_class']}, {meta['response_class']}"
                for meta in sorted(ops, key=lambda x: x["method_name"])
            )
            + f"\n\n__all__ = [{service_class!r}, "
            + ", ".join(f"{e!r}" for e in sorted(set(endpoint_exports)))
            + "]\n"
        )

        if not dry_run:
            (domain_dir / "service.py").write_text(service_content)
            (domain_dir / "__init__.py").write_text(init_content)

        domain_exports[domain] = [service_class] + sorted(set(endpoint_exports))

    return domain_exports
