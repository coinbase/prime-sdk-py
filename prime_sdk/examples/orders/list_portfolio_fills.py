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

# #docs operationId: PrimeRESTAPI_GetPortfolioFills
# #docs operationName: List Portfolio Fills

import argparse
import os
from prime_sdk.client_services import CompactLazyPrimeClient
from prime_sdk.services.orders import ListPortfolioFillsRequest

def main():
    parser = argparse.ArgumentParser(description="List fills for a portfolio")
    parser.add_argument("--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)")
    parser.add_argument("--start-date", required=True, help="Start date (ISO format: 2025-01-01T00:00:00, timezone Z will be added automatically)")
    parser.add_argument("--end-date", help="End date (ISO format: 2025-01-01T23:59:59, timezone Z will be added automatically)")
    parser.add_argument("--limit", type=int, help="Number of results to return")
    parser.add_argument("--cursor", help="Pagination cursor")
    args = parser.parse_args()

    client = CompactLazyPrimeClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    
    if not portfolio_id:
        print("Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id")
        return

    # Format dates with timezone information (API expects RFC3339 format)
    start_date = args.start_date
    if not start_date.endswith('Z') and not start_date.endswith('+00:00'):
        start_date = start_date + 'Z'
    
    end_date = args.end_date
    if end_date and not end_date.endswith('Z') and not end_date.endswith('+00:00'):
        end_date = end_date + 'Z'

    # Set up pagination if provided
    pagination = None
    if args.limit or args.cursor:
        from prime_sdk.utils import PaginationParams
        pagination = PaginationParams(
            limit=args.limit,
            cursor=args.cursor
        )
    
    request = ListPortfolioFillsRequest(
        portfolio_id=portfolio_id,
        start_date=start_date,
        end_date=end_date,
        pagination=pagination
    )
    
    try:
        response = client.orders.list_portfolio_fills(request)
        print(response)
    except Exception as e:
        print(f"failed to list portfolio fills: {e}")


if __name__ == "__main__":
    main()
