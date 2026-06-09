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

from ..enums import SigningStatus
from . import RiskAssessment


@dataclass(kw_only=True)
class OnchainTransactionDetails:
    signed_transaction: str | None
    risk_assessment: RiskAssessment | None
    chain_id: str | None
    nonce: str | None
    replaced_transaction_id: str | None
    destination_address: str | None
    skip_broadcast: bool | None
    failure_reason: str | None
    signing_status: SigningStatus | None
