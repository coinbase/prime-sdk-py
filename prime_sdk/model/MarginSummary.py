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

from . import AssetBalance, LoanInfo, MarginAddOn, MarketRate, PMAssetInfo


@dataclass(kw_only=True)
class MarginSummary:
    entity_id: str | None
    margin_equity: str | None
    margin_requirement: str | None
    excess_deficit: str | None
    pm_credit_consumed: str | None
    tf_credit_limit: str | None
    tf_credit_consumed: str | None
    tf_adjusted_asset_value: str | None
    tf_adjusted_liability_value: str | None
    tf_adjusted_credit_consumed: str | None
    tf_adjusted_equity: str | None
    frozen: bool | None
    frozen_reason: str | None
    tf_enabled: bool | None
    pm_enabled: bool | None
    market_rates: List[MarketRate] | None
    asset_balances: List[AssetBalance] | None
    tf_loans: List[LoanInfo] | None
    pm_loans: List[LoanInfo] | None
    short_collateral: List[LoanInfo] | None
    gross_market_value: str | None
    net_market_value: str | None
    long_market_value: str | None
    non_marginable_long_market_value: str | None
    short_market_value: str | None
    gross_leverage: str | None
    net_exposure: str | None
    portfolio_stress_triggered: MarginAddOn | None
    pm_asset_info: List[PMAssetInfo] | None
    pm_credit_limit: str | None
    pm_margin_limit: str | None
    pm_margin_consumed: str | None
