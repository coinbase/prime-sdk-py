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
from ...model import GetPortfolioProductsRequest as _GetPortfolioProductsRequest
from ...model import GetPortfolioProductsResponse as _GetPortfolioProductsResponse
from ...utils import PaginationParams


@dataclass(kw_only=True)
class ListProductsRequest(_GetPortfolioProductsRequest):
    """
    List Portfolio Products

    Attributes:
        portfolio_id: The portfolio ID
        product_type: Filter by product type (SPOT, FUTURE). If unset, returns all types
            available for your portfolio. Futures products require additional entitlements.
            - UNKNOWN_PRODUCT_TYPE: Unknown product type - SPOT: Spot product - FUTURE:
            Future product - OPTION: Option product
        contract_expiry_type: Filter by contract expiry type (EXPIRING or PERPETUAL). Only
            applicable when product_type = FUTURE. If unset, returns all futures kinds. -
            CONTRACT_EXPIRY_TYPE_UNSPECIFIED: Unspecified contract expiry type -
            CONTRACT_EXPIRY_TYPE_EXPIRING: Expiring futures contract -
            CONTRACT_EXPIRY_TYPE_PERPETUAL: Perpetual futures contract (no expiry)
        expiring_contract_status: Filter by expiry status for expiring futures. If unset,
            returns all expiring futures. - EXPIRING_CONTRACT_STATUS_UNKNOWN: Unknown/unset
            — returns all expiring contracts (backward compatible default) -
            EXPIRING_CONTRACT_STATUS_UNEXPIRED: Only unexpired contracts (contract_expiry is
            in the future) - EXPIRING_CONTRACT_STATUS_EXPIRED: Only expired contracts
            (contract_expiry is in the past) - EXPIRING_CONTRACT_STATUS_ALL: All contracts
            regardless of expiry status
    """

    pagination: PaginationParams | None = None

    allowed_status_codes: list[int] | None = None


@dataclass
class ListProductsResponse(BaseResponse, _GetPortfolioProductsResponse):
    """ListProductsResponse(products: 'list[Product]' = None, pagination: 'PaginatedResponse' = None)"""
