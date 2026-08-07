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
from ...model import GetInvoicesRequest as _GetInvoicesRequest
from ...model import GetInvoicesResponse as _GetInvoicesResponse
from ...utils import PaginationParams


@dataclass(kw_only=True)
class ListInvoicesRequest(_GetInvoicesRequest):
    """
    List Invoices

    Attributes:
        entity_id: The entity ID
        states: Invoice states to filter the response
        billing_year: Filter invoices by year
        billing_month: Integer representing the month to filter by, 1 for January, 12 for
            December
    """

    pagination: PaginationParams | None = None

    allowed_status_codes: list[int] | None = None


@dataclass
class ListInvoicesResponse(BaseResponse, _GetInvoicesResponse):
    """ListInvoicesResponse(invoices: 'list[Invoice]' = None)"""
