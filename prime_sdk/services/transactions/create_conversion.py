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
from ...model import CreateConversionRequest as _CreateConversionRequest
from ...model import CreateConversionResponse as _CreateConversionResponse


@dataclass(kw_only=True)
class CreateConversionRequest(BaseRequest, _CreateConversionRequest):
    """
    Create Conversion

    Attributes:
        portfolio_id: The ID of the portfolio
        wallet_id: The wallet ID that the conversion will originate from
        amount: The amount in whole units to convert
        destination: The UUID of the destination wallet
        idempotency_key: The idempotency key associated with this conversion
        source_symbol: The currency symbol to convert from
        destination_symbol: The currency symbol to convert to
    """


@dataclass
class CreateConversionResponse(BaseResponse, _CreateConversionResponse):
    """
    Attributes:
        activity_id: The activity ID for the conversion
        source_symbol: The currency symbol to convert from
        destination_symbol: The currency symbol to convert to
        amount: The amount in whole units to convert
        destination: The UUID of the destination wallet
        source: The UUID of the source wallet
        transaction_id: The UUID of the conversion transaction
    """
