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

# #docs operationId: PrimeRESTAPI_EditOrder
# #docs operationName: Edit Order (Beta)

import argparse
import os
import uuid

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.orders import EditOrderRequest


def main():
    parser = argparse.ArgumentParser(description="Edit an existing order")
    parser.add_argument(
        "--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    parser.add_argument("--order-id", required=True, help="Order ID to edit")
    parser.add_argument(
        "--orig-client-order-id", required=True, help="Original client order ID"
    )
    parser.add_argument("--base-quantity", help="New base quantity for the order")
    parser.add_argument("--limit-price", help="New limit price")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")

    if not portfolio_id:
        print(
            "Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id"
        )
        return

    request = EditOrderRequest(
        portfolio_id=portfolio_id,
        order_id=args.order_id,
        orig_client_order_id=args.orig_client_order_id,
        client_order_id=str(uuid.uuid4()),
        base_quantity=args.base_quantity,
        limit_price=args.limit_price,
    )

    try:
        response = client.orders.edit_order(request)
        print(response)
    except Exception as e:
        print(f"failed to edit order: {e}")


if __name__ == "__main__":
    main()
