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

# #docs operationId: PrimeRESTAPI_GetTransaction
# #docs operationName: Get Transaction

import argparse
import os

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.transactions import GetTransactionRequest


def main():
    parser = argparse.ArgumentParser(description="Get details for a specific transaction")
    parser.add_argument("transaction_id", nargs="?", help="Transaction ID")
    parser.add_argument("--transaction-id", dest="transaction_id_named", help="Transaction ID")
    parser.add_argument("--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")

    if not portfolio_id:
        print("Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id")
        return

    # Accept transaction ID from either positional or named argument
    transaction_id = args.transaction_id or args.transaction_id_named
    if not transaction_id:
        print("Error: Transaction ID is required. Provide as positional argument or use --transaction-id")
        return

    request = GetTransactionRequest(portfolio_id=portfolio_id, transaction_id=transaction_id)

    try:
        response = client.transactions.get_transaction(request)
        print(response)
    except Exception as e:
        print(f"failed to get transaction: {e}")


if __name__ == "__main__":
    main()
