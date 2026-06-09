from __future__ import annotations

import ast
import json
import re
from pathlib import Path

from tools.generator.utils.copyright import apply_copyright


def write_enum_compat(repo_root: Path, config_dir: Path) -> None:
    with open(config_dir / "enum-aliases.json") as f:
        config = json.load(f)

    enums_dir = repo_root / "prime_sdk" / "enums"
    legacy_lines = [
        "from __future__ import annotations\n",
        "\n",
        "from enum import Enum\n",
        "\n",
    ]

    for enum_name, members in config.get("legacy_enums", {}).items():
        legacy_lines.append(f"class {enum_name}(str, Enum):\n")
        for member, value in members.items():
            legacy_lines.append(f"    {member} = {value!r}\n")
        legacy_lines.append("\n")

    (enums_dir / "legacy.py").write_text(apply_copyright("".join(legacy_lines)))

    init_path = enums_dir / "__init__.py"
    init_content = init_path.read_text()
    init_content = re.sub(r"\n# Compatibility aliases\n.*", "", init_content, flags=re.DOTALL)

    alias_lines = ["\n# Compatibility aliases\n"]
    compat_exports: list[str] = []

    for alias, target in config.get("type_aliases", {}).items():
        alias_lines.append(f"from .{target} import {target} as {alias}\n")
        compat_exports.append(alias)

    for enum_name in config.get("legacy_enums", {}).keys():
        alias_lines.append(f"from .legacy import {enum_name}\n")
        compat_exports.append(enum_name)

    tree = ast.parse(init_content)
    all_exports: list[str] = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__all__":
                    all_exports = list(ast.literal_eval(node.value))

    all_exports = sorted(set(all_exports + compat_exports))
    base_init = init_content.split("__all__")[0].rstrip() + "\n"
    init_path.write_text(base_init + "".join(alias_lines) + f"\n__all__ = {all_exports!r}\n")
