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

from ...base_request import BaseRequest
from ...base_response import BaseResponse
from ...model import GetMarginSummariesRequest as _GetMarginSummariesRequest
from ...model import GetMarginSummariesResponse as _GetMarginSummariesResponse


@dataclass(kw_only=True)
class ListMarginCallSummariesRequest(BaseRequest, _GetMarginSummariesRequest):
    """
    List Margin Call Summaries

    Attributes:
        entity_id: The unique ID of the entity
        start_date: The start date of the range to query for in RFC3339 format. Must be
            within the last 3 months
        end_date: The end date of the range to query for in RFC3339 format
    """


@dataclass
class ListMarginCallSummariesResponse(BaseResponse, _GetMarginSummariesResponse):
    """ListMarginCallSummariesResponse(margin_summaries: 'list[MarginSummaryHistorical]' = None)"""
