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
from prime_sdk.credentials import Credentials
from prime_sdk.client import Client
from prime_sdk.services.orders import OrdersService, CreateOrderPreviewRequest
from prime_sdk.enums import OrderSide, OrderType

def main():
    parser = argparse.ArgumentParser(description="Create an order preview")
    parser.add_argument("--product-id", required=True, help="Product ID (e.g., SOL-USD)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", default="MARKET", help="Order type")
    parser.add_argument("--quantity", required=True, help="Base quantity")
    parser.add_argument("--credentials", default="PRIME_CREDENTIALS", 
                       help="Environment variable name for credentials (default: PRIME_CREDENTIALS)")
    args = parser.parse_args()

    credentials = Credentials.from_env(args.credentials)
    client = Client(credentials)
    orders_service = OrdersService(client)

    request = CreateOrderPreviewRequest(
        portfolio_id=credentials.portfolio_id,
        product_id=args.product_id,
        side=args.side,
        type=args.type,
        base_quantity=args.quantity
    )
    try:
        response = orders_service.create_order_preview(request)
        print(response)
    except Exception as e:
        print(f"failed to create order preview: {e}")


if __name__ == "__main__":
    main()
