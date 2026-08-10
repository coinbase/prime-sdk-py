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
from ...model import ListTFObligationsRequest as _ListTFObligationsRequest
from ...model import ListTFObligationsResponse as _ListTFObligationsResponse


@dataclass(kw_only=True)
class ListTradeFinanceObligationsRequest(BaseRequest, _ListTFObligationsRequest):
    """
    List Trade Finance Obligations

    Attributes:
        entity_id: The entity ID to retrieve obligations for
    """


@dataclass
class ListTradeFinanceObligationsResponse(BaseResponse, _ListTFObligationsResponse):
    """
    Response containing trade finance obligations for an entity

    Attributes:
        obligations: The list of obligations (loans) for the entity.
    """
