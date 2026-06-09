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

from __future__ import annotations

from dataclasses import dataclass

from ..enums import AddressBookType
from . import DisplayUser


@dataclass(kw_only=True)
class AddressBookEntry:
    id: str
    currency_symbol: str | None
    name: str
    address: str | None
    account_identifier: str | None
    account_identifier_name: str | None
    state: str
    explorer_link: str | None
    last_used_at: str | None
    added_at: str | None
    added_by: DisplayUser
    type: AddressBookType | None = AddressBookType.ADDRESS_BOOK_TYPE_UNSPECIFIED
    counterparty_id: str | None
