# Copyright 2026-present Coinbase Global, Inc.
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
from ...model import ListAdvancedTransfersRequest as _ListAdvancedTransfersRequest
from ...model import ListAdvancedTransfersResponse as _ListAdvancedTransfersResponse


@dataclass(kw_only=True)
class ListAdvancedTransfersRequest(BasePaginatedRequest, _ListAdvancedTransfersRequest):
    """
    List Advanced Transfers

    Attributes:
        portfolio_id: The portfolio ID
        state: The state of the Advanced Transfer to filter by
        type: The type of the Advanced Transfer to filter by
        start_time: UTC timestamp of creation from which to filter the response (inclusive,
            ISO-8601 format)
        end_time: UTC timestamp of creation until which to filter the response (exclusive,
            ISO-8601 format)
        reference_id: The reference ID of the Advanced Transfer to filter by
    """


@dataclass
class ListAdvancedTransfersResponse(BaseResponse, _ListAdvancedTransfersResponse):
    """
    ListAdvancedTransfersResponse contains the list of advanced transfers and pagination info.
    """
