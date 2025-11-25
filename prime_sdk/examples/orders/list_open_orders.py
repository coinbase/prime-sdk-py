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

# #docs operationId: PrimeRESTAPI_GetOpenOrders
# #docs operationName: List Open Orders

import argparse
import os
from datetime import datetime
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.orders import ListOpenOrdersRequest
from prime_sdk.enums import OrderSide, OrderType

def main():
    parser = argparse.ArgumentParser(description="List open orders for a portfolio")
    parser.add_argument("--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)")
    parser.add_argument("--product-ids", help="Product IDs filter (e.g., BTC-USD,ETH-USD)")
    parser.add_argument("--order-type", choices=[ot.value for ot in OrderType], 
                       help="Order type filter")
    parser.add_argument("--order-side", choices=[os.value for os in OrderSide], 
                       help="Order side filter")
    parser.add_argument("--start-date", help="Start date filter (ISO format: 2025-01-01T00:00:00)")
    parser.add_argument("--end-date", help="End date filter (ISO format: 2025-01-01T23:59:59)")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    
    if not portfolio_id:
        print("Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id")
        return

    # Parse datetime strings if provided
    start_date = None
    end_date = None
    if args.start_date:
        # Strip 'Z' suffix if present and create naive datetime
        date_str = args.start_date.rstrip('Z')
        try:
            start_date = datetime.fromisoformat(date_str)
        except ValueError:
            print(f"Error: Invalid start-date format. Use ISO format like '2025-01-01T00:00:00Z'")
            return

    if args.end_date:
        # Strip 'Z' suffix if present and create naive datetime
        date_str = args.end_date.rstrip('Z')
        try:
            end_date = datetime.fromisoformat(date_str)
        except ValueError:
            print(f"Error: Invalid end-date format. Use ISO format like '2025-01-01T23:59:59Z'")
            return

    # Parse enum values if provided
    order_type = None
    if args.order_type:
        order_type = OrderType(args.order_type)
    
    order_side = None
    if args.order_side:
        order_side = OrderSide(args.order_side)
    
    request = ListOpenOrdersRequest(
        portfolio_id=portfolio_id,
        product_ids=args.product_ids,
        order_type=order_type,
        order_side=order_side,
        start_date=start_date,
        end_date=end_date
    )
    
    try:
        response = client.orders.list_open_orders(request)
        print(response)
    except Exception as e:
        print(f"failed to list open orders: {e}")


if __name__ == "__main__":
    main()
