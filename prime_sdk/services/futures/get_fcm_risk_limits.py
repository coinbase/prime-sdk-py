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
from ...model import FcmRiskLimits


@dataclass
class GetFcmRiskLimitsRequest:
    entity_id: str
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class GetFcmRiskLimitsResponse(BaseResponse):
    cfm_risk_limit: str = None
    cfm_risk_limit_utilization: str = None
    cfm_total_margin: str = None
    cfm_delta_ote: str = None
    cfm_unsettled_realized_pnl: str = None
    cfm_unsettled_accrued_funding_pnl: str = None
