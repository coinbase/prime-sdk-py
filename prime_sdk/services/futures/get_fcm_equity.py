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
from ...model import GetFcmEquityRequest as _GetFcmEquityRequest
from ...model import GetFcmEquityResponse as _GetFcmEquityResponse


@dataclass(kw_only=True)
class GetFcmEquityRequest(_GetFcmEquityRequest):
    """
    Get FCM Equity

    Attributes:
        entity_id: Entity ID
    """

    allowed_status_codes: list[int] | None = None


@dataclass
class GetFcmEquityResponse(BaseResponse, _GetFcmEquityResponse):
    """
    Attributes:
        eod_account_equity: Prior EOD account equity (ending balance + realized P&L +
            commissions/fees)
        eod_unrealized_pnl: Prior EOD unrealized P&L on open futures positions
        current_excess_deficit: Current Derivatives Account Balance minus prior EOD margin
            requirement. (Positive = excess; negative = deficit)
        available_to_sweep: Excess funds in the Derivatives account available to transfer
            ("sweep") to the designated funding portfolio
    """
