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

# #docs operationId: PrimeRESTAPI_GetWalletDepositInstructions
# #docs operationName: Get Wallet Deposit Instructions

import argparse
import os
from prime_sdk.client_services import CompactLazyPrimeClient
from prime_sdk.services.wallets import GetWalletDepositInstructionsRequest
from prime_sdk.enums import WalletDepositType

def main():
    parser = argparse.ArgumentParser(description="Get deposit instructions for a wallet")
    parser.add_argument("wallet_id", nargs="?", help="Wallet ID")
    parser.add_argument("--wallet-id", dest="wallet_id_named", help="Wallet ID")
    parser.add_argument("--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)")
    parser.add_argument("--deposit-type", required=True, 
                       choices=[dt.value for dt in WalletDepositType], 
                       help="Deposit type")
    args = parser.parse_args()

    client = CompactLazyPrimeClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    
    if not portfolio_id:
        print("Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id")
        return

    # Accept wallet ID from either positional or named argument
    wallet_id = args.wallet_id or args.wallet_id_named
    if not wallet_id:
        print("Error: Wallet ID is required. Provide as positional argument or use --wallet-id")
        return

    # Parse deposit type
    deposit_type = WalletDepositType(args.deposit_type)
    
    request = GetWalletDepositInstructionsRequest(
        portfolio_id=portfolio_id,
        wallet_id=wallet_id,
        deposit_type=deposit_type
    )
    
    try:
        response = client.wallets.get_wallet_deposit_instructions(request)
        print(response)
    except Exception as e:
        print(f"failed to get wallet deposit instructions: {e}")


if __name__ == "__main__":
    main()
