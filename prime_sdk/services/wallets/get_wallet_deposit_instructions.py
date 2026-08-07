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
from ...enums import WalletDepositType
from ...model import (
    GetWalletDepositInstructionsRequest as _GetWalletDepositInstructionsRequest,
)
from ...model import (
    GetWalletDepositInstructionsResponse as _GetWalletDepositInstructionsResponse,
)


@dataclass
class GetWalletDepositInstructionsRequest(_GetWalletDepositInstructionsRequest):
    __doc__ = _GetWalletDepositInstructionsRequest.__doc__

    portfolio_id: str
    wallet_id: str
    deposit_type: WalletDepositType
    allowed_status_codes: list[int] | None = None


@dataclass
class GetWalletDepositInstructionsResponse(
    BaseResponse, _GetWalletDepositInstructionsResponse
):
    __doc__ = _GetWalletDepositInstructionsResponse.__doc__
