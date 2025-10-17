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

from dataclasses import asdict
from ...client import Client
from ...utils import append_query_param, append_pagination_params, to_body_dict
from .accept_quote import (
    AcceptQuoteRequest,
    AcceptQuoteResponse
)
from .cancel_order import (
    CancelOrderRequest,
    CancelOrderResponse
)
from .create_order import (
    CreateOrderRequest,
    CreateOrderResponse
)
from .create_order_preview import (
    CreateOrderPreviewRequest,
    CreateOrderPreviewResponse
)
from .create_quote import (
    CreateQuoteRequest,
    CreateQuoteResponse
)
from .edit_order import (
    EditOrderRequest,
    EditOrderResponse
)
from .get_order import (
    GetOrderRequest,
    GetOrderResponse
)
from .list_open_orders import (
    ListOpenOrdersRequest,
    ListOpenOrdersResponse
)
from .list_order_fills import (
    ListOrderFillsRequest,
    ListOrderFillsResponse
)
from .list_orders import (
    ListOrdersRequest,
    ListOrdersResponse
)
from .list_portfolio_fills import (
    ListPortfolioFillsRequest,
    ListPortfolioFillsResponse
)


class OrdersService:
    def __init__(self, client: Client):
        self.client = client

    def accept_quote(self, request: AcceptQuoteRequest) -> AcceptQuoteResponse:
        path = f"/portfolios/{request.portfolio_id}/accept_quote"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return AcceptQuoteResponse(**response.json())

    def cancel_order(self, request: CancelOrderRequest) -> CancelOrderResponse:
        path = f"/portfolios/{request.portfolio_id}/orders/{request.order_id}/cancel"
        response = self.client.request("POST", path, allowed_status_codes=request.allowed_status_codes)
        return CancelOrderResponse(**response.json())

    def create_order(self, request: CreateOrderRequest) -> CreateOrderResponse:
        path = f"/portfolios/{request.portfolio_id}/order"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateOrderResponse(**response.json())

    def create_order_preview(self, request: CreateOrderPreviewRequest) -> CreateOrderPreviewResponse:
        path = f"/portfolios/{request.portfolio_id}/order_preview"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateOrderPreviewResponse(**response.json())

    def create_quote(self, request: CreateQuoteRequest) -> CreateQuoteResponse:
        path = f"/portfolios/{request.portfolio_id}/rfq"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateQuoteResponse(**response.json())

    def edit_order(self, request: EditOrderRequest) -> EditOrderResponse:
        path = f"/portfolios/{request.portfolio_id}/orders/{request.order_id}/edit"
        body = to_body_dict(request)
        response = self.client.request("PUT", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return EditOrderResponse(**response.json())

    def get_order(self, request: GetOrderRequest) -> GetOrderResponse:
        path = f"/portfolios/{request.portfolio_id}/orders/{request.order_id}"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetOrderResponse(**response.json())

    def list_open_orders(self, request: ListOpenOrdersRequest) -> ListOpenOrdersResponse:
        path = f"/portfolios/{request.portfolio_id}/open_orders"

        query_params = append_query_param("", 'product_ids', request.product_ids)
        query_params = append_query_param(query_params, 'order_type', request.order_type)
        query_params = append_query_param(query_params, 'order_side', request.order_side)

        if request.start_date:
            query_params = append_query_param(
                query_params,
                'start_date',
                request.start_date.isoformat() + 'Z')
        if request.end_date:
            query_params = append_query_param(
                query_params,
                'end_date',
                request.end_date.isoformat() + 'Z')

        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListOpenOrdersResponse(**response.json())

    def list_order_fills(self, request: ListOrderFillsRequest) -> ListOrderFillsResponse:
        path = f"/portfolios/{request.portfolio_id}/orders/{request.order_id}/fills"
        query_params = append_pagination_params("", request.pagination)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListOrderFillsResponse(**response.json())

    def list_orders(self, request: ListOrdersRequest) -> ListOrdersResponse:
        path = f"/portfolios/{request.portfolio_id}/orders"

        query_params = append_query_param("", 'order_statuses', request.order_statuses)
        query_params = append_query_param(query_params, 'product_ids', request.product_ids)
        query_params = append_query_param(query_params, 'order_type', request.order_type)
        query_params = append_query_param(query_params, 'order_side', request.order_side)

        if request.start_date:
            query_params = append_query_param(query_params, 'start_date', request.start_date.isoformat() + 'Z')
        if request.end_date:
            query_params = append_query_param(query_params, 'end_date', request.end_date.isoformat() + 'Z')

        query_params = append_pagination_params(query_params, request.pagination)

        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListOrdersResponse(**response.json())

    def list_portfolio_fills(self, request: ListPortfolioFillsRequest) -> ListPortfolioFillsResponse:
        path = f"/portfolios/{request.portfolio_id}/fills"

        query_params = append_query_param("", 'start_date', request.start_date)

        if request.end_date:
            query_params = append_query_param(query_params, 'end_date', request.end_date)

        query_params = append_pagination_params(query_params, request.pagination)

        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListPortfolioFillsResponse(**response.json())