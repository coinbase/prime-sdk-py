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

from ..enums import XMCallStatus, XMCallType, XMMarginLevel
from . import XMSummary


@dataclass(kw_only=True)
class XMMarginCall:
    margin_call_id: str | None
    currency: str | None
    initial_notional_amount: str | None
    outstanding_notional_amount: str | None
    margin_call_type: XMCallType | None = XMCallType.XM_CALL_TYPE_UNSPECIFIED
    margin_call_status: XMCallStatus | None = XMCallStatus.XM_CALL_STATUS_UNSPECIFIED
    called_with_margin_level: XMMarginLevel | None = XMMarginLevel.XM_MARGIN_LEVEL_UNSPECIFIED
    called_with_margin_summary: XMSummary | None
    due_at: str | None
    created_at: str | None
    updated_at: str | None
