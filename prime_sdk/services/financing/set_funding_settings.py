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
from ...model import UpdateFundingSettingsRequest as _UpdateFundingSettingsRequest
from ...model import UpdateFundingSettingsResponse as _UpdateFundingSettingsResponse


@dataclass(kw_only=True)
class SetFundingSettingsRequest(BaseRequest, _UpdateFundingSettingsRequest):
    """
    Update Funding Settings

    Attributes:
        entity_id: Prime Entity ID
        designated_funding_portfolio_id: Set the Derivatives Funding Portfolio that will be
            used to fund FCM margin calls and receive excess margin sweeps. Only one
            portfolio per entity.
        automatic_conversion_enabled: When true, USDC in your Derivatives Funding Portfolio
            will be converted to USD to meet FCM margin calls (Auto-Convert USDC).
        automatic_loan_enabled: Deprecated: Auto-Initiate Loans is now always enabled for
            Financing customers. Any value sent for this field is ignored.
        automatic_excess_return_enabled: When true, any FCM account balance above your
            margin requirements will be automatically swept back to your Derivatives funding
            portfolio. (Auto-Return Excess Margin)
        excess_funds_target_amount: Weekend Buying Power: Setting a target amount to
            maintain in your Futures account above margin requirements. You can only
            withdraw funds in excess of this amount.
    """


@dataclass
class SetFundingSettingsResponse(BaseResponse, _UpdateFundingSettingsResponse):
    """
    Attributes:
        activity_id: Identifier for the created activity / proposal
        activity_type: Type of the activity (e.g. PCS proposal type)
        num_approvals_remaining: Number of approvals still required before the change
            applies
    """
