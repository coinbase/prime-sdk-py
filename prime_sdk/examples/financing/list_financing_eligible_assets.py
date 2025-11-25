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

# #docs operationId: PrimeRESTAPI_ListFinancingEligibleAssets
# #docs operationName: List Financing Eligible Assets

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.financing import ListFinancingEligibleAssetsRequest


def main():
    client = PrimeServicesClient.from_env()

    request = ListFinancingEligibleAssetsRequest()

    try:
        response = client.financing.list_financing_eligible_assets(request)

        if response.assets:
            print("Financing Eligible Assets (Trade Finance):")
            print(f"{'Symbol':<10} {'Asset Adjustment':<20} {'Liability Adjustment':<20}")
            print("-" * 50)
            for asset in response.assets:
                print(f"{asset.symbol:<10} {asset.asset_adjustment:<20} {asset.liability_adjustment:<20}")
            print(f"\nTotal: {len(response.assets)} assets")
        else:
            print("No eligible assets found")
    except Exception as e:
        print(f"failed to list financing eligible assets: {e}")


if __name__ == "__main__":
    main()
