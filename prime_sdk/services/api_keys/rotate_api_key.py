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
from ...model import RotateAPIKeyRequest as _RotateAPIKeyRequest
from ...model import RotateAPIKeyResponse as _RotateAPIKeyResponse


@dataclass(kw_only=True)
class RotateApiKeyRequest(BaseRequest, _RotateAPIKeyRequest):
    """
    Attributes:
        duration_seconds: How long the old key remains active after the new key is approved,
            in seconds. Set to 0 for immediate expiry on approval. Cannot extend beyond the
            original key's expiry.
    """


@dataclass
class RotateApiKeyResponse(BaseResponse, _RotateAPIKeyResponse):
    """
    Attributes:
        encrypted_credentials: Base64-encoded encrypted payload containing the new API key
            credentials. Decrypt using your current secret_key with HKDF-SHA256 +
            AES-256-GCM.
        activity_id: The Prime activity ID tracking the consensus approval for this
            rotation. Use with the Activities endpoints to monitor approval status.
    """
