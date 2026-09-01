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

"""Catch typed Prime API errors and inspect code / subcode / trace_id / body.

Required env vars:
    PRIME_CREDENTIALS   JSON with accessKey, passphrase, signingKey
    PRIME_PORTFOLIO_ID  Portfolio ID (or pass --portfolio-id)

Examples:
    python prime_sdk/examples/advanced/handle_api_errors.py
    python prime_sdk/examples/advanced/handle_api_errors.py --demo-validation
"""

import argparse
import os
import uuid

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.enums import OrderSide, OrderType
from prime_sdk.exceptions import (
    PrimeAPIError,
    PrimeBadRequestError,
    PrimeForbiddenError,
    PrimeInternalServerError,
    PrimeNotFoundError,
    PrimeServiceUnavailableError,
    PrimeTooManyRequestsError,
    PrimeUnauthorizedError,
)
from prime_sdk.services.orders import CreateOrderRequest, GetOrderRequest

MISSING_ORDER_ID = "00000000-0000-0000-0000-000000000000"


def print_api_error(error: PrimeAPIError) -> None:
    print(f"  exception: {type(error).__name__}")
    print(f"  status_code: {error.status_code}")
    print(f"  message: {error.message}")
    print(f"  code: {error.code}")
    print(f"  subcode: {error.subcode}")
    print(f"  trace_id: {error.trace_id}")
    if error.body is not None:
        print(f"  body: {type(error.body).__name__}")


def handle_order_lookup(
    client: PrimeServicesClient, portfolio_id: str, order_id: str
) -> None:
    print(f"GET order {order_id}")
    try:
        response = client.orders.get_order(
            GetOrderRequest(portfolio_id=portfolio_id, order_id=order_id)
        )
        print(response)
    except PrimeNotFoundError as error:
        print(
            "caught PrimeNotFoundError (HTTP 404) — the order or portfolio was not found"
        )
        print_api_error(error)
    except PrimeForbiddenError as error:
        print(
            "caught PrimeForbiddenError (HTTP 403) — this API key cannot read the order"
        )
        print_api_error(error)
    except PrimeUnauthorizedError as error:
        print("caught PrimeUnauthorizedError (HTTP 401) — check PRIME_CREDENTIALS")
        print_api_error(error)
    except PrimeTooManyRequestsError as error:
        print("caught PrimeTooManyRequestsError (HTTP 429) — back off and retry")
        print_api_error(error)
    except (PrimeInternalServerError, PrimeServiceUnavailableError) as error:
        print("caught a server-side error — retry after a short delay")
        print_api_error(error)
    except PrimeAPIError as error:
        print("caught PrimeAPIError")
        print_api_error(error)


def handle_invalid_create_order(client: PrimeServicesClient, portfolio_id: str) -> None:
    print("POST create_order with an invalid product_id")
    try:
        response = client.orders.create_order(
            CreateOrderRequest(
                portfolio_id=portfolio_id,
                product_id="NOT-A-PRODUCT",
                side=OrderSide.BUY,
                type=OrderType.MARKET,
                client_order_id=str(uuid.uuid4()),
                base_quantity="0.001",
            )
        )
        print(response)
    except PrimeBadRequestError as error:
        print(
            "caught PrimeBadRequestError (HTTP 400) — inspect subcode for the field that failed"
        )
        print_api_error(error)
    except PrimeAPIError as error:
        print("caught PrimeAPIError")
        print_api_error(error)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Demonstrate catching typed Prime API errors"
    )
    parser.add_argument(
        "--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    parser.add_argument(
        "--order-id",
        default=MISSING_ORDER_ID,
        help="Order ID to look up (default: a UUID that should 404)",
    )
    parser.add_argument(
        "--demo-validation",
        action="store_true",
        help="Also submit an invalid create_order request to show HTTP 400 handling",
    )
    args = parser.parse_args()

    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    if not portfolio_id:
        print(
            "Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id"
        )
        return

    client = PrimeServicesClient.from_env()
    handle_order_lookup(client, portfolio_id, args.order_id)
    if args.demo_validation:
        print()
        handle_invalid_create_order(client, portfolio_id)


if __name__ == "__main__":
    main()
