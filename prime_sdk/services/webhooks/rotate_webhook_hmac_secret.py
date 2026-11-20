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
from ...model import RotateWebhookHMACSecretRequest as _RotateWebhookHMACSecretRequest
from ...model import RotateWebhookHMACSecretResponse as _RotateWebhookHMACSecretResponse


@dataclass(kw_only=True)
class RotateWebhookHMACSecretRequest(BaseRequest, _RotateWebhookHMACSecretRequest):
    """
    Rotate Webhook HMAC Secret

    Attributes:
        revoke_previous_immediately: revoke_previous_immediately invalidates the old secret
            immediately instead of keeping it valid for the server grace window. Use when
            the secret may be compromised.
    """


@dataclass
class RotateWebhookHMACSecretResponse(BaseResponse, _RotateWebhookHMACSecretResponse):
    """
    RotateWebhookHMACSecretResponse is the response message for rotating a webhook HMAC signing secret.

    Attributes:
        hmac_secret: hmac_secret is the new plaintext HMAC signing secret. Returned exactly
            once; store it securely — it is never surfaced again.
        previous_secret_expires_at: previous_secret_expires_at is when the prior secret
            stops being accepted. Unset when revoke_previous_immediately was true.
    """
