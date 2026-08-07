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

from dataclasses import dataclass

from ...base_response import BaseResponse
from ...model import OrderPreviewRequest as _OrderPreviewRequest
from ...model import PostOrderPreviewResponse as _PostOrderPreviewResponse


@dataclass(kw_only=True)
class CreateOrderPreviewRequest(_OrderPreviewRequest):
    __doc__ = _OrderPreviewRequest.__doc__

    portfolio_id: str
    stp_id: str | None = None
    post_only: bool | None = None

    allowed_status_codes: list[int] | None = None


@dataclass
class CreateOrderPreviewResponse(BaseResponse, _PostOrderPreviewResponse):
    __doc__ = _PostOrderPreviewResponse.__doc__

    settl_currency: str = None
    post_only: bool = None
