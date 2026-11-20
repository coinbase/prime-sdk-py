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

# #docs operationId: PrimeBeta_ListWebhookSubscriptions
# #docs operationName: List Webhook Subscriptions

import argparse
import os

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.webhooks import ListWebhookSubscriptionsRequest
from prime_sdk.utils import CursorLimitPaginationParams


def main():
    parser = argparse.ArgumentParser(
        description="List webhook subscriptions for a portfolio"
    )
    parser.add_argument(
        "--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    parser.add_argument(
        "--include-disabled", action="store_true", help="Include disabled subscriptions"
    )
    parser.add_argument("--event-type-filter", help="Only return this event type")
    parser.add_argument("--cursor", help="Pagination cursor from a previous response")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()

    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    if not portfolio_id:
        print(
            "Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id"
        )
        return

    request = ListWebhookSubscriptionsRequest(
        portfolio_id=portfolio_id,
        include_disabled=args.include_disabled,
        event_type_filter=args.event_type_filter,
        pagination=CursorLimitPaginationParams(cursor=args.cursor or ""),
    )

    try:
        response = client.webhooks.list_webhook_subscriptions(request)
        print(response)
    except Exception as e:
        print(f"failed to list webhook subscriptions: {e}")


if __name__ == "__main__":
    main()
