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

from ...base_response import BaseResponse
from ...model import AcceptQuoteRequest as _AcceptQuoteRequest
from ...model import AcceptQuoteResponse as _AcceptQuoteResponse


@dataclass(kw_only=True)
class AcceptQuoteRequest(_AcceptQuoteRequest):
    """
    Accept Quote

    Attributes:
        portfolio_id: The ID of the portfolio that owns the order
        product_id: The ID of the product being traded for the order (e.g. `BTC-USD`)
        client_order_id: A client-generated ID used for reference purposes (note: order will
            be rejected if this ID is not unique among all currently active orders)
        quote_id: A quote id that was returned from the quote request
    """

    portfolio_id: str

    allowed_status_codes: list[int] | None = None


@dataclass
class AcceptQuoteResponse(BaseResponse, _AcceptQuoteResponse):
    """AcceptQuoteResponse(order_id: 'str' = None)"""
