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

# #docs operationId: PrimeRESTAPI_GetExistingLocates
# #docs operationName: List Existing Locates

import argparse
import os

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.financing import ListExistingLocatesRequest


def main():
    parser = argparse.ArgumentParser(description="List existing locate requests for a portfolio")
    parser.add_argument("--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)")
    parser.add_argument("--locate-ids", help="Comma-separated list of locate IDs to filter")
    parser.add_argument("--locate-date", help="Locate date to filter (ISO format)")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")

    if not portfolio_id:
        print("Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id")
        return

    request = ListExistingLocatesRequest(
        portfolio_id=portfolio_id,
        locate_ids=args.locate_ids,
        locate_date=args.locate_date,
    )

    try:
        response = client.financing.list_existing_locates(request)
        print(response)
    except Exception as e:
        print(f"failed to list existing locates: {e}")


if __name__ == "__main__":
    main()
