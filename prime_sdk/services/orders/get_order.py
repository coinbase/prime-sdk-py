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
from ...model import GetOrderRequest as _GetOrderRequest
from ...model import GetOrderResponse as _GetOrderResponse


@dataclass(kw_only=True)
class GetOrderRequest(BaseRequest, _GetOrderRequest):
    """
    Get Order by Order ID

    Attributes:
        portfolio_id: Portfolio ID
        order_id: Order ID
    """


@dataclass
class GetOrderResponse(BaseResponse, _GetOrderResponse):
    """GetOrderResponse(order: 'Order' = None)"""
