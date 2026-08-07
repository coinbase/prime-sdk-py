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
from ...enums import OrderSide, OrderType
from ...model import GetOrdersResponse as _GetOrdersResponse
from ...utils import PaginationParams


@dataclass
class ListOrdersRequest:
    portfolio_id: str
    order_statuses: str | None = None
    product_ids: str | None = None
    order_type: OrderType | None = None
    order_side: OrderSide | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    pagination: PaginationParams | None = None
    allowed_status_codes: list[int] | None = None


@dataclass
class ListOrdersResponse(BaseResponse, _GetOrdersResponse):
    __doc__ = _GetOrdersResponse.__doc__
