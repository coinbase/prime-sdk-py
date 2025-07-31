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
from prime_sdk.services.portfolios import PortfoliosService, GetPortfolioRequest
from prime_sdk.examples.constants import PORTFOLIO_ID

def main():
    credentials = Credentials.from_env("PRIME_CREDENTIALS")
    client = Client(credentials)
    portfolios_service = PortfoliosService(client)

    request = GetPortfolioRequest(
        portfolio_id=PORTFOLIO_ID
    )
    try:
        response = portfolios_service.get_portfolio(request)
        print(response)
    except Exception as e:
        print(f"failed to get portfolio: {e}")


if __name__ == "__main__":
    main()
