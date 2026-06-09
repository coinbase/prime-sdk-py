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
class CrossMarginPrimeXMPosition:
    currency: str | None
    market_price: str | None
    spot_balance: str | None
    spot_balance_notional: str | None
    futures_balance: str | None
    futures_balance_notional: str | None
    base_requirement: str | None
    total_position_margin: str | None
    basis_credit: str | None
    futures_netted_notional: str | None
    futures_netting_margin: str | None
    long_amount: str | None
    short_amount: str | None
    volatility_addon: str | None
    liquidity_addon: str | None
