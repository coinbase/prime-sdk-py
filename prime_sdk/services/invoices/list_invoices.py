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
from ...model import Invoice
from ...utils import PaginationParams


@dataclass
class ListInvoicesRequest:
    entity_id: str
    states: str | None = None
    billing_year: int | None = None
    billing_month: str | None = None
    pagination: PaginationParams | None = None
    allowed_status_codes: list[int] | None = None


@dataclass
class ListInvoicesResponse(BaseResponse):
    invoices: list[Invoice] = None
