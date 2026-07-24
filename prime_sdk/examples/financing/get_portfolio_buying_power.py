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

# #docs operationId: PrimeRESTAPI_GetBuyingPower
# #docs operationName: Get Portfolio Buying Power

import argparse
import os

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.financing import GetBuyingPowerRequest


def main():
    parser = argparse.ArgumentParser(
        description="Get portfolio buying power for a currency pair"
    )
    parser.add_argument(
        "--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    parser.add_argument(
        "--base-currency", required=True, help="Base currency (e.g., BTC)"
    )
    parser.add_argument(
        "--quote-currency", required=True, help="Quote currency (e.g., USD)"
    )
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")

    if not portfolio_id:
        print(
            "Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id"
        )
        return

    request = GetBuyingPowerRequest(
        portfolio_id=portfolio_id,
        base_currency=args.base_currency,
        quote_currency=args.quote_currency,
    )

    try:
        response = client.financing.get_portfolio_buying_power(request)
        print(response)
    except Exception as e:
        print(f"failed to get portfolio buying power: {e}")


if __name__ == "__main__":
    main()
