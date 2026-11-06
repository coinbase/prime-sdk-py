import pytest

from prime_sdk.enums import WebhookStatsPeriod
from prime_sdk.model import WebhookSubscription
from prime_sdk.services.financing import (
    FinancingService,
    GetEntityRewardsRateRequest,
    GetPortfolioRewardsRateRequest,
)
from prime_sdk.services.webhooks import (
    CreateWebhookSubscriptionRequest,
    DeleteWebhookSubscriptionRequest,
    GetWebhookDeliveryAttemptsRequest,
    GetWebhookDeliveryLogsRequest,
    GetWebhookEventTypesRequest,
    GetWebhookOwnerStatsRequest,
    GetWebhookSubscriptionRequest,
    GetWebhookSubscriptionStatsRequest,
    ListWebhookSubscriptionsRequest,
    ReplayWebhookEventRequest,
    RotateWebhookHMACSecretRequest,
    SendWebhookSimulationRequest,
    UpdateWebhookSubscriptionRequest,
    WebhooksService,
)
from prime_sdk.utils import CursorLimitPaginationParams


class _Response:
    def __init__(self, payload):
        self._payload = payload

    def json(self):
        return self._payload


class _RecordingClient:
    def __init__(self, payload=None):
        self.payload = payload or {}
        self.calls = []

    def request(
        self, method, path, body=None, query=None, allowed_status_codes=None, **_
    ):
        self.calls.append((method, path, query, body))
        return _Response(self.payload)


SUBS = "/portfolios/p1/webhooks/subscriptions"


@pytest.mark.parametrize(
    ("method_name", "request_obj", "expected"),
    [
        (
            "list_webhook_subscriptions",
            ListWebhookSubscriptionsRequest(
                portfolio_id="p1",
                include_disabled=True,
                event_type_filter="ORDER_FILLED",
                pagination=CursorLimitPaginationParams(cursor="c1"),
            ),
            (
                "GET",
                SUBS,
                "include_disabled=true&event_type_filter=ORDER_FILLED&cursor=c1",
                None,
            ),
        ),
        (
            "create_webhook_subscription",
            CreateWebhookSubscriptionRequest(
                portfolio_id="p1",
                target_url="https://example.com/hook",
                event_types=["ORDER_FILLED"],
            ),
            (
                "POST",
                SUBS,
                None,
                {
                    "event_types": ["ORDER_FILLED"],
                    "target_url": "https://example.com/hook",
                },
            ),
        ),
        (
            "get_webhook_subscription",
            GetWebhookSubscriptionRequest(portfolio_id="p1", subscription_id="s1"),
            ("GET", f"{SUBS}/s1", None, None),
        ),
        (
            "update_webhook_subscription",
            UpdateWebhookSubscriptionRequest(
                portfolio_id="p1", subscription_id="s1", is_enabled=False
            ),
            ("PATCH", f"{SUBS}/s1", None, {"is_enabled": False}),
        ),
        (
            "delete_webhook_subscription",
            DeleteWebhookSubscriptionRequest(portfolio_id="p1", subscription_id="s1"),
            ("DELETE", f"{SUBS}/s1", None, None),
        ),
        (
            "rotate_webhook_hmac_secret",
            RotateWebhookHMACSecretRequest(
                portfolio_id="p1",
                subscription_id="s1",
                revoke_previous_immediately=True,
            ),
            (
                "POST",
                f"{SUBS}/s1/rotate-hmac-secret",
                None,
                {"revoke_previous_immediately": True},
            ),
        ),
        (
            "send_webhook_simulation",
            SendWebhookSimulationRequest(
                portfolio_id="p1", subscription_id="s1", event_type="ORDER_FILLED"
            ),
            ("POST", f"{SUBS}/s1/simulate", None, {"event_type": "ORDER_FILLED"}),
        ),
        (
            "get_webhook_delivery_logs",
            GetWebhookDeliveryLogsRequest(
                portfolio_id="p1",
                subscription_id="s1",
                status_filter="WEBHOOK_DELIVERY_STATUS_FAILED",
            ),
            (
                "GET",
                f"{SUBS}/s1/deliveries",
                "status_filter=WEBHOOK_DELIVERY_STATUS_FAILED",
                None,
            ),
        ),
        (
            "get_webhook_delivery_attempts",
            GetWebhookDeliveryAttemptsRequest(
                portfolio_id="p1", subscription_id="s1", event_id="e1"
            ),
            ("GET", f"{SUBS}/s1/deliveries/e1/attempts", None, None),
        ),
        (
            "get_webhook_subscription_stats",
            GetWebhookSubscriptionStatsRequest(
                portfolio_id="p1",
                subscription_id="s1",
                period=WebhookStatsPeriod.WEBHOOK_STATS_PERIOD_24H,
            ),
            ("GET", f"{SUBS}/s1/stats", "period=WEBHOOK_STATS_PERIOD_24H", None),
        ),
        (
            "get_webhook_owner_stats",
            GetWebhookOwnerStatsRequest(portfolio_id="p1"),
            ("GET", "/portfolios/p1/webhooks/stats", "", None),
        ),
        (
            "replay_webhook_event",
            ReplayWebhookEventRequest(
                portfolio_id="p1", event_id="e1", subscription_id="s1"
            ),
            (
                "POST",
                "/portfolios/p1/webhooks/events/e1/replay",
                None,
                {"subscription_id": "s1"},
            ),
        ),
        (
            "get_webhook_event_types",
            GetWebhookEventTypesRequest(),
            ("GET", "/webhooks/event-types", None, None),
        ),
    ],
)
def test_webhooks_service_builds_requests(method_name, request_obj, expected):
    client = _RecordingClient()
    getattr(WebhooksService(client), method_name)(request_obj)
    assert client.calls == [expected]


def test_create_webhook_subscription_parses_subscription():
    client = _RecordingClient(
        {
            "subscription": {"subscription_id": "s1", "is_enabled": True},
            "hmac_secret": "secret",
        }
    )
    response = WebhooksService(client).create_webhook_subscription(
        CreateWebhookSubscriptionRequest(portfolio_id="p1")
    )
    assert isinstance(response.subscription, WebhookSubscription)
    assert response.subscription.subscription_id == "s1"


@pytest.mark.parametrize(
    ("method_name", "request_obj", "expected_path"),
    [
        (
            "get_entity_rewards_rate",
            GetEntityRewardsRateRequest(entity_id="e1"),
            "/entities/e1/rewards/rate",
        ),
        (
            "get_portfolio_rewards_rate",
            GetPortfolioRewardsRateRequest(portfolio_id="p1"),
            "/portfolios/p1/rewards/rate",
        ),
    ],
)
def test_rewards_rate_requests(method_name, request_obj, expected_path):
    client = _RecordingClient({"current_rate": "0.04", "available_rates": []})
    response = getattr(FinancingService(client), method_name)(request_obj)
    assert client.calls == [("GET", expected_path, None, None)]
    assert response.current_rate == "0.04"
