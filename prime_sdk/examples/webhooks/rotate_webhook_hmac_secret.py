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

# #docs operationId: PrimeBeta_RotateWebhookHMACSecret
# #docs operationName: Rotate Webhook HMAC Secret

import argparse
import os

from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.webhooks import RotateWebhookHMACSecretRequest


def save_secret(path: str, secret: str) -> None:
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as handle:
        handle.write(secret)


def main():
    parser = argparse.ArgumentParser(
        description="Rotate the HMAC signing secret for a webhook subscription"
    )
    parser.add_argument(
        "--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    parser.add_argument(
        "--subscription-id", required=True, help="Webhook subscription ID"
    )
    parser.add_argument(
        "--revoke-previous-immediately",
        action="store_true",
        help="Invalidate the old secret now instead of after the grace window",
    )
    parser.add_argument(
        "--secret-file",
        help="Write the new HMAC secret to this file (mode 0600) instead of discarding it",
    )
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()

    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    if not portfolio_id:
        print(
            "Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id"
        )
        return

    request = RotateWebhookHMACSecretRequest(
        portfolio_id=portfolio_id,
        subscription_id=args.subscription_id,
        revoke_previous_immediately=args.revoke_previous_immediately,
    )

    try:
        response = client.webhooks.rotate_webhook_hmac_secret(request)
        if response.hmac_secret:
            if args.secret_file:
                save_secret(args.secret_file, response.hmac_secret)
                print(f"New HMAC secret written to {args.secret_file}")
            else:
                print(
                    "New HMAC secret was returned but not saved; rerun with --secret-file"
                )
            response.hmac_secret = "<redacted>"
        print(response)
    except Exception as e:
        print(f"failed to rotate webhook HMAC secret: {e}")


if __name__ == "__main__":
    main()
