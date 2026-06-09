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

from ..enums import ProductPermissions, ProductType
from . import FcmTradingSessionDetails, FutureProductDetails, RFQProductDetails


@dataclass(kw_only=True)
class Product:
    id: str | None
    base_increment: str | None
    quote_increment: str | None
    base_min_size: str | None
    quote_min_size: str | None
    base_max_size: str | None
    quote_max_size: str | None
    permissions: List[ProductPermissions] | None
    price_increment: str | None
    rfq_product_details: RFQProductDetails | None
    product_type: ProductType | None
    fcm_trading_session_details: FcmTradingSessionDetails | None
    future_product_details: FutureProductDetails | None
