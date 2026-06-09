# Copyright 2026-present Coinbase Global, Inc.
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

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from ..enums import OrderSide, OrderStatus, OrderType, ProductType, TimeInForceType
from . import CommissionDetailTotal, OrderEdit


@dataclass(kw_only=True)
class Order:
    id: str | None
    user_id: str | None
    portfolio_id: str | None
    product_id: str | None
    side: OrderSide | None
    client_order_id: str | None
    type: OrderType | None
    base_quantity: str | None
    quote_value: str | None
    limit_price: str | None
    start_time: str | None
    expiry_time: str | None
    status: OrderStatus | None
    time_in_force: TimeInForceType | None
    created_at: str | None
    filled_quantity: str | None
    filled_value: str | None
    average_filled_price: str | None
    commission: str | None
    exchange_fee: str | None
    historical_pov: str | None
    stop_price: str | None
    net_average_filled_price: str | None
    user_context: str | None
    client_product_id: str | None
    post_only: bool | None
    order_edit_history: List[OrderEdit] | None
    is_raise_exact: bool | None
    display_size: str | None
    edit_history: List[OrderEdit] | None
    display_quote_size: str | None
    display_base_size: str | None
    peg_offset_type: str | None
    offset: str | None
    wig_level: str | None
    product_type: ProductType | None
    commission_detail_total: CommissionDetailTotal | None
