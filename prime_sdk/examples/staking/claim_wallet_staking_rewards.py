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

# #docs operationId: PrimeRESTAPI_ClaimWalletStakingRewards
# #docs operationName: Claim Wallet Staking Rewards

import argparse
import uuid
from prime_sdk.credentials import Credentials
from prime_sdk.client import Client
from prime_sdk.services.staking import (
    StakingService,
    ClaimWalletStakingRewardsRequest,
    ClaimRewardsInputs,
)


def main():
    parser = argparse.ArgumentParser(description="Claim wallet staking rewards (ALPHA)")
    parser.add_argument("--wallet-id", required=True, help="Wallet ID")
    parser.add_argument(
        "--amount",
        help="Amount to claim (optional, ETH only. If omitted, max available will be claimed)",
    )
    args = parser.parse_args()

    credentials = Credentials.from_env()
    client = Client(credentials)
    staking_service = StakingService(client)

    # Create inputs if amount is provided
    inputs = None
    if args.amount:
        inputs = ClaimRewardsInputs(amount=args.amount)

    request = ClaimWalletStakingRewardsRequest(
        portfolio_id=credentials.portfolio_id,
        wallet_id=args.wallet_id,
        idempotency_key=str(uuid.uuid4()),
        inputs=inputs,
    )

    try:
        response = staking_service.claim_wallet_staking_rewards(request)
        print(response)
    except Exception as e:
        print(f"failed to claim staking rewards: {e}")


if __name__ == "__main__":
    main()
