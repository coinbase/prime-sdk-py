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
from ...model import GetWalletRequest as _GetWalletRequest
from ...model import GetWalletResponse as _GetWalletResponse


@dataclass(kw_only=True)
class GetWalletRequest(BaseRequest, _GetWalletRequest):
    """
    Get Wallet by Wallet ID

    Attributes:
        portfolio_id: Portfolio ID
        wallet_id: Wallet ID
    """


@dataclass
class GetWalletResponse(BaseResponse, _GetWalletResponse):
    """
    Attributes:
        wallet.id: The unique UUID for the wallet
        wallet.name: The name of the wallet
        wallet.symbol: The asset stored in the wallet
        wallet.created_at: The UTC timestamp when this wallet was created
        wallet.address: The active address of the wallet
    """
