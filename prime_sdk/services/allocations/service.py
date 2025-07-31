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

from dataclasses import asdict
from ...client import Client
from ...utils import append_query_param, append_pagination_params, to_body_dict
from .create_portfolio_allocations import (
    CreatePortfolioAllocationsRequest,
    CreatePortfolioAllocationsResponse
)
from .create_portfolio_net_allocations import (
    CreatePortfolioNetAllocationsRequest,
    CreatePortfolioNetAllocationsResponse
)
from .get_allocation_by_id import (
    GetAllocationByIdRequest,
    GetAllocationByIdResponse
)
from .get_net_allocations_by_netting_id import (
    GetNetAllocationsByNettingIdRequest,
    GetNetAllocationsByNettingIdResponse
)
from .list_portfolio_allocations import (
    ListPortfolioAllocationsRequest,
    ListPortfolioAllocationsResponse
)


class AllocationsService:
    def __init__(self, client: Client):
        self.client = client

    def create_portfolio_allocations(self, request: CreatePortfolioAllocationsRequest) -> CreatePortfolioAllocationsResponse:
        path = "/allocations"

        body = to_body_dict(request)
        if request.allocation_legs:
            body["allocation_legs"] = [asdict(leg) for leg in request.allocation_legs]

        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreatePortfolioAllocationsResponse(**response.json())

    def create_portfolio_net_allocations(self, request: CreatePortfolioNetAllocationsRequest) -> CreatePortfolioNetAllocationsResponse:
        path = "/allocations/net"

        body = to_body_dict(request)
        if request.allocation_legs:
            body["allocation_legs"] = [asdict(leg) for leg in request.allocation_legs]

        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreatePortfolioNetAllocationsResponse(**response.json())

    def get_allocation_by_id(self, request: GetAllocationByIdRequest) -> GetAllocationByIdResponse:
        path = f"/portfolios/{request.portfolio_id}/allocations/{request.allocation_id}"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetAllocationByIdResponse(**response.json())

    def get_net_allocations_by_netting_id(self, request: GetNetAllocationsByNettingIdRequest) -> GetNetAllocationsByNettingIdResponse:
        path = f"/portfolios/{request.portfolio_id}/allocations/net/{request.netting_id}"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetNetAllocationsByNettingIdResponse(**response.json())

    def list_portfolio_allocations(self, request: ListPortfolioAllocationsRequest) -> ListPortfolioAllocationsResponse:
        path = f"/portfolios/{request.portfolio_id}/allocations"

        query_params = append_query_param("", 'product_ids', request.product_ids)
        query_params = append_query_param(query_params, 'order_side', request.order_side)

        if request.start_date:
            query_params = append_query_param(query_params, 'start_date', request.start_date.isoformat() + 'Z')
        if request.end_date:
            query_params = append_query_param(query_params, 'end_date', request.end_date.isoformat() + 'Z')

        query_params = append_pagination_params(query_params, request.pagination)

        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListPortfolioAllocationsResponse(**response.json())