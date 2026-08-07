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
from ...model import GetOpenOrdersRequest as _GetOpenOrdersRequest
from ...model import GetOpenOrdersResponse as _GetOpenOrdersResponse


@dataclass(kw_only=True)
class ListOpenOrdersRequest(_GetOpenOrdersRequest):
    __doc__ = _GetOpenOrdersRequest.__doc__

    order_statuses: str | None = None

    allowed_status_codes: list[int] | None = None


@dataclass
class ListOpenOrdersResponse(BaseResponse, _GetOpenOrdersResponse):
    __doc__ = _GetOpenOrdersResponse.__doc__
