# Copyright 2024-present Coinbase Global, Inc.
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

import base64
import hashlib
import hmac
import json
import time

import requests

from prime_sdk.base_response import safe_instantiate
from prime_sdk.credentials import Credentials
from prime_sdk.exceptions import PrimeApiError
from prime_sdk.generated.errors import resolve_error_class
from prime_sdk.version import VERSION

DEFAULT_V1_API_BASE_URL = "https://api.prime.coinbase.com/v1"
USER_AGENT = f"coinbase-prime-py/{VERSION}"


class Client:
    def __init__(
        self, credentials: Credentials, http_client: requests.Session | None = None
    ):
        self.http_base_url = DEFAULT_V1_API_BASE_URL
        self.credentials = credentials
        self.http_client = http_client if http_client else requests.Session()

    @staticmethod
    def from_env(
        variable_name: str = "PRIME_CREDENTIALS",
        http_client: requests.Session | None = None,
    ) -> "Client":
        credentials = Credentials.from_env(variable_name)
        return Client(credentials, http_client)

    def generate_headers(
        self, method: str, path: str, body: dict | None = None
    ) -> dict[str, str]:
        timestamp = str(int(time.time()))
        body_string = json.dumps(body) if body else ""
        message = f"{timestamp}{method}{path}{body_string}"
        signature = self.sign(message)

        return {
            "Accept": "application/json",
            "User-Agent": USER_AGENT,
            "X-CB-ACCESS-KEY": self.credentials.access_key,
            "X-CB-ACCESS-PASSPHRASE": self.credentials.passphrase,
            "X-CB-ACCESS-SIGNATURE": signature,
            "X-CB-ACCESS-TIMESTAMP": timestamp,
        }

    def sign(self, message: str) -> str:
        h = hmac.new(
            self.credentials.signing_key.encode(), message.encode(), hashlib.sha256
        )
        return base64.b64encode(h.digest()).decode()

    def request(
        self,
        method: str,
        path: str,
        query: str | None = "",
        body: dict | None = None,
        allowed_status_codes: list[int] | None = None,
        version: str = "v1",
    ) -> requests.Response:
        if allowed_status_codes is None:
            allowed_status_codes = [200]
        base_url = DEFAULT_V1_API_BASE_URL.replace("/v1", f"/{version}")
        full_path = f"{base_url}{path}"
        url = f"{full_path}?{query}" if query else full_path

        headers = self.generate_headers(method, f"/{version}{path}", body)
        response = self.http_client.request(method, url, headers=headers, json=body)

        if response.status_code not in allowed_status_codes:
            error_details: dict | None = None
            try:
                parsed = response.json()
                if isinstance(parsed, dict):
                    error_details = parsed
            except ValueError:
                pass

            if error_details is not None:
                body = safe_instantiate(
                    resolve_error_class(method, path, response.status_code),
                    error_details,
                )
                error_message = body.message or response.text
                raise PrimeApiError.from_status(
                    response.status_code,
                    error_message,
                    code=body.code,
                    subcode=body.subcode,
                    trace_id=body.trace_id,
                    body=body,
                )

            raise PrimeApiError.from_status(response.status_code, response.text)
        return response
