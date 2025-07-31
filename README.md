# Prime Python SDK README

## Overview

The *Prime Python SDK* is a sample library that demonstrates the usage of the [Coinbase Prime](https://prime.coinbase.com/) API via its [REST APIs](https://docs.cdp.coinbase.com/prime/reference). This SDK provides a structured way to integrate Coinbase Prime functionalities into your Python applications.

## Installation

### From PyPI (Recommended)

```bash
pip install prime-sdk-py
```

### From Source

```bash
git clone https://github.com/coinbase-samples/prime-sdk-py.git
cd prime-sdk-py
pip install -e .
```

## License

The *Prime Python SDK* sample library is free and open source and released under the [Apache License, Version 2.0](LICENSE).

The application and code are only available for demonstration purposes.

## Usage

### Setting Up Credentials

To use the *Prime Python SDK*, initialize the [Credentials](prime_sdk/credentials.py) class with your Prime API credentials. This class is designed to facilitate the secure handling of sensitive information required to authenticate API requests.

Ensure that your API credentials are stored securely and are not hard-coded directly in your source code. The Credentials class supports creating credentials from a JSON string or directly from environment variables, providing flexibility and enhancing security.

#### Example Initialization:
```python
from prime_sdk.credentials import Credentials

credentials = Credentials.from_env("PRIME_CREDENTIALS")
```

#### Environment Variable Format: 

The JSON format expected for `PRIME_CREDENTIALS` is:

```
{
  "accessKey": "",
  "passphrase": "",
  "signingKey": "",
  "portfolioId": "",
  "svcAccountId": "",
  "entityId": ""
}
```

### Obtaining API Credentials 

Coinbase Prime API credentials can be created in the Prime web console under Settings -> APIs. While not immediately necessary for most endpoints, your entity ID can be retrieved by calling [List Portfolios](https://docs.cdp.coinbase.com/prime/reference/primerestapi_getportfolios).

### Making API Calls

The SDK is organized into service modules that group related functionality. Each service provides methods for specific API operations.

#### Service-Based Architecture

The SDK uses a service-based architecture where each domain (portfolios, orders, transactions, etc.) has its own service class:

```python
from prime_sdk.credentials import Credentials
from prime_sdk.client import Client
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
except Exception as e:
    print(f"Failed to list portfolios: {e}")
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
from prime_sdk.services.transactions import (
    TransactionsService, 
    CreateTransferRequest
)

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
        amount="100.00",
        destination="TRADING",
        currency_symbol="USD",
        idempotency_key="uuid"
    )
    
    try:
        response = transactions_service.create_transfer(request)
        print(f"Transfer created: {response}")
    except Exception as e:
        print(f"Failed to create transfer: {e}")

if __name__ == "__main__":
    main()
```

### Supported Versions
The SDK is tested and confirmed to work with Python version 3.7 and newer.

## Local Development

### Making Changes to the SDK

If you need to make modifications to the SDK for your specific use case, follow these steps:

#### 1. Clone and Setup

```bash
git clone https://github.com/coinbase-samples/prime-sdk-py.git
cd prime-sdk-py
```

#### 2. Install in Development Mode

```bash
pip install -e .
```

This installs the SDK in "editable" mode, meaning changes to the source code will be immediately reflected without reinstallation.

#### 3. Running Tests

```bash
# Install test dependencies
pip install pytest

# Run tests
pytest tests/
```

#### 4. Code Structure

The SDK follows this structure:

```
prime_sdk/
├── credentials.py          # Authentication handling
├── client.py              # HTTP client
├── base_response.py       # Base response classes
├── utils.py               # Utility functions
├── enums.py               # Common enumerations
└── services/              # Service modules
    ├── portfolios/        # Portfolio operations
    ├── orders/            # Order management
    ├── transactions/      # Transaction operations
    ├── wallets/           # Wallet management
    └── ...                # Other services
```

Each service directory contains:
- `service.py` - The main service class with API methods
- Individual request/response modules (e.g., `list_portfolios.py`)
- `__init__.py` - Exports for the service