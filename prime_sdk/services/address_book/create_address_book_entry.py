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

from dataclasses import dataclass

from ...base_request import BaseRequest
from ...base_response import BaseResponse
from ...model import (
    CreatePortfolioAddressBookEntryRequest as _CreatePortfolioAddressBookEntryRequest,
)
from ...model import (
    CreatePortfolioAddressBookEntryResponse as _CreatePortfolioAddressBookEntryResponse,
)


@dataclass(kw_only=True)
class CreateAddressBookEntryRequest(
    BaseRequest, _CreatePortfolioAddressBookEntryRequest
):
    """
    Create Address Book Entry

    Attributes:
        portfolio_id: Portfolio ID
        address: Crypto address to add
        currency_symbol: Currency symbol of address to add
        name: Name of address book entry
        account_identifier: Account Identifier (memo/destination tag)
        chain_ids: List of compatible chain IDs for the address, empty for Solana
    """


@dataclass
class CreateAddressBookEntryResponse(
    BaseResponse, _CreatePortfolioAddressBookEntryResponse
):
    """CreateAddressBookEntryResponse(activity_type: 'str' = None, num_approvals_remaining: 'str' = None, activity_id: 'str' = None)"""
