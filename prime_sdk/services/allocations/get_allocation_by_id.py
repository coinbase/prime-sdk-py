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

from ...base_request import BaseRequest
from ...base_response import BaseResponse
from ...model import GetAllocationRequest as _GetAllocationRequest
from ...model import GetAllocationResponse as _GetAllocationResponse


@dataclass(kw_only=True)
class GetAllocationByIdRequest(BaseRequest, _GetAllocationRequest):
    """
    Get Allocation by ID

    Attributes:
        portfolio_id: The portfolio ID of the allocation
        allocation_id: The ID of the allocation
    """


@dataclass
class GetAllocationByIdResponse(BaseResponse, _GetAllocationResponse):
    """
    Attributes:
        allocation.root_id: The ID that ties together an allocation and all of its legs.
        allocation.reversal_id: The ID of the allocation if this allocation is a reversal.
            In this case, the root_id would be the original allocation ID.
        allocation.allocation_completed_at: Time the final leg of the root allocation was
            completed.
        allocation.user_id: The ID of the user that created the allocation.
        allocation.product_id: The ID of the product of the orders allocated.
        allocation.avg_price: Price the allocation was done at.
        allocation.base_quantity: Amount allocated in base asset units.
        allocation.quote_value: Amount allocated in quote asset units.
        allocation.fees_allocated: Fees from original trade execution allocated in quote
            asset units.
        allocation.source: Portfolio ID of the source portfolio.
        allocation.order_ids: All order IDs that were aggregated to calculate the avg_price,
            quantity to allocate in each leg. Each order_id should tie back to the single
            allocation root_id.
        allocation.destinations: Array of objects, each containing the leg ID, destination
            portfolio ID and amount in chosen units allocated to each portfolio: [{leg_id,
            portfolio_id, allocation_base, allocation_quote}, {leg_id, portfolio_id,
            allocation_base, allocation_quote}...]
        allocation.netting_id: The netting ID of the allocation, not empty if the allocation
            was submitted as part of a net allocation
    """
