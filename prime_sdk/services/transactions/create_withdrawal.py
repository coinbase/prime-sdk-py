# Copyright 2025-present Coinbase Global, Inc.
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

from dataclasses import dataclass

from ...base_response import BaseResponse
from ...model import CreateWalletWithdrawalRequest as _CreateWalletWithdrawalRequest
from ...model import CreateWalletWithdrawalResponse as _CreateWalletWithdrawalResponse


@dataclass
class PaymentMethod:
    payment_method_id: str


@dataclass
class Network:
    id: str
    type: str


@dataclass
class BlockchainAddress:
    address: str
    account_identifier: str | None = None
    network: Network | None = None


@dataclass
class Counterparty:
    counterparty_id: str


@dataclass(kw_only=True)
class CreateWithdrawalRequest(_CreateWalletWithdrawalRequest):
    __doc__ = _CreateWalletWithdrawalRequest.__doc__

    portfolio_id: str
    wallet_id: str

    allowed_status_codes: list[int] | None = None


@dataclass
class CreateWithdrawalResponse(BaseResponse, _CreateWalletWithdrawalResponse):
    __doc__ = _CreateWalletWithdrawalResponse.__doc__
