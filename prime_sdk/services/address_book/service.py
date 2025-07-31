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
from ...utils import append_query_param, append_pagination_params, to_body_dict
from .create_address_book_entry import CreateAddressBookEntryRequest, CreateAddressBookEntryResponse
from .get_address_book import GetAddressBookRequest, GetAddressBookResponse


class AddressBookService:
    def __init__(self, client: Client):
        self.client = client

    def create_address_book_entry(self, request: CreateAddressBookEntryRequest) -> CreateAddressBookEntryResponse:
        path = f"/portfolios/{request.portfolio_id}/address_book"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateAddressBookEntryResponse(**response.json())

    def get_address_book(self, request: GetAddressBookRequest) -> GetAddressBookResponse:
        path = f"/portfolios/{request.portfolio_id}/address_book"

        query_params = append_query_param("", 'currency_symbol', request.currency_symbol)
        query_params = append_query_param(query_params, 'search', request.search)
        query_params = append_pagination_params(query_params, request.pagination)

        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return GetAddressBookResponse(**response.json())