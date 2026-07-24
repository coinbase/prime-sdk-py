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

# #docs operationId: PrimeRESTAPI_GetPortfolioActivities
# #docs operationName: List Portfolio Activities

import argparse
import os
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.activities import ListActivitiesRequest


def main():
    parser = argparse.ArgumentParser(description="List activities")
    parser.add_argument("--symbols", help="Comma-separated list of symbols to filter")
    parser.add_argument(
        "--categories", help="Comma-separated list of categories to filter"
    )
    parser.add_argument("--statuses", help="Comma-separated list of statuses to filter")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = os.getenv("PRIME_PORTFOLIO_ID")

    request = ListActivitiesRequest(
        portfolio_id=portfolio_id,
        symbols=args.symbols,
        categories=args.categories,
        statuses=args.statuses,
    )
    try:
        response = client.activities.list_activities(request)
        print(response)
    except Exception as e:
        print(f"failed to list activities: {e}")


if __name__ == "__main__":
    main()
