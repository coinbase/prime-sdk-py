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

from typing import Any


class PrimeSDKError(Exception):
    """Base class for all errors raised by the Prime SDK."""


class PrimeAPIError(PrimeSDKError):
    """Raised when a Prime API request returns a non-allowed status code."""

    def __init__(
        self,
        status_code: int,
        message: str,
        *,
        code: str | None = None,
        subcode: str | None = None,
        trace_id: str | None = None,
        body: Any | None = None,
    ):
        self.status_code = status_code
        self.message = message
        self.code = code
        self.subcode = subcode
        self.trace_id = trace_id
        self.body = body
        super().__init__(f"Request failed with status {status_code}: {message}")

    @classmethod
    def from_status(
        cls,
        status_code: int,
        message: str,
        *,
        code: str | None = None,
        subcode: str | None = None,
        trace_id: str | None = None,
        body: Any | None = None,
    ) -> "PrimeAPIError":
        error_cls = _STATUS_EXCEPTIONS.get(status_code, cls)
        return error_cls(
            status_code,
            message,
            code=code,
            subcode=subcode,
            trace_id=trace_id,
            body=body,
        )


class PrimeBadRequestError(PrimeAPIError):
    """Raised when the Prime API returns HTTP 400."""


class PrimeUnauthorizedError(PrimeAPIError):
    """Raised when the Prime API returns HTTP 401."""


class PrimeForbiddenError(PrimeAPIError):
    """Raised when the Prime API returns HTTP 403."""


class PrimeNotFoundError(PrimeAPIError):
    """Raised when the Prime API returns HTTP 404."""


class PrimeTooManyRequestsError(PrimeAPIError):
    """Raised when the Prime API returns HTTP 429."""


class PrimeInternalServerError(PrimeAPIError):
    """Raised when the Prime API returns HTTP 500."""


class PrimeNotImplementedError(PrimeAPIError):
    """Raised when the Prime API returns HTTP 501."""


class PrimeServiceUnavailableError(PrimeAPIError):
    """Raised when the Prime API returns HTTP 503."""


_STATUS_EXCEPTIONS: dict[int, type[PrimeAPIError]] = {
    400: PrimeBadRequestError,
    401: PrimeUnauthorizedError,
    403: PrimeForbiddenError,
    404: PrimeNotFoundError,
    429: PrimeTooManyRequestsError,
    500: PrimeInternalServerError,
    501: PrimeNotImplementedError,
    503: PrimeServiceUnavailableError,
}
