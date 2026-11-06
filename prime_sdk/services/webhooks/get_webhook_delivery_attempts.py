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

from ...base_request import BaseRequest
from ...base_response import BaseResponse
from ...model import (
    GetWebhookDeliveryAttemptsRequest as _GetWebhookDeliveryAttemptsRequest,
)
from ...model import (
    GetWebhookDeliveryAttemptsResponse as _GetWebhookDeliveryAttemptsResponse,
)


@dataclass(kw_only=True)
class GetWebhookDeliveryAttemptsRequest(
    BaseRequest, _GetWebhookDeliveryAttemptsRequest
):
    """
    Get Webhook Delivery Attempts
    """


@dataclass
class GetWebhookDeliveryAttemptsResponse(
    BaseResponse, _GetWebhookDeliveryAttemptsResponse
):
    """
    GetWebhookDeliveryAttemptsResponse returns an event's payload, delivery state, and attempts for a subscription.

    Attributes:
        event_payload: event_payload is the raw JSON bytes delivered to the subscriber.
    """
