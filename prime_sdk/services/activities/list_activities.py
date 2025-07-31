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
from datetime import datetime
from ...base_response import BaseResponse
from ...model import Activity
from ...utils import PaginationParams, Pagination


@dataclass
class ListActivitiesRequest:
    portfolio_id: str
    symbols: Optional[str] = None
    categories: Optional[str] = None
    statuses: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    pagination: Optional[PaginationParams] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class ListActivitiesResponse(BaseResponse):
    activities: List[Activity] = None
    pagination: Pagination = None
