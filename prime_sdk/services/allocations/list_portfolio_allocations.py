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
from ...model import GetPortfolioAllocationsRequest as _GetPortfolioAllocationsRequest
from ...model import GetPortfolioAllocationsResponse as _GetPortfolioAllocationsResponse
from ...utils import PaginationParams


@dataclass(kw_only=True)
class ListPortfolioAllocationsRequest(_GetPortfolioAllocationsRequest):
    """
    List Portfolio Allocations

    Attributes:
        portfolio_id: Portfolio to retrieve allocations for.
        product_ids: List of products by which to filter the response.
        order_side: An order side to filter allocations on. - UNKNOWN_ORDER_SIDE: nil value
            - BUY: Buy order - SELL: Sell order
        start_date: A start date for the allocations to be queried from.
        end_date: An end date for the orders to be queried from.
    """

    pagination: PaginationParams | None = None

    allowed_status_codes: list[int] | None = None


@dataclass
class ListPortfolioAllocationsResponse(BaseResponse, _GetPortfolioAllocationsResponse):
    """
    Attributes:
        allocations: List of allocations.
    """
