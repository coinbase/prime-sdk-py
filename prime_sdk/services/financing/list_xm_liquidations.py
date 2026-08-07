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
from ...model import ListXMLiquidationsRequest as _ListXMLiquidationsRequest
from ...model import ListXMLiquidationsResponse as _ListXMLiquidationsResponse


@dataclass(kw_only=True)
class ListXMLiquidationsRequest(_ListXMLiquidationsRequest):
    """
    List Cross Margin Liquidations

    Attributes:
        entity_id: XM customer Prime Entity ID
        status: Filter results by liquidation status -
            XM_LIQUIDATION_STATUS_PRE_LIQUIDATION: Liquidation is in the pre-liquidation
            phase - XM_LIQUIDATION_STATUS_LIQUIDATING: Liquidation is actively in progress -
            XM_LIQUIDATION_STATUS_LIQUIDATED: Liquidation has completed successfully -
            XM_LIQUIDATION_STATUS_CANCELED: Liquidation was canceled -
            XM_LIQUIDATION_STATUS_FAILED: Liquidation failed
        start_time: Filter results to liquidations created at or after this time
        end_time: Filter results to liquidations created at or before this time
    """

    cursor: str | None = None
    limit: int | None = None
    sort_direction: str | None = None

    allowed_status_codes: list[int] | None = None


@dataclass
class ListXMLiquidationsResponse(BaseResponse, _ListXMLiquidationsResponse):
    """
    ListXMLiquidationsResponse contains a paginated list of XM liquidation summaries

    Attributes:
        liquidations: List of XM liquidation summaries
    """
