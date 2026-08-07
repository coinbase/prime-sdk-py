.PHONY: fetch-spec dev-deps promote-titles gen-models update-spec check-models

# Fetch the Prime API OpenAPI specification
fetch-spec:
	@mkdir -p apiSpec
	curl -o apiSpec/prime-public-api-spec.yaml https://api.prime.coinbase.com/v1/openapi.yaml

dev-deps:
	python3 -m pip install -r requirements-dev.txt

promote-titles:
	python3 apiSpec/promote_titles.py

gen-models: promote-titles
	cd apiSpec && python3 generate_models.py
	ruff format prime_sdk/generated/models.py

update-spec: fetch-spec gen-models

check-models: gen-models
	@git diff --exit-code prime_sdk/generated/models.py
