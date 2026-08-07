# Copyright 2026-present Coinbase Global, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Migrate service Request/Response dataclasses to inherit from generated models."""

from __future__ import annotations

import ast
import dataclasses
import glob
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).parent))

from model_config import (
    MANUAL_SERVICE_RESPONSES,
    SERVICE_REQUEST_BASES,
    SERVICE_RESPONSE_BASES,
)

import prime_sdk.generated.models as generated_models

GENERATED_REQUEST_NAMES: set[str] | None = None


def _generated_request_names() -> set[str]:
    global GENERATED_REQUEST_NAMES
    if GENERATED_REQUEST_NAMES is None:
        names: set[str] = set()
        for name in dir(generated_models):
            obj = getattr(generated_models, name)
            if (
                isinstance(obj, type)
                and dataclasses.is_dataclass(obj)
                and name.endswith("Request")
            ):
                names.add(name)
        GENERATED_REQUEST_NAMES = names
    return GENERATED_REQUEST_NAMES


def _generated_field_names(class_name: str) -> set[str]:
    obj = getattr(generated_models, class_name, None)
    if not isinstance(obj, type) or not dataclasses.is_dataclass(obj):
        return set()
    return {field.name for field in dataclasses.fields(obj)}


def _annotation_source(node: ast.AnnAssign) -> str:
    if node.annotation is None:
        return "Any"
    return ast.unparse(node.annotation)


def _default_source(node: ast.AnnAssign) -> str:
    if node.value is None:
        return ""
    return f" = {ast.unparse(node.value)}"


def _field_lines(class_def: ast.ClassDef) -> dict[str, str]:
    lines: dict[str, str] = {}
    for item in class_def.body:
        if isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
            name = item.target.id
            lines[name] = (
                f"    {name}: {_annotation_source(item)}{_default_source(item)}"
            )
    return lines


def _response_base_name(class_name: str) -> str:
    return SERVICE_RESPONSE_BASES.get(class_name, class_name)


def _request_base_name(class_name: str) -> str | None:
    base = SERVICE_REQUEST_BASES.get(class_name, class_name)
    if base in _generated_request_names():
        return base
    return None


def _should_migrate_request(class_name: str) -> bool:
    return _request_base_name(class_name) is not None


def _should_migrate_response(class_name: str) -> bool:
    if class_name in MANUAL_SERVICE_RESPONSES:
        return False
    base = _response_base_name(class_name)
    obj = getattr(generated_models, base, None)
    return isinstance(obj, type) and dataclasses.is_dataclass(obj)


def _is_already_migrated_request(class_def: ast.ClassDef, class_name: str) -> bool:
    base_name = _request_base_name(class_name)
    if base_name is None:
        return False
    for base in class_def.bases:
        if isinstance(base, ast.Name) and base.id == f"_{base_name}":
            return True
    return False


def _render_request_class(class_name: str, field_lines: dict[str, str]) -> str:
    base_name = _request_base_name(class_name)
    assert base_name is not None
    generated_fields = _generated_field_names(base_name)
    kw_only = bool(generated_fields)
    decorator = "@dataclass(kw_only=True)" if kw_only else "@dataclass"
    parts = [
        decorator,
        f"class {class_name}(_{base_name}):",
        f"    __doc__ = _{base_name}.__doc__",
        "",
    ]
    if kw_only:
        extra_fields = [
            field_lines[name]
            for name in field_lines
            if name not in generated_fields and name != "allowed_status_codes"
        ]
        allowed_status = field_lines.get(
            "allowed_status_codes",
            "    allowed_status_codes: list[int] | None = None",
        )
        parts.extend(extra_fields)
        if extra_fields:
            parts.append("")
        parts.append(allowed_status)
    else:
        parts.extend(field_lines.values())
    return "\n".join(parts)


def _render_response_class(class_name: str, field_lines: dict[str, str]) -> str:
    base_name = _response_base_name(class_name)
    generated_fields = _generated_field_names(base_name)
    extra_lines = [
        line for name, line in field_lines.items() if name not in generated_fields
    ]
    parts = [
        "@dataclass",
        f"class {class_name}(BaseResponse, _{base_name}):",
        f"    __doc__ = _{base_name}.__doc__",
    ]
    if extra_lines:
        parts.extend(["", *extra_lines])
    return "\n".join(parts)


def _format_decorator(source: str, decorator: ast.expr) -> str:
    segment = ast.get_source_segment(source, decorator) or ""
    if segment and not segment.startswith("@"):
        return f"@{segment}"
    return segment


def _node_source(source: str, node: ast.AST) -> str:
    if isinstance(node, ast.ClassDef) and node.decorator_list:
        decorators = "\n".join(
            _format_decorator(source, decorator) for decorator in node.decorator_list
        )
        body = ast.get_source_segment(source, node) or ""
        return f"{decorators}\n{body}".strip()
    return (ast.get_source_segment(source, node) or "").strip()


def _manual_response_note(class_name: str) -> str:
    return (
        "Intentionally hand-maintained: diverges from the generated spec model "
        f"for {class_name}."
    )


