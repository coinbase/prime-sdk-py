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
from ...model import CancelFuturesSweepRequest as _CancelFuturesSweepRequest
from ...model import CancelFuturesSweepResponse as _CancelFuturesSweepResponse


@dataclass(kw_only=True)
class CancelEntityFuturesSweepRequest(BaseRequest, _CancelFuturesSweepRequest):
    """
    Cancel Entity Futures Sweep

    Attributes:
        entity_id: Entity ID
    """


@dataclass
class CancelEntityFuturesSweepResponse(BaseResponse, _CancelFuturesSweepResponse):
    """
    Attributes:
        success: Success
        request_id: Request ID
    """
