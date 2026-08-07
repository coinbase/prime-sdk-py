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
from ...model import BlockchainAddress as _BlockchainAddress
from ...model import (
    CreateWalletDepositAddressRequest as _CreateWalletDepositAddressRequest,
)


@dataclass(kw_only=True)
class CreateWalletDepositAddressRequest(_CreateWalletDepositAddressRequest):
    """
    Create Wallet Deposit Address

    Attributes:
        portfolio_id: The ID of the portfolio that owns the wallet
        wallet_id: The wallet ID for which to create the deposit address
        network_id: The network name and type
    """

    portfolio_id: str
    wallet_id: str

    allowed_status_codes: list[int] | None = None


@dataclass
class CreateWalletDepositAddressResponse(BaseResponse, _BlockchainAddress):
    """
    Attributes:
        address: The address on the network
        account_identifier: The account identifier (used on some chains to distinguish
            accounts using the same address)
    """
