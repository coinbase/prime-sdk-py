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
from ...model import CreateWalletTransferRequest as _CreateWalletTransferRequest
from ...model import CreateWalletTransferResponse as _CreateWalletTransferResponse


@dataclass(kw_only=True)
class CreateTransferRequest(BaseRequest, _CreateWalletTransferRequest):
    """
    Create Transfer

    Attributes:
        portfolio_id: The portfolio ID
        wallet_id: The wallet ID that the transfer will originate from
        amount: The amount in whole units to send
        destination: The UUID of the destination wallet
        idempotency_key: The idempotency key associated with this transfer
        currency_symbol: The currency symbol to transfer
    """

    portfolio_id: str
    wallet_id: str


@dataclass
class CreateTransferResponse(BaseResponse, _CreateWalletTransferResponse):
    """
    Attributes:
        activity_id: The activity ID for the transfer
        approval_url: A URL to the activity associated with this transfer for approval
        symbol: The currency symbol of the transfer
        amount: The amount of the transfer
        fee: The network fee associated with the transfer
        destination_address: The destination address of the transfer
        destination_type: The destination type of the transfer
        source_address: The source address used for the transfer
        source_type: The source type used for the transfer
        transaction_id: The id of the just created transaction
    """
