# Prime SDK Python Generator

Holistic code generator for `prime-sdk-py`, mirroring the approach used by `prime-sdk-dotnet`.

## Prerequisites

- Python 3.10+
- `make install-dev` (installs `datamodel-code-generator`, `jinja2`, `pyyaml`, `ruff`, `pytest`)

## Usage

```bash
# From repo root
make generate          # Regenerate from committed spec
make update-spec       # Fetch live spec + regenerate
make bootstrap-operations  # Rebuild operations.json from services
```

### Generator CLI

```bash
.venv/bin/python tools/generator/generate.py [--live] [--dry-run] [--models-only] [--skip-models]
```

## Pipeline

1. **Models & enums** — `datamodel-code-generator` + post-processing into `prime_sdk/model/` and `prime_sdk/enums/`
2. **Client surface** — per-endpoint request/response modules and `service.py` classes from `config/operations.json`
3. **Finalize** — regenerate `prime_sdk/__init__.py` and `client_services.py`
4. **Compatibility** — type aliases for legacy import paths (`model.py`, `enums.py` shims)

## Configuration

| File | Purpose |
|------|---------|
| `config/generator-config.json` | Spec paths, datamodel-codegen settings |
| `config/naming.json` | Prefix stripping, enum renames, service class names |
| `config/operations.json` | Maps OpenAPI `operationId` → domain/method (103 operations) |
| `config/operations-overrides.json` | Manual overrides for spec/SDK path mismatches |
| `config/model-aliases.json` | Legacy model name aliases |
| `config/enum-aliases.json` | Legacy enum name aliases |
