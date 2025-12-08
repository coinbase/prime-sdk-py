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

# #docs operationId: PrimeRESTAPI_GetActivity
# #docs operationName: Get Activity

import argparse
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.activities import GetEntityActivityRequest

def main():
    parser = argparse.ArgumentParser(description="Get a specific entity activity by ID")
    parser.add_argument("activity_id", nargs="?", help="Activity ID")
    parser.add_argument("--activity-id", dest="activity_id_named", help="Activity ID")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()

    # Accept activity ID from either positional or named argument
    activity_id = args.activity_id or args.activity_id_named
    if not activity_id:
        print("Error: Activity ID is required. Provide as positional argument or use --activity-id")
        return

    request = GetEntityActivityRequest(
        activity_id=activity_id
    )
    
    try:
        response = client.activities.get_entity_activity(request)
        print(response)
    except Exception as e:
        print(f"failed to get entity activity: {e}")


if __name__ == "__main__":
    main()
