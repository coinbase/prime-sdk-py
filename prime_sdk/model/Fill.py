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

from ..enums import OrderSide, ProductType
from . import CommissionDetailTotal


@dataclass(kw_only=True)
class Fill:
    id: str | None
    order_id: str | None
    product_id: str | None
    client_product_id: str | None
    side: OrderSide | None
    filled_quantity: str | None
    filled_value: str | None
    price: str | None
    time: str | None
    commission: str | None
    venue: str | None
    venue_fees: str | None
    ces_commission: str | None
    product_type: ProductType | None
    commission_detail_total: CommissionDetailTotal | None
