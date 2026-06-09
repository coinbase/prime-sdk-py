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

# #docs operationId: PrimeRESTAPI_GetEntityActivities
# #docs operationName: List Entity Activities

import argparse
import os
from datetime import datetime

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.enums import ActivityLevel
from prime_sdk.services.activities import ListEntityActivitiesRequest
from prime_sdk.utils import PaginationParams


def main():
    parser = argparse.ArgumentParser(description="List entity activities")
    parser.add_argument("--entity-id", help="Entity ID (overrides PRIME_ENTITY_ID env var)")
    parser.add_argument(
        "--activity-level",
        choices=[level.value for level in ActivityLevel],
        help="Activity level filter",
    )
    parser.add_argument("--symbols", help="Comma-separated list of symbols to filter")
    parser.add_argument("--categories", help="Comma-separated list of categories to filter")
    parser.add_argument("--statuses", help="Comma-separated list of statuses to filter")
    parser.add_argument("--start-time", help="Start time filter (ISO format: 2025-01-01T00:00:00)")
    parser.add_argument("--end-time", help="End time filter (ISO format: 2025-01-01T00:00:00)")
    parser.add_argument("--limit", type=int, help="Number of results to return")
    parser.add_argument("--cursor", help="Pagination cursor")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    entity_id = args.entity_id or os.getenv("PRIME_ENTITY_ID")

    if not entity_id:
        print("Error: Entity ID is required. Set PRIME_ENTITY_ID env var or use --entity-id")
        return

    # Parse datetime strings if provided
    start_time = None
    end_time = None
    if args.start_time:
        try:
            start_time = datetime.fromisoformat(args.start_time.replace("Z", "+00:00"))
        except ValueError:
            print("Error: Invalid start-time format. Use ISO format like '2025-01-01T00:00:00'")
            return

    if args.end_time:
        try:
            end_time = datetime.fromisoformat(args.end_time.replace("Z", "+00:00"))
        except ValueError:
            print("Error: Invalid end-time format. Use ISO format like '2025-01-01T00:00:00'")
            return

    # Set up pagination if provided
    pagination = None
    if args.limit or args.cursor:
        pagination = PaginationParams(limit=args.limit, cursor=args.cursor)

    # Parse activity level if provided
    activity_level = None
    if args.activity_level:
        activity_level = ActivityLevel(args.activity_level)

    request = ListEntityActivitiesRequest(
        entity_id=entity_id,
        activity_level=activity_level,
        symbols=args.symbols,
        categories=args.categories,
        statuses=args.statuses,
        start_time=start_time,
        end_time=end_time,
        pagination=pagination,
    )

    try:
        response = client.activities.list_entity_activities(request)
        print(response)
    except Exception as e:
        print(f"failed to list entity activities: {e}")


if __name__ == "__main__":
    main()
