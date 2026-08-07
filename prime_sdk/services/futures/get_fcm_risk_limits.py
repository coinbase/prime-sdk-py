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
from ...model import GetFcmRiskLimitsRequest as _GetFcmRiskLimitsRequest
from ...model import GetFcmRiskLimitsResponse as _GetFcmRiskLimitsResponse


@dataclass(kw_only=True)
class GetFcmRiskLimitsRequest(BaseRequest, _GetFcmRiskLimitsRequest):
    """
    Get FCM Risk Limits

    Attributes:
        entity_id: Entity ID
    """


@dataclass
class GetFcmRiskLimitsResponse(BaseResponse, _GetFcmRiskLimitsResponse):
    """
    Attributes:
        cfm_risk_limit: Risk Limit set for a client
        cfm_risk_limit_utilization: Limit utilization calculated based on total margin and
            PnLs
        cfm_total_margin: The total margin required for both positions and open orders
        cfm_delta_ote: Open Trade Equity accrued during the current trading session
        cfm_unsettled_realized_pnl: Unsettled realized PNL for positions closed intraday
        cfm_unsettled_accrued_funding_pnl: Unsettled accrued funding PNL from the last
            settlement
        margin_utilization_percent: Margin utilization as a decimal percentage between 0 and
            1 (e.g. 0.5 means 50%)
    """
