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
import os
import uuid

from prime_sdk.credentials import Credentials
from prime_sdk.client import Client
from prime_sdk.enums import WalletType
from prime_sdk.services.wallets import WalletsService, CreateWalletRequest
from prime_sdk.examples.constants import PORTFOLIO_ID, WALLET_SYMBOL, WALLET_TYPE, WALLET_NAME as DEFAULT_WALLET_NAME

def main():
    credentials = Credentials.from_env("PRIME_CREDENTIALS")
    client = Client(credentials)
    wallets_service = WalletsService(client)

    wallet_name = os.getenv("WALLET_NAME", DEFAULT_WALLET_NAME)

    request = CreateWalletRequest(
        portfolio_id=PORTFOLIO_ID,
        name="testname12344",
        idempotency_key=str(uuid.uuid4()),
        symbol="SOL",
        wallet_type=WalletType.VAULT

    )
    try:
        response = wallets_service.create_wallet(request)
        print(response)
    except Exception as e:
        print(f"failed to create wallet: {e}")


if __name__ == "__main__":
    main()
