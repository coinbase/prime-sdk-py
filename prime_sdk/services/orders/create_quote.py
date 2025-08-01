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
from ...base_response import BaseResponse
from ...enums import OrderSide


@dataclass
class CreateQuoteRequest:
    portfolio_id: str
    product_id: str
    side: OrderSide
    client_quote_id: str
    limit_price: str
    base_quantity: Optional[str] = None
    quote_value: Optional[str] = None
    settl_currency: Optional[str] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class CreateQuoteResponse(BaseResponse):
    quote_id: str = None
    expiration_time: str = None
    best_price: str = None
    order_total: str = None
    price_inclusive_of_fees: str = None