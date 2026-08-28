# Copyright 2026-present Coinbase Global, Inc.
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

# #docs operationId: PrimeRESTAPI_GetConversionFees
# #docs operationName: Get Conversion Fees

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.financing import GetConversionFeesRequest


def main():
    client = PrimeServicesClient.from_env()

    request = GetConversionFeesRequest()

    try:
        response = client.financing.get_conversion_fees(request)
        print(response)
    except Exception as e:
        print(f"failed to get conversion fees: {e}")


if __name__ == "__main__":
    main()
