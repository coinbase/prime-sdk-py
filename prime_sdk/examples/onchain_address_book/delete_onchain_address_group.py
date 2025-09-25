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

# #docs operationId: PrimeRESTAPI_DeleteOnchainAddressGroup
# #docs operationName: Delete Onchain Address Group

import argparse
import os
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.onchain_address_book import DeleteOnchainAddressGroupRequest

def main():
    parser = argparse.ArgumentParser(description="Delete an onchain address group")
    parser.add_argument("address_group_id", nargs="?", help="Address Group ID")
    parser.add_argument("--address-group-id", dest="address_group_id_named", help="Address Group ID")
    parser.add_argument("--portfolio-id", help="Portfolio ID (or set PRIME_PORTFOLIO_ID env var)")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    if not portfolio_id:
        print("Error: Portfolio ID is required. Use --portfolio-id or set PRIME_PORTFOLIO_ID env var")
        return

    # Accept address group ID from either positional or named argument
    address_group_id = args.address_group_id or args.address_group_id_named
    if not address_group_id:
        print("Error: Address Group ID is required. Provide as positional argument or use --address-group-id")
        return
    
    request = DeleteOnchainAddressGroupRequest(
        portfolio_id=portfolio_id,
        address_group_id=address_group_id
    )
    
    try:
        response = client.onchain_address_book.delete_onchain_address_group(request)
        print(response)
    except Exception as e:
        print(f"failed to delete onchain address group: {e}")


if __name__ == "__main__":
    main()
