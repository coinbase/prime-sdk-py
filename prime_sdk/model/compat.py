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

from .WalletCryptoDepositInstructions import WalletCryptoDepositInstructions
from .WalletFiatDepositInstructions import WalletFiatDepositInstructions


@dataclass(kw_only=True)
class BalanceWithHolds:
    total: str | None = None
    holds: str | None = None


@dataclass(kw_only=True)
class Instructions:
    crypto_instructions: WalletCryptoDepositInstructions | None = None
    fiat_instructions: WalletFiatDepositInstructions | None = None
