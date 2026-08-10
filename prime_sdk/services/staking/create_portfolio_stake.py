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
from ...model import PortfolioStakingInitiateRequest as _PortfolioStakingInitiateRequest
from ...model import (
    PortfolioStakingInitiateResponse as _PortfolioStakingInitiateResponse,
)


@dataclass
class StakeMetadata:
    external_id: str | None = None


@dataclass(kw_only=True)
class CreatePortfolioStakeRequest(BaseRequest, _PortfolioStakingInitiateRequest):
    """
    Request to stake currency in a portfolio

    Attributes:
        portfolio_id: The portfolio ID
        idempotency_key: The client generated idempotency key (uuid required) for requested
            execution. Subsequent requests using the same key will not create new
            transactions.
        currency_symbol: The currency symbol to stake
        amount: The quantity of the chosen currency to stake
    """


@dataclass
class CreatePortfolioStakeResponse(BaseResponse, _PortfolioStakingInitiateResponse):
    """
    Attributes:
        activity_id: The ID for the created activity
        transaction_id: The ID for the created transaction
    """
