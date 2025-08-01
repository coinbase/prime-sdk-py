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
from typing import List, Optional
from ...base_response import BaseResponse
from ...model import Blockchain


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
    account_identifier: Optional[str] = None
    network: Optional[Network] = None


@dataclass
class Counterparty:
    counterparty_id: str


@dataclass
class CreateWithdrawalRequest:
    portfolio_id: str
    wallet_id: str
    amount: str
    destination_type: str
    idempotency_key: str
    currency_symbol: str
    payment_method: Optional[PaymentMethod] = None
    blockchain_address: Optional[BlockchainAddress] = None
    counterparty: Optional[Counterparty] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class CreateWithdrawalResponse(BaseResponse):
    activity_id: str = None
    approval_url: str = None
    symbol: str = None
    amount: str = None
    fee: str = None
    destination_type: str = None
    source_type: str = None
    blockchain_destination: Blockchain = None
    blockchain_source: Blockchain = None
    transaction_id: str = None