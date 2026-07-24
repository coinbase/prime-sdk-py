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

# #docs operationId: PrimeRESTAPI_ListAggregateEntityPositions
# #docs operationName: List Aggregate Entity Positions

import argparse
import os
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.positions import ListAggregateEntityPositionsRequest
from prime_sdk.utils import PaginationParams


def main():
    parser = argparse.ArgumentParser(
        description="List aggregate positions for an entity"
    )
    parser.add_argument(
        "--entity-id", help="Entity ID (overrides PRIME_ENTITY_ID env var)"
    )
    parser.add_argument("--limit", type=int, help="Number of results to return")
    parser.add_argument("--cursor", help="Pagination cursor")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()

    entity_id = args.entity_id or os.getenv("PRIME_ENTITY_ID")
    if not entity_id:
        print(
            "Error: Entity ID is required. Set PRIME_ENTITY_ID env var or use --entity-id"
        )
        return

    # Set up pagination if provided
    pagination = None
    if args.limit or args.cursor:
        pagination = PaginationParams(limit=args.limit, cursor=args.cursor)

    request = ListAggregateEntityPositionsRequest(
        entity_id=entity_id, pagination=pagination
    )

    try:
        response = client.positions.list_aggregate_entity_positions(request)
        print(response)
    except Exception as e:
        print(f"failed to list aggregate entity positions: {e}")


if __name__ == "__main__":
    main()
