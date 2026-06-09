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

from ..enums import ActivityCategory, ActivitySecondaryType, ActivityStatus, PrimeActivityType
from . import ActivityMetadataAccount, ActivityMetadataOrders, ActivityMetadataTransactions, UserAction


@dataclass(kw_only=True)
class Activity:
    id: str | None
    reference_id: str | None
    category: ActivityCategory | None = ActivityCategory.OTHER_ACTIVITY_CATEGORY
    type: PrimeActivityType | None = PrimeActivityType.OTHER_ACTIVITY_TYPE
    secondary_type: ActivitySecondaryType | None = ActivitySecondaryType.NO_SECONDARY_TYPE
    status: ActivityStatus | None = ActivityStatus.OTHER_ACTIVITY_STATUS
    created_by: str | None
    title: str | None
    description: str | None
    user_actions: List[UserAction] | None
    transactions_metadata: ActivityMetadataTransactions | None
    account_metadata: ActivityMetadataAccount | None
    orders_metadata: ActivityMetadataOrders | None
    symbols: List[str] | None
    created_at: str | None
    updated_at: str | None
    hierarchy_type: PrimeActivityType | None = PrimeActivityType.OTHER_ACTIVITY_TYPE
