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

# #docs operationId: PrimeRESTAPI_RotateAPIKey
# #docs operationName: Rotate API Key

import argparse
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.api_keys import RotateApiKeyRequest


def main():
    parser = argparse.ArgumentParser(description="Rotate the Prime API key")
    parser.add_argument(
        "--duration-seconds",
        type=int,
        help="Seconds the old key stays active after approval (0 = immediate expiry)",
    )
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()

    request = RotateApiKeyRequest(duration_seconds=args.duration_seconds)

    try:
        response = client.api_keys.rotate_api_key(request)
        print(response)
    except Exception as e:
        print(f"failed to rotate API key: {e}")


if __name__ == "__main__":
    main()
