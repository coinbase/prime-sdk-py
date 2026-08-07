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

from ...base_response import BaseResponse
from ...enums import StakeType
from ...model import GetStakingStatusRequest as _GetStakingStatusRequest
from ...model import GetStakingStatusResponse as _GetStakingStatusResponse


@dataclass
class StakingStatus:
    amount: str
    stake_type: StakeType
    estimated_stake_date: str
    estimated_hours_to_stake: int
    requested_at: str | None = None


@dataclass
class ValidatorStakingInfo:
    validator_address: str
    statuses: list[StakingStatus]


@dataclass(kw_only=True)
class GetStakingStatusRequest(_GetStakingStatusRequest):
    """
    Get Staking Status

    Attributes:
        portfolio_id: The portfolio ID
        wallet_id: The wallet ID
    """

    allowed_status_codes: list[int] | None = None


@dataclass
class GetStakingStatusResponse(BaseResponse, _GetStakingStatusResponse):
    """
    Attributes:
        portfolio_id: The portfolio ID
        wallet_id: The wallet ID
        wallet_address: The wallet address
        current_timestamp: Current timestamp at time of API call
        validators: List of validators with staking information for this wallet
    """
