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
from ...utils import append_pagination_params
from .get_product_candles import GetProductCandlesRequest, GetProductCandlesResponse
from .list_products import ListProductsRequest, ListProductsResponse


class ProductsService:
    def __init__(self, client: Client):
        self.client = client

    def get_product_candles(self, request: GetProductCandlesRequest) -> GetProductCandlesResponse:
        path = f"/portfolios/{request.portfolio_id}/candles"
        query_params = (
            f"product_id={request.product_id}&granularity={request.granularity}"
            f"&start_time={request.start_time}&end_time={request.end_time}"
        )
        response = self.client.request(
            "GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes
        )
        return GetProductCandlesResponse.from_response(response.json())

    def list_products(self, request: ListProductsRequest) -> ListProductsResponse:
        path = f"/portfolios/{request.portfolio_id}/products"
        query_params = append_pagination_params("", request.pagination)
        response = self.client.request(
            "GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes
        )
        return ListProductsResponse.from_response(response.json())
