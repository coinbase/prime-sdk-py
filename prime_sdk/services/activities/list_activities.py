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
from datetime import datetime

from ...base_response import BaseResponse
from ...model import GetPortfolioActivitiesResponse as _GetPortfolioActivitiesResponse
from ...utils import PaginationParams


@dataclass
class ListActivitiesRequest:
    portfolio_id: str
    symbols: str | None = None
    categories: str | None = None
    statuses: str | None = None
    start_time: datetime | None = None
    end_time: datetime | None = None
    pagination: PaginationParams | None = None
    allowed_status_codes: list[int] | None = None


@dataclass
class ListActivitiesResponse(BaseResponse, _GetPortfolioActivitiesResponse):
    __doc__ = _GetPortfolioActivitiesResponse.__doc__
