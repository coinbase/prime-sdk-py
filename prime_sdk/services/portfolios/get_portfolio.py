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
from ...model import GetPortfolioRequest as _GetPortfolioRequest
from ...model import GetPortfolioResponse as _GetPortfolioResponse


@dataclass(kw_only=True)
class GetPortfolioRequest(BaseRequest, _GetPortfolioRequest):
    """
    Get Portfolio by Portfolio ID

    Attributes:
        portfolio_id: The portfolio ID
    """


@dataclass
class GetPortfolioResponse(BaseResponse, _GetPortfolioResponse):
    """
    Attributes:
        portfolio.id: The unique ID of the portfolio
        portfolio.name: The name of the portfolio
        portfolio.entity_id: The ID of the entity to which the portfolio is associated
        portfolio.organization_id: The ID of the organization to which the portfolio is
            associated
        portfolio.entity_name: The name of the entity to which the portfolio is associated
    """
