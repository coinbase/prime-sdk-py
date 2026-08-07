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
from ...model import ListEntityBalancesRequest as _ListEntityBalancesRequest
from ...model import ListEntityBalancesResponse as _ListEntityBalancesResponse
from ...utils import PaginationParams


@dataclass(kw_only=True)
class ListEntityBalancesRequest(_ListEntityBalancesRequest):
    """
    List Entity Balances

    Attributes:
        entity_id: The entity ID
        symbols: A list of symbols by which to filter the response
        aggregation_type: A type by which to filter aggregated balances, defaults to "TOTAL"
            - UNKNOWN_BALANCE_TYPE: nil - TRADING_BALANCES: Trading balances -
            VAULT_BALANCES: Vault balances - TOTAL_BALANCES: Total balances (The sum of
            vault and trading + prime custody) - PRIME_CUSTODY_BALANCES: Prime custody
            balances - UNIFIED_TOTAL_BALANCES: Unified total balance across networks and
            wallet types (vault + trading + prime custody)
    """

    pagination: PaginationParams | None = None

    allowed_status_codes: list[int] | None = None


@dataclass
class ListEntityBalancesResponse(BaseResponse, _ListEntityBalancesResponse):
    """ListEntityBalancesResponse(balances: 'list[EntityBalance]' = None, pagination: 'PaginatedResponse' = None)"""
