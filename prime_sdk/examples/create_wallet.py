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
from prime_sdk.enums import WalletType
from prime_sdk.services.wallets import WalletsService, CreateWalletRequest

def main():
    parser = argparse.ArgumentParser(description="Create a wallet")
    parser.add_argument("--name", required=True, help="Wallet name")
    parser.add_argument("--symbol", required=True, help="Currency symbol (e.g., SOL, BTC)")
    parser.add_argument("--wallet-type", required=True, 
                       choices=['VAULT', 'TRADING', 'ONCHAIN'],
                       help="Wallet type (VAULT, TRADING, ONCHAIN)")
    args = parser.parse_args()

    credentials = Credentials.from_env()
    client = Client(credentials)
    wallets_service = WalletsService(client)

    # Convert string to WalletType enum
    wallet_type_map = {
        'VAULT': WalletType.VAULT,
        'TRADING': WalletType.TRADING,
        'ONCHAIN': WalletType.ONCHAIN
    }

    request = CreateWalletRequest(
        portfolio_id=credentials.portfolio_id,
        name=args.name,
        idempotency_key=str(uuid.uuid4()),
        symbol=args.symbol,
        wallet_type=wallet_type_map[args.wallet_type]
    )
    try:
        response = wallets_service.create_wallet(request)
        print(response)
    except Exception as e:
        print(f"failed to create wallet: {e}")


if __name__ == "__main__":
    main()
