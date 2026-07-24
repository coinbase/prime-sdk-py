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

# #docs operationId: PrimeRESTAPI_AcceptQuote
# #docs operationName: Accept Quote

import argparse
import os
import uuid
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.orders import AcceptQuoteRequest
from prime_sdk.enums import OrderSide


def main():
    parser = argparse.ArgumentParser(description="Accept a quote and create an order")
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
    parser.add_argument("--quote-id", required=True, help="Quote ID to accept")
    parser.add_argument("--settl-currency", help="Settlement currency")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")

    if not portfolio_id:
        print(
            "Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id"
        )
        return

    request = AcceptQuoteRequest(
        portfolio_id=portfolio_id,
        product_id=args.product_id,
        side=OrderSide(args.side),
        client_order_id=str(uuid.uuid4()),
        quote_id=args.quote_id,
        settl_currency=args.settl_currency,
    )

    try:
        response = client.orders.accept_quote(request)
        print(response)
    except Exception as e:
        print(f"failed to accept quote: {e}")


if __name__ == "__main__":
    main()
