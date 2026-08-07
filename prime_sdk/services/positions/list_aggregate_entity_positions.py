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
from ...model import (
    ListAggregateEntityPositionsRequest as _ListAggregateEntityPositionsRequest,
)
from ...model import (
    ListAggregateEntityPositionsResponse as _ListAggregateEntityPositionsResponse,
)
from ...utils import PaginationParams


@dataclass
class ListAggregateEntityPositionsRequest(_ListAggregateEntityPositionsRequest):
    __doc__ = _ListAggregateEntityPositionsRequest.__doc__

    entity_id: str
    pagination: PaginationParams | None = None
    allowed_status_codes: list[int] | None = None


@dataclass
class ListAggregateEntityPositionsResponse(
    BaseResponse, _ListAggregateEntityPositionsResponse
):
    __doc__ = _ListAggregateEntityPositionsResponse.__doc__
