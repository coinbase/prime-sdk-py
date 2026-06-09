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

from . import Network


@dataclass(kw_only=True)
class NetworkDetails:
    network: Network | None
    name: str | None
    max_decimals: str | None
    default: bool | None
    trading_supported: bool | None
    vault_supported: bool | None
    prime_custody_supported: bool | None
    destination_tag_required: bool | None
    network_link: str | None
    network_scoped_symbol: str | None
    min_withdrawal_amount: str | None
    max_withdrawal_amount: str | None
    min_deposit_amount: str | None
