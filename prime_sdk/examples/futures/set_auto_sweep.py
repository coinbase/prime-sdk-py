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

# #docs operationId: PrimeRESTAPI_SetAutoSweep
# #docs operationName: Set Auto Sweep

import argparse
import os

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.futures import SetAutoSweepRequest


def main():
    parser = argparse.ArgumentParser(description="Set auto sweep on or off for an entity")
    parser.add_argument("--entity-id", help="Entity ID (overrides PRIME_ENTITY_ID env var)")
    parser.add_argument("--enable", dest="auto_sweep", action="store_true", help="Enable auto sweep")
    parser.add_argument("--disable", dest="auto_sweep", action="store_false", help="Disable auto sweep")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()

    entity_id = args.entity_id or os.getenv("PRIME_ENTITY_ID")
    if not entity_id:
        print("Error: Entity ID is required. Set PRIME_ENTITY_ID env var or use --entity-id")
        return

    if args.auto_sweep is None:
        print("Error: Must specify either --enable or --disable")
        return

    request = SetAutoSweepRequest(entity_id=entity_id, auto_sweep=args.auto_sweep)

    try:
        response = client.futures.set_auto_sweep(request)
        print(response)
    except Exception as e:
        print(f"failed to set auto sweep: {e}")


if __name__ == "__main__":
    main()
