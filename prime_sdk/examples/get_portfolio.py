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
import argparse
from prime_sdk.credentials import Credentials
from prime_sdk.client import Client
from prime_sdk.services.portfolios import PortfoliosService, GetPortfolioRequest

def main():
    credentials = Credentials.from_env()
    
    parser = argparse.ArgumentParser(description="Get portfolio details")
    parser.add_argument("--portfolio-id", default=credentials.portfolio_id)
    args = parser.parse_args()

    client = Client(credentials)
    portfolios_service = PortfoliosService(client)

    request = GetPortfolioRequest(
        portfolio_id=args.portfolio_id
    )
    try:
        response = portfolios_service.get_portfolio(request)
        print(response)
    except Exception as e:
        print(f"failed to get portfolio: {e}")


if __name__ == "__main__":
    main()
