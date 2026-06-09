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

# #docs operationId: PrimeRESTAPI_GetPortfolioTransactions
# #docs operationName: List Portfolio Transactions

import argparse
import os
from datetime import datetime

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.transactions import ListPortfolioTransactionsRequest
from prime_sdk.utils import PaginationParams


def main():
    parser = argparse.ArgumentParser(description="List transactions for a portfolio")
    parser.add_argument("--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)")
    parser.add_argument("--types", help="Transaction types filter (e.g., DEPOSIT,WITHDRAWAL)")
    parser.add_argument("--symbols", help="Symbols filter (e.g., BTC,ETH,USDC)")
    parser.add_argument("--start", help="Start time filter (ISO format: 2025-01-01T00:00:00)")
    parser.add_argument("--end", help="End time filter (ISO format: 2025-01-01T23:59:59)")
    parser.add_argument("--limit", type=int, help="Number of results to return")
    parser.add_argument("--cursor", help="Pagination cursor")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")

    if not portfolio_id:
        print("Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id")
        return

    # Parse datetime strings if provided
    start_time = None
    end_time = None
    if args.start:
        try:
            start_time = datetime.fromisoformat(args.start.replace("Z", "+00:00"))
        except ValueError:
            print("Error: Invalid start time format. Use ISO format like '2025-01-01T00:00:00'")
            return

    if args.end:
        try:
            end_time = datetime.fromisoformat(args.end.replace("Z", "+00:00"))
        except ValueError:
            print("Error: Invalid end time format. Use ISO format like '2025-01-01T23:59:59'")
            return

    # Set up pagination if provided
    pagination = None
    if args.limit or args.cursor:
        pagination = PaginationParams(limit=args.limit, cursor=args.cursor)

    request = ListPortfolioTransactionsRequest(
        portfolio_id=portfolio_id,
        types=args.types,
        symbols=args.symbols,
        start=start_time,
        end=end_time,
        pagination=pagination,
    )

    try:
        response = client.transactions.list_portfolio_transactions(request)
        print(response)
    except Exception as e:
        print(f"failed to list portfolio transactions: {e}")


if __name__ == "__main__":
    main()
