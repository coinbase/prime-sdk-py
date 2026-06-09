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

# #docs operationId: PrimeRESTAPI_CreateNetAllocation
# #docs operationName: Create Portfolio Net Allocations

import argparse
import uuid

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.enums import SizeType
from prime_sdk.services.allocations import (
    CreatePortfolioNetAllocationsRequest,
    NetAllocationLeg,
)


def main():
    parser = argparse.ArgumentParser(description="Create portfolio net allocations (netting)")
    parser.add_argument("--source-portfolio-id", required=True, help="Source portfolio ID")
    parser.add_argument("--product-id", required=True, help="Product ID (e.g., BTC-USD)")
    parser.add_argument("--order-ids", required=True, help="Comma-separated list of order IDs")
    parser.add_argument("--destination-portfolio-id", required=True, help="Destination portfolio ID")
    parser.add_argument("--amount", required=True, help="Amount to allocate")
    parser.add_argument(
        "--size-type",
        required=True,
        choices=["BASE", "QUOTE", "PERCENT"],
        help="Size type",
    )
    parser.add_argument("--remainder-destination-portfolio-id", help="Portfolio ID for remainder")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()

    # Parse order IDs
    order_ids = [oid.strip() for oid in args.order_ids.split(",")]

    # Create net allocation leg
    net_allocation_leg = NetAllocationLeg(
        allocation_leg_id=str(uuid.uuid4()),
        destination_portfolio_id=args.destination_portfolio_id,
        amount=args.amount,
    )

    request = CreatePortfolioNetAllocationsRequest(
        allocation_id=str(uuid.uuid4()),
        source_portfolio_id=args.source_portfolio_id,
        product_id=args.product_id,
        order_ids=order_ids,
        allocation_legs=[net_allocation_leg],
        size_type=SizeType(args.size_type),
        remainder_destination_portfolio_id=args.remainder_destination_portfolio_id,
    )

    try:
        response = client.allocations.create_portfolio_net_allocations(request)
        print(response)
    except Exception as e:
        print(f"failed to create portfolio net allocations: {e}")


if __name__ == "__main__":
    main()
