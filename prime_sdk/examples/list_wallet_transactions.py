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

import argparse
from prime_sdk.credentials import Credentials
from prime_sdk.client import Client
from prime_sdk.services.transactions import TransactionsService, ListWalletTransactionsRequest


def main():
    parser = argparse.ArgumentParser(description="List wallet transactions")
    parser.add_argument("--wallet-id", required=True, help="Wallet ID")
    parser.add_argument("--types", help="Transaction types (e.g., DEPOSIT, WITHDRAWAL)")
    parser.add_argument("--credentials", default="PRIME_CREDENTIALS", 
                       help="Environment variable name for credentials (default: PRIME_CREDENTIALS)")
    args = parser.parse_args()

    credentials = Credentials.from_env(args.credentials)
    client = Client(credentials)
    transactions_service = TransactionsService(client)

    request = ListWalletTransactionsRequest(
        portfolio_id=credentials.portfolio_id,
        wallet_id=args.wallet_id,
        types=args.types
    )
    
    try:
        response = transactions_service.list_wallet_transactions(request)
        print(response)
    except Exception as e:
        print(f"failed to list wallet transactions: {e}")


if __name__ == "__main__":
    main()