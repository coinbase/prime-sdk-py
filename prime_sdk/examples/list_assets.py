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
from prime_sdk.credentials import Credentials
from prime_sdk.client import Client
from prime_sdk.services.assets import AssetsService, ListAssetsRequest


def main():
    credentials = Credentials.from_env()
    client = Client(credentials)
    assets_service = AssetsService(client)

    request = ListAssetsRequest(entity_id=credentials.entity_id)
    try:
        response = assets_service.list_assets(request)
        print(response)
    except Exception as e:
        print(f"failed to list assets: {e}")


if __name__ == "__main__":
    main()