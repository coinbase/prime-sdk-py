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


@dataclass
class EditOrderRequest:
    portfolio_id: str
    order_id: str
    orig_client_order_id: Optional[str] = None
    client_order_id: Optional[str] = None
    base_quantity: Optional[str] = None
    quote_value: Optional[str] = None
    limit_price: Optional[str] = None
    expiry_time: Optional[str] = None
    display_quote_size: Optional[str] = None
    display_base_size: Optional[str] = None
    stop_price: Optional[str] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class EditOrderResponse(BaseResponse):
    order_id: str = None
