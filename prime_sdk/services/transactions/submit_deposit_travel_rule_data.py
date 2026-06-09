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
from typing import List, Optional

from ...base_response import BaseResponse


@dataclass
class NaturalPersonName:
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None


@dataclass
class DetailedAddress:
    address_1: Optional[str] = None
    address_2: Optional[str] = None
    address_3: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country_code: Optional[str] = None


@dataclass
class TravelRuleParty:
    name: Optional[str] = None
    natural_person_name: Optional[NaturalPersonName] = None
    address: Optional[DetailedAddress] = None
    wallet_type: Optional[str] = None
    vasp_id: Optional[str] = None
    vasp_name: Optional[str] = None
    personal_id: Optional[str] = None
    date_of_birth: Optional[str] = None
    telephone_number: Optional[str] = None
    account_id: Optional[str] = None


@dataclass
class SubmitDepositTravelRuleDataRequest:
    portfolio_id: str
    transaction_id: str
    originator: Optional[TravelRuleParty] = None
    beneficiary: Optional[TravelRuleParty] = None
    is_self: Optional[bool] = None
    opt_out_of_ownership_verification: Optional[bool] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class SubmitDepositTravelRuleDataResponse(BaseResponse):
    ownership_verification_required: bool = None
