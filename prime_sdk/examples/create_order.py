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
import uuid

from prime_sdk.credentials import Credentials
from prime_sdk.client import Client
from prime_sdk.services.orders import OrdersService, CreateOrderRequest
from prime_sdk.examples.constants import PORTFOLIO_ID, PRODUCT_ID, SIDE, TYPE, QUANTITY

def main():
    credentials = Credentials.from_env("PRIME_CREDENTIALS")
    client = Client(credentials)
    orders_service = OrdersService(client)

    request = CreateOrderRequest(
        portfolio_id=PORTFOLIO_ID,
        product_id=PRODUCT_ID,
        client_order_id=str(uuid.uuid4()),
        side=SIDE,
        type=TYPE,
        base_quantity=QUANTITY
    )
    try:
        response = orders_service.create_order(request)
        print(response)
    except Exception as e:
        print(f"failed to create order: {e}")


if __name__ == "__main__":
    main()
