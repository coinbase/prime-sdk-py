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
from ...model import GetMarginConversionsRequest as _GetMarginConversionsRequest
from ...model import GetMarginConversionsResponse as _GetMarginConversionsResponse


@dataclass(kw_only=True)
class ListMarginConversionsRequest(_GetMarginConversionsRequest):
    """
    List Margin Conversions

    Attributes:
        portfolio_id: The unique ID of the portfolio
        start_date: The start date of the range to query for in RFC3339 format
        end_date: The end date of the range to query for in RFC3339 format
    """

    allowed_status_codes: list[int] | None = None


@dataclass
class ListMarginConversionsResponse(BaseResponse, _GetMarginConversionsResponse):
    """ListMarginConversionsResponse(conversions: 'list[Conversion]' = None)"""
