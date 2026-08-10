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

from ...base_request import BasePaginatedRequest
from ...base_response import BaseResponse
from ...model import GetEntityUsersRequest as _GetEntityUsersRequest
from ...model import GetEntityUsersResponse as _GetEntityUsersResponse


@dataclass(kw_only=True)
class ListEntityUsersRequest(BasePaginatedRequest, _GetEntityUsersRequest):
    """
    List Users

    Attributes:
        entity_id: The entity ID
    """


@dataclass
class ListEntityUsersResponse(BaseResponse, _GetEntityUsersResponse):
    """
    Attributes:
        users: The entity users.
    """
