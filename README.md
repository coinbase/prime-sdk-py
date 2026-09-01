# Prime Python SDK

## Overview

The **Prime Python SDK** is the official Python client for the [Coinbase Prime](https://prime.coinbase.com/) [REST API](https://docs.cdp.coinbase.com/prime/reference). Use it to build production applications that manage portfolios, orders, transfers, staking, financing, and other Prime capabilities from Python.

## Installation

### From PyPI (Recommended)

```bash
pip install prime-sdk-py
```

### From Source

```bash
git clone https://github.com/coinbase/prime-sdk-py.git
cd prime-sdk-py
pip install -e .
```

## Usage

### Setting Up Credentials

To use the *Prime Python SDK*, initialize the [Credentials](prime_sdk/credentials.py) class with your Prime API credentials. This class is designed to facilitate the secure handling of sensitive information required to authenticate API requests.

Ensure that your API credentials are stored securely and are not hard-coded directly in your source code. The Credentials class supports creating credentials from a JSON string or directly from environment variables, providing flexibility and enhancing security.

#### Example Initialization:
```python
from prime_sdk.credentials import Credentials

credentials = Credentials.from_env()
```

#### Environment Variable Format

The SDK supports two formats for credentials configuration:

##### New Format

Set separate environment variables for better security separation:

```bash
export PRIME_CREDENTIALS='{
  "accessKey": "your-access-key",
  "passphrase": "your-passphrase",
  "signingKey": "your-signing-key"
}'

export PRIME_PORTFOLIO_ID="your-portfolio-id"
export PRIME_ENTITY_ID="your-entity-id"
export PRIME_WALLET_ID="your-custody-wallet-id"
export PRIME_ONCHAIN_WALLET_ID="your-web3-onchain-wallet-id"
```

Optional fields: `svcAccountId` in JSON; `PRIME_PORTFOLIO_ID` and `PRIME_ENTITY_ID` for portfolio/entity context.

`PRIME_WALLET_ID` and `PRIME_ONCHAIN_WALLET_ID` are convenience variables for the [example scripts](prime_sdk/examples/). They are not read by the SDK itself. Use `PRIME_WALLET_ID` for standard custody wallet examples (balances, deposits, transfers, staking). Use `PRIME_ONCHAIN_WALLET_ID` for web3/onchain wallet examples (`list_web3_wallet_balances`, `create_onchain_transaction`). Example scripts fall back to these env vars when `--wallet-id` is omitted.

##### Legacy Format (Backwards Compatible)

All credentials in a single environment variable:

```bash
export PRIME_CREDENTIALS='{
  "accessKey": "your-access-key",
  "passphrase": "your-passphrase",
  "signingKey": "your-signing-key", 
  "portfolioId": "your-portfolio-id",
  "svcAccountId": "your-service-account-id",
  "entityId": "your-entity-id"
}'
```

If `PRIME_PORTFOLIO_ID` and/or `PRIME_ENTITY_ID` are set, they override `portfolioId` and `entityId` in the JSON. Only `accessKey`, `passphrase`, and `signingKey` are required in `PRIME_CREDENTIALS`.

### Obtaining API Credentials 

Coinbase Prime API credentials can be created in the Prime web console under Settings -> APIs. While not immediately necessary for most endpoints, your entity ID can be retrieved by calling [List Portfolios](https://docs.cdp.coinbase.com/prime/reference/primerestapi_getportfolios).

### Making API Calls

The SDK is organized into service modules that group related functionality. Each service provides methods for specific API operations.

#### Service-Based Architecture

The SDK uses a service-based architecture where each domain (portfolios, orders, transactions, etc.) has its own service class:

```python
from prime_sdk.credentials import Credentials
from prime_sdk.client import Client
from prime_sdk.exceptions import PrimeAPIError
from prime_sdk.services.portfolios import PortfoliosService, ListPortfoliosRequest

# Initialize credentials and client
credentials = Credentials.from_env("PRIME_CREDENTIALS")
client = Client(credentials)

# Create the service
portfolios_service = PortfoliosService(client)

# Make the API call
request = ListPortfoliosRequest()
try:
    response = portfolios_service.list_portfolios(request)
    print(response)
except PrimeAPIError as e:
    print(f"Failed to list portfolios: {e}")
    print(f"code={e.code} subcode={e.subcode} trace_id={e.trace_id}")
```

API failures raise `PrimeAPIError` (or an HTTP-status subclass such as `PrimeNotFoundError`). The exception includes `status_code`, `message`, and when the API returns a JSON error body, `code`, `subcode`, `trace_id`, and a generated `body` dataclass.

```python
from prime_sdk import PrimeAPIError, PrimeNotFoundError

try:
    response = portfolios_service.list_portfolios(request)
except PrimeNotFoundError as e:
    print(e.trace_id)
except PrimeAPIError as e:
    print(e.status_code, e.message, e.code)
```

A full walkthrough that looks up a missing order (HTTP 404) and optionally submits an invalid create-order request (HTTP 400) lives in [`prime_sdk/examples/advanced/handle_api_errors.py`](prime_sdk/examples/advanced/handle_api_errors.py):

```bash
python prime_sdk/examples/advanced/handle_api_errors.py
python prime_sdk/examples/advanced/handle_api_errors.py --demo-validation
```

#### Available Services

The SDK provides the following services:

- **PortfoliosService** - Portfolio management (`prime_sdk.services.portfolios`)
- **OrdersService** - Order management (`prime_sdk.services.orders`) 
- **TransactionsService** - Transaction operations (`prime_sdk.services.transactions`)
- **WalletsService** - Wallet management (`prime_sdk.services.wallets`)
- **ActivitiesService** - Activity tracking (`prime_sdk.services.activities`)
- **AssetsService** - Asset information (`prime_sdk.services.assets`)
- **BalancesService** - Balance queries (`prime_sdk.services.balances`)
- **UsersService** - User management (`prime_sdk.services.users`)
- **ProductsService** - Product information (`prime_sdk.services.products`)
- **StakingService** - Staking operations (`prime_sdk.services.staking`)

#### Complete Example: Creating a Transfer

```python
from prime_sdk.credentials import Credentials
from prime_sdk.client import Client
from prime_sdk.services.transactions import TransactionsService, CreateTransferRequest


def main():
    # Initialize credentials and client
    credentials = Credentials.from_env("PRIME_CREDENTIALS")
    client = Client(credentials)

    # Create the transactions service
    transactions_service = TransactionsService(client)

    # Create a transfer request
    request = CreateTransferRequest(
        portfolio_id="your-portfolio-id",
        wallet_id="your-wallet-id",
        amount="0.01",
        destination="your-destination-wallet-id",
        currency_symbol="ETH",
        idempotency_key=str(uuid.uuid4()),
    )

    try:
        response = transactions_service.create_transfer(request)
        print(f"Transfer created: {response}")
    except Exception as e:
        print(f"Failed to create transfer: {e}")


if __name__ == "__main__":
    main()
```

## Services Client (Recommended)

For most use cases, we recommend using the **PrimeServicesClient** which provides a more convenient way to access all Prime services through a single client interface. This approach eliminates the need to manually create individual service instances.

### Quick Start with Services Client

```python
from prime_sdk.client_services import PrimeServicesClient

# Create client from environment variables
client = PrimeServicesClient.from_env()

# Access any service directly
portfolios = client.portfolios.list_portfolios(request)
orders = client.orders.create_order(request)
transactions = client.transactions.create_transfer(request)
```

### Complete Example with Services Client

```python
import os
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.transactions import CreateTransferRequest


def main():
    # Create client from environment
    client = PrimeServicesClient.from_env()

    # Create transfer request
    request = CreateTransferRequest(
        portfolio_id="your-portfolio_id",
        wallet_id="your-wallet-id",
        amount="0.01",
        destination="your-destination-wallet-id",
        currency_symbol="USD",
        idempotency_key=str(uuid.uuid4()),
    )

    try:
        # Use the services client - no need to create individual services
        response = client.transactions.create_transfer(request)
        print(f"Transfer created: {response}")
    except Exception as e:
        print(f"Failed to create transfer: {e}")


if __name__ == "__main__":
    main()
```

### Services Client vs Individual Services

**Use Services Client when:**
- Building applications that use multiple Prime services
- You want a simple, unified interface
- You prefer convenience over fine-grained control

**Use Individual Services when:**
- You only need one or two specific services
- You want explicit control over service instantiation
- You're building a minimal application with specific performance requirements

### Supported Versions
The SDK is tested and confirmed to work with Python version 3.7 and newer.

## Local Development

### Making Changes to the SDK

If you need to make modifications to the SDK for your specific use case, follow these steps:

#### 1. Clone and Setup

```bash
git clone https://github.com/coinbase/prime-sdk-py.git
cd prime-sdk-py
```

#### 2. Install in Development Mode

```bash
pip install -e .
```

This installs the SDK in "editable" mode, meaning changes to the source code will be immediately reflected without reinstallation.

#### 3. Running Tests

```bash
# Install development dependencies
make dev-deps

# Run tests
pytest tests/
```

#### 4. Formatting and linting

```bash
make dev-deps
make format      # auto-format all Python code with ruff
make format-check # verify formatting (CI)
make lint        # run ruff check (CI)
make check       # format-check + lint
```

#### 5. Updating the OpenAPI Spec

Models are generated from the Prime OpenAPI specification. To fetch the latest spec and regenerate models:

```bash
make dev-deps
make update-spec
```

Use `make gen-models` to regenerate models from the committed spec without re-fetching from the network. CI uses `make check-models` to verify committed generated output matches the spec.

#### 6. Code Structure

The SDK follows this structure:

```
prime_sdk/
├── credentials.py          # Authentication handling
├── client.py              # HTTP client
├── base_response.py       # Base response classes
├── utils.py               # Utility functions
├── enums.py               # Hand-curated enumerations
├── model.py               # Public model re-exports (backward-compatible)
├── model_manual.py        # Hand-maintained model extensions
├── generated/
│   ├── models.py          # Generated dataclasses from OpenAPI (schemas + request bodies; do not edit)
│   └── errors.py          # Generated API error bodies and route lookup (do not edit)
└── services/              # Service modules
    ├── portfolios/        # Portfolio operations
    ├── orders/            # Order management
    ├── transactions/      # Transaction operations
    ├── wallets/           # Wallet management
    └── ...                # Other services

apiSpec/
├── prime-public-api-spec.yaml
├── promote_titles.py      # Promotes spec titles to descriptions
├── generate_models.py     # Generates prime_sdk/generated/models.py and errors.py
└── model_config.py        # Backward-compatibility aliases and field rules
```

Each service directory contains:
- `service.py` - The main service class with API methods
- Individual request/response modules (e.g., `list_portfolios.py`) whose dataclasses inherit generated model fields and docstrings
- `__init__.py` - Exports for the service

## 🚨 Security and Bug Reports

If you discover a security vulnerability within this SDK, please see our [Security Policy](SECURITY.md) for disclosure information.

## 📧 Contact

- [GitHub Issues](https://github.com/coinbase/prime-sdk-py/issues)

## License

The Prime Python SDK is open source and released under the [Apache License, Version 2.0](LICENSE).
