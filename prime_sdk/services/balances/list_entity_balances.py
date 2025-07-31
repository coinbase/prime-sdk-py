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
from typing import List, Optional
from ...base_response import BaseResponse
from ...model import EntityBalance
from ...utils import PaginationParams, Pagination
from ...enums import AggregationType


@dataclass
class ListEntityBalancesRequest:
    entity_id: str
    symbols: Optional[List[str]] = None
    pagination: Optional[PaginationParams] = None
    aggregation_type: Optional[AggregationType] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class ListEntityBalancesResponse(BaseResponse):
    balances: List[EntityBalance] = None
    pagination: Pagination = None
