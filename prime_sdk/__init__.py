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

# Core classes
from .client import Client
from .client_services import PrimeServicesClient
from .credentials import Credentials

# Service classes - primary interface
from .services.activities import ActivitiesService
from .services.address_book import AddressBookService
from .services.allocations import AllocationsService
from .services.assets import AssetsService
from .services.balances import BalancesService
from .services.commission import CommissionService
from .services.financing import FinancingService
from .services.futures import FuturesService
from .services.invoices import InvoicesService
from .services.onchain_address_book import OnchainAddressBookService
from .services.orders import OrdersService
from .services.payment_methods import PaymentMethodsService
from .services.portfolios import PortfoliosService
from .services.positions import PositionsService
from .services.products import ProductsService
from .services.staking import StakingService
from .services.transactions import TransactionsService
from .services.users import UsersService
from .services.wallets import WalletsService

__all__ = [
    # Core classes
    "Client",
    "PrimeServicesClient",
    "Credentials",
    
    # Service classes
    "ActivitiesService",
    "AddressBookService", 
    "AllocationsService",
    "AssetsService",
    "BalancesService",
    "CommissionService",
    "FinancingService",
    "FuturesService",
    "InvoicesService",
    "OnchainAddressBookService",
    "OrdersService",
    "PaymentMethodsService",
    "PortfoliosService",
    "PositionsService",
    "ProductsService",
    "StakingService",
    "TransactionsService",
    "UsersService",
    "WalletsService",
]

# For request/response classes, users should import directly from services:
# from prime_sdk.services.wallets import CreateWalletRequest, CreateWalletResponse
# from prime_sdk.services.transactions import CreateConversionRequest, CreateConversionResponse
# etc.