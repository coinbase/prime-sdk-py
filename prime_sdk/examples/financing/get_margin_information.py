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

# #docs operationId: PrimeRESTAPI_GetMarginInformation
# #docs operationName: Get Margin Information

import argparse
import os
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.financing import GetMarginInformationRequest


def main():
    parser = argparse.ArgumentParser(description="Get margin information for an entity")
    parser.add_argument("entity_id", nargs="?", help="Entity ID")
    parser.add_argument("--entity-id", dest="entity_id_named", help="Entity ID")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()

    # Accept entity ID from either positional or named argument
    entity_id = args.entity_id or args.entity_id_named or os.getenv("PRIME_ENTITY_ID")
    if not entity_id:
        print("Error: Entity ID is required. Provide as positional argument, use --entity-id, or set PRIME_ENTITY_ID env var")
        print("Example: python get_margin_information.py abc123")
        print("Example: python get_margin_information.py --entity-id abc123")
        return

    request = GetMarginInformationRequest(
        entity_id=entity_id
    )

    try:
        response = client.financing.get_margin_information(request)
        print(response)
    except Exception as e:
        print(f"failed to get margin information: {e}")


if __name__ == "__main__":
    main()
