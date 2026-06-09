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

# #docs operationId: PrimeRESTAPI_CancelOrder
# #docs operationName: Cancel Order

import argparse
import os

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.orders import CancelOrderRequest


def main():
    parser = argparse.ArgumentParser(description="Cancel an existing order")
    parser.add_argument("order_id", nargs="?", help="Order ID to cancel")
    parser.add_argument("--order-id", dest="order_id_named", help="Order ID to cancel")
    parser.add_argument("--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")

    if not portfolio_id:
        print("Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id")
        return

    # Accept order ID from either positional or named argument
    order_id = args.order_id or args.order_id_named
    if not order_id:
        print("Error: Order ID is required. Provide as positional argument or use --order-id")
        print("Example: python cancel_order.py abc123")
        print("Example: python cancel_order.py --order-id abc123")
        return

    request = CancelOrderRequest(portfolio_id=portfolio_id, order_id=order_id)

    try:
        response = client.orders.cancel_order(request)
        print(response)
    except Exception as e:
        print(f"failed to cancel order: {e}")


if __name__ == "__main__":
    main()
