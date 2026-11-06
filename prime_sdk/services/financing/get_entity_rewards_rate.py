# Copyright 2026-present Coinbase Global, Inc.
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
from ...model import GetEntityRewardsRateRequest as _GetEntityRewardsRateRequest
from ...model import GetRewardsRateResponse as _GetRewardsRateResponse


@dataclass(kw_only=True)
class GetEntityRewardsRateRequest(BaseRequest, _GetEntityRewardsRateRequest):
    """
    Get Entity Rewards Rate (Beta)

    Attributes:
        entity_id: The ID of the Prime entity whose rewards rate information is requested.
    """


@dataclass
class GetEntityRewardsRateResponse(BaseResponse, _GetRewardsRateResponse):
    """
    GetRewardsRateResponse returns the current rewards rate and the available rates.

    Attributes:
        current_rate: The current effective rewards rate.
        available_rates: All available rewards rates, including qualifying bounds for each
            rate.
    """
