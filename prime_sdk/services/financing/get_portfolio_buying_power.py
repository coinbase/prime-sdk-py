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
from ...model import GetBuyingPowerRequest as _GetBuyingPowerRequest
from ...model import GetBuyingPowerResponse as _GetBuyingPowerResponse


@dataclass(kw_only=True)
class GetBuyingPowerRequest(BaseRequest, _GetBuyingPowerRequest):
    """
    Get Portfolio Buying Power

    Attributes:
        portfolio_id: The unique ID of the portfolio
        base_currency: The symbol for the base currency
        quote_currency: The symbol for the quote currency
    """


@dataclass
class GetBuyingPowerResponse(BaseResponse, _GetBuyingPowerResponse):
    """
    Attributes:
        buying_power.portfolio_id: The unique ID of the portfolio
        buying_power.base_currency: The symbol for the base currency
        buying_power.quote_currency: The symbol for the quote currency
        buying_power.base_buying_power: The buying power for the base currency
        buying_power.quote_buying_power: The buying power for the quote currency
    """
