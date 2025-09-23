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

# #docs operationId: PrimeRESTAPI_GetPortfolioProductCandles
# #docs operationName: Get Product Candles

# TODO: fix the granularity choices

import argparse
import os
from datetime import datetime, timedelta
from prime_sdk.client_services import CompactLazyPrimeClient
from prime_sdk.services.products import GetProductCandlesRequest

def main():
    parser = argparse.ArgumentParser(description="Get candle data for a product")
    parser.add_argument("product_id", nargs="?", help="Product ID (e.g., BTC-USD)")
    parser.add_argument("--product-id", dest="product_id_named", help="Product ID (e.g., BTC-USD)")
    parser.add_argument("--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)")
    parser.add_argument("--granularity", required=True, 
                       choices=["1", "2", "3", "4", "5", "6", "7", "8", "9"], 
                       help="Candle granularity (1=1m, 2=5m, 3=15m, 4=1h, 5=6h, 6=1d, 7=30m, 8=2h, 9=4h)")
    parser.add_argument("--start-time", type=int, 
                       help="Start time as Unix timestamp (defaults to yesterday 9am)")
    parser.add_argument("--end-time", type=int, 
                       help="End time as Unix timestamp (defaults to yesterday 4pm)")
    args = parser.parse_args()

    client = CompactLazyPrimeClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    
    if not portfolio_id:
        print("Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id")
        return

    # Accept product ID from either positional or named argument
    product_id = args.product_id or args.product_id_named
    if not product_id:
        print("Error: Product ID is required. Provide as positional argument or use --product-id")
        return

    # Set default start/end times to yesterday 9am-4pm if not provided
    if args.start_time is None or args.end_time is None:
        # Get yesterday's date
        yesterday = datetime.now() - timedelta(days=1)
        
        # Default start time: yesterday at 9:00 AM
        default_start = yesterday.replace(hour=9, minute=0, second=0, microsecond=0)
        start_time = args.start_time if args.start_time is not None else int(default_start.timestamp())
        
        # Default end time: yesterday at 4:00 PM
        default_end = yesterday.replace(hour=16, minute=0, second=0, microsecond=0)
        end_time = args.end_time if args.end_time is not None else int(default_end.timestamp())
        
        print(f"Using default times: {default_start.strftime('%Y-%m-%d %H:%M')} to {default_end.strftime('%Y-%m-%d %H:%M')}")
    else:
        start_time = args.start_time
        end_time = args.end_time
    
    request = GetProductCandlesRequest(
        portfolio_id=portfolio_id,
        product_id=product_id,
        granularity=args.granularity,
        start_time=start_time,
        end_time=end_time
    )
    
    try:
        response = client.products.get_product_candles(request)
        print(response)
    except Exception as e:
        print(f"failed to get product candles: {e}")


if __name__ == "__main__":
    main()
