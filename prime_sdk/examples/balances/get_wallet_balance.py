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

# #docs operationId: PrimeRESTAPI_GetWalletBalance
# #docs operationName: Get Wallet Balance

import argparse
import os
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.balances import GetWalletBalanceRequest

def main():
    parser = argparse.ArgumentParser(description="Get balance for a specific wallet")
    parser.add_argument("wallet_id", nargs="?", help="Wallet ID")
    parser.add_argument("--wallet-id", dest="wallet_id_named", help="Wallet ID")
    parser.add_argument("--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")

    if not portfolio_id:
        print("Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id")
        return

    # Accept wallet ID from either positional or named argument
    wallet_id = args.wallet_id or args.wallet_id_named
    if not wallet_id:
        print("Error: Wallet ID is required. Provide as positional argument or use --wallet-id")
        return
    
    request = GetWalletBalanceRequest(
        portfolio_id=portfolio_id,
        wallet_id=wallet_id
    )
    
    try:
        response = client.balances.get_wallet_balance(request)
        print(response)
    except Exception as e:
        print(f"failed to get wallet balance: {e}")


if __name__ == "__main__":
    main()
