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
from typing import List, Optional
from ...base_response import BaseResponse
from ...enums import UnstakeEstimateType, UnstakeType


@dataclass
class UnstakeStatusDetail:
    amount: str
    estimate_type: UnstakeEstimateType
    estimate_description: str
    unstake_type: Optional[UnstakeType] = None
    finishing_at: Optional[str] = None
    remaining_hours: Optional[int] = None
    requested_at: Optional[str] = None


@dataclass
class ValidatorUnstakeStatus:
    validator_address: str
    statuses: List[UnstakeStatusDetail]


@dataclass
class GetUnstakingStatusRequest:
    portfolio_id: str
    wallet_id: str
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class GetUnstakingStatusResponse(BaseResponse):
    portfolio_id: str = None
    wallet_id: str = None
    wallet_address: str = None
    current_timestamp: str = None
    validators: List[ValidatorUnstakeStatus] = None
