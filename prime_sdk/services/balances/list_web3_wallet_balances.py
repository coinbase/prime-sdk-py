# Copyright 2024-present Coinbase Global, Inc.
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
from ...model import ListWeb3WalletBalancesRequest as _ListWeb3WalletBalancesRequest
from ...model import ListWeb3WalletBalancesResponse as _ListWeb3WalletBalancesResponse


@dataclass(kw_only=True)
class ListWeb3WalletBalancesRequest(
    BaseCursorLimitPaginatedRequest, _ListWeb3WalletBalancesRequest
):
    """
    List Onchain Wallet Balances

    Attributes:
        portfolio_id: Portfolio to retrieve balances for.
        wallet_id: Onchain wallet to retrieve balances for.
        visibility_statuses: Visibility statuses to filter balances on. Leaving this field
            empty will return only VISIBLE balances. - UNKNOWN_VISIBILITY_STATUS: nil -
            VISIBLE: Visible - HIDDEN: Hidden - SPAM: Spam
    """


@dataclass
class ListWeb3WalletBalancesResponse(BaseResponse, _ListWeb3WalletBalancesResponse):
    """
    Attributes:
        balances: List of balances in the onchain wallet
        defi_balances: DeFi balances only return for the initial request. No pagination
            support.
    """
