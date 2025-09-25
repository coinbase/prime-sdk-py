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

# #docs operationId: PrimeRESTAPI_GetPortfolioUsers
# #docs operationName: List Portfolio Users

import argparse
import os
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.users import ListPortfolioUsersRequest
from prime_sdk.utils import PaginationParams

def main():
    parser = argparse.ArgumentParser(description="List users for a portfolio")
    parser.add_argument("portfolio_id", nargs="?", help="Portfolio ID")
    parser.add_argument("--portfolio-id", dest="portfolio_id_named", help="Portfolio ID")
    parser.add_argument("--limit", type=int, help="Number of results to return")
    parser.add_argument("--cursor", help="Pagination cursor")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    
    # Accept portfolio ID from either positional or named argument
    portfolio_id = args.portfolio_id or args.portfolio_id_named or os.getenv("PRIME_PORTFOLIO_ID")
    if not portfolio_id:
        print("Error: Portfolio ID is required. Provide as positional argument, use --portfolio-id, or set PRIME_PORTFOLIO_ID env var")
        return

    # Set up pagination if provided
    pagination = None
    if args.limit or args.cursor:
        pagination = PaginationParams(
            limit=args.limit,
            cursor=args.cursor
        )
    
    request = ListPortfolioUsersRequest(
        portfolio_id=portfolio_id,
        pagination=pagination
    )
    
    try:
        response = client.users.list_portfolio_users(request)
        print(response)
    except Exception as e:
        print(f"failed to list portfolio users: {e}")


if __name__ == "__main__":
    main()
