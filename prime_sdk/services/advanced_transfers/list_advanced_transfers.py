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

from ...base_response import BaseResponse
from ...model import AdvancedTransfer
from ...utils import Pagination, PaginationParams


@dataclass
class ListAdvancedTransfersRequest:
    portfolio_id: str
    state: str | None = None
    type: str | None = None
    start_time: str | None = None
    end_time: str | None = None
    reference_id: str | None = None
    pagination: PaginationParams | None = None
    allowed_status_codes: list[int] | None = None


@dataclass
class ListAdvancedTransfersResponse(BaseResponse):
    advanced_transfers: list[AdvancedTransfer] = None
    pagination: Pagination = None
