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
from prime_sdk.client_services import CompactLazyPrimeClient
from prime_sdk.services.activities import GetEntityActivityRequest

def main():
    parser = argparse.ArgumentParser(description="Get a specific entity activity by ID")
    parser.add_argument("activity_id", nargs="?", help="Activity ID to retrieve")
    parser.add_argument("--activity-id", required=True, help="Activity ID to retrieve")
    args = parser.parse_args()

    client = CompactLazyPrimeClient.from_env()
    
    activity_id = args.activity_id or getattr(args, 'activity_id_named', None)
    if not activity_id:
        print("Error: Activity ID required as positional or --activity-id")
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
