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

from ...client import Client
from .cancel_entity_futures_sweep import (
    CancelEntityFuturesSweepRequest,
    CancelEntityFuturesSweepResponse
)
from .schedule_entity_futures_sweep import (
    ScheduleEntityFuturesSweepRequest,
    ScheduleEntityFuturesSweepResponse
)
from .list_entity_futures_sweeps import (
    ListEntityFuturesSweepsRequest,
    ListEntityFuturesSweepsResponse
)
from .set_auto_sweep import (
    SetAutoSweepRequest,
    SetAutoSweepResponse
)
from .get_entity_fcm_balance import (
    GetEntityFcmBalanceRequest,
    GetEntityFcmBalanceResponse
)
from .get_entity_positions import (
    GetEntityPositionsRequest,
    GetEntityPositionsResponse
)
from .get_fcm_margin_call_details import (
    GetFcmMarginCallDetailsRequest,
    GetFcmMarginCallDetailsResponse
)
from .get_fcm_risk_limits import (
    GetFcmRiskLimitsRequest,
    GetFcmRiskLimitsResponse
)
from ...utils import to_body_dict


class FuturesService:
    def __init__(self, client: Client):
        self.client = client

    def cancel_entity_futures_sweep(self, request: CancelEntityFuturesSweepRequest) -> CancelEntityFuturesSweepResponse:
        path = f"/entities/{request.entity_id}/futures_sweep"
        response = self.client.request("DELETE", path, allowed_status_codes=request.allowed_status_codes)
        return CancelEntityFuturesSweepResponse(**response.json())

    def schedule_entity_futures_sweep(self, request: ScheduleEntityFuturesSweepRequest) -> ScheduleEntityFuturesSweepResponse:
        path = f"/entities/{request.entity_id}/futures_sweep"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return ScheduleEntityFuturesSweepResponse(**response.json())

    def list_entity_futures_sweeps(self, request: ListEntityFuturesSweepsRequest) -> ListEntityFuturesSweepsResponse:
        path = f"/entities/{request.entity_id}/futures_sweeps"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return ListEntityFuturesSweepsResponse(**response.json())

    def set_auto_sweep(self, request: SetAutoSweepRequest) -> SetAutoSweepResponse:
        path = f"/entities/{request.entity_id}/auto_sweep"
        body = to_body_dict(request)
        response = self.client.request("PUT", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return SetAutoSweepResponse(**response.json())

    def get_entity_fcm_balance(self, request: GetEntityFcmBalanceRequest) -> GetEntityFcmBalanceResponse:
        path = f"/entities/{request.entity_id}/fcm_balance"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetEntityFcmBalanceResponse(**response.json())

    def get_entity_positions(self, request: GetEntityPositionsRequest) -> GetEntityPositionsResponse:
        path = f"/entities/{request.entity_id}/positions"
        query_params = ""
        if request.product_id:
            query_params = f"product_id={request.product_id}"
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return GetEntityPositionsResponse(**response.json())

    def get_fcm_margin_call_details(self, request: GetFcmMarginCallDetailsRequest) -> GetFcmMarginCallDetailsResponse:
        path = f"/entities/{request.entity_id}/futures/margin_call_details"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetFcmMarginCallDetailsResponse(**response.json())

    def get_fcm_risk_limits(self, request: GetFcmRiskLimitsRequest) -> GetFcmRiskLimitsResponse:
        path = f"/entities/{request.entity_id}/futures/risk_limits"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetFcmRiskLimitsResponse(**response.json())