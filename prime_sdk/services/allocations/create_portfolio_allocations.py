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
from warnings import warn

from ...base_request import BaseRequest
from ...base_response import BaseResponse
from ...model import CreateAllocationRequest as _CreateAllocationRequest
from ...model import CreateAllocationResponse as _CreateAllocationResponse


@dataclass
class AllocationLeg:
    allocation_leg_id: str
    destination_portfolio_id: str
    amount: str
    leg_id: str | None = None

    def __post_init__(self):
        if self.leg_id:
            warn(
                "The 'leg_id' field is deprecated and will be removed in a future version. Use 'allocation_leg_id' instead.",
                DeprecationWarning,
            )
            self.allocation_leg_id = self.leg_id
        else:
            self.leg_id = self.allocation_leg_id


@dataclass(kw_only=True)
class CreatePortfolioAllocationsRequest(BaseRequest, _CreateAllocationRequest):
    """
    Attributes:
        allocation_id: The ID of the allocation
        source_portfolio_id: The source portfolio id for the allocation
        product_id: The product for the allocation
        order_ids: The list of order ids in the allocation
        allocation_legs: The list of allocation_legs for the allocation
        remainder_destination_portfolio: The portfolio where to allocate the remainder of
            the size
    """


@dataclass
class CreatePortfolioAllocationsResponse(BaseResponse, _CreateAllocationResponse):
    """
    Attributes:
        body.success: The success boolean for the post allocation
        body.allocation_id: The allocation id for the post allocation
        body.failure_reason: The failure reason for the post allocation
    """
