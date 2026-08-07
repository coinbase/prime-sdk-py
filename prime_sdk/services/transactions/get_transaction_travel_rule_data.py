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
    GetTransactionTravelRuleDataRequest as _GetTransactionTravelRuleDataRequest,
)
from ...model import (
    GetTransactionTravelRuleDataResponse as _GetTransactionTravelRuleDataResponse,
)


@dataclass(kw_only=True)
class GetTransactionTravelRuleDataRequest(
    BaseRequest, _GetTransactionTravelRuleDataRequest
):
    """
    Get Transaction Travel Rule Data

    Attributes:
        portfolio_id: The portfolio ID that owns the transaction
        transaction_id: The transaction ID to look up travel rule data for
    """


@dataclass
class GetTransactionTravelRuleDataResponse(
    BaseResponse, _GetTransactionTravelRuleDataResponse
):
    """
    Response containing fulfilled travel rule data for a transaction

    Attributes:
        fulfilled: Whether data requirements are fulfilled
        is_self: Whether the transfer is to/from a self-owned wallet
        amount: The crypto amount of the transaction (e.g. "1.23 BTC")
        amount_currency: The currency of the crypto amount
        fiat_amount: The fiat amount of the transaction (e.g. "123.45 USD")
        fiat_amount_currency: The currency of the fiat amount
        blockchain_network: The blockchain network for the transaction
    """
