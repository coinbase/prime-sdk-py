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
from typing import List, Optional
from warnings import warn
from ...base_response import BaseResponse
from ...enums import SizeType


@dataclass
class AllocationLeg:
    allocation_leg_id: str
    destination_portfolio_id: str
    amount: str
    leg_id: Optional[str] = None

    def __post_init__(self):
        if self.leg_id:
            warn("The 'leg_id' field is deprecated and will be removed in a future version. Use 'allocation_leg_id' instead.", DeprecationWarning)
            self.allocation_leg_id = self.leg_id
        else:
            self.leg_id = self.allocation_leg_id


@dataclass
class CreatePortfolioAllocationsRequest:
    allocation_id: str
    source_portfolio_id: str
    product_id: str
    order_ids: List[str]
    allocation_legs: List[AllocationLeg]
    size_type: SizeType
    remainder_destination_portfolio_id: str
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class CreatePortfolioAllocationsResponse(BaseResponse):
    success: bool = None
    allocation_id: str = None
    failure_reason: str = None
