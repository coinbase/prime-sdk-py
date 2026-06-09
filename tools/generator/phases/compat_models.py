from __future__ import annotations

import ast
import json
import re
from pathlib import Path

from tools.generator.utils.copyright import apply_copyright


def write_compat_models(repo_root: Path, config_dir: Path, models_output: str = "prime_sdk/model") -> list[str]:
    with open(config_dir / "model-aliases.json") as f:
        config = json.load(f)

    models_dir = repo_root / models_output
    compat_exports: list[str] = []

    import_lines: list[str] = []
    class_lines: list[str] = []

    for model_name, spec in config.get("compat_models", {}).items():
        for imp in spec.get("imports", []):
            line = imp + "\n"
            if line not in import_lines:
                import_lines.append(line)
        class_lines.append("@dataclass(kw_only=True)\n")
        class_lines.append(f"class {model_name}:\n")
        for field_name, field_type in spec["fields"].items():
            class_lines.append(f"    {field_name}: {field_type}\n")
        class_lines.append("\n")
        compat_exports.append(model_name)

    lines = [
        "from __future__ import annotations\n",
        "\n",
        "from dataclasses import dataclass\n",
    ]
    lines.extend(import_lines)
    lines.append("\n")
    lines.extend(class_lines)

    (models_dir / "compat.py").write_text(apply_copyright("".join(lines)))

    init_path = models_dir / "__init__.py"
    init_content = init_path.read_text()

    # Strip prior compatibility section if re-running
    init_content = re.sub(r"\n# Compatibility aliases\n.*", "", init_content, flags=re.DOTALL)

    alias_lines = ["\n# Compatibility aliases\n"]
    for alias, target in config.get("type_aliases", {}).items():
        alias_lines.append(f"from .{target} import {target} as {alias}\n")
        compat_exports.append(alias)

    for model_name in config.get("compat_models", {}).keys():
        alias_lines.append(f"from .compat import {model_name}\n")

    tree = ast.parse(init_content)
    all_exports: list[str] = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__all__":
                    all_exports = list(ast.literal_eval(node.value))

    all_exports = sorted(set(all_exports + compat_exports))
    base_init = init_content.split("__all__")[0].rstrip() + "\n"
    new_init = base_init + "".join(alias_lines) + f"\n__all__ = {all_exports!r}\n"
    init_path.write_text(new_init)

    return compat_exports
