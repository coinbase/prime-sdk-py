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

# #docs operationId: PrimeRESTAPI_SubmitDepositTravelRuleData
# #docs operationName: Submit Deposit Travel Rule Data

import argparse
import os
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.transactions import (
    SubmitDepositTravelRuleDataRequest,
    TravelRuleParty,
)


def main():
    parser = argparse.ArgumentParser(
        description="Submit travel rule data for an existing deposit transaction"
    )
    parser.add_argument(
        "--portfolio-id", help="Portfolio ID (overrides PRIME_PORTFOLIO_ID env var)"
    )
    parser.add_argument("--transaction-id", required=True, help="Transaction ID")
    parser.add_argument(
        "--is-self",
        action="store_true",
        help="True if user owns the counterparty address (self-transfer)",
    )
    parser.add_argument(
        "--opt-out-verification",
        action="store_true",
        help="True to skip wallet ownership verification",
    )
    parser.add_argument("--originator-name", help="Originator's name")
    parser.add_argument("--beneficiary-name", help="Beneficiary's name")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()

    portfolio_id = args.portfolio_id or os.getenv("PRIME_PORTFOLIO_ID")
    if not portfolio_id:
        print(
            "Error: Portfolio ID is required. Set PRIME_PORTFOLIO_ID env var or use --portfolio-id"
        )
        return

    # Build originator if name is provided
    originator = None
    if args.originator_name:
        originator = TravelRuleParty(name=args.originator_name)

    # Build beneficiary if name is provided
    beneficiary = None
    if args.beneficiary_name:
        beneficiary = TravelRuleParty(name=args.beneficiary_name)

    request = SubmitDepositTravelRuleDataRequest(
        portfolio_id=portfolio_id,
        transaction_id=args.transaction_id,
        originator=originator,
        beneficiary=beneficiary,
        is_self=args.is_self,
        opt_out_of_ownership_verification=args.opt_out_verification,
    )

    try:
        response = client.transactions.submit_deposit_travel_rule_data(request)
        print(response)
    except Exception as e:
        print(f"failed to submit travel rule data: {e}")


if __name__ == "__main__":
    main()
