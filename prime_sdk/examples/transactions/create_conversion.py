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

#docs operationId: PrimeRESTAPI_CreateConversion

import argparse
import os
import uuid
from prime_sdk import CompactLazyPrimeClient
from prime_sdk.services.transactions import CreateConversionRequest


def main():
    parser = argparse.ArgumentParser(description="Create a conversion transaction")
    parser.add_argument(
        "--portfolio-id",
        help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    parser.add_argument(
        "--wallet-id",
        required=True,
        help="Wallet ID for the conversion"
    )
    parser.add_argument(
        "--amount",
        required=True,
        help="Amount to convert"
    )
    parser.add_argument(
        "--source-symbol",
        required=True,
        help="Source symbol to convert from (e.g., BTC)"
    )
    parser.add_argument(
        "--destination-symbol", 
        required=True,
        help="Destination symbol to convert to (e.g., ETH)"
    )
    parser.add_argument(
        "--destination",
        required=True,
        help="Destination address or identifier"
    )
    parser.add_argument(
        "--idempotency-key",
        help="Idempotency key (auto-generated if not provided)"
    )
    
    args = parser.parse_args()
    
    # Get portfolio ID from args or environment
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    if not portfolio_id:
        print("Error: Portfolio ID must be provided via --portfolio-id argument or PRIME_PORTFOLIO_ID environment variable")
        return
    
    # Generate idempotency key if not provided
    idempotency_key = args.idempotency_key or str(uuid.uuid4())
    
    # Initialize the client
    client = CompactLazyPrimeClient.from_env()
    
    request = CreateConversionRequest(
        portfolio_id=portfolio_id,
        wallet_id=args.wallet_id,
        amount=args.amount,
        source_symbol=args.source_symbol,
        destination_symbol=args.destination_symbol,
        destination=args.destination,
        idempotency_key=idempotency_key
    )
    
    try:
        response = client.transactions.create_conversion(request)
        print(response)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
