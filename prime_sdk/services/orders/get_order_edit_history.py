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
from ...model import GetOrderEditHistoryRequest as _GetOrderEditHistoryRequest
from ...model import GetOrderEditHistoryResponse as _GetOrderEditHistoryResponse


@dataclass(kw_only=True)
class GetOrderEditHistoryRequest(BaseRequest, _GetOrderEditHistoryRequest):
    """
    List Order Edit History

    Attributes:
        portfolio_id: The portfolio ID
        order_id: The order ID
    """


@dataclass
class GetOrderEditHistoryResponse(BaseResponse, _GetOrderEditHistoryResponse):
    """
    Order Edit History by Order ID and Portfolio ID

    Attributes:
        order_id: The order ID
        order_edit_history: The history of order edits (deprecated: use edit_history
            instead)
        edit_history: The history of order edits
    """
