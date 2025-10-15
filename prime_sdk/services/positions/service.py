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
from prime_sdk.utils import append_pagination_params
from .list_aggregate_entity_positions import (
    ListAggregateEntityPositionsRequest,
    ListAggregateEntityPositionsResponse
)
from .list_entity_positions import (
    ListEntityPositionsRequest,
    ListEntityPositionsResponse
)


class PositionsService:
    def __init__(self, client: Client):
        self.client = client

    def list_aggregate_entity_positions(self, request: ListAggregateEntityPositionsRequest) -> ListAggregateEntityPositionsResponse:
        path = f"/entities/{request.entity_id}/aggregate_positions"
        query_params = append_pagination_params("", request.pagination)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListAggregateEntityPositionsResponse(**response.json())

    def list_entity_positions(self, request: ListEntityPositionsRequest) -> ListEntityPositionsResponse:
        path = f"/entities/{request.entity_id}/positions"
        query_params = append_pagination_params("", request.pagination)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListEntityPositionsResponse(**response.json())