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

# #docs operationId: PrimeRESTAPI_GetPortfolioBalances
# #docs operationName: List Portfolio Balances

import argparse
import os

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.enums import BalanceType
from prime_sdk.services.balances import ListPortfolioBalancesRequest


def main():
    parser = argparse.ArgumentParser(description="List balances for a portfolio")
    parser.add_argument(
        "--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    parser.add_argument(
        "--symbols", help="Comma-separated list of symbols to filter (e.g., BTC,ETH)"
    )
    parser.add_argument(
        "--balance-type",
        choices=[bt.value for bt in BalanceType],
        help="Balance type filter",
    )
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")

    if not portfolio_id:
        print(
            "Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id"
        )
        return

    # Parse balance type if provided
    balance_type = None
    if args.balance_type:
        balance_type = BalanceType(args.balance_type)

    request = ListPortfolioBalancesRequest(
        portfolio_id=portfolio_id,
        symbols=args.symbols,
        balance_type=balance_type,
    )

    try:
        response = client.balances.list_portfolio_balances(request)
        print(response)
    except Exception as e:
        print(f"failed to list portfolio balances: {e}")


if __name__ == "__main__":
    main()
