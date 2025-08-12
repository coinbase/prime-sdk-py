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
from prime_sdk.services.payment_methods import PaymentMethodsService, ListEntityPaymentMethodsRequest

def main():
    parser = argparse.ArgumentParser(description="List payment methods")
    parser.add_argument("--entity-id", help="Entity ID (defaults to credentials)")
    parser.add_argument("--credentials", default="PRIME_CREDENTIALS", 
                       help="Environment variable name for credentials (default: PRIME_CREDENTIALS)")
    args = parser.parse_args()

    credentials = Credentials.from_env(args.credentials)
    client = Client(credentials)
    payment_methods_service = PaymentMethodsService(client)

    entity_id = args.entity_id or credentials.entity_id
    
    request = ListEntityPaymentMethodsRequest(
        entity_id=entity_id
    )
    try:
        response = payment_methods_service.list_entity_payment_methods(request)
        print(response)
    except Exception as e:
        print(f"failed to list payment methods: {e}")


if __name__ == "__main__":
    main()