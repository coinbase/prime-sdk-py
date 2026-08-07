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
from ...model import GetOrdersRequest as _GetOrdersRequest
from ...model import GetOrdersResponse as _GetOrdersResponse
from ...utils import PaginationParams


@dataclass(kw_only=True)
class ListOrdersRequest(_GetOrdersRequest):
    """
    List Portfolio Orders

    Attributes:
        portfolio_id: Portfolio ID
        order_statuses: List of statuses by which to filter the response -
            UNKNOWN_ORDER_STATUS: nil value - OPEN: The order is open but unfilled - FILLED:
            The order was filled - CANCELLED: The order was cancelled - EXPIRED: The order
            has expired - FAILED: Order submission failed - PENDING: The order has been sent
            but is not yet confirmed
        product_ids: List of products by which to filter the response
        order_type: Order type by which to filter the response - UNKNOWN_ORDER_TYPE: nil
            value - MARKET: A [market
            order](https://en.wikipedia.org/wiki/Order_(exchange)#Market_order) - LIMIT: A
            [limit order](https://en.wikipedia.org/wiki/Order_(exchange)#Limit_order) -
            TWAP: A [time-weighted average price order](https://en.wikipedia.org/wiki/Time-
            weighted_average_price) - BLOCK: A [block
            trade](https://en.wikipedia.org/wiki/Block_trade) - VWAP: A [volume-weighted
            average price order](https://en.wikipedia.org/wiki/Volume-
            weighted_average_price) - STOP_LIMIT: A [conditional order combined of stop
            order and limit order](https://en.wikipedia.org/wiki/Order_(exchange)#Stop-
            limit_order) - RFQ: A [request for
            quote](https://en.wikipedia.org/wiki/Request_for_quote) - PEG: A pegged order
            that dynamically adjust based on market conditions while maintaining execution
            discretion and avoiding adverse selection
        order_side: An order side to filter on. - UNKNOWN_ORDER_SIDE: nil value - BUY: Buy
            order - SELL: Sell order
        start_date: A start date for the orders to be queried from
        end_date: An end date for the orders to be queried from
    """

    pagination: PaginationParams | None = None

    allowed_status_codes: list[int] | None = None


@dataclass
class ListOrdersResponse(BaseResponse, _GetOrdersResponse):
    """
    Attributes:
        orders: List of orders
    """
