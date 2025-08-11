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
from prime_sdk.utils import append_pagination_params, to_body_dict
from .create_conversion import (
    CreateConversionRequest,
    CreateConversionResponse
)
from .create_onchain_transaction import (
    CreateOnchainTransactionRequest,
    CreateOnchainTransactionResponse
)
from .create_transfer import (
    CreateTransferRequest,
    CreateTransferResponse
)
from .create_withdrawal import (
    CreateWithdrawalRequest,
    CreateWithdrawalResponse
)
from .get_transaction import (
    GetTransactionRequest,
    GetTransactionResponse
)
from .list_portfolio_transactions import (
    ListPortfolioTransactionsRequest,
    ListPortfolioTransactionsResponse
)
from .list_wallet_transactions import (
    ListWalletTransactionsRequest,
    ListWalletTransactionsResponse
)


class TransactionsService:
    def __init__(self, client: Client):
        self.client = client

    def create_conversion(self, request: CreateConversionRequest) -> CreateConversionResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/conversion"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateConversionResponse(**response.json())

    def create_onchain_transaction(self, request: CreateOnchainTransactionRequest) -> CreateOnchainTransactionResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/transactions"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateOnchainTransactionResponse(**response.json())

    def create_transfer(self, request: CreateTransferRequest) -> CreateTransferResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/transfers"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateTransferResponse(**response.json())

    def create_withdrawal(self, request: CreateWithdrawalRequest) -> CreateWithdrawalResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/withdrawals"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateWithdrawalResponse(**response.json())

    def get_transaction(self, request: GetTransactionRequest) -> GetTransactionResponse:
        path = f"/portfolios/{request.portfolio_id}/transactions/{request.transaction_id}"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetTransactionResponse(**response.json())

    def list_portfolio_transactions(self, request: ListPortfolioTransactionsRequest) -> ListPortfolioTransactionsResponse:
        path = f"/portfolios/{request.portfolio_id}/transactions"
        query_params = append_pagination_params("", request.pagination)
        if request.symbols:
            query_params = f"{query_params}&symbols={request.symbols}" if query_params else f"symbols={request.symbols}"
        if request.types:
            query_params = f"{query_params}&types={request.types}" if query_params else f"types={request.types}"
        if request.start:
            query_params = f"{query_params}&start={request.start.isoformat()}" if query_params else f"start={request.start.isoformat()}"
        if request.end:
            query_params = f"{query_params}&end={request.end.isoformat()}" if query_params else f"end={request.end.isoformat()}"
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListPortfolioTransactionsResponse(**response.json())

    def list_wallet_transactions(self, request: ListWalletTransactionsRequest) -> ListWalletTransactionsResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/transactions"
        query_params = append_pagination_params("", request.pagination)
        if request.types:
            query_params = f"{query_params}&types={request.types}" if query_params else f"types={request.types}"
        if request.start:
            query_params = f"{query_params}&start={request.start.isoformat()}" if query_params else f"start={request.start.isoformat()}"
        if request.end:
            query_params = f"{query_params}&end={request.end.isoformat()}" if query_params else f"end={request.end.isoformat()}"
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListWalletTransactionsResponse(**response.json())