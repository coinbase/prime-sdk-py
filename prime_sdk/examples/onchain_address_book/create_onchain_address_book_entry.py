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

# #docs operationId: PrimeRESTAPI_CreateOnchainAddressBookEntry
# #docs operationName: Create Onchain Address Book Entry

import argparse
import os
from prime_sdk.client_services import CompactLazyPrimeClient
from prime_sdk.services.onchain_address_book import CreateOnchainAddressBookEntryRequest, AddressGroup, Address
from prime_sdk.enums import NetworkType

def main():
    parser = argparse.ArgumentParser(description="Create an onchain address book entry")
    parser.add_argument("--portfolio-id", help="Portfolio ID (or set PRIME_PORTFOLIO_ID env var)")
    parser.add_argument("--name", required=True, help="Address group name")
    parser.add_argument("--network-type", choices=["NETWORK_TYPE_EVM", "NETWORK_TYPE_SOLANA"], 
                       required=True, help="Network type")
    parser.add_argument("--address-name", required=True, help="Address name")
    parser.add_argument("--address", required=True, help="The blockchain address")
    parser.add_argument("--chain-ids", required=True, help="Comma-separated chain IDs (e.g., 1,137)")
    args = parser.parse_args()

    client = CompactLazyPrimeClient.from_env()
    
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    if not portfolio_id:
        print("Error: Portfolio ID is required. Use --portfolio-id or set PRIME_PORTFOLIO_ID env var")
        return

    # Parse chain IDs
    chain_ids = [chain_id.strip() for chain_id in args.chain_ids.split(',')]
    
    # Create Address object (now imported from onchain_address_book service)
    address = Address(
        name=args.address_name,
        address=args.address,
        chain_ids=chain_ids
    )
    
    # Create AddressGroup object (now imported from onchain_address_book service)
    address_group = AddressGroup(
        id=None,
        name=args.name,
        network_type=NetworkType(args.network_type).value,  # Convert enum to string value
        addresses=[address],
        added_at=None,
    )
    
    request = CreateOnchainAddressBookEntryRequest(
        portfolio_id=portfolio_id,
        address_group=address_group
    )
    
    try:
        response = client.onchain_address_book.create_onchain_address_book_entry(request)
        print(response)
    except Exception as e:
        print(f"failed to create onchain address book entry: {e}")


if __name__ == "__main__":
    main()
