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

from dataclasses import dataclass

from ...base_response import BaseResponse
from ...model import GetInterestAccrualsRequest as _GetInterestAccrualsRequest
from ...model import GetInterestAccrualsResponse as _GetInterestAccrualsResponse


@dataclass(kw_only=True)
class ListInterestAccrualsRequest(_GetInterestAccrualsRequest):
    __doc__ = _GetInterestAccrualsRequest.__doc__

    allowed_status_codes: list[int] | None = None


@dataclass
class ListInterestAccrualsResponse(BaseResponse, _GetInterestAccrualsResponse):
    __doc__ = _GetInterestAccrualsResponse.__doc__
