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

from dataclasses import asdict
from ...client import Client
from ...utils import append_query_param, to_body_dict
from .create_new_locate import (
    CreateNewLocateRequest,
    CreateNewLocateResponse
)
from .list_existing_locates import (
    ListExistingLocatesRequest,
    ListExistingLocatesResponse
)
from .get_entity_locate_availabilities import (
    GetEntityLocateAvailabilitiesRequest,
    GetEntityLocateAvailabilitiesResponse
)
from .get_portfolio_buying_power import (
    GetBuyingPowerRequest,
    GetBuyingPowerResponse
)
from .get_portfolio_withdrawal_power import (
    GetPortfolioWithdrawalPowerRequest,
    GetPortfolioWithdrawalPowerResponse
)
from .get_margin_information import (
    GetMarginInformationRequest,
    GetMarginInformationResponse
)
from .get_cross_margin_overview import (
    GetCrossMarginOverviewRequest,
    GetCrossMarginOverviewResponse
)
from .list_margin_call_summaries import (
    ListMarginCallSummariesRequest,
    ListMarginCallSummariesResponse
)
from .list_margin_conversions import (
    ListMarginConversionsRequest,
    ListMarginConversionsResponse
)
from .get_portfolio_credit_information import (
    GetPortfolioCreditInformationRequest,
    GetPortfolioCreditInformationResponse
)
from .get_trade_finance_tiered_pricing_fees import (
    GetTradeFinanceTieredPricingFeesRequest,
    GetTradeFinanceTieredPricingFeesResponse
)
from .list_interest_accruals import (
    ListInterestAccrualsRequest,
    ListInterestAccrualsResponse
)
from .list_interest_accruals_for_portfolio import (
    ListInterestAccrualsForPortfolioRequest,
    ListInterestAccrualsForPortfolioResponse
)


class FinancingService:
    def __init__(self, client: Client):
        self.client = client

    # Locates
    def create_new_locate(self, request: CreateNewLocateRequest) -> CreateNewLocateResponse:
        path = f"/portfolios/{request.portfolio_id}/locates"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateNewLocateResponse(**response.json())

    def list_existing_locates(self, request: ListExistingLocatesRequest) -> ListExistingLocatesResponse:
        path = f"/portfolios/{request.portfolio_id}/locates"
        query_params = append_query_param("", "locate_ids", request.locate_ids)
        query_params = append_query_param(query_params, "locate_date", request.locate_date)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListExistingLocatesResponse(**response.json())

    def get_entity_locate_availabilities(self, request: GetEntityLocateAvailabilitiesRequest) -> GetEntityLocateAvailabilitiesResponse:
        path = f"/entities/{request.entity_id}/locates_availability"
        query_params = append_query_param("", "locate_date", request.locate_date)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return GetEntityLocateAvailabilitiesResponse(**response.json())

    # Power
    def get_portfolio_buying_power(self, request: GetBuyingPowerRequest) -> GetBuyingPowerResponse:
        path = f"/portfolios/{request.portfolio_id}/buying_power"
        query_params = append_query_param("", "base_currency", request.base_currency)
        query_params = append_query_param(query_params, "quote_currency", request.quote_currency)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return GetBuyingPowerResponse(**response.json())

    def get_portfolio_withdrawal_power(self, request: GetPortfolioWithdrawalPowerRequest) -> GetPortfolioWithdrawalPowerResponse:
        path = f"/portfolios/{request.portfolio_id}/withdrawal_power"
        query_params = append_query_param("", "symbol", request.symbol)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return GetPortfolioWithdrawalPowerResponse(**response.json())

    # Margin
    def get_margin_information(self, request: GetMarginInformationRequest) -> GetMarginInformationResponse:
        path = f"/entities/{request.entity_id}/margin"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetMarginInformationResponse(**response.json())

    def get_cross_margin_overview(self, request: GetCrossMarginOverviewRequest) -> GetCrossMarginOverviewResponse:
        path = f"/entities/{request.entity_id}/cross_margin"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetCrossMarginOverviewResponse(**response.json())

    def list_margin_call_summaries(self, request: ListMarginCallSummariesRequest) -> ListMarginCallSummariesResponse:
        path = f"/entities/{request.entity_id}/margin_summaries"
        query_params = append_query_param("", "start_date", request.start_date)
        query_params = append_query_param(query_params, "end_date", request.end_date)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListMarginCallSummariesResponse(**response.json())

    def list_margin_conversions(self, request: ListMarginConversionsRequest) -> ListMarginConversionsResponse:
        path = f"/portfolios/{request.portfolio_id}/margin_conversions"
        query_params = append_query_param("", "start_date", request.start_date)
        query_params = append_query_param(query_params, "end_date", request.end_date)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListMarginConversionsResponse(**response.json())

    # Credit
    def get_portfolio_credit_information(self, request: GetPortfolioCreditInformationRequest) -> GetPortfolioCreditInformationResponse:
        path = f"/portfolios/{request.portfolio_id}/credit"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetPortfolioCreditInformationResponse(**response.json())

    # Fees
    def get_trade_finance_tiered_pricing_fees(self, request: GetTradeFinanceTieredPricingFeesRequest) -> GetTradeFinanceTieredPricingFeesResponse:
        path = f"/portfolios/{request.portfolio_id}/tf_tiered_fees"
        query_params = append_query_param("", "effective_at", request.effective_at)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return GetTradeFinanceTieredPricingFeesResponse(**response.json())

    # Interest Accruals
    def list_interest_accruals(self, request: ListInterestAccrualsRequest) -> ListInterestAccrualsResponse:
        path = f"/entities/{request.entity_id}/accruals"
        query_params = append_query_param("", "portfolio_id", request.portfolio_id)
        query_params = append_query_param(query_params, "start_date", request.start_date)
        query_params = append_query_param(query_params, "end_date", request.end_date)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListInterestAccrualsResponse(**response.json())

    def list_interest_accruals_for_portfolio(self, request: ListInterestAccrualsForPortfolioRequest) -> ListInterestAccrualsForPortfolioResponse:
        path = f"/portfolios/{request.portfolio_id}/accruals"
        query_params = append_query_param("", "start_date", request.start_date)
        query_params = append_query_param(query_params, "end_date", request.end_date)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListInterestAccrualsForPortfolioResponse(**response.json())