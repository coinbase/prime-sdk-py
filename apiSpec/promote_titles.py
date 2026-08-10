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

"""Promote OpenAPI property titles to descriptions for generated docstrings."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

SOURCE_SPEC_PATH = Path(__file__).parent / "prime-public-api-spec.yaml"
AUGMENTED_SPEC_PATH = Path(__file__).parent / ".prime-public-api-spec.augmented.yaml"

PLACEHOLDER_TITLE_PATTERN = re.compile(r"^\s*next:\s*\d+\s*$", re.IGNORECASE)

SCHEMA_CHILD_KEYS = frozenset(
    {
        "properties",
        "items",
        "allOf",
        "anyOf",
        "oneOf",
        "additionalProperties",
    }
)


def is_promotable_title(title: object) -> bool:
    if not isinstance(title, str):
        return False
    if not title.strip():
        return False
    return PLACEHOLDER_TITLE_PATTERN.match(title) is None


def walk_schema_node(node: object, promoted: dict[str, int]) -> None:
    if not node or not isinstance(node, dict):
        if isinstance(node, list):
            for item in node:
                walk_schema_node(item, promoted)
        return

    properties = node.get("properties")
    if isinstance(properties, dict):
        for property_schema in properties.values():
            if (
                isinstance(property_schema, dict)
                and property_schema.get("title")
                and not property_schema.get("description")
                and is_promotable_title(property_schema["title"])
            ):
                property_schema["description"] = property_schema["title"]
                promoted["count"] += 1
            walk_schema_node(property_schema, promoted)

    if "items" in node:
        walk_schema_node(node["items"], promoted)

    for combinator in ("allOf", "anyOf", "oneOf"):
        if isinstance(node.get(combinator), list):
            for sub_schema in node[combinator]:
                walk_schema_node(sub_schema, promoted)

    additional_properties = node.get("additionalProperties")
    if isinstance(additional_properties, dict):
        walk_schema_node(additional_properties, promoted)

    for key, value in node.items():
        if key in SCHEMA_CHILD_KEYS:
            continue
        walk_schema_node(value, promoted)


def promote_property_titles(spec: dict) -> int:
    promoted: dict[str, int] = {"count": 0}
    walk_schema_node(spec.get("paths"), promoted)
    walk_schema_node(spec.get("components"), promoted)
    return promoted["count"]


def main() -> None:
    with SOURCE_SPEC_PATH.open(encoding="utf-8") as handle:
        spec = yaml.safe_load(handle)

    count = promote_property_titles(spec)

    with AUGMENTED_SPEC_PATH.open("w", encoding="utf-8") as handle:
        yaml.dump(spec, handle, sort_keys=False)

    print(f"Promoted {count} property title(s) to description in {AUGMENTED_SPEC_PATH}")


if __name__ == "__main__":
    main()
