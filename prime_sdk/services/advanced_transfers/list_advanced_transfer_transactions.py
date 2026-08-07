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

from ...base_response import BaseResponse
from ...model import (
    ListAdvancedTransferTransactionsRequest as _ListAdvancedTransferTransactionsRequest,
)
from ...model import (
    ListAdvancedTransferTransactionsResponse as _ListAdvancedTransferTransactionsResponse,
)


@dataclass(kw_only=True)
class ListAdvancedTransferTransactionsRequest(_ListAdvancedTransferTransactionsRequest):
    """
    List transactions associated with an Advanced Transfer

    Attributes:
        portfolio_id: The portfolio ID
        advanced_transfer_id: The ID of the Advanced Transfer
    """

    allowed_status_codes: list[int] | None = None


@dataclass
class ListAdvancedTransferTransactionsResponse(
    BaseResponse, _ListAdvancedTransferTransactionsResponse
):
    """
    ListAdvancedTransferTransactionsResponse contains the transactions associated with an advanced transfer.

    Attributes:
        transactions: The transactions associated with an Advanced Transfer
    """
