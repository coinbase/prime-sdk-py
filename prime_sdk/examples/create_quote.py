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
import uuid
from prime_sdk.credentials import Credentials
from prime_sdk.client import Client
from prime_sdk.services.orders import OrdersService, CreateQuoteRequest
from prime_sdk.enums import OrderSide


def main():
    parser = argparse.ArgumentParser(description="Create a quote for a product")
    parser.add_argument("--product-id", required=True, help="Product ID (e.g., BTC-USD)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--limit-price", required=True, help="Limit price for the quote")
    parser.add_argument("--base-quantity", help="Base quantity (e.g., amount of BTC)")
    parser.add_argument("--quote-value", help="Quote value (e.g., USD amount)")
    parser.add_argument("--settl-currency", help="Settlement currency (optional)")
    parser.add_argument("--credentials", default="PRIME_CREDENTIALS", 
                       help="Environment variable name for credentials (default: PRIME_CREDENTIALS)")
    args = parser.parse_args()

    # Validate that either base_quantity or quote_value is provided
    if not args.base_quantity and not args.quote_value:
        print("Error: Either --base-quantity or --quote-value must be provided")
        return
    
    if args.base_quantity and args.quote_value:
        print("Error: Provide either --base-quantity or --quote-value, not both")
        return

    credentials = Credentials.from_env(args.credentials)
    client = Client(credentials)
    orders_service = OrdersService(client)

    # Convert side string to enum
    side = OrderSide.BUY if args.side == "BUY" else OrderSide.SELL

    request = CreateQuoteRequest(
        portfolio_id=credentials.portfolio_id,
        product_id=args.product_id,
        side=side,
        client_quote_id=str(uuid.uuid4()),
        limit_price=args.limit_price,
        base_quantity=args.base_quantity,
        quote_value=args.quote_value,
        settl_currency=args.settl_currency
    )
    
    try:
        response = orders_service.create_quote(request)
        print(response)
    except Exception as e:
        print(f"failed to create quote: {e}")


if __name__ == "__main__":
    main()