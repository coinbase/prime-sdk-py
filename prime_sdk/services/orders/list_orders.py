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
from typing import List, Optional
from datetime import datetime
from ...base_response import BaseResponse
from ...enums import OrderSide, OrderType
from ...utils import PaginationParams, Pagination
from ...model import Order


@dataclass
class ListOrdersRequest:
    portfolio_id: str
    order_statuses: Optional[str] = None
    product_ids: Optional[str] = None
    order_type: Optional[OrderType] = None
    order_side: Optional[OrderSide] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    pagination: Optional[PaginationParams] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class ListOrdersResponse(BaseResponse):
    orders: List[Order] = None
    pagination: Pagination = None