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

# #docs operationId: PrimeRESTAPI_ListEntityBalances
# #docs operationName: List Entity Balances

import argparse
import os
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.balances import ListEntityBalancesRequest
from prime_sdk.enums import AggregationType
from prime_sdk.utils import PaginationParams


def main():
    parser = argparse.ArgumentParser(description="List balances for an entity")
    parser.add_argument(
        "--entity-id", help="Entity ID (overrides PRIME_ENTITY_ID env var)"
    )
    parser.add_argument(
        "--symbols", help="Comma-separated list of symbols to filter (e.g., BTC,ETH)"
    )
    parser.add_argument(
        "--aggregation-type",
        choices=[agg.value for agg in AggregationType],
        help="Aggregation type for balances",
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

    # Parse aggregation type if provided
    aggregation_type = None
    if args.aggregation_type:
        aggregation_type = AggregationType(args.aggregation_type)

    # Parse symbols list if provided
    symbols = None
    if args.symbols:
        symbols = [symbol.strip() for symbol in args.symbols.split(",")]

    request = ListEntityBalancesRequest(
        entity_id=entity_id,
        symbols=symbols,
        aggregation_type=aggregation_type,
        pagination=pagination,
    )

    try:
        response = client.balances.list_entity_balances(request)
        print(response)
    except Exception as e:
        print(f"failed to list entity balances: {e}")


if __name__ == "__main__":
    main()
