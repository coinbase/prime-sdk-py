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

from ...client import Client
from ...utils import append_query_param, append_pagination_params
from .list_invoices import (
    ListInvoicesRequest,
    ListInvoicesResponse
)


class InvoicesService:
    def __init__(self, client: Client):
        self.client = client

    def list_invoices(self, request: ListInvoicesRequest) -> ListInvoicesResponse:
        path = f"/entities/{request.entity_id}/invoices"
        query_params = append_query_param("", 'states', request.states)
        query_params = append_query_param(query_params, 'billing_year', request.billing_year)
        query_params = append_query_param(query_params, 'billing_month', request.billing_month)
        query_params = append_pagination_params(query_params, request.pagination)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListInvoicesResponse(**response.json())