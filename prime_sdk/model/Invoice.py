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

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from ..enums import InvoiceState
from . import InvoiceItem


@dataclass(kw_only=True)
class Invoice:
    id: str | None
    billing_month: int | None
    billing_year: int | None
    due_date: str | None
    invoice_number: str | None
    state: InvoiceState | None = InvoiceState.INVOICE_STATE_UNSPECIFIED
    usd_amount_paid: float | None
    usd_amount_owed: float | None
    invoice_items: List[InvoiceItem] | None
