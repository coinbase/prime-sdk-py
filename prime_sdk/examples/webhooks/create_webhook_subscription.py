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

# #docs operationId: PrimeBeta_CreateWebhookSubscription
# #docs operationName: Create Webhook Subscription

import argparse
import os

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.model import WebhookOAuthConfigInput
from prime_sdk.services.webhooks import CreateWebhookSubscriptionRequest


def save_secret(path: str, secret: str) -> None:
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as handle:
        handle.write(secret)


def main():
    parser = argparse.ArgumentParser(
        description="Create a webhook subscription for a portfolio"
    )
    parser.add_argument(
        "--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    parser.add_argument(
        "--target-url", required=True, help="HTTPS URL that receives webhook events"
    )
    parser.add_argument(
        "--event-types",
        required=True,
        help="Comma-separated event types (see get_webhook_event_types.py)",
    )
    parser.add_argument(
        "--auth-type",
        default="WEBHOOK_AUTH_TYPE_HMAC",
        choices=[
            "WEBHOOK_AUTH_TYPE_HMAC",
            "WEBHOOK_AUTH_TYPE_OAUTH",
            "WEBHOOK_AUTH_TYPE_MTLS",
            "WEBHOOK_AUTH_TYPE_OAUTH_MTLS",
        ],
        help="How Prime authenticates to your endpoint",
    )
    parser.add_argument("--description", help="Optional description")
    parser.add_argument("--idempotency-key", help="Optional idempotency key")
    parser.add_argument("--oauth-token-url", help="OAuth token URL (OAuth auth types)")
    parser.add_argument("--oauth-client-id", help="OAuth client ID (OAuth auth types)")
    parser.add_argument(
        "--oauth-scopes", help="Comma-separated OAuth scopes (OAuth auth types)"
    )
    parser.add_argument(
        "--secret-file",
        help="Write the one-time HMAC secret to this file (mode 0600) instead of discarding it",
    )
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()

    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    if not portfolio_id:
        print(
            "Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id"
        )
        return

    oauth_config = None
    if "OAUTH" in args.auth_type:
        client_secret = os.getenv("PRIME_WEBHOOK_OAUTH_CLIENT_SECRET")
        if not (args.oauth_token_url and args.oauth_client_id and client_secret):
            print(
                "Error: OAuth auth types require --oauth-token-url, --oauth-client-id, "
                "and the PRIME_WEBHOOK_OAUTH_CLIENT_SECRET env var"
            )
            return
        oauth_config = WebhookOAuthConfigInput(
            token_url=args.oauth_token_url,
            client_id=args.oauth_client_id,
            client_secret=client_secret,
            scopes=args.oauth_scopes.split(",") if args.oauth_scopes else None,
        )

    request = CreateWebhookSubscriptionRequest(
        portfolio_id=portfolio_id,
        target_url=args.target_url,
        event_types=[e.strip() for e in args.event_types.split(",") if e.strip()],
        auth_type=args.auth_type,
        oauth_config=oauth_config,
        description=args.description,
        idempotency_key=args.idempotency_key,
    )

    try:
        response = client.webhooks.create_webhook_subscription(request)
        if response.hmac_secret:
            if args.secret_file:
                save_secret(args.secret_file, response.hmac_secret)
                print(f"HMAC secret written to {args.secret_file}")
            else:
                print(
                    "HMAC secret was returned but not saved; rerun with --secret-file "
                    "or rotate it with rotate_webhook_hmac_secret.py"
                )
            response.hmac_secret = "<redacted>"
        print(response)
    except Exception as e:
        print(f"failed to create webhook subscription: {e}")


if __name__ == "__main__":
    main()
