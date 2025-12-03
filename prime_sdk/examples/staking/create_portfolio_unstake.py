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

# #docs operationId: PrimeRESTAPI_CreatePortfolioUnstake
# #docs operationName: Create Portfolio Unstake

import argparse
import uuid
from prime_sdk.credentials import Credentials
from prime_sdk.client import Client
from prime_sdk.services.staking import StakingService, CreatePortfolioUnstakeRequest


def main():
    parser = argparse.ArgumentParser(description="Create a portfolio-level unstake request")
    parser.add_argument("--currency-symbol", required=True, help="Currency symbol (e.g., ETH)")
    parser.add_argument("--amount", required=True, help="Amount to unstake")
    args = parser.parse_args()

    credentials = Credentials.from_env()
    client = Client(credentials)
    staking_service = StakingService(client)

    request = CreatePortfolioUnstakeRequest(
        portfolio_id=credentials.portfolio_id,
        idempotency_key=str(uuid.uuid4()),
        currency_symbol=args.currency_symbol,
        amount=args.amount
    )

    try:
        response = staking_service.create_portfolio_unstake(request)
        print(response)
    except Exception as e:
        print(f"failed to create portfolio unstake: {e}")


if __name__ == "__main__":
    main()
