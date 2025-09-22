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

# #docs operationId: PrimeRESTAPI_ListWallets
# #docs operationName: List Wallets

import argparse
import os
from prime_sdk.client_services import CompactLazyPrimeClient
from prime_sdk.services.wallets import ListWalletsRequest
from prime_sdk.enums import WalletType

def main():
    parser = argparse.ArgumentParser(description="List wallets for a portfolio")
    parser.add_argument("--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)")
    parser.add_argument("--type", choices=[wt.value for wt in WalletType], 
                       help="Wallet type filter")
    parser.add_argument("--symbols", help="Comma-separated list of symbols to filter (e.g., BTC,ETH)")
    parser.add_argument("--limit", type=int, help="Number of results to return")
    parser.add_argument("--cursor", help="Pagination cursor")
    args = parser.parse_args()

    client = CompactLazyPrimeClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    
    if not portfolio_id:
        print("Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id")
        return

    # Set up pagination if provided
    pagination = None
    if args.limit or args.cursor:
        from prime_sdk.utils import PaginationParams
        pagination = PaginationParams(
            limit=args.limit,
            cursor=args.cursor
        )

    # Parse wallet type if provided
    wallet_type = None
    if args.type:
        wallet_type = WalletType(args.type)

    # Parse symbols list if provided
    symbols = None
    if args.symbols:
        symbols = [symbol.strip() for symbol in args.symbols.split(',')]
    
    request = ListWalletsRequest(
        portfolio_id=portfolio_id,
        type=wallet_type,
        symbols=symbols,
        pagination=pagination
    )
    
    try:
        response = client.wallets.list_wallets(request)
        print(response)
    except Exception as e:
        print(f"failed to list wallets: {e}")


if __name__ == "__main__":
    main()
