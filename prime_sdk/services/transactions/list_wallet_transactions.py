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
from datetime import datetime

from ...base_response import BaseResponse
from ...model import GetWalletTransactionsRequest as _GetWalletTransactionsRequest
from ...model import GetWalletTransactionsResponse as _GetWalletTransactionsResponse
from ...utils import PaginationParams


@dataclass(kw_only=True)
class ListWalletTransactionsRequest(_GetWalletTransactionsRequest):
    __doc__ = _GetWalletTransactionsRequest.__doc__

    start: datetime | None = None
    end: datetime | None = None
    pagination: PaginationParams | None = None

    allowed_status_codes: list[int] | None = None


@dataclass
class ListWalletTransactionsResponse(BaseResponse, _GetWalletTransactionsResponse):
    __doc__ = _GetWalletTransactionsResponse.__doc__
