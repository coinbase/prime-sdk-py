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
from prime_sdk.services.staking import StakingService, CreateStakeRequest, StakingInputs


def main():
    parser = argparse.ArgumentParser(description="Create a stake")
    parser.add_argument("--wallet-id", required=True, help="Wallet ID")
    parser.add_argument("--amount", required=True, help="Amount to stake")
    parser.add_argument("--validator-address", help="Validator address (optional)")
    parser.add_argument("--credentials", default="PRIME_CREDENTIALS", 
                       help="Environment variable name for credentials (default: PRIME_CREDENTIALS)")
    args = parser.parse_args()

    credentials = Credentials.from_env(args.credentials)
    client = Client(credentials)
    staking_service = StakingService(client)

    staking_inputs = StakingInputs(
        amount=args.amount,
        validator_address=args.validator_address
    )

    request = CreateStakeRequest(
        portfolio_id=credentials.portfolio_id,
        wallet_id=args.wallet_id,
        idempotency_key=str(uuid.uuid4()),
        inputs=staking_inputs
    )

    try:
        response = staking_service.create_stake(request)
        print(response)
    except Exception as e:
        print(f"failed to create stake: {e}")


if __name__ == "__main__":
    main()