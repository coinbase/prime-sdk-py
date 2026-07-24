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

# #docs operationId: PrimeRESTAPI_CreateOrder
# #docs operationName: Create Order

import argparse
import os
import uuid
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.orders import CreateOrderRequest
from prime_sdk.enums import OrderSide, OrderType


def main():
    parser = argparse.ArgumentParser(description="Create a new order")
    parser.add_argument(
        "--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    parser.add_argument(
        "--product-id", required=True, help="Product ID (e.g., BTC-USD, ETH-USD)"
    )
    parser.add_argument(
        "--side",
        required=True,
        choices=[side.value for side in OrderSide],
        help="Order side",
    )
    parser.add_argument(
        "--type",
        choices=[ot.value for ot in OrderType],
        default="MARKET",
        help="Order type (default: MARKET)",
    )
    parser.add_argument("--base-quantity", help="Base quantity for the order")
    parser.add_argument("--quote-value", help="Quote value for the order")
    parser.add_argument("--limit-price", help="Limit price (required for LIMIT orders)")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")

    if not portfolio_id:
        print(
            "Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id"
        )
        return

    # Validate required quantity/value
    if not args.base_quantity and not args.quote_value:
        print("Error: Either --base-quantity or --quote-value is required")
        return

    # Validate limit price for LIMIT orders
    if OrderType(args.type) == OrderType.LIMIT and not args.limit_price:
        print("Error: --limit-price is required for LIMIT orders")
        return

    request = CreateOrderRequest(
        portfolio_id=portfolio_id,
        product_id=args.product_id,
        side=OrderSide(args.side),
        type=OrderType(args.type),
        client_order_id=str(uuid.uuid4()),
        base_quantity=args.base_quantity,
        quote_value=args.quote_value,
        limit_price=args.limit_price,
    )

    try:
        response = client.orders.create_order(request)
        print(response)
    except Exception as e:
        print(f"failed to create order: {e}")


if __name__ == "__main__":
    main()
