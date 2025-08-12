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
from prime_sdk.model import Network
from prime_sdk.services.transactions import (
    TransactionsService, 
    CreateWithdrawalRequest,
    PaymentMethod,
    BlockchainAddress,
    Network,
    Counterparty
)


def main():
    parser = argparse.ArgumentParser(description="Create a withdrawal")
    parser.add_argument("--wallet-id", required=True, help="Wallet ID")
    parser.add_argument("--amount", required=True, help="Amount to withdraw")
    parser.add_argument("--currency-symbol", required=True, help="Currency symbol (e.g., USDC)")
    parser.add_argument("--destination-type", required=True, 
                       choices=["PAYMENT_METHOD", "BLOCKCHAIN_ADDRESS", "COUNTERPARTY"],
                       help="Destination type")

    # Payment method options
    parser.add_argument("--payment-method-id", help="Payment method ID (for PAYMENT_METHOD destination)")
    
    # Blockchain address options
    parser.add_argument("--blockchain-address", help="Blockchain address (for BLOCKCHAIN_ADDRESS destination)")
    parser.add_argument("--account-identifier", help="Account identifier (optional for blockchain)")
    parser.add_argument("--network-id", help="Network ID (e.g., ethereum-mainnet)")
    parser.add_argument("--network-type", help="Network type (e.g., NETWORK_TYPE_EVM)")
    
    # Counterparty options
    parser.add_argument("--counterparty-id", help="Counterparty ID (for COUNTERPARTY destination)")
    
    parser.add_argument("--credentials", default="PRIME_CREDENTIALS", 
                       help="Environment variable name for credentials (default: PRIME_CREDENTIALS)")
    args = parser.parse_args()

    # Validate destination-specific arguments
    if args.destination_type == "PAYMENT_METHOD" and not args.payment_method_id:
        print("Error: --payment-method-id is required for PAYMENT_METHOD destination")
        return
    
    if args.destination_type == "BLOCKCHAIN_ADDRESS" and not args.blockchain_address:
        print("Error: --blockchain-address is required for BLOCKCHAIN_ADDRESS destination")
        return
        
    if args.destination_type == "COUNTERPARTY" and not args.counterparty_id:
        print("Error: --counterparty-id is required for COUNTERPARTY destination")
        return

    credentials = Credentials.from_env(args.credentials)
    client = Client(credentials)
    transactions_service = TransactionsService(client)

    # Build request based on destination type
    payment_method = None
    blockchain_address = None
    counterparty = None
    
    if args.destination_type == "PAYMENT_METHOD":
        payment_method = PaymentMethod(payment_method_id=args.payment_method_id)
    elif args.destination_type == "BLOCKCHAIN_ADDRESS":
        network = None
        if args.network_id and args.network_type:
            network = Network(id=args.network_id, type=args.network_type)
        blockchain_address = BlockchainAddress(
            address=args.blockchain_address,
            account_identifier=args.account_identifier,
            network=network
        )
    elif args.destination_type == "COUNTERPARTY":
        counterparty = Counterparty(counterparty_id=args.counterparty_id)

    request = CreateWithdrawalRequest(
        portfolio_id=credentials.portfolio_id,
        wallet_id=args.wallet_id,
        amount=args.amount,
        destination_type=args.destination_type,
        idempotency_key=str(uuid.uuid4()),
        currency_symbol=args.currency_symbol,
        payment_method=payment_method,
        blockchain_address=blockchain_address,
        counterparty=counterparty
    )
    
    try:
        response = transactions_service.create_withdrawal(request)
        print(response)
    except Exception as e:
        print(f"failed to create withdrawal: {e}")


if __name__ == "__main__":
    main()