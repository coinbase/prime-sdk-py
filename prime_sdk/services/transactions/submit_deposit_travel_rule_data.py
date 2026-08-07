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

from ...base_request import BaseRequest
from ...base_response import BaseResponse
from ...model import (
    SubmitDepositTravelRuleDataRequest as _SubmitDepositTravelRuleDataRequest,
)
from ...model import (
    SubmitDepositTravelRuleDataResponse as _SubmitDepositTravelRuleDataResponse,
)


@dataclass
class NaturalPersonName:
    first_name: str | None = None
    middle_name: str | None = None
    last_name: str | None = None


@dataclass
class DetailedAddress:
    address_1: str | None = None
    address_2: str | None = None
    address_3: str | None = None
    city: str | None = None
    state: str | None = None
    postal_code: str | None = None
    country_code: str | None = None


@dataclass
class TravelRuleParty:
    name: str | None = None
    natural_person_name: NaturalPersonName | None = None
    address: DetailedAddress | None = None
    wallet_type: str | None = None
    vasp_id: str | None = None
    vasp_name: str | None = None
    vasp_address: str | None = None
    personal_id: str | None = None
    date_of_birth: str | None = None
    telephone_number: str | None = None
    account_id: str | None = None


@dataclass(kw_only=True)
class SubmitDepositTravelRuleDataRequest(
    BaseRequest, _SubmitDepositTravelRuleDataRequest
):
    """
    Submit Deposit Travel Rule Data

    Attributes:
        portfolio_id: The portfolio ID that owns the transaction
        transaction_id: The transaction ID associated with the entry
        is_self: True if user owns the counterparty address (self-transfer) If false,
            beneficiary is required
        opt_out_of_ownership_verification: True to skip wallet ownership verification
    """

    portfolio_id: str
    transaction_id: str


@dataclass
class SubmitDepositTravelRuleDataResponse(
    BaseResponse, _SubmitDepositTravelRuleDataResponse
):
    """
    Response after submitting travel rule data for a deposit

    Attributes:
        ownership_verification_required: Whether additional ownership verification is
            required
    """
