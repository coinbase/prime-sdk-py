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


@dataclass
class GetStakingStatusRequest:
    portfolio_id: str
    wallet_id: str
    allowed_status_codes: list[int] | None = None


@dataclass
class GetStakingStatusResponse(BaseResponse):
    portfolio_id: str = None
    wallet_id: str = None
    wallet_address: str = None
    current_timestamp: str = None
    validators: list[ValidatorStakingInfo] = None
