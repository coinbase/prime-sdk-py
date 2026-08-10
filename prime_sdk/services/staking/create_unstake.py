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
from ...model import StakingUnstakeRequest as _StakingUnstakeRequest
from ...model import StakingUnstakeResponse as _StakingUnstakeResponse


@dataclass(kw_only=True)
class CreateUnstakeRequest(BaseRequest, _StakingUnstakeRequest):
    """
    Request to unstake a wallet

    Attributes:
        portfolio_id: The portfolio ID
        wallet_id: The wallet ID
        idempotency_key: The client generated idempotency key for requested execution.
            Subsequent requests using the same key will fail
    """


@dataclass
class CreateUnstakeResponse(BaseResponse, _StakingUnstakeResponse):
    """
    StakingUnstakeResponse contains the response data from initiating an unstaking operation.

    Attributes:
        wallet_id: The wallet ID
        transaction_id: ID of the newly created transaction, can be used to fetch details of
            the current state of execution
        activity_id: The ID for the activity generated for this request
    """
