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

# #docs operationId: PrimeRESTAPI_CreateOnchainTransaction
# #docs operationName: Create Onchain Transaction

import argparse
import os

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.transactions import (
    CreateOnchainTransactionRequest,
    EvmParams,
    Rpc,
)


def main():
    parser = argparse.ArgumentParser(description="Create an onchain transaction")
    parser.add_argument("--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)")
    parser.add_argument("--wallet-id", required=True, help="Wallet ID")
    parser.add_argument(
        "--raw-unsigned-txn",
        required=True,
        help="Raw unsigned transaction (hex encoded)",
    )
    parser.add_argument(
        "--skip-broadcast",
        action="store_true",
        help="Skip broadcasting the transaction",
    )
    parser.add_argument("--rpc-url", help="Custom RPC URL")
    parser.add_argument("--chain-id", help="Chain ID for EVM transactions")
    parser.add_argument("--disable-dynamic-gas", action="store_true", help="Disable dynamic gas for EVM")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")

    if not portfolio_id:
        print("Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id")
        return

    # Build optional RPC params
    rpc = None
    if args.skip_broadcast or args.rpc_url:
        rpc = Rpc(
            skip_broadcast=args.skip_broadcast if args.skip_broadcast else None,
            url=args.rpc_url,
        )

    # Build optional EVM params
    evm_params = None
    if args.chain_id or args.disable_dynamic_gas:
        evm_params = EvmParams(
            chain_id=args.chain_id,
            disable_dynamic_gas=args.disable_dynamic_gas if args.disable_dynamic_gas else None,
        )

    request = CreateOnchainTransactionRequest(
        portfolio_id=portfolio_id,
        wallet_id=args.wallet_id,
        raw_unsigned_txn=args.raw_unsigned_txn,
        rpc=rpc,
        evm_params=evm_params,
    )

    try:
        response = client.transactions.create_onchain_transaction(request)
        print(response)
    except Exception as e:
        print(f"failed to create onchain transaction: {e}")


if __name__ == "__main__":
    main()
