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
from prime_sdk.credentials import Credentials
from prime_sdk.client import Client
from prime_sdk.services.balances import BalancesService, GetWalletBalanceRequest

def main():
    parser = argparse.ArgumentParser(description="Get wallet balance")
    parser.add_argument("--wallet-id", required=True, help="Wallet ID")
    parser.add_argument("--portfolio-id", help="Portfolio ID (defaults to credentials)")
    parser.add_argument("--credentials", default="PRIME_CREDENTIALS", 
                       help="Environment variable name for credentials (default: PRIME_CREDENTIALS)")
    args = parser.parse_args()

    credentials = Credentials.from_env(args.credentials)
    client = Client(credentials)
    balances_service = BalancesService(client)

    portfolio_id = args.portfolio_id or credentials.portfolio_id
    
    request = GetWalletBalanceRequest(
        portfolio_id=portfolio_id,
        wallet_id=args.wallet_id
    )
    try:
        response = balances_service.get_wallet_balance(request)
        print(response)
    except Exception as e:
        print(f"failed to get wallet balance: {e}")


if __name__ == "__main__":
    main()