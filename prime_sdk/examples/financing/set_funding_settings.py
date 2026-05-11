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

# #docs operationId: PrimeBeta_SetFundingSettings
# #docs operationName: Update Funding Settings (Beta)

import argparse
import os
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.financing import SetFundingSettingsRequest


def main():
    parser = argparse.ArgumentParser(description="Update FCM funding settings for an entity")
    parser.add_argument("--entity-id", help="Entity ID (overrides PRIME_ENTITY_ID env var)")
    parser.add_argument("--designated-funding-portfolio-id", required=True,
                        help="Portfolio ID to use for FCM margin calls and excess margin sweeps")
    parser.add_argument("--automatic-conversion-enabled", required=True,
                        choices=["true", "false"],
                        help="Enable automatic USDC-to-USD conversion for margin calls")
    parser.add_argument("--automatic-loan-enabled", required=True,
                        choices=["true", "false"],
                        help="Enable automatic loan initiation for margin calls")
    parser.add_argument("--automatic-excess-return-enabled", required=True,
                        choices=["true", "false"],
                        help="Enable automatic return of excess FCM margin")
    parser.add_argument("--excess-funds-target-amount", required=True,
                        help="Target amount to maintain in the futures account above margin requirements")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()

    entity_id = args.entity_id or os.getenv("PRIME_ENTITY_ID")
    if not entity_id:
        print("Error: Entity ID is required. Set PRIME_ENTITY_ID env var or use --entity-id")
        return

    request = SetFundingSettingsRequest(
        entity_id=entity_id,
        designated_funding_portfolio_id=args.designated_funding_portfolio_id,
        automatic_conversion_enabled=args.automatic_conversion_enabled == "true",
        automatic_loan_enabled=args.automatic_loan_enabled == "true",
        automatic_excess_return_enabled=args.automatic_excess_return_enabled == "true",
        excess_funds_target_amount=args.excess_funds_target_amount
    )

    try:
        response = client.financing.set_funding_settings(request)
        print(response)
    except Exception as e:
        print(f"failed to set funding settings: {e}")


if __name__ == "__main__":
    main()
