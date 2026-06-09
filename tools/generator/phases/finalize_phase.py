from __future__ import annotations

from pathlib import Path

from tools.generator.utils.copyright import apply_copyright


def _pascal_to_snake(name: str) -> str:
    import re

    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower().replace("service", "").strip("_")


def run_finalize_phase(
    repo_root: Path,
    domain_exports: dict[str, list[str]],
    naming_config: dict,
    dry_run: bool = False,
) -> None:
    prime_sdk = repo_root / "prime_sdk"

    service_imports = []
    service_all = []
    lazy_props = []
    factory_mappings = []

    for domain in sorted(domain_exports.keys()):
        service_class = naming_config["domain_to_service_class"][domain]
        service_imports.append(f"from .services.{domain} import {service_class}")
        service_all.append(service_class)
        attr = domain
        lazy_props.append(
            f"    {attr} = lazy_service(lambda: __import__('prime_sdk.services.{domain}.service', "
            f"fromlist=['{service_class}']).{service_class})"
        )
        factory_mappings.append(f"            '{attr}': 'prime_sdk.services.{domain}.service.{service_class}',")

    init_content = apply_copyright(
        "# Core classes\n"
        "from .client import Client\n"
        "from .client_services import PrimeServicesClient\n"
        "from .credentials import Credentials\n\n"
        "# Service classes - primary interface\n" + "\n".join(service_imports) + "\n\n__all__ = [\n"
        '    "Client",\n'
        '    "PrimeServicesClient",\n'
        '    "Credentials",\n' + "".join(f'    "{s}",\n' for s in service_all) + "]\n"
    )

    client_services_header = '''"""
Compact lazy-loading implementation using a decorator pattern.
"""

from typing import Optional, Any, Dict, Type, Callable
import requests
from prime_sdk.client import Client
from prime_sdk.credentials import Credentials


class LazyProperty:
    def __init__(self, factory: Callable[['PrimeServicesClient'], Any]):
        self.factory = factory
        self.attr_name = None

    def __set_name__(self, owner: Type, name: str):
        self.attr_name = f'_lazy_{name}'

    def __get__(self, instance: 'PrimeServicesClient', owner: Type = None):
        if instance is None:
            return self
        if hasattr(instance, self.attr_name):
            return getattr(instance, self.attr_name)
        service = self.factory(instance)
        setattr(instance, self.attr_name, service)
        return service


def lazy_service(service_factory):
    def factory(client_instance: 'PrimeServicesClient'):
        if callable(service_factory) and getattr(service_factory, '__name__', None) == '<lambda>':
            service_class = service_factory()
        else:
            service_class = service_factory
        return service_class(client_instance._client)
    return LazyProperty(factory)


class PrimeServicesClient:
    def __init__(self, credentials: Credentials, http_client: Optional[requests.Session] = None):
        self._client = Client(credentials, http_client)

    @classmethod
    def from_env(cls, variable_name: str = 'PRIME_CREDENTIALS',
                 http_client: Optional[requests.Session] = None) -> 'PrimeServicesClient':
        credentials = Credentials.from_env(variable_name)
        return cls(credentials, http_client)

    @property
    def client(self) -> Client:
        return self._client

'''

    client_services_content = apply_copyright(client_services_header + "\n".join(lazy_props) + "\n")

    if not dry_run:
        (prime_sdk / "__init__.py").write_text(init_content)
        (prime_sdk / "client_services.py").write_text(client_services_content)
        (prime_sdk / "py.typed").write_text("")

        # Compatibility shim for old import path (enums.py module vs enums/ package)
        enums_shim = apply_copyright(
            "# Compatibility shim - import from prime_sdk.enums package.\nfrom .enums import *  # noqa: F403\n"
        )
        (prime_sdk / "enums.py").write_text(enums_shim)
