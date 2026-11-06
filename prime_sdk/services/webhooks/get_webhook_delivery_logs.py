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

from ...base_request import BaseCursorLimitPaginatedRequest
from ...base_response import BaseResponse
from ...model import GetWebhookDeliveryLogsRequest as _GetWebhookDeliveryLogsRequest
from ...model import GetWebhookDeliveryLogsResponse as _GetWebhookDeliveryLogsResponse


@dataclass(kw_only=True)
class GetWebhookDeliveryLogsRequest(
    BaseCursorLimitPaginatedRequest, _GetWebhookDeliveryLogsRequest
):
    """
    Get Webhook Delivery Logs
    """


@dataclass
class GetWebhookDeliveryLogsResponse(BaseResponse, _GetWebhookDeliveryLogsResponse):
    """
    GetWebhookDeliveryLogsResponse returns a page of delivery logs and pagination metadata.
    """
