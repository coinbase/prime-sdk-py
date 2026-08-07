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

from ...base_response import BaseResponse
from ...model import ListWeb3WalletBalancesRequest as _ListWeb3WalletBalancesRequest
from ...model import ListWeb3WalletBalancesResponse as _ListWeb3WalletBalancesResponse
from ...utils import PaginationParams


@dataclass
class ListWeb3WalletBalancesRequest(_ListWeb3WalletBalancesRequest):
    __doc__ = _ListWeb3WalletBalancesRequest.__doc__

    portfolio_id: str
    wallet_id: str
    visibility_statuses: str | None = None
    pagination: PaginationParams | None = None
    allowed_status_codes: list[int] | None = None


@dataclass
class ListWeb3WalletBalancesResponse(BaseResponse, _ListWeb3WalletBalancesResponse):
    __doc__ = _ListWeb3WalletBalancesResponse.__doc__
