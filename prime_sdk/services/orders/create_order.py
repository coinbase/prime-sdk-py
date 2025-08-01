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
from typing import List, Optional
from ...base_response import BaseResponse
from ...enums import OrderSide, OrderType, TimeInForce


@dataclass
class CreateOrderRequest:
    portfolio_id: str
    side: OrderSide
    client_order_id: str
    product_id: str
    type: OrderType
    base_quantity: Optional[str] = None
    quote_value: Optional[str] = None
    limit_price: Optional[str] = None
    start_time: Optional[str] = None
    expiry_time: Optional[str] = None
    time_in_force: Optional[TimeInForce] = None
    stp_id: Optional[str] = None
    display_quote_size: Optional[str] = None
    display_base_size: Optional[str] = None
    is_raise_exact: Optional[str] = None
    historical_pov: Optional[str] = None
    stop_price: Optional[str] = None
    settl_currency: Optional[str] = None
    post_only: Optional[bool] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class CreateOrderResponse(BaseResponse):
    order_id: str = None
