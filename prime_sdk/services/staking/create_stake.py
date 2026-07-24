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
from ...model import ValidatorAllocation


@dataclass
class StakingInputs:
    amount: str | None = None
    validator_address: str | None = None
    end_date: str | None = None
    validator_allocations: list[ValidatorAllocation] | None = None


@dataclass
class WalletStakingMetadata:
    external_id: str | None = None


@dataclass
class CreateStakeRequest:
    portfolio_id: str
    wallet_id: str
    idempotency_key: str
    inputs: StakingInputs | None = None
    metadata: WalletStakingMetadata | None = None
    allowed_status_codes: list[int] | None = None


@dataclass
class CreateStakeResponse(BaseResponse):
    wallet_id: str = None
    transaction_id: str = None
    activity_id: str = None
