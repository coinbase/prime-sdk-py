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

# #docs operationId: PrimeRESTAPI_GetTFTieredPricingFees
# #docs operationName: Get Trade Finance Tiered Pricing Fees

import argparse
import os
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.financing import GetTradeFinanceTieredPricingFeesRequest


def main():
    parser = argparse.ArgumentParser(description="Get trade finance tiered pricing fees")
    parser.add_argument("--entity-id", help="Entity ID (overrides PRIME_ENTITY_ID env var)")
    parser.add_argument("--effective-at", help="Effective date (ISO format)")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    entity_id = args.entity_id or os.getenv("PRIME_ENTITY_ID")

    if not entity_id:
        print("Error: Entity ID is required. Set PRIME_ENTITY_ID env var or use --entity-id")
        return

    request = GetTradeFinanceTieredPricingFeesRequest(
        entity_id=entity_id,
        effective_at=args.effective_at
    )

    try:
        response = client.financing.get_trade_finance_tiered_pricing_fees(request)
        print(response)
    except Exception as e:
        print(f"failed to get trade finance tiered pricing fees: {e}")


if __name__ == "__main__":
    main()
