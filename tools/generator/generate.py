#!/usr/bin/env python3
"""Holistic Prime SDK Python code generator."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = Path(__file__).resolve().parent / "config"
sys.path.insert(0, str(REPO_ROOT))

from tools.generator.phases.client_surface_phase import run_client_surface_phase
from tools.generator.phases.compat_models import write_compat_models
from tools.generator.phases.enum_compat import write_enum_compat
from tools.generator.phases.finalize_phase import run_finalize_phase
from tools.generator.phases.models_phase import run_models_phase
from tools.generator.utils.naming import load_naming_config
from tools.generator.utils.ruff_fixup import run_ruff_fixup


def resolve_spec_path(live: bool, gen_config: dict) -> Path:
    committed = REPO_ROOT / gen_config["committed_spec_path"]
    if live:
        subprocess.run(
            ["make", "fetch-spec"],
            cwd=REPO_ROOT,
            check=True,
        )
        return committed
    if committed.exists():
        return committed
    raise FileNotFoundError(f"Spec not found at {committed}. Run `make fetch-spec` first.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Prime SDK Python surface")
    parser.add_argument("--live", action="store_true", help="Fetch live spec before generating")
    parser.add_argument("--dry-run", action="store_true", help="Validate without writing files")
    parser.add_argument("--models-only", action="store_true", help="Only regenerate models/enums")
    parser.add_argument("--skip-models", action="store_true", help="Skip model generation")
    args = parser.parse_args()

    with open(CONFIG_DIR / "generator-config.json") as f:
        gen_config = json.load(f)
    naming_config = load_naming_config(CONFIG_DIR)

    spec_path = resolve_spec_path(args.live, gen_config)
    print(f"Using spec: {spec_path}")

    if not args.skip_models:
        print("Phase 1: Generating models and enums...")
        run_models_phase(spec_path, REPO_ROOT, gen_config, naming_config, dry_run=args.dry_run)
    if args.models_only:
        if not args.dry_run:
            write_compat_models(REPO_ROOT, CONFIG_DIR, gen_config["models_output"])
            run_ruff_fixup(REPO_ROOT / "prime_sdk")
        return 0

    print("Phase 2: Generating client surface...")
    domain_exports = run_client_surface_phase(
        spec_path,
        REPO_ROOT,
        CONFIG_DIR,
        naming_config,
        dry_run=args.dry_run,
    )

    print("Phase 3: Finalizing package exports...")
    run_finalize_phase(REPO_ROOT, domain_exports, naming_config, dry_run=args.dry_run)

    if not args.skip_models and not args.dry_run:
        print("Phase 4: Writing compatibility aliases...")
        write_compat_models(REPO_ROOT, CONFIG_DIR, gen_config["models_output"])
        write_enum_compat(REPO_ROOT, CONFIG_DIR)

    if not args.dry_run:
        print("Phase 5: Formatting and lint-fixing generated output...")
        run_ruff_fixup(REPO_ROOT / "prime_sdk")

    print("Generation complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
