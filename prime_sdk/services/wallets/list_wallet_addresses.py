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

from ...base_request import BaseCursorLimitPaginatedRequest
from ...base_response import BaseResponse
from ...model import ListWalletAddressesRequest as _ListWalletAddressesRequest
from ...model import ListWalletAddressesResponse as _ListWalletAddressesResponse


@dataclass(kw_only=True)
class ListWalletAddressesRequest(
    BaseCursorLimitPaginatedRequest, _ListWalletAddressesRequest
):
    """
    List Wallet Addresses

    Attributes:
        portfolio_id: The portfolio ID associated with the wallet
        wallet_id: The wallet ID for which to retrieve all deposit addresses
        network_id: The blockchain network name and type, provide an empty network to
            retrieve addresses across all networks for this wallet
    """


@dataclass
class ListWalletAddressesResponse(BaseResponse, _ListWalletAddressesResponse):
    """
    Attributes:
        addresses: Addresses
    """
