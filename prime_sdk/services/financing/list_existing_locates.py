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

from ...base_response import BaseResponse
from ...model import GetExistingLocatesRequest as _GetExistingLocatesRequest
from ...model import GetExistingLocatesResponse as _GetExistingLocatesResponse


@dataclass(kw_only=True)
class ListExistingLocatesRequest(_GetExistingLocatesRequest):
    """
    List Existing Locates

    Attributes:
        portfolio_id: The unique ID of the portfolio
        locate_ids: The IDs of specific locates to filter for
        conversion_date: Deprecated: Use locate_date instead
        locate_date: The date of the locates in YYYY-MM-DD format
    """

    allowed_status_codes: list[int] | None = None


@dataclass
class ListExistingLocatesResponse(BaseResponse, _GetExistingLocatesResponse):
    """ListExistingLocatesResponse(locates: 'list[ExistingLocate]' = None)"""
