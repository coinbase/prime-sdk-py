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

# #docs operationId: PrimeRESTAPI_GetAllocation
# #docs operationName: Get Allocation By ID

import argparse
import os
from prime_sdk import CompactLazyPrimeClient
from prime_sdk.services.allocations import GetAllocationByIdRequest


def main():
    parser = argparse.ArgumentParser(description="Get allocation by ID")
    parser.add_argument(
        "allocation_id",
        nargs="?",
        help="Allocation ID"
    )
    parser.add_argument(
        "--portfolio-id",
        help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    parser.add_argument(
        "--allocation-id",
        dest="allocation_id_named",
        help="Allocation ID"
    )
    
    args = parser.parse_args()
    
    # Get portfolio ID from args or environment
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    if not portfolio_id:
        print("Error: Portfolio ID must be provided via --portfolio-id argument or PRIME_PORTFOLIO_ID environment variable")
        return
    
    # Get allocation ID from positional argument or named argument
    allocation_id = args.allocation_id or args.allocation_id_named
    if not allocation_id:
        print("Error: Allocation ID must be provided as positional argument or --allocation-id")
        return
    
    # Initialize the client
    client = CompactLazyPrimeClient.from_env()
    
    request = GetAllocationByIdRequest(
        portfolio_id=portfolio_id,
        allocation_id=allocation_id
    )
    
    try:
        response = client.allocations.get_allocation_by_id(request)
        print(response)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
