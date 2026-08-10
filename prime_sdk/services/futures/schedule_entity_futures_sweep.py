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
from ...model import ScheduleFuturesSweepRequest as _ScheduleFuturesSweepRequest
from ...model import ScheduleFuturesSweepResponse as _ScheduleFuturesSweepResponse


@dataclass(kw_only=True)
class ScheduleEntityFuturesSweepRequest(BaseRequest, _ScheduleFuturesSweepRequest):
    """
    Schedule Entity Futures Sweep

    Attributes:
        entity_id: Entity ID
        amount: Amount. Default to sweep all if not provided
        currency: Currency. Required
    """


@dataclass
class ScheduleEntityFuturesSweepResponse(BaseResponse, _ScheduleFuturesSweepResponse):
    """
    Attributes:
        success: Success
        request_id: Request ID
    """
