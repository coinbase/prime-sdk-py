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

from prime_sdk.client import Client
from prime_sdk.utils import append_pagination_params, append_query_param, to_body_dict
from .create_wallet import (
    CreateWalletRequest,
    CreateWalletResponse
)
from .create_wallet_deposit_address import (
    CreateWalletDepositAddressRequest,
    CreateWalletDepositAddressResponse
)
from .get_wallet import (
    GetWalletRequest,
    GetWalletResponse
)
from .get_wallet_deposit_instructions import (
    GetWalletDepositInstructionsRequest,
    GetWalletDepositInstructionsResponse
)
from .list_wallet_addresses import (
    ListWalletAddressesRequest,
    ListWalletAddressesResponse
)
from .list_wallets import (
    ListWalletsRequest,
    ListWalletsResponse
)


class WalletsService:
    def __init__(self, client: Client):
        self.client = client

    def create_wallet(self, request: CreateWalletRequest) -> CreateWalletResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateWalletResponse(**response.json())

    def create_wallet_deposit_address(self, request: CreateWalletDepositAddressRequest) -> CreateWalletDepositAddressResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/addresses"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateWalletDepositAddressResponse(**response.json())

    def get_wallet(self, request: GetWalletRequest) -> GetWalletResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetWalletResponse(**response.json())

    def get_wallet_deposit_instructions(self, request: GetWalletDepositInstructionsRequest) -> GetWalletDepositInstructionsResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/deposit_instructions"
        query_params = f"deposit_type={request.deposit_type.value}"
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return GetWalletDepositInstructionsResponse(**response.json())

    def list_wallet_addresses(self, request: ListWalletAddressesRequest) -> ListWalletAddressesResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/addresses"
        query_params = f"network_id={request.network_id}"
        query_params = append_pagination_params(query_params, request.pagination)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListWalletAddressesResponse(**response.json())

    def list_wallets(self, request: ListWalletsRequest) -> ListWalletsResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets"
        query_params = append_pagination_params("", request.pagination)
        query_params = append_query_param(query_params, "type", request.type.value if request.type else None)
        query_params = append_query_param(query_params, "symbols", request.symbols)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListWalletsResponse(**response.json())