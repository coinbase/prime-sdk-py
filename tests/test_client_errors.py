import json
from unittest.mock import Mock

from prime_sdk.client import Client
from prime_sdk.credentials import Credentials
from prime_sdk.exceptions import (
    PrimeAPIError,
    PrimeApiError,
    PrimeBadRequestError,
    PrimeForbiddenError,
    PrimeInternalServerError,
    PrimeNotFoundError,
    PrimeTooManyRequestsError,
    PrimeUnauthorizedError,
)
from prime_sdk.generated.errors import (
    CreateOrderBadRequestErrorResponse,
    ErrorResponse,
    InternalServerErrorResponse,
    TooManyRequestsErrorResponse,
    UnauthorizedErrorResponse,
)


def _client(status_code: int, payload) -> Client:
    session = Mock()
    response = Mock()
    response.status_code = status_code
    if isinstance(payload, dict):
        response.json.return_value = payload
        response.text = json.dumps(payload)
    else:
        response.json.side_effect = ValueError("No JSON")
        response.text = str(payload)
    session.request.return_value = response
    credentials = Credentials(
        access_key="access-key",
        passphrase="passphrase",
        signing_key="signing-key",
    )
    return Client(credentials, http_client=session)


def test_create_order_bad_request_raises_typed_error():
    client = _client(
        400,
        {
            "code": "VALIDATION_ERROR",
            "message": "invalid order",
            "subcode": "ORDER_SIZE_INVALID",
            "trace_id": "trace-1",
        },
    )

    try:
        client.request("POST", "/portfolios/port-1/order", body={})
        raise AssertionError("expected PrimeBadRequestError")
    except PrimeBadRequestError as exc:
        assert exc.status_code == 400
        assert exc.message == "invalid order"
        assert exc.code == "VALIDATION_ERROR"
        assert exc.subcode == "ORDER_SIZE_INVALID"
        assert exc.trace_id == "trace-1"
        assert isinstance(exc.body, CreateOrderBadRequestErrorResponse)
        assert isinstance(exc, PrimeApiError)
        assert isinstance(exc, PrimeAPIError)
        assert PrimeAPIError is PrimeApiError


def test_forbidden_and_not_found_use_status_subclasses():
    forbidden = _client(403, {"message": "denied", "code": "PERMISSION_DENIED"})
    try:
        forbidden.request("POST", "/portfolios/port-1/order")
        raise AssertionError("expected PrimeForbiddenError")
    except PrimeForbiddenError as exc:
        assert exc.code == "PERMISSION_DENIED"

    missing = _client(404, {"message": "missing", "code": "RESOURCE_NOT_FOUND"})
    try:
        missing.request("POST", "/portfolios/port-1/order")
        raise AssertionError("expected PrimeNotFoundError")
    except PrimeNotFoundError as exc:
        assert exc.message == "missing"


def test_rate_limit_and_internal_error():
    limited = _client(429, {"message": "slow down", "code": "RATE_LIMIT_EXCEEDED"})
    try:
        limited.request("POST", "/portfolios/port-1/order")
        raise AssertionError("expected PrimeTooManyRequestsError")
    except PrimeTooManyRequestsError as exc:
        assert isinstance(exc.body, TooManyRequestsErrorResponse)

    internal = _client(500, {"message": "boom", "code": "INTERNAL_ERROR"})
    try:
        internal.request("POST", "/portfolios/port-1/order")
        raise AssertionError("expected PrimeInternalServerError")
    except PrimeInternalServerError as exc:
        assert isinstance(exc.body, InternalServerErrorResponse)


def test_unlisted_status_on_matched_route_uses_shared_class():
    client = _client(401, {"message": "nope", "code": "AUTHENTICATION_FAILED"})

    try:
        client.request("POST", "/portfolios/port-1/order")
        raise AssertionError("expected PrimeUnauthorizedError")
    except PrimeUnauthorizedError as exc:
        assert isinstance(exc.body, UnauthorizedErrorResponse)


def test_unmatched_path_falls_back_to_error_response():
    client = _client(400, {"message": "bad", "code": "VALIDATION_ERROR"})

    try:
        client.request("POST", "/not-a-real-path")
        raise AssertionError("expected PrimeBadRequestError")
    except PrimeBadRequestError as exc:
        assert type(exc.body) is ErrorResponse
        assert exc.message == "bad"


def test_non_json_body_still_raises_status_subclass():
    client = _client(404, "not found")

    try:
        client.request("GET", "/portfolios/port-1/order")
        raise AssertionError("expected PrimeNotFoundError")
    except PrimeNotFoundError as exc:
        assert exc.message == "not found"
        assert exc.body is None
        assert exc.code is None


def test_allowed_status_codes_suppress_raise():
    client = _client(400, {"message": "ignored"})
    response = client.request(
        "POST",
        "/portfolios/port-1/order",
        allowed_status_codes=[200, 400],
    )
    assert response.status_code == 400
