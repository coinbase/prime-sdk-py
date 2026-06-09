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

# #docs operationId: PrimeRESTAPI_ListWeb3WalletBalances
# #docs operationName: List Web3 Wallet Balances

import argparse
import os

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.balances import ListWeb3WalletBalancesRequest
from prime_sdk.utils import PaginationParams


def main():
    parser = argparse.ArgumentParser(description="List Web3 balances for a wallet")
    parser.add_argument("--wallet-id", required=True, help="Wallet ID")
    parser.add_argument("--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)")
    parser.add_argument("--visibility-statuses", help="Comma-separated list of visibility statuses")
    parser.add_argument("--limit", type=int, help="Number of results to return")
    parser.add_argument("--cursor", help="Pagination cursor")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")

    if not portfolio_id:
        print("Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id")
        return

    # Set up pagination if provided
    pagination = None
    if args.limit or args.cursor:
        pagination = PaginationParams(limit=args.limit, cursor=args.cursor)

    request = ListWeb3WalletBalancesRequest(
        portfolio_id=portfolio_id,
        wallet_id=args.wallet_id,
        visibility_statuses=args.visibility_statuses,
        pagination=pagination,
    )

    try:
        response = client.balances.list_web3_wallet_balances(request)
        print(response)
    except Exception as e:
        print(f"failed to list web3 wallet balances: {e}")


if __name__ == "__main__":
    main()
