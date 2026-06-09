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

# #docs operationId: PrimeRESTAPI_GetUnstakingStatus
# #docs operationName: Get Unstaking Status

import argparse

from prime_sdk.client import Client
from prime_sdk.credentials import Credentials
from prime_sdk.services.staking import GetUnstakingStatusRequest, StakingService


def main():
    parser = argparse.ArgumentParser(description="Get unstaking status for a wallet")
    parser.add_argument("wallet_id", nargs="?", help="Wallet ID")
    parser.add_argument("--wallet-id", dest="wallet_id_named", help="Wallet ID")
    args = parser.parse_args()

    credentials = Credentials.from_env()
    client = Client(credentials)
    staking_service = StakingService(client)

    # Accept wallet ID from either positional or named argument
    wallet_id = args.wallet_id or args.wallet_id_named
    if not wallet_id:
        print("Error: Wallet ID is required. Provide as positional argument or use --wallet-id")
        return

    request = GetUnstakingStatusRequest(portfolio_id=credentials.portfolio_id, wallet_id=wallet_id)

    try:
        response = staking_service.get_unstaking_status(request)
        print(response)
    except Exception as e:
        print(f"failed to get unstaking status: {e}")


if __name__ == "__main__":
    main()
