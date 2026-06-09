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


@dataclass(kw_only=True)
class PMAssetInfo:
    symbol: str | None
    amount: str | None
    price: str | None
    notional_amount: str | None
    asset_tier: str | None
    margin_eligible: bool | None
    base_margin_requirement: str | None
    base_margin_requirement_notional: str | None
    adv_30d: str | None
    hist_5d_vol: str | None
    hist_30d_vol: str | None
    hist_90d_vol: str | None
    volatility_addon: str | None
    liquidity_addon: str | None
    total_position_margin: str | None
    short_nominal: str | None
    long_nominal: str | None
