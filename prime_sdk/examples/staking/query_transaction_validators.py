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

# #docs operationId: PrimeRESTAPI_ListTransactionValidators
# #docs operationName: List Transaction Validators

import argparse

from prime_sdk.client import Client
from prime_sdk.credentials import Credentials
from prime_sdk.services.staking import QueryTransactionValidatorsRequest, StakingService


def main():
    parser = argparse.ArgumentParser(
        description="List ETH 0x02 validators associated with wallet-level stake transactions"
    )
    parser.add_argument(
        "--transaction-ids",
        required=True,
        help="Comma-separated list of transaction IDs (max 100)",
    )
    parser.add_argument("--cursor", help="Pagination cursor")
    parser.add_argument("--limit", type=int, help="Maximum results per page (default 100, max 1000)")
    parser.add_argument(
        "--sort-direction",
        choices=["DESC", "ASC"],
        help="Sort direction (default DESC)",
    )
    args = parser.parse_args()

    credentials = Credentials.from_env()
    client = Client(credentials)
    staking_service = StakingService(client)

    # Parse transaction IDs
    transaction_ids = [tx_id.strip() for tx_id in args.transaction_ids.split(",")]

    if len(transaction_ids) > 100:
        print("Error: Maximum 100 transaction IDs allowed")
        return

    request = QueryTransactionValidatorsRequest(
        portfolio_id=credentials.portfolio_id,
        transaction_ids=transaction_ids,
        cursor=args.cursor,
        limit=args.limit,
        sort_direction=args.sort_direction,
    )

    try:
        response = staking_service.query_transaction_validators(request)
        print(response)
    except Exception as e:
        print(f"failed to list transaction validators: {e}")


if __name__ == "__main__":
    main()
