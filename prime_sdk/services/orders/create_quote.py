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

from ...base_request import BaseRequest
from ...base_response import BaseResponse
from ...model import CreateQuoteRequest as _CreateQuoteRequest
from ...model import QuoteResponse as _QuoteResponse


@dataclass(kw_only=True)
class CreateQuoteRequest(BaseRequest, _CreateQuoteRequest):
    """
    Create Quote Request

    Attributes:
        portfolio_id: The ID of the portfolio that owns the order
        product_id: The ID of the product being traded for the order (e.g. `BTC-USD`)
        client_quote_id: A client-generated order ID used for reference purposes (note:
            order will be rejected if this ID is not unique among all currently active
            orders)
        base_quantity: Order size in base asset units (either `base_quantity` or
            `quote_value` is required)
        quote_value: Order size in quote asset units, i.e. the amount the user wants to
            spend (when buying) or receive (when selling); the quantity in base units will
            be determined based on the market liquidity and indicated `quote_value` (either
            `base_quantity` or `quote_value` is required)
        limit_price: The limit price
        settl_currency: The currency in which the settlement will be made
        quote_duration_ms: Optional quote timeout in milliseconds. Defaults to 3000 ms (3
            seconds) if not specified. Maximum allowed value is 30000 ms (30 seconds);
            requests with a larger value are rejected. Mirrors FIX tag 8090
            (QuoteRequestGoodForMs).
    """

    portfolio_id: str


@dataclass
class CreateQuoteResponse(BaseResponse, _QuoteResponse):
    """
    Copied from https://github.cbhq.net/institutional/trading/blob/3e6da61aceb64c7cbe6f0c0f8fbdb98fd3e868dc/proxy/trading/protos/coinbase/brokerage/proxy/trading/api/orderentry.proto#L366-L370

    Attributes:
        order_total: total quote amount for previewing
        quote_duration_ms: Echo of the quote_duration_ms supplied in the request. 0 if the
            client did not supply a value, in which case the server applies the default of
            3000 ms (3 seconds).
    """
