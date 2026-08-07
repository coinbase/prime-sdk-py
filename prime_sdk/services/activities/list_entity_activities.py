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
from ...model import GetEntityActivitiesRequest as _GetEntityActivitiesRequest
from ...model import GetEntityActivitiesResponse as _GetEntityActivitiesResponse
from ...utils import PaginationParams


@dataclass(kw_only=True)
class ListEntityActivitiesRequest(_GetEntityActivitiesRequest):
    __doc__ = _GetEntityActivitiesRequest.__doc__

    pagination: PaginationParams | None = None

    allowed_status_codes: list[int] | None = None


@dataclass
class ListEntityActivitiesResponse(BaseResponse, _GetEntityActivitiesResponse):
    __doc__ = _GetEntityActivitiesResponse.__doc__
