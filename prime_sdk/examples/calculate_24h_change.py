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
from datetime import datetime, timedelta
from prime_sdk.credentials import Credentials
from prime_sdk.client import Client
from prime_sdk.services.products import ProductsService, GetProductCandlesRequest


def calculate_24h_change(products_service, portfolio_id, product_id):
    """
    Calculate 24-hour price change for a given product.
    Uses single API call with FIVE_MINUTES granularity to get 24 hours of data.
    A more complex version of this script would use two separate API requests.
    
    Args:
        products_service: ProductsService instance
        portfolio_id: The portfolio ID
        product_id: The product to analyze (e.g., "BTC-USD")
    
    Returns:
        dict: Contains current_price, price_24h_ago, change_amount, change_percentage
    """
    # Calculate timestamps (API expects ISO 8601 format)
    current_time = datetime.utcnow()
    past_time = current_time - timedelta(hours=24)

    # Format as ISO 8601 with Z suffix
    start_time_str = past_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    end_time_str = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Get 24 hours of 5-minute candles (288 candles total)
    request = GetProductCandlesRequest(
        portfolio_id=portfolio_id,
        product_id=product_id,
        granularity="FIVE_MINUTES",
        start_time=start_time_str,
        end_time=end_time_str
    )
    
    response = products_service.get_product_candles(request)
    
    if not response.candles or len(response.candles) < 2:
        raise Exception("Insufficient price data available")
        
    price_24h_ago = float(response.candles[0].close)
    current_price = float(response.candles[-1].close)
    
    change_amount = current_price - price_24h_ago
    change_percentage = (change_amount / price_24h_ago) * 100
    
    results = {
        'product_id': product_id,
        'current_price': current_price,
        'price_24h_ago': price_24h_ago,
        'change_amount': change_amount,
        'change_percentage': change_percentage,
        'candles_count': len(response.candles)
    }
    
    print(f"Product: {product_id}")
    print(f"Current Price: ${current_price:,.2f}")
    print(f"Price 24h Ago: ${price_24h_ago:,.2f}")
    print(f"Change Amount: ${change_amount:+,.2f}")
    print(f"Change Percentage: {change_percentage:+.2f}%")
    print(f"Data points: {len(response.candles)} candles")
        
    return results


def main():
    parser = argparse.ArgumentParser(description="Calculate 24-hour price change for a product")
    parser.add_argument("--product-id", nargs='+', required=True, help="Product ID(s) (e.g., BTC-USD or BTC-USD ETH-USD SOL-USD)")
    args = parser.parse_args()

    credentials = Credentials.from_env()
    client = Client(credentials)
    products_service = ProductsService(client)

    products_to_analyze = args.product_id

    for product in products_to_analyze:
        try:
            calculate_24h_change(products_service, credentials.portfolio_id, product)
            print(f"\n{'='*60}")
        except Exception as e:
            print(f"Failed to analyze {product}: {e}")
            print(f"\n{'='*60}")


if __name__ == "__main__":
    main()