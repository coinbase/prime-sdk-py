from __future__ import annotations

import ast
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from tools.generator.utils.copyright import apply_copyright
from tools.generator.utils.naming import (
    resolve_enum_name,
    resolve_model_name,
    should_skip_schema,
    strip_prefixes,
)

EXTERNAL_TYPE_REPLACEMENTS = {
    r"api\.ActivityType": "PrimeActivityType",
    r"api_1\.LimitOrderEdit": "OrderEdit",
    r"type_1\.Date": "str",
    r"FcmFuturesSweep_1\.RequestAmount": "SweepAmount",
    r"FuturesSweep_1\.RequestAmount": "SweepAmount",
    r"FcmFuturesSweepStatus": "FuturesSweepStatus",
}

CLASS_NAME_ALIASES = {
    "RequestAmount": "SweepAmount",
    "LimitOrderEdit": "OrderEdit",
}


def _run_datamodel_codegen(spec_path: Path, temp_dir: Path, config: dict) -> list[Path]:
    dmc_bin = Path(sys.executable).parent / "datamodel-codegen"
    cmd = [
        str(dmc_bin),
        "--input",
        str(spec_path),
        "--input-file-type",
        "openapi",
        "--output-model-type",
        config.get("datamodel_codegen", {}).get("output_model_type", "dataclasses.dataclass"),
        "--output",
        str(temp_dir),
        "--use-subclass-enum",
        "--field-constraints",
        "--snake-case-field",
        "--capitalize-enum-members",
        "--strip-default-none",
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    return list(temp_dir.rglob("*.py"))


def _extract_definitions(source: str, source_path: str = "") -> list[tuple[str, str, bool, str]]:
    tree = ast.parse(source)
    definitions: list[tuple[str, str, bool, str]] = []
    lines = source.splitlines(keepends=True)

    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        start = node.lineno - 1
        if node.decorator_list:
            start = node.decorator_list[0].lineno - 1
        end = node.end_lineno or node.lineno
        segment = "".join(lines[start:end])
        is_enum = any(
            (isinstance(base, ast.Name) and base.id == "Enum")
            or (isinstance(base, ast.Attribute) and base.attr == "Enum")
            for base in node.bases
        )
        definitions.append((node.name, segment, is_enum, source_path))
    return definitions


def _resolve_class_name(raw_name: str, source_path: str, naming_config: dict) -> str:
    if raw_name in CLASS_NAME_ALIASES:
        return CLASS_NAME_ALIASES[raw_name]
    if raw_name == "ActivityType":
        if "custody" in source_path:
            return "CustodyActivityType"
        if "public_rest_api" in source_path:
            return "PrimeActivityType"
    return strip_prefixes(raw_name, naming_config)


def _sanitize_content(content: str, naming_config: dict) -> str:
    for old, new in naming_config.get("content_replacements", {}).items():
        content = content.replace(old, new)
    for pattern, replacement in EXTERNAL_TYPE_REPLACEMENTS.items():
        content = re.sub(pattern, replacement, content)
    content = re.sub(r"list\[", "List[", content)
    content = re.sub(r" \| None", " | None", content)
    if "@dataclass" not in content and "class " in content and "(str, Enum)" not in content:
        content = content.replace("class ", "@dataclass(kw_only=True)\nclass ", 1)
    content = content.replace("@dataclass\n", "@dataclass(kw_only=True)\n")
    content = content.replace("@dataclass()", "@dataclass(kw_only=True)")
    return content


def _build_imports(content: str, class_name: str, enum_names: set[str], model_names: set[str]) -> str:
    lines = [
        "from __future__ import annotations\n",
        "\n",
        "from dataclasses import dataclass\n",
    ]
    if "(str, Enum)" in content or "Enum)" in content:
        lines.append("from enum import Enum\n")
    if "List[" in content:
        lines.append("from typing import List\n")
    if "Optional[" in content or "| None" in content:
        lines.append("from typing import Optional\n")
    if "Dict[" in content:
        lines.append("from typing import Dict\n")
    if "Any" in content:
        lines.append("from typing import Any\n")

    type_refs = set(re.findall(r":\s*([A-Z][A-Za-z0-9_]*)", content))
    type_refs.update(re.findall(r"List\[([A-Z][A-Za-z0-9_]*)\]", content))
    type_refs.update(re.findall(r"Optional\[([A-Z][A-Za-z0-9_]*)\]", content))
    skip = {"Optional", "List", "Dict", "Any", "Union", class_name}
    enum_imports = sorted(n for n in enum_names if n in type_refs and n not in skip)
    model_imports = sorted(n for n in model_names if n in type_refs and n not in skip)
    if enum_imports:
        lines.append(f"from ..enums import {', '.join(enum_imports)}\n")
    if model_imports:
        lines.append(f"from . import {', '.join(model_imports)}\n")
    return "".join(lines)


def run_models_phase(
    spec_path: Path,
    repo_root: Path,
    gen_config: dict,
    naming_config: dict,
    dry_run: bool = False,
) -> None:
    models_dir = repo_root / gen_config["models_output"]
    enums_dir = repo_root / gen_config["enums_output"]
    common_dir = repo_root / "prime_sdk" / "common"

    if not dry_run:
        for d in (models_dir, enums_dir, common_dir):
            if d.exists():
                shutil.rmtree(d)
            d.mkdir(parents=True)

    all_definitions: list[tuple[str, str, bool, str]] = []

    with tempfile.TemporaryDirectory() as tmp:
        temp_dir = Path(tmp)
        generated_files = _run_datamodel_codegen(spec_path, temp_dir, gen_config)
        for py_file in generated_files:
            if "google" in str(py_file):
                continue
            source = py_file.read_text()
            all_definitions.extend(_extract_definitions(source, str(py_file)))

    enum_defs: dict[str, str] = {}
    model_defs: dict[str, str] = {}

    for raw_name, content, is_enum, source_path in all_definitions:
        if should_skip_schema(raw_name, naming_config):
            continue
        clean_name = _resolve_class_name(raw_name, source_path, naming_config)
        content = _sanitize_content(content, naming_config)
        content = content.replace(f"class {raw_name}", f"class {clean_name}", 1)

        if is_enum:
            clean_name = resolve_enum_name(clean_name, naming_config)
            enum_defs[clean_name] = content
        else:
            clean_name = resolve_model_name(clean_name, naming_config)
            if clean_name.endswith("Request") or clean_name.endswith("Response"):
                continue
            if clean_name == "Activity":
                content = re.sub(
                    r"type: \w+ \| None = \w+\.\w+",
                    "type: PrimeActivityType | None = PrimeActivityType.OTHER_ACTIVITY_TYPE",
                    content,
                )
                content = re.sub(
                    r"type: \w+ \| None",
                    "type: PrimeActivityType | None",
                    content,
                    count=1,
                )
            model_defs[clean_name] = content

    enum_names = set(enum_defs.keys())
    model_names = set(model_defs.keys())

    enum_exports: list[str] = []
    for name, content in sorted(enum_defs.items()):
        header = _build_imports(content, name, enum_names, model_names)
        file_content = apply_copyright(header + "\n" + content)
        if not dry_run:
            (enums_dir / f"{name}.py").write_text(file_content)
        enum_exports.append(name)

    model_exports: list[str] = []
    for name, content in sorted(model_defs.items()):
        target_dir = common_dir if name == "Pagination" else models_dir
        header = _build_imports(content, name, enum_names, model_names)
        file_content = apply_copyright(header + "\n" + content)
        if not dry_run:
            (target_dir / f"{name}.py").write_text(file_content)
        if name != "Pagination":
            model_exports.append(name)

    if not dry_run:
        enums_init = apply_copyright(
            "\n".join(f"from .{n} import {n}" for n in sorted(enum_exports))
            + f"\n\n__all__ = {sorted(enum_exports)!r}\n"
        )
        (enums_dir / "__init__.py").write_text(enums_init)

        models_init = apply_copyright(
            "\n".join(f"from .{n} import {n}" for n in sorted(model_exports))
            + f"\n\n__all__ = {sorted(model_exports)!r}\n"
        )
        (models_dir / "__init__.py").write_text(models_init)

        if (common_dir / "Pagination.py").exists():
            (common_dir / "__init__.py").write_text(
                apply_copyright("from .Pagination import Pagination\n\n__all__ = ['Pagination']\n")
            )
