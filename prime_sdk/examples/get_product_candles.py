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
from prime_sdk.services.products import ProductsService, GetProductCandlesRequest


def main():
    parser = argparse.ArgumentParser(description="Get product candles data")
    parser.add_argument("--product-id", required=True, help="Product ID (e.g., SOL-USD)")
    parser.add_argument("--granularity", default="ONE_HOUR", 
                       choices=["ONE_MINUTE", "FIVE_MINUTES", "FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS", "ONE_DAY"],
                       help="Granularity for candles (default: ONE_HOUR)")
    parser.add_argument("--start-time", type=int, default=1735768092, help="Start time as Unix timestamp (default: 1735768092)")
    parser.add_argument("--end-time", type=int, default=1736891292, help="End time as Unix timestamp (default: 1736891292)")
    args = parser.parse_args()

    credentials = Credentials.from_env()
    client = Client(credentials)
    products_service = ProductsService(client)

    start_time = args.start_time
    end_time = args.end_time

    request = GetProductCandlesRequest(
        portfolio_id=credentials.portfolio_id,
        product_id=args.product_id,
        granularity=args.granularity,
        start_time=start_time,
        end_time=end_time
    )
    
    try:
        response = products_service.get_product_candles(request)
        print(response)
    except Exception as e:
        print(f"failed to get product candles: {e}")


if __name__ == "__main__":
    main()