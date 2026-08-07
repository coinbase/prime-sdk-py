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
from ...model import GetPostTradeCreditRequest as _GetPostTradeCreditRequest
from ...model import GetPostTradeCreditResponse as _GetPostTradeCreditResponse


@dataclass(kw_only=True)
class GetPortfolioCreditInformationRequest(BaseRequest, _GetPostTradeCreditRequest):
    """
    Get Portfolio Credit Information

    Attributes:
        portfolio_id: The portfolio ID
    """


@dataclass
class GetPortfolioCreditInformationResponse(BaseResponse, _GetPostTradeCreditResponse):
    """
    Attributes:
        post_trade_credit.portfolio_id: The unique ID of the portfolio
        post_trade_credit.currency: The currency symbol credit is denoted in
        post_trade_credit.limit: The maximum credit limit
        post_trade_credit.utilized: The amount of credit used
        post_trade_credit.available: The amount of credit available
        post_trade_credit.frozen: Whether or not a portfolio is frozen due to balance
            outstanding or other reason
        post_trade_credit.frozen_reason: The reason why the portfolio is frozen
        post_trade_credit.enabled: Whether the portfolio has credit enabled
        post_trade_credit.adjusted_credit_utilized: The amount of adjusted credit used
        post_trade_credit.adjusted_portfolio_equity: The amount of adjusted portfolio equity
    """
