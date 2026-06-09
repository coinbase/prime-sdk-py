# Copyright 2026-present Coinbase Global, Inc.
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

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from ..enums import AllocationStatus, OrderSide
from . import DestinationAlloc


@dataclass(kw_only=True)
class Allocation:
    root_id: str | None
    reversal_id: str | None
    allocation_completed_at: str | None
    user_id: str | None
    product_id: str | None
    side: OrderSide | None
    avg_price: str | None
    base_quantity: str | None
    quote_value: str | None
    fees_allocated: str | None
    status: AllocationStatus | None = AllocationStatus.ALLOCATION_STATUS_UNSPECIFIED
    source: str | None
    order_ids: List[str] | None
    destinations: List[DestinationAlloc] | None
    netting_id: str | None
