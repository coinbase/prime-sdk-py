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

from enum import Enum


class XMCallStatus(str, Enum):
    XM_CALL_STATUS_UNSPECIFIED = "XM_CALL_STATUS_UNSPECIFIED"
    CALL_STATUS_OPEN = "CALL_STATUS_OPEN"
    CALL_STATUS_AGED = "CALL_STATUS_AGED"
    CALL_STATUS_SETTLED = "CALL_STATUS_SETTLED"
    CALL_STATUS_CANCELED = "CALL_STATUS_CANCELED"
