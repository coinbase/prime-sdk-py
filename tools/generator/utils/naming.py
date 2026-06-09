import json
import re
from pathlib import Path


def load_naming_config(config_dir: Path) -> dict:
    with open(config_dir / "naming.json") as f:
        return json.load(f)


def strip_prefixes(name: str, config: dict) -> str:
    result = name
    for old, new in config.get("file_path_replacements", {}).items():
        result = result.replace(old, new)
    for old, new in config.get("content_replacements", {}).items():
        result = result.replace(old, new)
    return result


def to_snake_case(name: str) -> str:
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def to_pascal_case(name: str) -> str:
    return "".join(part.capitalize() for part in name.split("_"))


def should_skip_schema(name: str, config: dict) -> bool:
    for pattern in config.get("skip_schema_patterns", []):
        if re.search(pattern, name):
            return True
    return False


def resolve_enum_name(name: str, config: dict) -> str:
    mappings = config.get("enum_name_mappings", {})
    return mappings.get(name, name)


def resolve_model_name(name: str, config: dict) -> str:
    name = strip_prefixes(name, config)
    common = config.get("common_models", {})
    return common.get(name, name)
