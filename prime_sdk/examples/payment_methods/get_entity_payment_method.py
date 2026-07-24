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

# #docs operationId: PrimeRESTAPI_GetEntityPaymentMethodDetails
# #docs operationName: Get Entity Payment Method

import argparse
import os

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.payment_methods import GetEntityPaymentMethodRequest


def main():
    parser = argparse.ArgumentParser(
        description="Get details for a specific payment method"
    )
    parser.add_argument("payment_method_id", nargs="?", help="Payment Method ID")
    parser.add_argument(
        "--payment-method-id", dest="payment_method_id_named", help="Payment Method ID"
    )
    parser.add_argument(
        "--entity-id", help="Entity ID (overrides PRIME_ENTITY_ID env var)"
    )
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    entity_id = args.entity_id or os.getenv("PRIME_ENTITY_ID")

    if not entity_id:
        print(
            "Error: Entity ID is required. Set PRIME_ENTITY_ID env var or use --entity-id"
        )
        return

    # Accept payment method ID from either positional or named argument
    payment_method_id = args.payment_method_id or args.payment_method_id_named
    if not payment_method_id:
        print(
            "Error: Payment Method ID is required. Provide as positional argument or use --payment-method-id"
        )
        return

    request = GetEntityPaymentMethodRequest(
        entity_id=entity_id, payment_method_id=payment_method_id
    )

    try:
        response = client.payment_methods.get_entity_payment_method(request)
        print(response)
    except Exception as e:
        print(f"failed to get entity payment method: {e}")


if __name__ == "__main__":
    main()
