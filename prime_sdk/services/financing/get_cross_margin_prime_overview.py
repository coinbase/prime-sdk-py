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
    GetCrossMarginPrimeOverviewRequest as _GetCrossMarginPrimeOverviewRequest,
)
from ...model import (
    GetCrossMarginPrimeOverviewResponse as _GetCrossMarginPrimeOverviewResponse,
)


@dataclass(kw_only=True)
class GetCrossMarginPrimeOverviewRequest(
    BaseRequest, _GetCrossMarginPrimeOverviewRequest
):
    """
    Get Prime Cross Margin Overview

    Attributes:
        entity_id: Prime entity ID for the XM (cross-margin) customer.
    """


@dataclass
class GetCrossMarginPrimeOverviewResponse(
    BaseResponse, _GetCrossMarginPrimeOverviewResponse
):
    """
    Attributes:
        evaluated_at: When margin metrics were evaluated.
    """
