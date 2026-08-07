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

from dataclasses import dataclass

from ...base_response import BaseResponse
from ...model import GetWalletsRequest as _GetWalletsRequest
from ...model import GetWalletsResponse as _GetWalletsResponse
from ...utils import PaginationParams


@dataclass(kw_only=True)
class ListWalletsRequest(_GetWalletsRequest):
    """
    List Portfolio Wallets

    Attributes:
        portfolio_id: The portfolio ID
        type: The wallet type - VAULT: A crypto vault - TRADING: A trading wallet -
            WALLET_TYPE_OTHER: Other wallet types (like consumer, etc) - QC: A QC Wallet -
            ONCHAIN: An Onchain wallet
        symbols: The wallet symbol
        get_network_unified_wallets: Flag to request retrieval of all wallets across all
            networks for a given symbol
    """

    pagination: PaginationParams | None = None

    allowed_status_codes: list[int] | None = None


@dataclass
class ListWalletsResponse(BaseResponse, _GetWalletsResponse):
    """ListWalletsResponse(wallets: 'list[Wallet]' = None, pagination: 'PaginatedResponse' = None)"""
