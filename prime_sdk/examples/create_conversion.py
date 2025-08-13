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
import argparse
import uuid

from prime_sdk.credentials import Credentials
from prime_sdk.client import Client
from prime_sdk.services.transactions import TransactionsService, CreateConversionRequest

def main():
    parser = argparse.ArgumentParser(description="Create a conversion")
    parser.add_argument("--wallet_id", required=True, help="Wallet ID")
    parser.add_argument("--amount", required=True, help="Amount to convert")
    parser.add_argument("--destination", required=True, help="Destination Wallet ID")
    parser.add_argument("--source-symbol", required=True, help="Source asset symbol")
    parser.add_argument("--destination-symbol", required=True, help="Destination asset symbol")
    args = parser.parse_args()

    credentials = Credentials.from_env()
    client = Client(credentials)
    transactions_service = TransactionsService(client)

    request = CreateConversionRequest(
        portfolio_id=credentials.portfolio_id,
        wallet_id=args.wallet_id,
        amount=args.amount,
        destination=args.destination,
        idempotency_key=str(uuid.uuid4()),
        source_symbol=args.source_symbol,
        destination_symbol=args.destination_symbol
    )

    try:
        response = transactions_service.create_conversion(request)
        print(response)
    except Exception as e:
        print(f"failed to create conversion: {e}")


if __name__ == "__main__":
    main()