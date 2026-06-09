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

from ..enums import FcmPositionSide


@dataclass(kw_only=True)
class FcmPosition:
    product_id: str | None
    side: FcmPositionSide | None = FcmPositionSide.FCM_POSITION_SIDE_UNSPECIFIED
    number_of_contracts: str | None
    daily_realized_pnl: str | None
    unrealized_pnl: str | None
    current_price: str | None
    avg_entry_price: str | None
    expiration_time: str | None
