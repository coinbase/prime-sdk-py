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
from prime_sdk.services.orders import OrdersService, AcceptQuoteRequest
from prime_sdk.enums import OrderSide


def main():
    parser = argparse.ArgumentParser(description="Accept a quote to create an order")
    parser.add_argument("--product-id", required=True, help="Product ID (e.g., BTC-USD)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--quote-id", required=True, help="Quote ID from create_quote response")
    parser.add_argument("--settl-currency", help="Settlement currency (optional)")
    args = parser.parse_args()

    credentials = Credentials.from_env()
    client = Client(credentials)
    orders_service = OrdersService(client)

    side = OrderSide.BUY if args.side == "BUY" else OrderSide.SELL

    request = AcceptQuoteRequest(
        portfolio_id=credentials.portfolio_id,
        product_id=args.product_id,
        side=side,
        client_order_id=str(uuid.uuid4()),
        quote_id=args.quote_id,
        settl_currency=args.settl_currency
    )
    
    try:
        response = orders_service.accept_quote(request)
        print(response)
    except Exception as e:
        print(f"failed to accept quote: {e}")


if __name__ == "__main__":
    main()