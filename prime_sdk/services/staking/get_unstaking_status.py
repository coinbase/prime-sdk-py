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

from ...base_response import BaseResponse
from ...enums import UnstakeEstimateType, UnstakeType
from ...model import GetUnstakingStatusResponse as _GetUnstakingStatusResponse


@dataclass
class UnstakeStatusDetail:
    amount: str
    estimate_type: UnstakeEstimateType
    estimate_description: str
    unstake_type: UnstakeType | None = None
    finishing_at: str | None = None
    remaining_hours: int | None = None
    requested_at: str | None = None


@dataclass
class ValidatorUnstakeStatus:
    validator_address: str
    statuses: list[UnstakeStatusDetail]


@dataclass
class GetUnstakingStatusRequest:
    portfolio_id: str
    wallet_id: str
    allowed_status_codes: list[int] | None = None


@dataclass
class GetUnstakingStatusResponse(BaseResponse, _GetUnstakingStatusResponse):
    __doc__ = _GetUnstakingStatusResponse.__doc__
