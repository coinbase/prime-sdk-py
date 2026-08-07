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
from ...enums import AggregationType
from ...model import ListEntityBalancesRequest as _ListEntityBalancesRequest
from ...model import ListEntityBalancesResponse as _ListEntityBalancesResponse
from ...utils import PaginationParams


@dataclass
class ListEntityBalancesRequest(_ListEntityBalancesRequest):
    __doc__ = _ListEntityBalancesRequest.__doc__

    entity_id: str
    symbols: list[str] | None = None
    pagination: PaginationParams | None = None
    aggregation_type: AggregationType | None = None
    allowed_status_codes: list[int] | None = None


@dataclass
class ListEntityBalancesResponse(BaseResponse, _ListEntityBalancesResponse):
    __doc__ = _ListEntityBalancesResponse.__doc__
