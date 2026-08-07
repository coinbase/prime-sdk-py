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

from ...base_request import BaseRequest
from ...base_response import BaseResponse
from ...model import (
    GetWalletDepositInstructionsRequest as _GetWalletDepositInstructionsRequest,
)
from ...model import (
    GetWalletDepositInstructionsResponse as _GetWalletDepositInstructionsResponse,
)


@dataclass(kw_only=True)
class GetWalletDepositInstructionsRequest(
    BaseRequest, _GetWalletDepositInstructionsRequest
):
    """
    Get Wallet Deposit Instructions

    Attributes:
        portfolio_id: The portfolio ID
        wallet_id: The wallet ID
        deposit_type: The deposit type - UNKNOWN_WALLET_DEPOSIT_TYPE: nil value - CRYPTO: A
            cryptocurrency deposit - WIRE: A wire deposit - SEN: DEPRECATED. A Silvergate
            Exchange Network deposit - SWIFT: A SWIFT deposit - SEPA: A SEPA deposit (Single
            Euro Payments Area)
    """


@dataclass
class GetWalletDepositInstructionsResponse(
    BaseResponse, _GetWalletDepositInstructionsResponse
):
    """
    Attributes:
        crypto_instructions.id: The ID of the wallet
        crypto_instructions.name: The name of the wallet
        crypto_instructions.address: The address of the wallet
        crypto_instructions.account_identifier: The tag/memo of the address, if applicable
            -- required for certain assets (e.g. XRP, XLM, etc.)
        crypto_instructions.account_identifier_name: The blockchain network's terminology
            for the unique identifier used to identify the receiver of the transaction
            (different blockchain networks use different names, such as `destination_tag` or
            `memo`)
        fiat_instructions.id: The id of the wallet
        fiat_instructions.name: The name of the wallet
        fiat_instructions.account_number: The fiat account number
        fiat_instructions.routing_number: The fiat routing number
        fiat_instructions.reference_code: Reference code to be used as a memo/description
    """
