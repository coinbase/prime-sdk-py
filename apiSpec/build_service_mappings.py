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

"""Helper to derive service model mappings from service.py endpoint paths."""

from __future__ import annotations

import ast
import glob
import re
from pathlib import Path

import yaml
from generate_models import class_name_for_schema

ROOT = Path(__file__).resolve().parents[1]
AUGMENTED_SPEC_PATH = Path(__file__).parent / ".prime-public-api-spec.augmented.yaml"
REF_PATTERN = re.compile(r"^#/components/schemas/(.+)$")
PATH_PARAM_PATTERN = re.compile(r"\{[^}]+\}")


def _normalize_path(path: str) -> str:
    return PATH_PARAM_PATTERN.sub("{param}", path)


def _extract_path_and_method(
    function: ast.FunctionDef,
) -> tuple[str | None, str | None]:
    path_hint = None
    method_hint = None
    for stmt in function.body:
        if isinstance(stmt, ast.Assign):
            for target in stmt.targets:
                if isinstance(target, ast.Name) and target.id == "path":
                    if isinstance(stmt.value, ast.JoinedStr):
                        parts: list[str] = []
                        for value in stmt.value.values:
                            if isinstance(value, ast.Constant):
                                parts.append(str(value.value))
                            elif isinstance(value, ast.FormattedValue):
                                parts.append("{param}")
                        path_hint = "".join(parts)
                    elif isinstance(stmt.value, ast.Constant) and isinstance(
                        stmt.value.value, str
                    ):
                        path_hint = stmt.value.value
    for node in ast.walk(function):
        if not isinstance(node, ast.Call):
            continue
        if (
            isinstance(node.func, ast.Attribute)
            and node.func.attr == "request"
            and node.args
            and isinstance(node.args[0], ast.Constant)
        ):
            method_hint = node.args[0].value
    return method_hint, path_hint


def _response_class(function: ast.FunctionDef) -> str | None:
    if function.returns and isinstance(function.returns, ast.Name):
        return function.returns.id
    for stmt in function.body:
        if isinstance(stmt, ast.Return) and isinstance(stmt.value, ast.Call):
            call = stmt.value
            if (
                isinstance(call.func, ast.Attribute)
                and call.func.attr == "from_response"
                and isinstance(call.func.value, ast.Name)
            ):
                return call.func.value.id
    return None


def build_response_mapping() -> dict[str, str]:
    with AUGMENTED_SPEC_PATH.open(encoding="utf-8") as handle:
        spec = yaml.safe_load(handle)

    ops_by_path: dict[tuple[str, str], dict] = {}
    for path, methods in spec["paths"].items():
        api_path = _normalize_path(path.replace("/v1", ""))
        for method, operation in methods.items():
            if method.lower() in {
                "get",
                "post",
                "put",
                "patch",
                "delete",
            } and isinstance(operation, dict):
                ops_by_path[(method.upper(), api_path)] = operation

    mapping: dict[str, str] = {}
    for service_file in sorted(
        glob.glob(str(ROOT / "prime_sdk/services/*/service.py"))
    ):
        tree = ast.parse(Path(service_file).read_text(encoding="utf-8"))
        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue
            for function in node.body:
                if not isinstance(
                    function, ast.FunctionDef
                ) or function.name.startswith("_"):
                    continue
                response_class = _response_class(function)
                if not response_class:
                    continue
                method_hint, path_hint = _extract_path_and_method(function)
                if not method_hint or not path_hint:
                    continue
                operation = ops_by_path.get((method_hint, _normalize_path(path_hint)))
                if not operation:
                    continue
                response_schema = (
                    operation.get("responses", {})
                    .get("200", {})
                    .get("content", {})
                    .get("application/json", {})
                    .get("schema", {})
                )
                ref = response_schema.get("$ref")
                if not ref:
                    continue
                match = REF_PATTERN.match(ref)
                if not match:
                    continue
                generated_name = class_name_for_schema(match.group(1))
                if generated_name != response_class:
                    mapping[response_class] = generated_name
    return mapping


def _request_class(function: ast.FunctionDef) -> str | None:
    for arg in function.args.args[1:]:
        if arg.annotation and isinstance(arg.annotation, ast.Name):
            return arg.annotation.id
    return None


def build_request_mapping() -> dict[str, str]:
    with AUGMENTED_SPEC_PATH.open(encoding="utf-8") as handle:
        spec = yaml.safe_load(handle)

    ops_by_path: dict[tuple[str, str], dict] = {}
    for path, methods in spec["paths"].items():
        api_path = _normalize_path(path.replace("/v1", ""))
        for method, operation in methods.items():
            if method.lower() in {
                "get",
                "post",
                "put",
                "patch",
                "delete",
            } and isinstance(operation, dict):
                ops_by_path[(method.upper(), api_path)] = operation

    from generate_models import operation_id_to_class_name

    mapping: dict[str, str] = {}
    for service_file in sorted(
        glob.glob(str(ROOT / "prime_sdk/services/*/service.py"))
    ):
        tree = ast.parse(Path(service_file).read_text(encoding="utf-8"))
        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue
            for function in node.body:
                if not isinstance(
                    function, ast.FunctionDef
                ) or function.name.startswith("_"):
                    continue
                request_class = _request_class(function)
                if not request_class:
                    continue
                method_hint, path_hint = _extract_path_and_method(function)
                if not method_hint or not path_hint:
                    continue
                operation = ops_by_path.get((method_hint, _normalize_path(path_hint)))
                if not operation:
                    continue
                operation_id = operation.get("operationId")
                if not operation_id:
                    continue
                generated_name = operation_id_to_class_name(operation_id)
                if generated_name != request_class:
                    mapping[request_class] = generated_name
    return mapping


if __name__ == "__main__":
    print("SERVICE_RESPONSE_BASES = {")
    for service_name, generated_name in sorted(build_response_mapping().items()):
        print(f'    "{service_name}": "{generated_name}",')
    print("}")
    print()
    print("SERVICE_REQUEST_BASES = {")
    for service_name, generated_name in sorted(build_request_mapping().items()):
        print(f'    "{service_name}": "{generated_name}",')
    print("}")
