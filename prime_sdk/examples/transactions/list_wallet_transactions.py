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

# #docs operationId: PrimeRESTAPI_GetWalletTransactions
# #docs operationName: List Wallet Transactions

import argparse
import os
from datetime import datetime
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.transactions import ListWalletTransactionsRequest
from prime_sdk.utils import PaginationParams


def main():
    parser = argparse.ArgumentParser(
        description="List transactions for a specific wallet"
    )
    parser.add_argument("wallet_id", nargs="?", help="Wallet ID")
    parser.add_argument("--wallet-id", dest="wallet_id_named", help="Wallet ID")
    parser.add_argument(
        "--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    parser.add_argument(
        "--types", help="Transaction types filter (e.g., DEPOSIT,WITHDRAWAL)"
    )
    parser.add_argument(
        "--start", help="Start time filter (ISO format: 2025-01-01T00:00:00)"
    )
    parser.add_argument(
        "--end", help="End time filter (ISO format: 2025-01-01T23:59:59)"
    )
    parser.add_argument("--limit", type=int, help="Number of results to return")
    parser.add_argument("--cursor", help="Pagination cursor")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")

    if not portfolio_id:
        print(
            "Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id"
        )
        return

    # Accept wallet ID from either positional or named argument
    wallet_id = args.wallet_id or args.wallet_id_named or os.getenv("PRIME_WALLET_ID")
    if not wallet_id:
        print(
            "Error: Wallet ID is required. Provide as positional argument or use --wallet-id"
        )
        return

    # Parse datetime strings if provided
    start_time = None
    end_time = None
    if args.start:
        try:
            start_time = datetime.fromisoformat(args.start.replace("Z", "+00:00"))
        except ValueError:
            print(
                "Error: Invalid start time format. Use ISO format like '2025-01-01T00:00:00'"
            )
            return

    if args.end:
        try:
            end_time = datetime.fromisoformat(args.end.replace("Z", "+00:00"))
        except ValueError:
            print(
                "Error: Invalid end time format. Use ISO format like '2025-01-01T23:59:59'"
            )
            return

    # Set up pagination if provided
    pagination = None
    if args.limit or args.cursor:
        pagination = PaginationParams(limit=args.limit, cursor=args.cursor)

    request = ListWalletTransactionsRequest(
        portfolio_id=portfolio_id,
        wallet_id=wallet_id,
        types=args.types,
        start=start_time,
        end=end_time,
        pagination=pagination,
    )

    try:
        response = client.transactions.list_wallet_transactions(request)
        print(response)
    except Exception as e:
        print(f"failed to list wallet transactions: {e}")


if __name__ == "__main__":
    main()
