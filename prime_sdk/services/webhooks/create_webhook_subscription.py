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
    CreateWebhookSubscriptionRequest as _CreateWebhookSubscriptionRequest,
)
from ...model import (
    CreateWebhookSubscriptionResponse as _CreateWebhookSubscriptionResponse,
)


@dataclass(kw_only=True)
class CreateWebhookSubscriptionRequest(BaseRequest, _CreateWebhookSubscriptionRequest):
    """
    Create Webhook Subscription

    Attributes:
        portfolio_id: Populated from the URL path.
    """


@dataclass
class CreateWebhookSubscriptionResponse(
    BaseResponse, _CreateWebhookSubscriptionResponse
):
    """
    CreateWebhookSubscriptionResponse returns the created subscription and its one-time HMAC secret.

    Attributes:
        hmac_secret: hmac_secret is the plaintext HMAC signing secret. Returned exactly once
            on creation; store it securely — it is never surfaced again.
    """
