.PHONY: fetch-spec generate update-spec bootstrap-operations lint test install-dev

SPEC_URL ?= https://api.prime.coinbase.com/v1/openapi.yaml
SPEC_FILE := apiSpec/prime-public-api-spec.yaml
PYTHON ?= python3
VENV ?= .venv
VENV_BIN = $(VENV)/bin

fetch-spec:
	@mkdir -p apiSpec
	curl -fsSL "$(SPEC_URL)" -o "$(SPEC_FILE)"

install-dev:
	$(PYTHON) -m venv $(VENV)
	$(VENV_BIN)/pip install -e ".[dev]"

bootstrap-operations: install-dev
	$(VENV_BIN)/python tools/generator/bootstrap_operations.py

generate: install-dev
	$(VENV_BIN)/python tools/generator/generate.py

update-spec: fetch-spec generate

lint: install-dev
	$(VENV_BIN)/ruff format prime_sdk tools/generator
	$(VENV_BIN)/ruff check prime_sdk tools/generator

lint-fix: install-dev
	$(VENV_BIN)/ruff format prime_sdk tools/generator
	$(VENV_BIN)/ruff check --fix prime_sdk tools/generator

test: install-dev
	$(VENV_BIN)/pytest tests/ -v
