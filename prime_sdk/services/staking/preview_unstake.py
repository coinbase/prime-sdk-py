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
from ...model import PreviewUnstakeRequest as _PreviewUnstakeRequest
from ...model import PreviewUnstakeResponse as _PreviewUnstakeResponse


@dataclass(kw_only=True)
class PreviewUnstakeRequest(_PreviewUnstakeRequest):
    """
    Preview Unstake

    Attributes:
        portfolio_id: The portfolio ID
        wallet_id: The wallet ID
        amount: Amount to preview unstaking
    """

    portfolio_id: str
    wallet_id: str

    allowed_status_codes: list[int] | None = None


@dataclass
class PreviewUnstakeResponse(BaseResponse, _PreviewUnstakeResponse):
    """
    PreviewUnstakeResponse contains the response data from previewing an unstaking operation.

    Attributes:
        estimated_amount: Estimated amount that would be unstaked
        wallet_id: The wallet ID
        wallet_address: The blockchain address of the wallet
        current_timestamp: Timestamp at which this preview was generated (ISO 8601)
        validators: Per-validator breakdown of the unstake simulation
    """
