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

from ..enums import TravelRuleWalletType
from . import DetailedAddress, NaturalPersonName


@dataclass(kw_only=True)
class TravelRuleParty:
    name: str | None
    natural_person_name: NaturalPersonName | None
    address: DetailedAddress | None
    wallet_type: TravelRuleWalletType | None = TravelRuleWalletType.TRAVEL_RULE_WALLET_TYPE_UNSPECIFIED
    vasp_id: str | None
    vasp_name: str | None
    personal_id: str | None
    date_of_birth: str | None
    telephone_number: str | None
    account_id: str | None
