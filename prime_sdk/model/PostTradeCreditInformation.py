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

from . import AmountDue


@dataclass(kw_only=True)
class PostTradeCreditInformation:
    portfolio_id: str | None
    currency: str | None
    limit: str | None
    utilized: str | None
    available: str | None
    frozen: bool | None
    frozen_reason: str | None
    amounts_due: List[AmountDue] | None
    enabled: bool | None
    adjusted_credit_utilized: str | None
    adjusted_portfolio_equity: str | None
