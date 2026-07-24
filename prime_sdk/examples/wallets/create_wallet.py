# Copyright 2025-present Coinbase Global, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# #docs operationId: PrimeRESTAPI_CreateWallet
# #docs operationName: Create Wallet

import argparse
import os
import uuid
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.wallets import CreateWalletRequest
from prime_sdk.enums import WalletType


def main():
    parser = argparse.ArgumentParser(description="Create a new wallet for a portfolio")
    parser.add_argument(
        "--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    parser.add_argument("--name", required=True, help="Wallet name")
    parser.add_argument(
        "--symbol", required=True, help="Currency symbol (e.g., BTC, ETH)"
    )
    parser.add_argument(
        "--wallet-type",
        choices=["VAULT", "TRADING", "ONCHAIN", "OTHER"],
        required=True,
        help="Wallet type",
    )
    parser.add_argument(
        "--idempotency-key", help="Idempotency key (auto-generated if not provided)"
    )
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()

    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    if not portfolio_id:
        print(
            "Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id"
        )
        return

    # Generate idempotency key if not provided
    idempotency_key = args.idempotency_key or str(uuid.uuid4())

    # Convert wallet type string to enum
    wallet_type = WalletType(args.wallet_type)

    request = CreateWalletRequest(
        portfolio_id=portfolio_id,
        name=args.name,
        symbol=args.symbol,
        idempotency_key=idempotency_key,
        wallet_type=wallet_type,
    )

    try:
        response = client.wallets.create_wallet(request)
        print(response)
    except Exception as e:
        print(f"failed to create wallet: {e}")


if __name__ == "__main__":
    main()
