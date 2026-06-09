from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class Parameter:
    name: str
    location: str
    required: bool
    schema: dict[str, Any]
    description: str = ""


@dataclass
class Operation:
    operation_id: str
    method: str
    path: str
    summary: str = ""
    parameters: list[Parameter] = field(default_factory=list)
    request_body_schema: dict[str, Any] | None = None
    response_schema: dict[str, Any] | None = None
    tags: list[str] = field(default_factory=list)


class SpecParser:
    def __init__(self, spec_path: Path):
        with open(spec_path) as f:
            self.spec = yaml.safe_load(f)
        self.schemas = self.spec.get("components", {}).get("schemas", {})

    def load_operations(self) -> list[Operation]:
        operations: list[Operation] = []
        for path, methods in self.spec.get("paths", {}).items():
            for method, op in methods.items():
                if method not in ("get", "post", "put", "patch", "delete"):
                    continue
                if "operationId" not in op:
                    continue
                params = []
                for p in op.get("parameters", []):
                    params.append(
                        Parameter(
                            name=p["name"],
                            location=p["in"],
                            required=p.get("required", False),
                            schema=p.get("schema", {}),
                            description=p.get("description", ""),
                        )
                    )
                request_body_schema = None
                if "requestBody" in op:
                    content = op["requestBody"].get("content", {})
                    json_content = content.get("application/json", {})
                    if "schema" in json_content:
                        request_body_schema = self._resolve_schema(json_content["schema"])

                response_schema = None
                responses = op.get("responses", {})
                for code in ("200", "201", "default"):
                    if code in responses:
                        content = responses[code].get("content", {})
                        json_content = content.get("application/json", {})
                        if "schema" in json_content:
                            response_schema = self._resolve_schema(json_content["schema"])
                            break

                operations.append(
                    Operation(
                        operation_id=op["operationId"],
                        method=method.upper(),
                        path=path,
                        summary=op.get("summary", ""),
                        parameters=params,
                        request_body_schema=request_body_schema,
                        response_schema=response_schema,
                        tags=op.get("tags", []),
                    )
                )
        return operations

    def _resolve_schema(self, schema: dict[str, Any]) -> dict[str, Any]:
        if "$ref" in schema:
            ref = schema["$ref"]
            schema_name = ref.split("/")[-1]
            resolved = dict(self.schemas.get(schema_name, {}))
            resolved["__ref_name__"] = schema_name
            return resolved
        return schema

    def get_schema(self, name: str) -> dict[str, Any]:
        return self.schemas.get(name, {})
