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
from ...model import GetTransactionRequest as _GetTransactionRequest
from ...model import GetTransactionResponse as _GetTransactionResponse


@dataclass(kw_only=True)
class GetTransactionRequest(BaseRequest, _GetTransactionRequest):
    """
    Get Transaction by Transaction ID

    Attributes:
        portfolio_id: The portfolio ID
        transaction_id: The transaction ID
    """


@dataclass
class GetTransactionResponse(BaseResponse, _GetTransactionResponse):
    """
    Attributes:
        transaction.id: The ID of the transaction
        transaction.wallet_id: The wallet ID of the transaction
        transaction.portfolio_id: The portfolio ID of the transaction
        transaction.symbol: The asset symbol
        transaction.created_at: The transaction creation time (as a UTC timestamp)
        transaction.completed_at: The transaction completion time (as a UTC timestamp)
        transaction.amount: The transaction amount in whole units
        transaction.network_fees: The blockchain network fees (in whole units) required in
            order to broadcast the transaction
        transaction.fees: The fees that the customer paid for the transaction (in whole
            units)
        transaction.fee_symbol: The asset in which fees will be paid
        transaction.blockchain_ids: The cryptocurrency network transaction hashes/IDs
            generated upon broadcast
        transaction.transaction_id: The 8 character alphanumeric short form id for the
            transaction
        transaction.destination_symbol: The destination asset symbol
        transaction.network: The network name specific to web3/onchain wallet transactions
        transaction.estimated_asset_changes: The estimated asset changes (web3)
        transaction.idempotency_key: The idempotency key associated with the transaction
            creation request
    """
