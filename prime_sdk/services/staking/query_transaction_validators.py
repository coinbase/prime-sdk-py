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
    ListTransactionValidatorsRequest as _ListTransactionValidatorsRequest,
)
from ...model import (
    ListTransactionValidatorsResponse as _ListTransactionValidatorsResponse,
)


@dataclass(kw_only=True)
class QueryTransactionValidatorsRequest(_ListTransactionValidatorsRequest):
    """
    List Transaction Validators

    Attributes:
        portfolio_id: The portfolio ID
        transaction_ids: List of transaction IDs to filter validators by. Maximum of 100
            transaction IDs allowed per request.
        cursor: Cursor for pagination
        limit: Maximum number of transaction-validator associations to return per page.
            Default is 100, maximum is 1000.
    """

    portfolio_id: str

    allowed_status_codes: list[int] | None = None


@dataclass
class QueryTransactionValidatorsResponse(
    BaseResponse, _ListTransactionValidatorsResponse
):
    """
    Attributes:
        transaction_validators: List of transaction-to-validator associations. Each entry
            represents one transaction staking to one validator.
    """
