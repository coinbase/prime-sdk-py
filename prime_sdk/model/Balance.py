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
class Balance:
    symbol: str | None
    amount: str | None
    holds: str | None
    bonded_amount: str | None
    reserved_amount: str | None
    unbonding_amount: str | None
    unvested_amount: str | None
    pending_rewards_amount: str | None
    past_rewards_amount: str | None
    bondable_amount: str | None
    withdrawable_amount: str | None
    fiat_amount: str | None
    unbondable_amount: str | None
    claimable_rewards_amount: str | None
