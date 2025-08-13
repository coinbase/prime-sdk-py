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
from prime_sdk.services.balances import BalancesService, ListPortfolioBalancesRequest

def main():
    parser = argparse.ArgumentParser(description="List portfolio balances")
    parser.add_argument("--symbols", help="Asset symbols, e.g. BTC")
    parser.add_argument("--balance-type", choices=["TRADING_BALANCES", "VAULT_BALANCES", "TOTAL_BALANCES", "PRIME_CUSTODY_BALANCES"], help="Balance type filter")
    args = parser.parse_args()

    credentials = Credentials.from_env()
    client = Client(credentials)
    balances_service = BalancesService(client)

    
    from prime_sdk.enums import BalanceType
    balance_type = None
    if args.balance_type:
        balance_type = BalanceType(args.balance_type)
    
    request = ListPortfolioBalancesRequest(
        portfolio_id=credentials.portfolio_id,
        symbols=args.symbols,
        balance_type=balance_type
    )
    try:
        response = balances_service.list_portfolio_balances(request)
        print(response)
    except Exception as e:
        print(f"failed to list portfolio balances: {e}")


if __name__ == "__main__":
    main()