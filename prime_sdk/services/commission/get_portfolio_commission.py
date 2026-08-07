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

from ...base_request import BaseRequest
from ...base_response import BaseResponse
from ...model import GetPortfolioCommissionRequest as _GetPortfolioCommissionRequest
from ...model import GetPortfolioCommissionResponse as _GetPortfolioCommissionResponse


@dataclass(kw_only=True)
class GetPortfolioCommissionRequest(BaseRequest, _GetPortfolioCommissionRequest):
    """
    Get Portfolio Commission

    Attributes:
        product_id: Specific trading pair to check commission (e.g BTC-USD)
    """


@dataclass
class GetPortfolioCommissionResponse(BaseResponse, _GetPortfolioCommissionResponse):
    """
    Attributes:
        commission.type: Fee model (all_in or cost_plus)
        commission.rate: Commission rate (in whole percentage. Commission of 15bps is
            "0.0015")
        commission.trading_volume: Average 30 days over past 3 months (e.g. 90 days divided
            by 3)
    """
