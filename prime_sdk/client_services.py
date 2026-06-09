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

"""
Compact lazy-loading implementation using a decorator pattern.
"""

from typing import Any, Callable, Optional, Type

import requests

from prime_sdk.client import Client
from prime_sdk.credentials import Credentials


class LazyProperty:
    def __init__(self, factory: Callable[["PrimeServicesClient"], Any]):
        self.factory = factory
        self.attr_name = None

    def __set_name__(self, owner: Type, name: str):
        self.attr_name = f"_lazy_{name}"

    def __get__(self, instance: "PrimeServicesClient", owner: Type = None):
        if instance is None:
            return self
        if hasattr(instance, self.attr_name):
            return getattr(instance, self.attr_name)
        service = self.factory(instance)
        setattr(instance, self.attr_name, service)
        return service


def lazy_service(service_factory):
    def factory(client_instance: "PrimeServicesClient"):
        if callable(service_factory) and getattr(service_factory, "__name__", None) == "<lambda>":
            service_class = service_factory()
        else:
            service_class = service_factory
        return service_class(client_instance._client)

    return LazyProperty(factory)


class PrimeServicesClient:
    def __init__(self, credentials: Credentials, http_client: Optional[requests.Session] = None):
        self._client = Client(credentials, http_client)

    @classmethod
    def from_env(
        cls, variable_name: str = "PRIME_CREDENTIALS", http_client: Optional[requests.Session] = None
    ) -> "PrimeServicesClient":
        credentials = Credentials.from_env(variable_name)
        return cls(credentials, http_client)

    @property
    def client(self) -> Client:
        return self._client

    activities = lazy_service(
        lambda: __import__("prime_sdk.services.activities.service", fromlist=["ActivitiesService"]).ActivitiesService
    )
    address_book = lazy_service(
        lambda: (
            __import__("prime_sdk.services.address_book.service", fromlist=["AddressBookService"]).AddressBookService
        )
    )
    advanced_transfers = lazy_service(
        lambda: (
            __import__(
                "prime_sdk.services.advanced_transfers.service", fromlist=["AdvancedTransfersService"]
            ).AdvancedTransfersService
        )
    )
    allocations = lazy_service(
        lambda: __import__("prime_sdk.services.allocations.service", fromlist=["AllocationsService"]).AllocationsService
    )
    assets = lazy_service(
        lambda: __import__("prime_sdk.services.assets.service", fromlist=["AssetsService"]).AssetsService
    )
    balances = lazy_service(
        lambda: __import__("prime_sdk.services.balances.service", fromlist=["BalancesService"]).BalancesService
    )
    commission = lazy_service(
        lambda: __import__("prime_sdk.services.commission.service", fromlist=["CommissionService"]).CommissionService
    )
    financing = lazy_service(
        lambda: __import__("prime_sdk.services.financing.service", fromlist=["FinancingService"]).FinancingService
    )
    futures = lazy_service(
        lambda: __import__("prime_sdk.services.futures.service", fromlist=["FuturesService"]).FuturesService
    )
    invoices = lazy_service(
        lambda: __import__("prime_sdk.services.invoices.service", fromlist=["InvoicesService"]).InvoicesService
    )
    onchain_address_book = lazy_service(
        lambda: (
            __import__(
                "prime_sdk.services.onchain_address_book.service", fromlist=["OnchainAddressBookService"]
            ).OnchainAddressBookService
        )
    )
    orders = lazy_service(
        lambda: __import__("prime_sdk.services.orders.service", fromlist=["OrdersService"]).OrdersService
    )
    payment_methods = lazy_service(
        lambda: (
            __import__(
                "prime_sdk.services.payment_methods.service", fromlist=["PaymentMethodsService"]
            ).PaymentMethodsService
        )
    )
    portfolios = lazy_service(
        lambda: __import__("prime_sdk.services.portfolios.service", fromlist=["PortfoliosService"]).PortfoliosService
    )
    positions = lazy_service(
        lambda: __import__("prime_sdk.services.positions.service", fromlist=["PositionsService"]).PositionsService
    )
    products = lazy_service(
        lambda: __import__("prime_sdk.services.products.service", fromlist=["ProductsService"]).ProductsService
    )
    staking = lazy_service(
        lambda: __import__("prime_sdk.services.staking.service", fromlist=["StakingService"]).StakingService
    )
    transactions = lazy_service(
        lambda: (
            __import__("prime_sdk.services.transactions.service", fromlist=["TransactionsService"]).TransactionsService
        )
    )
    users = lazy_service(lambda: __import__("prime_sdk.services.users.service", fromlist=["UsersService"]).UsersService)
    wallets = lazy_service(
        lambda: __import__("prime_sdk.services.wallets.service", fromlist=["WalletsService"]).WalletsService
    )
