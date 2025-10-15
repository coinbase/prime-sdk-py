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

# #docs operationId: PrimeRESTAPI_GetPortfolioActivity
# #docs operationName: Get Portfolio Activity

import argparse
import os
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.activities import GetActivityRequest

def main():
    parser = argparse.ArgumentParser(description="Get a specific activity by ID")
    parser.add_argument("activity_id", nargs="?", help="Activity ID to retrieve")
    parser.add_argument("--activity-id", required=True, help="Activity ID to retrieve")
    parser.add_argument("--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    
    if not portfolio_id:
        print("Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id")
        return
    
    activity_id = args.activity_id or getattr(args, 'activity_id_named', None)
    if not activity_id:
        print("Error: Activity ID required as positional or --activity-id")
        return

    request = GetActivityRequest(
        portfolio_id=portfolio_id,
        activity_id=activity_id
    )
    
    try:
        response = client.activities.get_activity(request)
        print(response)
    except Exception as e:
        print(f"failed to get activity: {e}")


if __name__ == "__main__":
    main()
