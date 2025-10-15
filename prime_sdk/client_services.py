"""
Compact lazy-loading implementation using a decorator pattern.
This approach is more concise and uses Python's descriptor protocol.
"""

from typing import Optional, Any, Dict, Type, Callable
import requests
from prime_sdk.client import Client
from prime_sdk.credentials import Credentials


class LazyProperty:
    """
    A descriptor that implements lazy loading for service properties.
    This is a more elegant and reusable approach.
    """
    
    def __init__(self, factory: Callable[['PrimeServicesClient'], Any]):
        self.factory = factory
        self.attr_name = None
    
    def __set_name__(self, owner: Type, name: str):
        self.attr_name = f'_lazy_{name}'
    
    def __get__(self, instance: 'PrimeServicesClient', owner: Type = None):
        if instance is None:
            return self
        
        # Check if already cached
        if hasattr(instance, self.attr_name):
            return getattr(instance, self.attr_name)
        
        # Create and cache the service
        service = self.factory(instance)
        setattr(instance, self.attr_name, service)
        return service


def lazy_service(service_factory):
    """
    Decorator factory for creating lazy service properties.
    Usage: @lazy_service(lambda: OrdersService) or @lazy_service(OrdersService)
    """
    def factory(client_instance: 'PrimeServicesClient'):
        # Handle both lambda functions and direct class references
        if callable(service_factory) and getattr(service_factory, '__name__', None) == '<lambda>':
            # It's a lambda function that returns the class
            service_class = service_factory()
        else:
            # It's a direct class reference
            service_class = service_factory
        return service_class(client_instance._client)
    
    return LazyProperty(factory)


class PrimeServicesClient:
    """
    A very compact lazy-loading client using descriptors.
    This approach is the most concise and elegant.
    """
    
    def __init__(self, credentials: Credentials, http_client: Optional[requests.Session] = None):
        self._client = Client(credentials, http_client)
    
    @classmethod
    def from_env(cls, variable_name: str = 'PRIME_CREDENTIALS', 
                 http_client: Optional[requests.Session] = None) -> 'PrimeServicesClient':
        """Create a PrimeServicesClient with credentials from environment variables."""
        credentials = Credentials.from_env(variable_name)
        return cls(credentials, http_client)
    
    @property
    def client(self) -> Client:
        """Access to the underlying Prime SDK client."""
        return self._client
    
    # Import services dynamically to avoid circular imports
    activities = lazy_service(lambda: __import__('prime_sdk.services.activities.service', fromlist=['ActivitiesService']).ActivitiesService)
    orders = lazy_service(lambda: __import__('prime_sdk.services.orders.service', fromlist=['OrdersService']).OrdersService)
    portfolios = lazy_service(lambda: __import__('prime_sdk.services.portfolios.service', fromlist=['PortfoliosService']).PortfoliosService)
    wallets = lazy_service(lambda: __import__('prime_sdk.services.wallets.service', fromlist=['WalletsService']).WalletsService)
    assets = lazy_service(lambda: __import__('prime_sdk.services.assets.service', fromlist=['AssetsService']).AssetsService)
    balances = lazy_service(lambda: __import__('prime_sdk.services.balances.service', fromlist=['BalancesService']).BalancesService)
    transactions = lazy_service(lambda: __import__('prime_sdk.services.transactions.service', fromlist=['TransactionsService']).TransactionsService)
    products = lazy_service(lambda: __import__('prime_sdk.services.products.service', fromlist=['ProductsService']).ProductsService)
    address_book = lazy_service(lambda: __import__('prime_sdk.services.address_book.service', fromlist=['AddressBookService']).AddressBookService)
    allocations = lazy_service(lambda: __import__('prime_sdk.services.allocations.service', fromlist=['AllocationsService']).AllocationsService)
    commission = lazy_service(lambda: __import__('prime_sdk.services.commission.service', fromlist=['CommissionService']).CommissionService)
    financing = lazy_service(lambda: __import__('prime_sdk.services.financing.service', fromlist=['FinancingService']).FinancingService)
    futures = lazy_service(lambda: __import__('prime_sdk.services.futures.service', fromlist=['FuturesService']).FuturesService)
    invoices = lazy_service(lambda: __import__('prime_sdk.services.invoices.service', fromlist=['InvoicesService']).InvoicesService)
    onchain_address_book = lazy_service(lambda: __import__('prime_sdk.services.onchain_address_book.service', fromlist=['OnchainAddressBookService']).OnchainAddressBookService)
    payment_methods = lazy_service(lambda: __import__('prime_sdk.services.payment_methods.service', fromlist=['PaymentMethodsService']).PaymentMethodsService)
    positions = lazy_service(lambda: __import__('prime_sdk.services.positions.service', fromlist=['PositionsService']).PositionsService)
    staking = lazy_service(lambda: __import__('prime_sdk.services.staking.service', fromlist=['StakingService']).StakingService)
    users = lazy_service(lambda: __import__('prime_sdk.services.users.service', fromlist=['UsersService']).UsersService)


