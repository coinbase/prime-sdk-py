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
from ...enums import OrderSide, OrderType, TimeInForce


@dataclass
class CreateOrderRequest:
    portfolio_id: str
    side: OrderSide
    client_order_id: str
    product_id: str
    type: OrderType
    base_quantity: str | None = None
    quote_value: str | None = None
    limit_price: str | None = None
    start_time: str | None = None
    expiry_time: str | None = None
    time_in_force: TimeInForce | None = None
    stp_id: str | None = None
    display_quote_size: str | None = None
    display_base_size: str | None = None
    is_raise_exact: str | None = None
    historical_pov: str | None = None
    stop_price: str | None = None
    settl_currency: str | None = None
    post_only: bool | None = None
    allowed_status_codes: list[int] | None = None


@dataclass
class CreateOrderResponse(BaseResponse):
    order_id: str = None
