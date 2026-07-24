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

# #docs operationId: PrimeRESTAPI_UpdateOnchainAddressGroup
# #docs operationName: Update Onchain Address Book

import argparse
import os
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.onchain_address_book import UpdateOnchainAddressBookRequest
from prime_sdk.model import AddressGroup, OnchainAddress
from prime_sdk.enums import NetworkType


def main():
    parser = argparse.ArgumentParser(description="Update an onchain address book entry")
    parser.add_argument(
        "--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    parser.add_argument(
        "--address-group-id", required=True, help="Address group ID to update"
    )
    parser.add_argument("--name", required=True, help="Updated address group name")
    parser.add_argument(
        "--network-type",
        choices=["NETWORK_TYPE_EVM", "NETWORK_TYPE_SOLANA"],
        required=True,
        help="Network type",
    )
    parser.add_argument("--address-name", required=True, help="Address name")
    parser.add_argument("--address", required=True, help="The blockchain address")
    parser.add_argument(
        "--chain-ids", required=True, help="Comma-separated chain IDs (e.g., 1,137)"
    )
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()

    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    if not portfolio_id:
        print(
            "Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id"
        )
        return

    # Parse chain IDs
    chain_ids = [chain_id.strip() for chain_id in args.chain_ids.split(",")]

    # Create OnchainAddress object
    address = OnchainAddress(
        name=args.address_name, address=args.address, chain_ids=chain_ids
    )

    # Create AddressGroup object (now imported from onchain_address_book service)
    address_group = AddressGroup(
        id=args.address_group_id,
        name=args.name,
        network_type=NetworkType(
            args.network_type
        ).value,  # Convert enum to string value
        addresses=[address],
        added_at="",
    )

    request = UpdateOnchainAddressBookRequest(
        portfolio_id=portfolio_id, address_group=address_group
    )

    try:
        response = client.onchain_address_book.update_onchain_address_book(request)
        print(response)
    except Exception as e:
        print(f"failed to update onchain address book: {e}")


if __name__ == "__main__":
    main()
