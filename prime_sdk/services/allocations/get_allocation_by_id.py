# Copyright 2024-present Coinbase Global, Inc.
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
from ...model import GetAllocationRequest as _GetAllocationRequest
from ...model import GetAllocationResponse as _GetAllocationResponse


@dataclass(kw_only=True)
class GetAllocationByIdRequest(_GetAllocationRequest):
    """
    Get Allocation by ID

    Attributes:
        portfolio_id: The portfolio ID of the allocation
        allocation_id: The ID of the allocation
    """

    allowed_status_codes: list[int] | None = None


@dataclass
class GetAllocationByIdResponse(BaseResponse, _GetAllocationResponse):
    """GetAllocationByIdResponse(allocation: 'Allocation' = None)"""
