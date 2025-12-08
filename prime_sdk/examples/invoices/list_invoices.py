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

# #docs operationId: PrimeRESTAPI_GetInvoices
# #docs operationName: List Invoices

import argparse
import os
from prime_sdk.client_services import PrimeServicesClient
from prime_sdk.services.invoices import ListInvoicesRequest
from prime_sdk.utils import PaginationParams

def main():
    parser = argparse.ArgumentParser(description="List invoices for an entity")
    parser.add_argument("--entity-id", help="Entity ID (overrides PRIME_ENTITY_ID env var)")
    parser.add_argument("--states", help="Invoice states filter (e.g., DRAFT,SENT,PAID)")
    parser.add_argument("--billing-year", type=int, help="Billing year filter (e.g., 2025)")
    parser.add_argument("--billing-month", help="Billing month filter (e.g., JANUARY, FEBRUARY)")
    parser.add_argument("--limit", type=int, help="Number of results to return")
    parser.add_argument("--cursor", help="Pagination cursor")
    args = parser.parse_args()

    client = PrimeServicesClient.from_env()
    
    entity_id = args.entity_id or os.getenv("PRIME_ENTITY_ID")
    if not entity_id:
        print("Error: Entity ID is required. Set PRIME_ENTITY_ID env var or use --entity-id")
        return

    # Set up pagination if provided
    pagination = None
    if args.limit or args.cursor:
        pagination = PaginationParams(
            limit=args.limit,
            cursor=args.cursor
        )
    
    request = ListInvoicesRequest(
        entity_id=entity_id,
        states=args.states,
        billing_year=args.billing_year,
        billing_month=args.billing_month,
        pagination=pagination
    )
    
    try:
        response = client.invoices.list_invoices(request)
        print(response)
    except Exception as e:
        print(f"failed to list invoices: {e}")


if __name__ == "__main__":
    main()
