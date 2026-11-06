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
        transaction.amount: The transaction amount (in whole units). For example, "1.50"
            represents 1.5 of the associated symbol. Examples: - "100" - "1.123456"
            (precision varies by asset; USDC, for example, supports up to 6 decimal places)
            - "0.50"
        transaction.network_fees: The blockchain network fees (in whole units) required in
            order to broadcast the transaction. Does not carry the Advanced Transfer
            Coinbase fee.
        transaction.fees: The charged fee (in whole units). On the transfer, coinbase_fees
            is set and fees is 0. On the send, the same charge is on fees and fee_symbol,
            and coinbase_fees is omitted. Crypto and fiat sends that belong to the transfer
            use those transfer and send fields. A bank withdrawal that is not part of the
            transfer is unchanged.
        transaction.fee_symbol: The asset in which fees is denominated. On the send, the
            same charge is on fees and fee_symbol, and coinbase_fees is omitted. On the
            transfer, fee_symbol is empty.
        transaction.blockchain_ids: The cryptocurrency network transaction hashes/IDs
            generated upon broadcast
        transaction.transaction_id: The 8 character alphanumeric short form id for the
            transaction
        transaction.destination_symbol: The destination asset symbol
        transaction.network: The network name specific to web3/onchain wallet transactions
        transaction.estimated_asset_changes: The estimated asset changes (web3/onchain)
        transaction.idempotency_key: The idempotency key associated with the transaction
            creation request
        transaction.coinbase_fees: Coinbase fees on the transfer (amount, symbol,
            wallet_id), where fees is 0. On the send, the same charge is on fees and
            fee_symbol, and coinbase_fees is omitted. When you total fees, do not add
            coinbase_fees from the transfer to the send's fees, or you will count the charge
            twice. A wallet transaction list includes the fees paid by that wallet. Get
            Transaction and the portfolio transaction list include every fee paid in the
            requesting portfolio. Fees paid in the counterparty's portfolio are omitted.
    """
