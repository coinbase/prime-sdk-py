# Copyright 2024-present Coinbase Global, Inc.
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

from ...client import Client
from ...utils import append_query_param, append_pagination_params
from .get_wallet_balance import (
    GetWalletBalanceRequest,
    GetWalletBalanceResponse
)
from .list_entity_balances import (
    ListEntityBalancesRequest,
    ListEntityBalancesResponse
)
from .list_web3_wallet_balances import (
    ListWeb3WalletBalancesRequest,
    ListWeb3WalletBalancesResponse
)
from .list_portfolio_balances import (
    ListPortfolioBalancesRequest,
    ListPortfolioBalancesResponse
)


class BalancesService:
    def __init__(self, client: Client):
        self.client = client

    def get_wallet_balance(self, request: GetWalletBalanceRequest) -> GetWalletBalanceResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/balance"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetWalletBalanceResponse(**response.json())

    def list_entity_balances(self, request: ListEntityBalancesRequest) -> ListEntityBalancesResponse:
        path = f"/entities/{request.entity_id}/balances"

        query_params = append_query_param("", "symbols", request.symbols)
        query_params = append_query_param(query_params, "aggregation_type", request.aggregation_type)
        query_params = append_pagination_params(query_params, request.pagination)

        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListEntityBalancesResponse(**response.json())

    def list_web3_wallet_balances(self, request: ListWeb3WalletBalancesRequest) -> ListWeb3WalletBalancesResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/web3_balances"

        query_params = append_query_param("", 'visibility_statuses', request.visibility_statuses)
        query_params = append_pagination_params(query_params, request.pagination)

        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListWeb3WalletBalancesResponse(**response.json())

    def list_portfolio_balances(self, request: ListPortfolioBalancesRequest) -> ListPortfolioBalancesResponse:
        path = f"/portfolios/{request.portfolio_id}/balances"

        query_params = append_query_param("", 'symbols', request.symbols)
        query_params = append_query_param(query_params, 'balance_type', request.balance_type)
        query_params = append_pagination_params(query_params, request.pagination)

        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListPortfolioBalancesResponse(**response.json())