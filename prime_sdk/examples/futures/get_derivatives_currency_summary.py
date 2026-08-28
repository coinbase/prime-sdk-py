# Copyright 2026-present Coinbase Global, Inc.
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

# #docs operationId: PrimeRESTAPI_GetDerivativesCurrencySummary
# #docs operationName: Get Portfolio Derivatives Currency Summary

import argparse
import os

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.futures import GetDerivativesCurrencySummaryRequest


def main():
    parser = argparse.ArgumentParser(
        description="Get portfolio derivatives currency summary"
    )
    parser.add_argument(
        "--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")

    if not portfolio_id:
        print(
            "Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id"
        )
        return

    request = GetDerivativesCurrencySummaryRequest(portfolio_id=portfolio_id)

    try:
        response = client.futures.get_derivatives_currency_summary(request)
        print(response)
    except Exception as e:
        print(f"failed to get derivatives currency summary: {e}")


if __name__ == "__main__":
    main()
