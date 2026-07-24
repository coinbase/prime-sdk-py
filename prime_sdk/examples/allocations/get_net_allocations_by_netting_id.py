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

# #docs operationId: PrimeRESTAPI_GetAllocationsByClientNettingId
# #docs operationName: Get Net Allocations By Netting ID

import argparse
import os

from prime_sdk import PrimeServicesClient
from prime_sdk.services.allocations import GetNetAllocationsByNettingIdRequest


def main():
    parser = argparse.ArgumentParser(description="Get net allocations by netting ID")
    parser.add_argument("netting_id", nargs="?", help="Netting ID")
    parser.add_argument(
        "--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    parser.add_argument("--netting-id", dest="netting_id_named", help="Netting ID")

    args = parser.parse_args()

    # Get portfolio ID from args or environment
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    if not portfolio_id:
        print(
            "Error: Portfolio ID must be provided via --portfolio-id argument or PRIME_PORTFOLIO_ID environment variable"
        )
        return

    # Get netting ID from positional argument or named argument
    netting_id = args.netting_id or args.netting_id_named
    if not netting_id:
        print(
            "Error: Netting ID must be provided as positional argument or --netting-id"
        )
        return

    # Initialize the client
    client = PrimeServicesClient.from_env()

    request = GetNetAllocationsByNettingIdRequest(
        portfolio_id=portfolio_id, netting_id=netting_id
    )

    try:
        response = client.allocations.get_net_allocations_by_netting_id(request)
        print(response)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
