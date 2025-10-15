# Copyright 2024-present Coinbase Global, Inc.
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

from .service import OnchainAddressBookService
from .create_onchain_address_book_entry import (
    CreateOnchainAddressBookEntryRequest,
    CreateOnchainAddressBookEntryResponse
)
from .delete_onchain_address_group import (
    DeleteOnchainAddressGroupRequest,
    DeleteOnchainAddressGroupResponse
)
from .list_onchain_address_groups import (
    ListOnchainAddressGroupsRequest,
    ListOnchainAddressGroupsResponse
)
from .update_onchain_address_book import (
    UpdateOnchainAddressBookRequest,
    UpdateOnchainAddressBookResponse
)

# Import model classes used by onchain address book to avoid import conflicts
from ...model import AddressGroup

# TODO: A better fix may be to rename this model? its a breaking change maybe?
# For the first Address class (onchain address book), we need to import it specifically
import prime_sdk.model as _model
# Get the first Address class definition for onchain address book
Address = _model.Address

__all__ = [
    "OnchainAddressBookService",
    "CreateOnchainAddressBookEntryRequest",
    "CreateOnchainAddressBookEntryResponse",
    "DeleteOnchainAddressGroupRequest",
    "DeleteOnchainAddressGroupResponse",
    "ListOnchainAddressGroupsRequest",
    "ListOnchainAddressGroupsResponse",
    "UpdateOnchainAddressBookRequest",
    "UpdateOnchainAddressBookResponse",
    "AddressGroup",
    "Address"
]