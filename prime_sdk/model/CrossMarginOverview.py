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

from ..enums import XMControlStatus, XMEntityCallStatus, XMMarginLevel
from . import ActiveLiquidationSummary, XMLoan, XMMarginCall, XMSummary


@dataclass(kw_only=True)
class CrossMarginOverview:
    control_status: XMControlStatus | None = XMControlStatus.XM_CONTROL_STATUS_UNSPECIFIED
    call_status: XMEntityCallStatus | None = XMEntityCallStatus.XM_ENTITY_CALL_STATUS_UNSPECIFIED
    margin_level: XMMarginLevel | None = XMMarginLevel.XM_MARGIN_LEVEL_UNSPECIFIED
    margin_summary: XMSummary | None
    active_margin_calls: List[XMMarginCall] | None
    active_loans: List[XMLoan] | None
    active_liquidation: ActiveLiquidationSummary | None
