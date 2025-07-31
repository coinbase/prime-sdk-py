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
from ...utils import to_body_dict
from .create_onchain_address_book_entry import (
    CreateOnchainAddressBookEntryRequest,
    CreateOnchainAddressBookEntryResponse
)
from .delete_onchain_address_group import (
    DeleteOnchainAddressGroupRequest,
    DeleteOnchainAddressGroupResponse
)
from .list_onchain_address_groups import (
    ListOnchainAddressGroupsRequest,
    ListOnchainAddressGroupsResponse
)
from .update_onchain_address_book import (
    UpdateOnchainAddressBookRequest,
    UpdateOnchainAddressBookResponse
)


class OnchainAddressBookService:
    def __init__(self, client: Client):
        self.client = client

    def create_onchain_address_book_entry(self, request: CreateOnchainAddressBookEntryRequest) -> CreateOnchainAddressBookEntryResponse:
        path = f"/portfolios/{request.portfolio_id}/onchain_address_group"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateOnchainAddressBookEntryResponse(**response.json())

    def delete_onchain_address_group(self, request: DeleteOnchainAddressGroupRequest) -> DeleteOnchainAddressGroupResponse:
        path = f"/portfolios/{request.portfolio_id}/onchain_address_group/{request.address_group_id}"
        response = self.client.request("DELETE", path, allowed_status_codes=request.allowed_status_codes)
        return DeleteOnchainAddressGroupResponse(**response.json())

    def list_onchain_address_groups(self, request: ListOnchainAddressGroupsRequest) -> ListOnchainAddressGroupsResponse:
        path = f"/portfolios/{request.portfolio_id}/onchain_address_groups"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return ListOnchainAddressGroupsResponse(**response.json())

    def update_onchain_address_book(self, request: UpdateOnchainAddressBookRequest) -> UpdateOnchainAddressBookResponse:
        path = f"/portfolios/{request.portfolio_id}/onchain_address_group"
        body = to_body_dict(request)
        response = self.client.request("PUT", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return UpdateOnchainAddressBookResponse(**response.json())