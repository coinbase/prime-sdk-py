from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def run_ruff_fixup(*paths: Path) -> None:
    """Format and auto-fix lint issues in generated output."""
    ruff = Path(sys.executable).parent / "ruff"
    if not ruff.exists():
        return
    targets = [str(path) for path in paths if path.exists()]
    if not targets:
        return
    subprocess.run([str(ruff), "format", *targets], check=False)
    subprocess.run([str(ruff), "check", "--fix", *targets], check=False)
