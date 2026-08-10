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

"""Hand-maintained model extensions that are not represented in the OpenAPI spec."""

from dataclasses import dataclass

from prime_sdk.generated.models import RiskNettingInfo


@dataclass
class MarginCall:
    id: str = None
    initial_notional_amount: str = None
    outstanding_notional_amount: str = None
    created_at: str = None
    due_at: str = None


@dataclass
class CrossMarginSummary:
    margin_requirement: str = None
    account_equity: str = None
    margin_excess_shortfall: str = None
    consumed_credit: str = None
    xm_credit_limit: str = None
    xm_margin_limit: str = None
    consumed_margin_limit: str = None
    spot_equity: str = None
    futures_equity: str = None
    risk_netting_info: RiskNettingInfo = None
