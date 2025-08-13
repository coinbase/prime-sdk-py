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
from prime_sdk.enums import WalletType
from prime_sdk.services.wallets import WalletsService, ListWalletsRequest

def main():
    parser = argparse.ArgumentParser(description="List wallets")
    parser.add_argument("--type", choices=["VAULT", "TRADING", "ONCHAIN"],
                       help="Filter by wallet type (optional)")
    parser.add_argument("--symbols", help="Filter by currency symbols (optional)")
    args = parser.parse_args()

    credentials = Credentials.from_env()
    client = Client(credentials)
    wallets_service = WalletsService(client)

    request = ListWalletsRequest(
        portfolio_id=credentials.portfolio_id,
        type=WalletType(args.type) if args.type else None,
        symbols=args.symbols
    )
    try:
        response = wallets_service.list_wallets(request)
        print(response)
    except Exception as e:
        print(f"failed to list wallets: {e}")


if __name__ == "__main__":
    main()