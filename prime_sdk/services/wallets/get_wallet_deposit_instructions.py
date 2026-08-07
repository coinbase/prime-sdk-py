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
from ...model import (
    GetWalletDepositInstructionsRequest as _GetWalletDepositInstructionsRequest,
)
from ...model import (
    GetWalletDepositInstructionsResponse as _GetWalletDepositInstructionsResponse,
)


@dataclass(kw_only=True)
class GetWalletDepositInstructionsRequest(_GetWalletDepositInstructionsRequest):
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

    allowed_status_codes: list[int] | None = None


@dataclass
class GetWalletDepositInstructionsResponse(
    BaseResponse, _GetWalletDepositInstructionsResponse
):
    """GetWalletDepositInstructionsResponse(crypto_instructions: 'CryptoInstructions' = None, fiat_instructions: 'FiatInstructions' = None)"""
