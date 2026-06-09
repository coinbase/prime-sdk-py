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

from . import XMRiskNettingInfo


@dataclass(kw_only=True)
class XMSummary:
    margin_requirement: str | None
    account_equity: str | None
    margin_excess_shortfall: str | None
    consumed_credit: str | None
    xm_credit_limit: str | None
    xm_margin_limit: str | None
    spot_equity: str | None
    futures_equity: str | None
    risk_netting_info: XMRiskNettingInfo | None