# Even more advanced: Generic factory approach
class FactoryPrimeServicesClient:
    """
    Advanced approach using a generic factory pattern.
    This allows for the most flexibility and customization.
    """
    
    def __init__(self, credentials: Credentials, http_client: Optional[requests.Session] = None):
        self._client = Client(credentials, http_client)
        self._service_factories: Dict[str, Callable[[], Any]] = {}
        self._service_cache: Dict[str, Any] = {}
        self._setup_service_factories()
    
    @classmethod
    def from_env(cls, variable_name: str = 'PRIME_CREDENTIALS', 
                 http_client: Optional[requests.Session] = None) -> 'FactoryPrimeServicesClient':
        """Create a FactoryPrimeServicesClient with credentials from environment variables."""
        credentials = Credentials.from_env(variable_name)
        return cls(credentials, http_client)
    
    def _setup_service_factories(self):
        """Setup factory functions for all services."""
        # This could be loaded from configuration, metadata, or auto-discovered
        service_mappings = {
            'activities': 'prime_sdk.services.activities.service.ActivitiesService',
            'address_book': 'prime_sdk.services.address_book.service.AddressBookService',
            'allocations': 'prime_sdk.services.allocations.service.AllocationsService',
            'assets': 'prime_sdk.services.assets.service.AssetsService',
            'balances': 'prime_sdk.services.balances.service.BalancesService',
            'commission': 'prime_sdk.services.commission.service.CommissionService',
            'financing': 'prime_sdk.services.financing.service.FinancingService',
            'futures': 'prime_sdk.services.futures.service.FuturesService',
            'invoices': 'prime_sdk.services.invoices.service.InvoicesService',
            'onchain_address_book': 'prime_sdk.services.onchain_address_book.service.OnchainAddressBookService',
            'orders': 'prime_sdk.services.orders.service.OrdersService',
            'payment_methods': 'prime_sdk.services.payment_methods.service.PaymentMethodsService',
            'portfolios': 'prime_sdk.services.portfolios.service.PortfoliosService',
            'positions': 'prime_sdk.services.positions.service.PositionsService',
            'products': 'prime_sdk.services.products.service.ProductsService',
            'staking': 'prime_sdk.services.staking.service.StakingService',
            'transactions': 'prime_sdk.services.transactions.service.TransactionsService',
            'users': 'prime_sdk.services.users.service.UsersService',
            'wallets': 'prime_sdk.services.wallets.service.WalletsService',
        }
        
        for service_name, import_path in service_mappings.items():
            self._service_factories[service_name] = self._create_factory(import_path)
    
    def _create_factory(self, import_path: str) -> Callable[[], Any]:
        """Create a factory function for a service class."""
        def factory():
            module_path, class_name = import_path.rsplit('.', 1)
            module = __import__(module_path, fromlist=[class_name])
            service_class = getattr(module, class_name)
            return service_class(self._client)
        return factory
    
    def get_service(self, service_name: str) -> Any:
        """Get a service by name, creating it lazily if needed."""
        if service_name not in self._service_cache:
            if service_name not in self._service_factories:
                raise ValueError(f"Unknown service: {service_name}")
            self._service_cache[service_name] = self._service_factories[service_name]()
        return self._service_cache[service_name]
    
    def __getattr__(self, name: str) -> Any:
        """Allow accessing services as attributes."""
        if name in self._service_factories:
            return self.get_service(name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    
    @property
    def client(self) -> Client:
        """Access to the underlying Prime SDK client."""
        return self._client
    
    def list_available_services(self) -> list[str]:
        """List all available services."""
        return list(self._service_factories.keys())


# Usage examples
if __name__ == "__main__":
    print("=== Compact Lazy Client (Descriptor Pattern) ===")
    
    compact_client = PrimeServicesClient.from_env()
    
    # Services are created on first access
    orders = compact_client.orders
    print(f"Orders service: {type(orders).__name__}")
    
    portfolios = compact_client.portfolios
    print(f"Portfolios service: {type(portfolios).__name__}")
    
    print(f"Same orders instance: {compact_client.orders is orders}")
    
    print("\n=== Factory Lazy Client ===")
    
    factory_client = FactoryPrimeServicesClient.from_env()
    
    print(f"Available services: {factory_client.list_available_services()}")
    
    # Access services
    wallets = factory_client.wallets
    assets = factory_client.assets
    
    print(f"Wallets service: {type(wallets).__name__}")
    print(f"Assets service: {type(assets).__name__}")


