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
from ...model import OrderPreviewRequest as _OrderPreviewRequest
from ...model import PostOrderPreviewResponse as _PostOrderPreviewResponse


@dataclass(kw_only=True)
class CreateOrderPreviewRequest(BaseRequest, _OrderPreviewRequest):
    """
    Get Order Preview

    Attributes:
        portfolio_id: The ID of the portfolio that owns the order
        product_id: The ID of the product being traded for the order (e.g. `BTC-USD`)
        base_quantity: Order size in base asset units (either `base_quantity` or
            `quote_value` is required)
        quote_value: Order size in quote asset units, i.e. the amount the user wants to
            spend (when buying) or receive (when selling); the quantity in base units will
            be determined based on the market liquidity and indicated `quote_value` (either
            `base_quantity` or `quote_value` is required)
        limit_price: The limit price (required for TWAP, VWAP, LIMIT and STOP_LIMIT orders)
        start_time: The start time of the order in UTC (TWAP, VWAP only)
        expiry_time: The expiry time of the order in UTC (TWAP, VWAP, LIMIT and STOP_LIMIT
            GTD only)
        is_raise_exact: Raise Exact order flag
        historical_pov: Historical percentage of volume
        stop_price: Specifies the stop price at which the order activates. The order is
            activated if the last trade price on Coinbase Exchange crosses the stop price
            specified on the order
        settl_currency: The currency in which the settlement will be made
        postOnly: Specifies whether the order is treated as a post only order.
        display_quote_size: The maximum order size that will show up on venue order books
            (in quote currency).
        display_base_size: The maximum order size that will show up on venue order books (in
            base currency).
        offset: Offset value for PEG orders. 0 means peg to BBO. Only non-negative values
            are allowed (PEG orders only)
        wig_level: WIG (Would if Good) level - the best price a pegged order would be placed
            on venues, opposite to limit_price (PEG orders only)
        is_buy_exact: Buy Exact order flag. When true, fees for a BUY order sized in
            quote_value are charged on top of the requested quote_value instead of being
            carved out of it. Only valid for BUY orders sized in quote_value on SPOT
            products.
    """

    stp_id: str | None = None
    post_only: bool | None = None


@dataclass
class CreateOrderPreviewResponse(BaseResponse, _PostOrderPreviewResponse):
    """
    Attributes:
        portfolio_id: The ID of the portfolio that owns the order
        product_id: The ID of the product being traded by the order
        base_quantity: Order size in base asset units (either `base_quantity` or
            `quote_value` is required)
        quote_value: Order size in quote asset units, i.e. the amount the user wants to
            spend (when buying) or receive (when selling); the quantity in base units will
            be determined based on the market liquidity and indicated `quote_value`. Either
            `base_quantity` or `quote_value` is required
        limit_price: The limit price (required for TWAP, VWAP, LIMIT, and STOP_LIMIT orders)
        start_time: The start time of the order in UTC (only applies to TWAP orders.)
        expiry_time: The expiry time of the order in UTC (TWAP, VWAP, LIMIT and STOP_LIMIT
            GTD only). Required for TWAP and VWAP orders if historical_pov is unspecified
        commission: Indicate the total commission paid on this order in quote currency -
            only applicable if the order has any fills
        slippage: How much slippage is expected
        best_bid: Current best bid for order book
        best_ask: Current best ask for order book
        average_filled_price: Indicate expected average filled price based on the current
            order book
        order_total: Order quantity + fees
        historical_pov: The estimated participation rate for a TWAP/VWAP order. This field
            can be specified instead of expiry time, and will be used to compute the expiry
            time of the order based on historical participation rate.
        is_raise_exact: Raise Exact order flag
        stop_price: Stop price for the order
        display_size: The maximum order size that will show up on venue order books.
        display_quote_size: The maximum order size that will show up on venue order books
            (in quote currency).
        display_base_size: The maximum order size that will show up on venue order books (in
            base currency).
        is_buy_exact: Buy Exact order flag
    """

    settl_currency: str = None
    post_only: bool = None