def migrate_file(path: Path) -> bool:
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    lines = source.splitlines()

    first_import = next(
        (
            index
            for index, line in enumerate(lines)
            if line.startswith(("from ", "import "))
        ),
        len(lines),
    )
    header = "\n".join(lines[:first_import]).rstrip()
    original_imports = [
        line for line in lines[first_import:] if line.startswith(("from ", "import "))
    ]
    body_nodes = [
        node for node in tree.body if not isinstance(node, (ast.Import, ast.ImportFrom))
    ]

    model_imports: set[str] = set()
    rendered_blocks: list[str] = []
    needs_dataclass = False
    needs_base_response = False
    changed = False

    for node in body_nodes:
        if isinstance(node, ast.ClassDef):
            if node.name.endswith("Request") and _should_migrate_request(node.name):
                base_name = _request_base_name(node.name)
                assert base_name is not None
                model_imports.add(base_name)
                if _is_already_migrated_request(node, node.name):
                    rendered = _render_request_class(node.name, _field_lines(node))
                    if rendered != _node_source(source, node).strip():
                        changed = True
                    rendered_blocks.append(rendered)
                else:
                    rendered_blocks.append(
                        _render_request_class(node.name, _field_lines(node))
                    )
                    changed = True
                needs_dataclass = True
                continue
            if node.name.endswith("Response") and _should_migrate_response(node.name):
                base_name = _response_base_name(node.name)
                model_imports.add(base_name)
                rendered_blocks.append(
                    _render_response_class(node.name, _field_lines(node))
                )
                needs_dataclass = True
                needs_base_response = True
                changed = True
                continue
            if node.name.endswith("Response") and node.name in MANUAL_SERVICE_RESPONSES:
                preserved = _node_source(source, node)
                if _manual_response_note(node.name) not in preserved:
                    preserved = (
                        preserved.rstrip()
                        + f"\n\n    # {_manual_response_note(node.name)}"
                    )
                rendered_blocks.append(preserved)
                needs_dataclass = True
                needs_base_response = True
                continue

        segment = _node_source(source, node)
        if segment:
            rendered_blocks.append(segment)
            if isinstance(node, ast.ClassDef):
                needs_dataclass = True
                if node.name.endswith("Response"):
                    needs_base_response = True

    if not changed:
        return False

    import_lines: list[str] = []
    if needs_dataclass:
        import_lines.append("from dataclasses import dataclass")
    if needs_base_response:
        import_lines.append("from ...base_response import BaseResponse")
    for base_name in sorted(model_imports):
        import_lines.append(f"from ...model import {base_name} as _{base_name}")

    model_import_names = {f"_{name}" for name in model_imports}
    skip_until_blank = False
    for line in original_imports:
        if skip_until_blank:
            if line.strip() == "" or line.strip() == ")":
                skip_until_blank = False
            continue
        if line in import_lines:
            continue
        if line == "from dataclasses import dataclass":
            continue
        if line == "from ...base_response import BaseResponse":
            continue
        if line.startswith("from ...model import "):
            if line.rstrip().endswith("("):
                skip_until_blank = True
                continue
            imported = line.removeprefix("from ...model import ").split(" as ")[0]
            imported_names = [part.strip() for part in imported.split(",")]
            if all(name in model_imports for name in imported_names):
                continue
            alias_match = re.search(r" as (_\w+)", line)
            if alias_match and alias_match.group(1) in model_import_names:
                continue
        import_lines.append(line)

    output = header + "\n\n"
    output += "\n".join(import_lines) + "\n\n"
    output += "\n\n".join(rendered_blocks).rstrip() + "\n"
    path.write_text(output, encoding="utf-8")
    return True


def add_manual_response_notes(path: Path) -> bool:
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    updated = False
    for node in tree.body:
        if (
            isinstance(node, ast.ClassDef)
            and node.name in MANUAL_SERVICE_RESPONSES
            and _manual_response_note(node.name) not in source
        ):
            updated = True
            break
    if not updated:
        return False

    lines = source.splitlines()
    new_lines: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        new_lines.append(line)
        if (
            line.startswith("class ")
            and line.split()[1].rstrip(":") in MANUAL_SERVICE_RESPONSES
        ):
            class_name = line.split()[1].rstrip(":")
            block = "\n".join(lines[index:])
            if _manual_response_note(class_name) in block:
                index += 1
                continue
            while index + 1 < len(lines):
                index += 1
                new_lines.append(lines[index])
                if lines[index] and not lines[index].startswith(" "):
                    break
            new_lines.append("")
            new_lines.append(f"    # {_manual_response_note(class_name)}")
        index += 1
    path.write_text("\n".join(new_lines).rstrip() + "\n", encoding="utf-8")
    return True


def main() -> None:
    changed = 0
    for file_path in sorted(glob.glob(str(ROOT / "prime_sdk/services/*/*.py"))):
        path = Path(file_path)
        if path.name in {"__init__.py", "service.py"}:
            continue
        if migrate_file(path):
            changed += 1
            print(f"Migrated {path.relative_to(ROOT)}")
    for class_name in MANUAL_SERVICE_RESPONSES:
        for file_path in glob.glob(str(ROOT / "prime_sdk/services/*/*.py")):
            path = Path(file_path)
            if path.name in {"__init__.py", "service.py"}:
                continue
            source = path.read_text(encoding="utf-8")
            if f"class {class_name}" in source and add_manual_response_notes(path):
                print(f"Annotated manual response in {path.relative_to(ROOT)}")
    print(f"Updated {changed} service files")


if __name__ == "__main__":
    main()
