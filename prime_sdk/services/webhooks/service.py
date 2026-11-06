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

from ...client import Client
from ...utils import append_pagination_params, append_query_param, to_body_dict
from .create_webhook_subscription import (
    CreateWebhookSubscriptionRequest,
    CreateWebhookSubscriptionResponse,
)
from .delete_webhook_subscription import (
    DeleteWebhookSubscriptionRequest,
    DeleteWebhookSubscriptionResponse,
)
from .get_webhook_delivery_attempts import (
    GetWebhookDeliveryAttemptsRequest,
    GetWebhookDeliveryAttemptsResponse,
)
from .get_webhook_delivery_logs import (
    GetWebhookDeliveryLogsRequest,
    GetWebhookDeliveryLogsResponse,
)
from .get_webhook_event_types import (
    GetWebhookEventTypesRequest,
    GetWebhookEventTypesResponse,
)
from .get_webhook_owner_stats import (
    GetWebhookOwnerStatsRequest,
    GetWebhookOwnerStatsResponse,
)
from .get_webhook_subscription import (
    GetWebhookSubscriptionRequest,
    GetWebhookSubscriptionResponse,
)
from .get_webhook_subscription_stats import (
    GetWebhookSubscriptionStatsRequest,
    GetWebhookSubscriptionStatsResponse,
)
from .list_webhook_subscriptions import (
    ListWebhookSubscriptionsRequest,
    ListWebhookSubscriptionsResponse,
)
from .replay_webhook_event import (
    ReplayWebhookEventRequest,
    ReplayWebhookEventResponse,
)
from .rotate_webhook_hmac_secret import (
    RotateWebhookHMACSecretRequest,
    RotateWebhookHMACSecretResponse,
)
from .send_webhook_simulation import (
    SendWebhookSimulationRequest,
    SendWebhookSimulationResponse,
)
from .update_webhook_subscription import (
    UpdateWebhookSubscriptionRequest,
    UpdateWebhookSubscriptionResponse,
)


def _enum_value(value):
    return getattr(value, "value", value)


