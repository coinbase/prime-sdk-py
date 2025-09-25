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

# #docs operationId: PrimeRESTAPI_CreateWalletWithdrawal  
# #docs operationName: Create Withdrawal

import argparse
import os
import uuid
from prime_sdk import PrimeServicesClient
from prime_sdk.services.transactions import (
    CreateWithdrawalRequest,
    PaymentMethod,
    BlockchainAddress,
    Network,
    Counterparty
)

def main():
    parser = argparse.ArgumentParser(description="Create a withdrawal transaction")
    parser.add_argument(
        "--portfolio-id",
        help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    parser.add_argument(
        "--wallet-id",
        required=True,
        help="Wallet ID for the withdrawal"
    )
    parser.add_argument(
        "--amount",
        required=True,
        help="Amount to withdraw"
    )
    parser.add_argument(
        "--currency-symbol",
        required=True,
        help="Currency symbol (e.g., BTC, ETH, USD)"
    )
    parser.add_argument(
        "--destination-type",
        required=True,
        choices=["PAYMENT_METHOD", "BLOCKCHAIN", "COUNTERPARTY"],
        help="Type of destination for the withdrawal"
    )
    parser.add_argument(
        "--idempotency-key",
        help="Idempotency key (auto-generated if not provided)"
    )
    
    # Payment method specific arguments
    parser.add_argument(
        "--payment-method-id",
        help="Payment method ID (required for PAYMENT_METHOD destination type)"
    )
    
    # Blockchain address specific arguments
    parser.add_argument(
        "--blockchain-address",
        help="Blockchain address (required for BLOCKCHAIN_ADDRESS destination type)"
    )
    parser.add_argument(
        "--account-identifier",
        help="Account identifier for blockchain address (optional)"
    )
    parser.add_argument(
        "--network-id",
        help="Network ID for blockchain address (optional)"
    )
    parser.add_argument(
        "--network-type",
        help="Network type for blockchain address (optional)"
    )
    
    
    args = parser.parse_args()
    
    # Get portfolio ID from args or environment
    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    if not portfolio_id:
        print("Error: Portfolio ID must be provided via --portfolio-id argument or PRIME_PORTFOLIO_ID environment variable")
        return
    
    # Generate idempotency key if not provided
    idempotency_key = args.idempotency_key or str(uuid.uuid4())
    
    # Validate destination type specific requirements
    payment_method = None
    blockchain_address = None
    counterparty = None
    
    if args.destination_type == "PAYMENT_METHOD":
        if not args.payment_method_id:
            print("Error: --payment-method-id is required when destination-type is PAYMENT_METHOD")
            return
        payment_method = PaymentMethod(payment_method_id=args.payment_method_id)
    
    elif args.destination_type == "BLOCKCHAIN":
        if not args.blockchain_address:
            print("Error: --blockchain-address is required when destination-type is BLOCKCHAIN")
            return
        
        network = None
        if args.network_id or args.network_type:
            if not (args.network_id and args.network_type):
                print("Error: Both --network-id and --network-type must be provided together")
                return
            network = Network(id=args.network_id, type=args.network_type)
        
        blockchain_address = BlockchainAddress(
            address=args.blockchain_address,
            account_identifier=args.account_identifier,
            network=network
        )
    
    # Initialize the client
    client = PrimeServicesClient.from_env()
    
    request = CreateWithdrawalRequest(
        portfolio_id=portfolio_id,
        wallet_id=args.wallet_id,
        amount=args.amount,
        currency_symbol=args.currency_symbol,
        destination_type="DESTINATION_"+args.destination_type,
        idempotency_key=idempotency_key,
        payment_method=payment_method,
        blockchain_address=blockchain_address,
        counterparty=counterparty
    )
    
    try:
        response = client.transactions.create_withdrawal(request)
        print(response)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
