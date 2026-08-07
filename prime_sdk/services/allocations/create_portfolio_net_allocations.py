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
from ...model import CreateNetAllocationRequest as _CreateNetAllocationRequest
from ...model import CreateNetAllocationResponse as _CreateNetAllocationResponse


@dataclass
class NetAllocationLeg:
    allocation_leg_id: str
    destination_portfolio_id: str
    amount: str


@dataclass(kw_only=True)
class CreatePortfolioNetAllocationsRequest(_CreateNetAllocationRequest):
    """
    Attributes:
        source_portfolio_id: The source portfolio id for the allocation
        product_id: The product for the allocation
        order_ids: The list of order ids in the allocation
        allocation_legs: The list of allocation_legs for the allocation
        remainder_destination_portfolio: The portfolio where to allocate the remainder of
            the size
        netting_id: The ID to identify an in-flight net allocation.
    """

    allocation_id: str
    remainder_destination_portfolio_id: str

    allowed_status_codes: list[int] | None = None


@dataclass
class CreatePortfolioNetAllocationsResponse(BaseResponse, _CreateNetAllocationResponse):
    """CreatePortfolioNetAllocationsResponse(body: 'CreateNetAllocationResponseBody' = None)"""
