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

from . import MarginAddOn, XMPosition


@dataclass(kw_only=True)
class XMRiskNettingInfo:
    dco_margin_requirement: str | None
    portfolio_margin_requirement: str | None
    integrated_portfolio_margin_requirement: str | None
    ineligible_futures_margin_requirement: str | None
    position_margin_requirement: str | None
    portfolio_margin_addon: str | None
    integrated_position_margin_requirement: str | None
    integrated_portfolio_margin_addon: str | None
    netted_futures_notional: str | None
    total_gmv_basis: str | None
    ipm_cash_balance: str | None
    integrated_scenario_addon: MarginAddOn | None
    all_integrated_scenario_addons: List[MarginAddOn] | None
    xm_positions: List[XMPosition] | None
