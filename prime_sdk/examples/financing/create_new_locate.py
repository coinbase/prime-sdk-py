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

# #docs operationId: PrimeRESTAPI_CreateNewLocate
# #docs operationName: Create New Locate

import argparse
import os
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.financing import CreateNewLocateRequest


def main():
    parser = argparse.ArgumentParser(description="Create a new locate request")
    parser.add_argument("--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)")
    parser.add_argument("--symbol", required=True, help="Currency symbol (e.g., BTC)")
    parser.add_argument("--amount", required=True, help="Amount to locate")
    parser.add_argument("--locate-date", help="Locate date (ISO format)")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")

    if not portfolio_id:
        print("Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id")
        return

    request = CreateNewLocateRequest(
        portfolio_id=portfolio_id,
        symbol=args.symbol,
        amount=args.amount,
        locate_date=args.locate_date
    )

    try:
        response = client.financing.create_new_locate(request)
        print(response)
    except Exception as e:
        print(f"failed to create new locate: {e}")


if __name__ == "__main__":
    main()
