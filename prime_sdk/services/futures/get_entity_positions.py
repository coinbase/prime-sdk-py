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

from ...base_request import BaseCursorLimitPaginatedRequest
from ...base_response import BaseResponse
from ...model import ListEntityPositionsRequest as _ListEntityPositionsRequest
from ...model import ListEntityPositionsResponse as _ListEntityPositionsResponse


@dataclass(kw_only=True)
class GetEntityPositionsRequest(
    BaseCursorLimitPaginatedRequest, _ListEntityPositionsRequest
):
    """
    List Entity Positions

    Attributes:
        entity_id: The unique ID of the entity
    """

    product_id: str | None = None


@dataclass
class GetEntityPositionsResponse(BaseResponse, _ListEntityPositionsResponse):
    """GetEntityPositionsResponse(positions: 'list[Position]' = None, pagination: 'PaginatedResponse' = None)"""

    clearing_account_id: str = None
