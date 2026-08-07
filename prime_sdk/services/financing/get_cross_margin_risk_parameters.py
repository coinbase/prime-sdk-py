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
from ...model import (
    GetCrossMarginRiskParametersRequest as _GetCrossMarginRiskParametersRequest,
)
from ...model import (
    GetCrossMarginRiskParametersResponse as _GetCrossMarginRiskParametersResponse,
)


@dataclass(kw_only=True)
class GetCrossMarginRiskParametersRequest(
    BaseRequest, _GetCrossMarginRiskParametersRequest
):
    """
    Get Cross Margin Risk Parameters

    Attributes:
        entity_id: XM customer Prime Entity ID.
    """


@dataclass
class GetCrossMarginRiskParametersResponse(
    BaseResponse, _GetCrossMarginRiskParametersResponse
):
    """
    Attributes:
        risk_parameters: Current XM tier risk parameters for the entity's client tier.
        offset_credit_matrix_long_short: Offset credit rate matrix for long/short tier
            pairs.
        offset_credit_matrix_long_long: Offset credit rate matrix for long/long tier pairs.
        offset_credit_matrix_short_short: Offset credit rate matrix for short/short tier
            pairs.
        margin_period_of_risk: Margin period of risk (number of days).
    """
