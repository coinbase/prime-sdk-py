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

# #docs operationId: PrimeRESTAPI_CreatePortfolioAddressBookEntry
# #docs operationName: Create Address Book Entry

import argparse
import os
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.address_book import CreateAddressBookEntryRequest


def main():
    parser = argparse.ArgumentParser(description="Create an address book entry")
    parser.add_argument("--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)")
    parser.add_argument("--address", required=True, help="Blockchain address")
    parser.add_argument("--currency-symbol", required=True, help="Currency symbol (e.g., BTC)")
    parser.add_argument("--name", required=True, help="Name for this address")
    parser.add_argument("--account-identifier", help="Account identifier (e.g., memo, destination tag)")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")

    if not portfolio_id:
        print("Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id")
        return

    request = CreateAddressBookEntryRequest(
        portfolio_id=portfolio_id,
        address=args.address,
        currency_symbol=args.currency_symbol,
        name=args.name,
        account_identifier=args.account_identifier
    )

    try:
        response = client.address_book.create_address_book_entry(request)
        print(response)
    except Exception as e:
        print(f"failed to create address book entry: {e}")


if __name__ == "__main__":
    main()
