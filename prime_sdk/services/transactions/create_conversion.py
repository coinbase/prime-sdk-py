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
from typing import List, Optional
from ...base_response import BaseResponse


@dataclass
class CreateConversionRequest:
    portfolio_id: str
    wallet_id: str
    amount: str
    destination: str
    idempotency_key: str
    source_symbol: str
    destination_symbol: str
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class CreateConversionResponse(BaseResponse):
    activity_id: str = None
    source_symbol: str = None
    destination_symbol: str = None
    amount: str = None
    destination: str = None
    source: str = None
    transaction_id: str = None