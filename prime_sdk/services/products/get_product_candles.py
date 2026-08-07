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
from ...model import GetCandlesRequest as _GetCandlesRequest
from ...model import GetCandlesResponse as _GetCandlesResponse


@dataclass(kw_only=True)
class GetProductCandlesRequest(BaseRequest, _GetCandlesRequest):
    """
    Get Public Product Candles (Beta)

    Attributes:
        portfolio_id: The portfolio id requesting market data.
        product_id: The trading pair.
        start_time: Timestamp for starting range of aggregations
        end_time: Timestamp for ending range of aggregations
        granularity: The timeframe each candle represents.
    """


@dataclass
class GetProductCandlesResponse(BaseResponse, _GetCandlesResponse):
    """
    Candle response structure
    """
