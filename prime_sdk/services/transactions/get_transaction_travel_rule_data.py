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

from dataclasses import dataclass

from ...base_response import BaseResponse
from .submit_deposit_travel_rule_data import TravelRuleParty


@dataclass
class GetTransactionTravelRuleDataRequest:
    portfolio_id: str
    transaction_id: str
    allowed_status_codes: list[int] | None = None


@dataclass
class GetTransactionTravelRuleDataResponse(BaseResponse):
    fulfilled: bool = None
    is_self: bool = None
    originator: TravelRuleParty = None
    beneficiary: TravelRuleParty = None
    amount: str = None
    amount_currency: str = None
    fiat_amount: str = None
    fiat_amount_currency: str = None
    blockchain_network: str = None
