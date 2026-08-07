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
from ...model import GetFcmBalanceRequest as _GetFcmBalanceRequest
from ...model import GetFcmBalanceResponse as _GetFcmBalanceResponse


@dataclass(kw_only=True)
class GetEntityFcmBalanceRequest(_GetFcmBalanceRequest):
    """
    Get Entity FCM Balance

    Attributes:
        entity_id: Entity ID
    """

    allowed_status_codes: list[int] | None = None


@dataclass
class GetEntityFcmBalanceResponse(BaseResponse, _GetFcmBalanceResponse):
    """
    Attributes:
        portfolio_id: Portfolio ID
        cfm_usd_balance: CFM USD balance
        unrealized_pnl: Unrealized PNL
        daily_realized_pnl: Daily realized PNL
        excess_liquidity: Excess liquidity
        futures_buying_power: Futures buying power
        initial_margin: Initial margin
        maintenance_margin: Maintenance margin
        clearing_account_id: Clearing account ID
        cfm_unsettled_accrued_funding_pnl: Unsettled accrued funding PNL from the last
            settlement
    """