class WebhooksService:
    def __init__(self, client: Client):
        self.client = client

    def list_webhook_subscriptions(
        self, request: ListWebhookSubscriptionsRequest
    ) -> ListWebhookSubscriptionsResponse:
        path = f"/portfolios/{request.portfolio_id}/webhooks/subscriptions"
        query_params = append_query_param(
            "", "include_disabled", "true" if request.include_disabled else None
        )
        query_params = append_query_param(
            query_params, "event_type_filter", request.event_type_filter
        )
        query_params = append_pagination_params(query_params, request.pagination)
        response = self.client.request(
            "GET",
            path,
            query=query_params,
            allowed_status_codes=request.allowed_status_codes,
        )
        return ListWebhookSubscriptionsResponse.from_response(response.json())

    def create_webhook_subscription(
        self, request: CreateWebhookSubscriptionRequest
    ) -> CreateWebhookSubscriptionResponse:
        path = f"/portfolios/{request.portfolio_id}/webhooks/subscriptions"
        body = to_body_dict(request)
        response = self.client.request(
            "POST", path, body=body, allowed_status_codes=request.allowed_status_codes
        )
        return CreateWebhookSubscriptionResponse.from_response(response.json())

    def get_webhook_subscription(
        self, request: GetWebhookSubscriptionRequest
    ) -> GetWebhookSubscriptionResponse:
        path = f"/portfolios/{request.portfolio_id}/webhooks/subscriptions/{request.subscription_id}"
        response = self.client.request(
            "GET", path, allowed_status_codes=request.allowed_status_codes
        )
        return GetWebhookSubscriptionResponse.from_response(response.json())

    def update_webhook_subscription(
        self, request: UpdateWebhookSubscriptionRequest
    ) -> UpdateWebhookSubscriptionResponse:
        path = f"/portfolios/{request.portfolio_id}/webhooks/subscriptions/{request.subscription_id}"
        body = to_body_dict(request)
        response = self.client.request(
            "PATCH", path, body=body, allowed_status_codes=request.allowed_status_codes
        )
        return UpdateWebhookSubscriptionResponse.from_response(response.json())

    def delete_webhook_subscription(
        self, request: DeleteWebhookSubscriptionRequest
    ) -> DeleteWebhookSubscriptionResponse:
        path = f"/portfolios/{request.portfolio_id}/webhooks/subscriptions/{request.subscription_id}"
        response = self.client.request(
            "DELETE", path, allowed_status_codes=request.allowed_status_codes
        )
        return DeleteWebhookSubscriptionResponse.from_response(response.json())

    def rotate_webhook_hmac_secret(
        self, request: RotateWebhookHMACSecretRequest
    ) -> RotateWebhookHMACSecretResponse:
        path = f"/portfolios/{request.portfolio_id}/webhooks/subscriptions/{request.subscription_id}/rotate-hmac-secret"
        body = to_body_dict(request)
        response = self.client.request(
            "POST", path, body=body, allowed_status_codes=request.allowed_status_codes
        )
        return RotateWebhookHMACSecretResponse.from_response(response.json())

    def send_webhook_simulation(
        self, request: SendWebhookSimulationRequest
    ) -> SendWebhookSimulationResponse:
        path = f"/portfolios/{request.portfolio_id}/webhooks/subscriptions/{request.subscription_id}/simulate"
        body = to_body_dict(request)
        response = self.client.request(
            "POST", path, body=body, allowed_status_codes=request.allowed_status_codes
        )
        return SendWebhookSimulationResponse.from_response(response.json())

    def get_webhook_delivery_logs(
        self, request: GetWebhookDeliveryLogsRequest
    ) -> GetWebhookDeliveryLogsResponse:
        path = f"/portfolios/{request.portfolio_id}/webhooks/subscriptions/{request.subscription_id}/deliveries"
        query_params = append_query_param(
            "", "status_filter", _enum_value(request.status_filter)
        )
        query_params = append_query_param(
            query_params, "event_type_filter", request.event_type_filter
        )
        query_params = append_pagination_params(query_params, request.pagination)
        response = self.client.request(
            "GET",
            path,
            query=query_params,
            allowed_status_codes=request.allowed_status_codes,
        )
        return GetWebhookDeliveryLogsResponse.from_response(response.json())

    def get_webhook_delivery_attempts(
        self, request: GetWebhookDeliveryAttemptsRequest
    ) -> GetWebhookDeliveryAttemptsResponse:
        path = f"/portfolios/{request.portfolio_id}/webhooks/subscriptions/{request.subscription_id}/deliveries/{request.event_id}/attempts"
        response = self.client.request(
            "GET", path, allowed_status_codes=request.allowed_status_codes
        )
        return GetWebhookDeliveryAttemptsResponse.from_response(response.json())

    def get_webhook_subscription_stats(
        self, request: GetWebhookSubscriptionStatsRequest
    ) -> GetWebhookSubscriptionStatsResponse:
        path = f"/portfolios/{request.portfolio_id}/webhooks/subscriptions/{request.subscription_id}/stats"
        query_params = append_query_param("", "period", _enum_value(request.period))
        response = self.client.request(
            "GET",
            path,
            query=query_params,
            allowed_status_codes=request.allowed_status_codes,
        )
        return GetWebhookSubscriptionStatsResponse.from_response(response.json())

    def get_webhook_owner_stats(
        self, request: GetWebhookOwnerStatsRequest
    ) -> GetWebhookOwnerStatsResponse:
        path = f"/portfolios/{request.portfolio_id}/webhooks/stats"
        query_params = append_query_param("", "period", _enum_value(request.period))
        response = self.client.request(
            "GET",
            path,
            query=query_params,
            allowed_status_codes=request.allowed_status_codes,
        )
        return GetWebhookOwnerStatsResponse.from_response(response.json())

    def replay_webhook_event(
        self, request: ReplayWebhookEventRequest
    ) -> ReplayWebhookEventResponse:
        path = f"/portfolios/{request.portfolio_id}/webhooks/events/{request.event_id}/replay"
        body = to_body_dict(request)
        response = self.client.request(
            "POST", path, body=body, allowed_status_codes=request.allowed_status_codes
        )
        return ReplayWebhookEventResponse.from_response(response.json())

    def get_webhook_event_types(
        self, request: GetWebhookEventTypesRequest
    ) -> GetWebhookEventTypesResponse:
        path = "/webhooks/event-types"
        response = self.client.request(
            "GET", path, allowed_status_codes=request.allowed_status_codes
        )
        return GetWebhookEventTypesResponse.from_response(response.json())
