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

#docs operationId: PrimeRESTAPI_ListPortfolioAllocations

import argparse
import os
from datetime import datetime
from prime_sdk import CompactLazyPrimeClient
from prime_sdk.services.allocations import ListPortfolioAllocationsRequest
from prime_sdk.enums import OrderSide
from prime_sdk.utils import PaginationParams


def main():
    parser = argparse.ArgumentParser(description="List portfolio allocations")
    parser.add_argument(
        "--portfolio-id",
        help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    parser.add_argument(
        "--start-date",
        required=True,
        help="Start date in ISO format (e.g., 2025-01-01T00:00:00Z)"
    )
    parser.add_argument(
        "--end-date",
        help="End date in ISO format (e.g., 2025-01-02T00:00:00Z)"
    )
    parser.add_argument(
        "--product-ids",
        help="Comma-separated list of product IDs to filter"
    )
    parser.add_argument(
        "--order-side",
        choices=["BUY", "SELL"],
        help="Order side filter"
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Number of results to return"
    )
    parser.add_argument(
        "--cursor",
        help="Pagination cursor"
    )
    
    args = parser.parse_args()
    
    # Get portfolio ID from args or environment
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    if not portfolio_id:
        print("Error: Portfolio ID must be provided via --portfolio-id argument or PRIME_PORTFOLIO_ID environment variable")
        return
    
    # Parse start date
    try:
        if args.start_date.endswith('Z'):
            # Handle UTC format by removing Z and parsing as naive datetime (UTC)
            start_date = datetime.fromisoformat(args.start_date[:-1])
        else:
            start_date = datetime.fromisoformat(args.start_date)
    except ValueError:
        print("Error: Invalid start date format. Use ISO format like 2025-01-01T00:00:00Z")
        return
    
    # Parse end date if provided
    end_date = None
    if args.end_date:
        try:
            if args.end_date.endswith('Z'):
                # Handle UTC format by removing Z and parsing as naive datetime (UTC)
                end_date = datetime.fromisoformat(args.end_date[:-1])
            else:
                end_date = datetime.fromisoformat(args.end_date)
        except ValueError:
            print("Error: Invalid end date format. Use ISO format like 2025-01-02T00:00:00Z")
            return
    
    # Parse product IDs if provided
    product_ids = None
    if args.product_ids:
        product_ids = args.product_ids  # Note: The service expects a string, not a list
    
    # Parse order side if provided
    order_side = None
    if args.order_side:
        order_side = OrderSide(args.order_side)
    
    # Set up pagination if provided
    pagination = None
    if args.limit or args.cursor:
        pagination = PaginationParams(
            limit=args.limit,
            cursor=args.cursor
        )
    
    # Initialize the client
    client = CompactLazyPrimeClient.from_env()
    
    request = ListPortfolioAllocationsRequest(
        portfolio_id=portfolio_id,
        start_date=start_date,
        end_date=end_date,
        product_ids=product_ids,
        order_side=order_side,
        pagination=pagination
    )
    
    try:
        response = client.allocations.list_portfolio_allocations(request)
        print(response)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
