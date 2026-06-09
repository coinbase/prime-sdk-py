# Copyright 2026-present Coinbase Global, Inc.
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
from ...utils import append_pagination_params, append_query_param, to_body_dict
from .cancel_advanced_transfer import CancelAdvancedTransferRequest, CancelAdvancedTransferResponse
from .create_advanced_transfer import CreateAdvancedTransferRequest, CreateAdvancedTransferResponse
from .list_advanced_transfer_transactions import (
    ListAdvancedTransferTransactionsRequest,
    ListAdvancedTransferTransactionsResponse,
)
from .list_advanced_transfers import ListAdvancedTransfersRequest, ListAdvancedTransfersResponse


class AdvancedTransfersService:
    def __init__(self, client: Client):
        self.client = client

    def cancel_advanced_transfer(self, request: CancelAdvancedTransferRequest) -> CancelAdvancedTransferResponse:
        path = f"/portfolios/{request.portfolio_id}/advanced_transfers/{request.advanced_transfer_id}/cancel"
        response = self.client.request("POST", path, allowed_status_codes=request.allowed_status_codes)
        return CancelAdvancedTransferResponse.from_response(response.json())

    def create_advanced_transfer(self, request: CreateAdvancedTransferRequest) -> CreateAdvancedTransferResponse:
        path = f"/portfolios/{request.portfolio_id}/advanced_transfers"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateAdvancedTransferResponse.from_response(response.json())

    def list_advanced_transfer_transactions(
        self, request: ListAdvancedTransferTransactionsRequest
    ) -> ListAdvancedTransferTransactionsResponse:
        path = f"/portfolios/{request.portfolio_id}/advanced_transfers/{request.advanced_transfer_id}/transactions"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return ListAdvancedTransferTransactionsResponse.from_response(response.json())

    def list_advanced_transfers(self, request: ListAdvancedTransfersRequest) -> ListAdvancedTransfersResponse:
        path = f"/portfolios/{request.portfolio_id}/advanced_transfers"
        query_params = append_pagination_params("", request.pagination)
        query_params = append_query_param(query_params, "state", request.state)
        query_params = append_query_param(query_params, "type", request.type)
        query_params = append_query_param(query_params, "start_time", request.start_time)
        query_params = append_query_param(query_params, "end_time", request.end_time)
        query_params = append_query_param(query_params, "reference_id", request.reference_id)
        response = self.client.request(
            "GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes
        )
        return ListAdvancedTransfersResponse.from_response(response.json())
