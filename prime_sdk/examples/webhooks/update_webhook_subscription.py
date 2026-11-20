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

# #docs operationId: PrimeBeta_UpdateWebhookSubscription
# #docs operationName: Update Webhook Subscription

import argparse
import os

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.webhooks import UpdateWebhookSubscriptionRequest


def main():
    parser = argparse.ArgumentParser(description="Update a webhook subscription")
    parser.add_argument(
        "--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    parser.add_argument(
        "--subscription-id", required=True, help="Webhook subscription ID"
    )
    parser.add_argument("--target-url", help="New target URL")
    parser.add_argument("--event-types", help="Comma-separated replacement event types")
    parser.add_argument("--description", help="New description")
    enabled = parser.add_mutually_exclusive_group()
    enabled.add_argument(
        "--enable", dest="is_enabled", action="store_true", default=None
    )
    enabled.add_argument("--disable", dest="is_enabled", action="store_false")
    parser.add_argument(
        "--update-mask",
        help="Comma-separated fields to update (e.g. target_url,is_enabled)",
    )
    parser.add_argument(
        "--expected-version", help="Optimistic concurrency version from a prior read"
    )
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()

    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    if not portfolio_id:
        print(
            "Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id"
        )
        return

    event_types = None
    if args.event_types:
        event_types = [e.strip() for e in args.event_types.split(",") if e.strip()]

    if (
        args.target_url is None
        and event_types is None
        and args.description is None
        and args.is_enabled is None
    ):
        print(
            "Error: Provide at least one of --target-url, --event-types, "
            "--description, --enable, or --disable"
        )
        return

    request = UpdateWebhookSubscriptionRequest(
        portfolio_id=portfolio_id,
        subscription_id=args.subscription_id,
        target_url=args.target_url,
        event_types=event_types,
        description=args.description,
        is_enabled=args.is_enabled,
        update_mask=args.update_mask,
        expected_version=args.expected_version,
    )

    try:
        response = client.webhooks.update_webhook_subscription(request)
        print(response)
    except Exception as e:
        print(f"failed to update webhook subscription: {e}")


if __name__ == "__main__":
    main()
