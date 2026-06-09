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
class XMPosition:
    currency: str | None
    market_price: str | None
    margin_eligible: bool | None
    market_cap: str | None
    adv30_days: str | None
    hist5d_vol: str | None
    hist30d_vol: str | None
    hist90d_vol: str | None
    margin_requirement: str | None
    spot_balance: str | None
    spot_balance_notional: str | None
    spot_total_position_margin: str | None
    futures_balance: str | None
    futures_balance_notional: str | None
    futures_total_position_margin: str | None
    gmv_basis: str | None
    base_requirement: str | None
    liq_shorts_add_on: str | None
    liq_longs_add_on: str | None
    vol_shorts_add_on: str | None
    vol_longs_add_on: str | None
    vol5days_add_on: str | None
    vol30days_add_on: str | None
    vol90days_add_on: str | None
    total_position_margin: str | None
