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

"""Compatibility configuration for generated Prime SDK models."""

from __future__ import annotations

# Public class name -> generated spec short-name.
CLASS_ALIASES: dict[str, str] = {
    "AccountMetadata": "ActivityMetadataAccount",
    "ActivityResponse": "GetActivityResponse",
    "Add": "DisplayUser",
    "Address": "AddressBookEntry",
    "AssetNetwork": "NetworkDetails",
    "BalanceWithHolds": "AggregatedFiatBalance",
    "Blockchain": "BlockchainAddress",
    "Collection": "NFTCollection",
    "ConsensusMetadata": "ActivityMetadataConsensus",
    "CrossMarginCall": "XMMarginCall",
    "CrossMarginLoan": "XMLoan",
    "CrossMarginPrimeFuturesEquityBreakdown": "CrossMarginPrimeDerivativesEquityBreakdown",
    "CryptoInstructions": "WalletCryptoDepositInstructions",
    "Destination": "DestinationAlloc",
    "Details": "PaymentMethodDetails",
    "EditHistory": "OrderEdit",
    "FcmMarginCall": "FCMMarginCall",
    "FcmRiskLimits": "GetFcmRiskLimitsResponse",
    "Fee": "TieredPricingFee",
    "FiatInstructions": "WalletFiatDepositInstructions",
    "FuturesPosition": "FcmPosition",
    "Instructions": "GetWalletDepositInstructionsResponse",
    "Item": "NFTItem",
    "Locate": "ExistingLocate",
    "MarginSummaryRecord": "MarginSummaryHistorical",
    "OnchainAddress": "AddressEntry",
    "OnchainBalance": "Web3Balance",
    "OnchainDetails": "OnchainTransactionDetails",
    "OrderEditHistory": "LimitOrderEdit",
    "PmAssetInfo": "PMAssetInfo",
    "PmLoan": "LoanInfo",
    "PortfolioStressTriggered": "MarginAddOn",
    "PostTradeCredit": "PostTradeCreditInformation",
    "Reference": "PositionReference",
    "RequestedAmount": "AmountDue",
    "RfqProductDetails": "RFQProductDetails",
    "RiskNettingInfo": "XMRiskNettingInfo",
    "ScenarioAddon": "MarginAddOn",
    "Sweep": "FcmFuturesSweep",
    "TfLoan": "LoanInfo",
    "TransactionsMetadata": "ActivityMetadataTransactions",
    "User": "EntityUser",
    "XmPosition": "XMPosition",
}

# Generated class short-name -> spec field name -> public field name.
FIELD_RENAMES: dict[str, dict[str, str]] = {
    "CrossMarginPrimeMarginSummary": {
        "derivatives_equity_breakdown": "futures_equity_breakdown"
    },
}

# Extra fields to add to generated classes for backward compatibility.
EXTRA_FIELDS: dict[str, dict[str, str]] = {
    "FcmPosition": {
        "symbol": "str",
        "long": "str",
        "short": "str",
        "position_reference": "str",
    },
    "PaymentMethodDetails": {
        "bank_name": "str",
        "bank_name_2": "str",
    },
}

# Enum schema keys that collide on short-name.
ENUM_NAME_OVERRIDES: dict[str, str] = {
    "coinbase.custody.api.ActivityType": "CustodyActivityType",
    "coinbase.public_rest_api.ActivityType": "PrimeActivityType",
}

# Fields that should import types from prime_sdk.enums instead of str.
ENUM_FIELD_IMPORTS: dict[str, dict[str, str]] = {
    "AddressGroup": {"network_type": "NetworkType"},
}

# Schema key -> generated class short-name (when short_name() would collide or misname).
SCHEMA_CLASS_OVERRIDES: dict[str, str] = {
    "coinbase.public_rest_api.Locate": "LocateAvailability",
}

# operationId -> generated request class name (defaults strip PrimeRESTAPI_ prefix).
REQUEST_CLASS_NAME_OVERRIDES: dict[str, str] = {
    "PrimeRESTAPI_CreateQuoteRequest": "CreateQuoteRequest",
    "PrimeRESTAPI_ListTransactionValidators": "ListTransactionValidatorsRequest",
    "PrimeRESTAPI_OrderPreview": "OrderPreviewRequest",
}

# Service Response class -> generated model class to inherit from (when names differ).
SERVICE_RESPONSE_BASES: dict[str, str] = {
    "CancelEntityFuturesSweepResponse": "CancelFuturesSweepResponse",
    "ClaimWalletStakingRewardsResponse": "StakingClaimRewardsResponse",
    "CreateAddressBookEntryResponse": "CreatePortfolioAddressBookEntryResponse",
    "CreateNewLocateResponse": "CreateNewLocatesResponse",
    "CreateOnchainAddressBookEntryResponse": "ActivityCreationResponse",
    "CreateOrderPreviewResponse": "PostOrderPreviewResponse",
    "CreatePortfolioAllocationsResponse": "CreateAllocationResponse",
    "CreatePortfolioNetAllocationsResponse": "CreateNetAllocationResponse",
    "CreatePortfolioStakeResponse": "PortfolioStakingInitiateResponse",
    "CreatePortfolioUnstakeResponse": "PortfolioStakingUnstakeResponse",
    "CreateQuoteResponse": "QuoteResponse",
    "CreateStakeResponse": "StakingInitiateResponse",
    "CreateTransferResponse": "CreateWalletTransferResponse",
    "CreateUnstakeResponse": "StakingUnstakeResponse",
    "CreateWalletDepositAddressResponse": "BlockchainAddress",
    "CreateWithdrawalResponse": "CreateWalletWithdrawalResponse",
    "DeleteOnchainAddressGroupResponse": "ActivityCreationResponse",
    "GetActivityResponse": "GetPortfolioActivityResponse",
    "GetAddressBookResponse": "GetPortfolioAddressBookResponse",
    "GetAllocationByIdResponse": "GetAllocationResponse",
    "GetCounterpartyIdResponse": "GetPortfolioCounterpartyIDResponse",
    "GetEntityActivityResponse": "GetActivityResponse",
    "GetEntityFcmBalanceResponse": "GetFcmBalanceResponse",
    "GetEntityLocateAvailabilitiesResponse": "GetLocateAvailabilitiesResponse",
    "GetEntityPaymentMethodResponse": "GetEntityPaymentMethodDetailsResponse",
    "GetEntityPositionsResponse": "ListEntityPositionsResponse",
    "GetNetAllocationsByNettingIdResponse": "GetAllocationsByClientNettingIdResponse",
    "GetPortfolioCreditInformationResponse": "GetPostTradeCreditResponse",
    "GetPortfolioWithdrawalPowerResponse": "GetWithdrawalPowerResponse",
    "GetProductCandlesResponse": "GetCandlesResponse",
    "GetTradeFinanceTieredPricingFeesResponse": "GetTFTieredPricingFeesResponse",
    "ListActivitiesResponse": "GetPortfolioActivitiesResponse",
    "ListAssetsResponse": "GetEntityAssetsResponse",
    "ListEntityActivitiesResponse": "GetEntityActivitiesResponse",
    "ListEntityFuturesSweepsResponse": "GetFuturesSweepsResponse",
    "ListEntityPaymentMethodsResponse": "GetEntityPaymentMethodsResponse",
    "ListEntityUsersResponse": "GetEntityUsersResponse",
    "ListExistingLocatesResponse": "GetExistingLocatesResponse",
    "ListInterestAccrualsForPortfolioResponse": "GetPortfolioInterestAccrualsResponse",
    "ListInterestAccrualsResponse": "GetInterestAccrualsResponse",
    "ListInvoicesResponse": "GetInvoicesResponse",
    "ListMarginCallSummariesResponse": "GetMarginSummariesResponse",
    "ListMarginConversionsResponse": "GetMarginConversionsResponse",
    "ListOpenOrdersResponse": "GetOpenOrdersResponse",
    "ListOrderFillsResponse": "GetOrderFillsResponse",
    "ListOrdersResponse": "GetOrdersResponse",
    "ListPortfolioAllocationsResponse": "GetPortfolioAllocationsResponse",
    "ListPortfolioBalancesResponse": "GetPortfolioBalancesResponse",
    "ListPortfolioFillsResponse": "GetPortfolioFillsResponse",
    "ListPortfolioTransactionsResponse": "GetPortfolioTransactionsResponse",
    "ListPortfolioUsersResponse": "GetPortfolioUsersResponse",
    "ListPortfoliosResponse": "GetPortfoliosResponse",
    "ListProductsResponse": "GetPortfolioProductsResponse",
    "ListTradeFinanceObligationsResponse": "ListTFObligationsResponse",
    "ListWalletTransactionsResponse": "GetWalletTransactionsResponse",
    "ListWalletsResponse": "GetWalletsResponse",
    "QueryTransactionValidatorsResponse": "ListTransactionValidatorsResponse",
    "RotateApiKeyResponse": "RotateAPIKeyResponse",
    "ScheduleEntityFuturesSweepResponse": "ScheduleFuturesSweepResponse",
    "SetFcmSettingsResponse": "GetFcmSettingsResponse",
    "SetFundingSettingsResponse": "UpdateFundingSettingsResponse",
    "UpdateOnchainAddressBookResponse": "ActivityCreationResponse",
}

# Service Response classes that intentionally diverge from the generated spec model.
MANUAL_SERVICE_RESPONSES: frozenset[str] = frozenset()

# Service Request class -> generated request class to inherit from (when names differ).
SERVICE_REQUEST_BASES: dict[str, str] = {
    "CancelEntityFuturesSweepRequest": "CancelFuturesSweepRequest",
    "ClaimWalletStakingRewardsRequest": "StakingClaimRewardsRequest",
    "CreateAddressBookEntryRequest": "CreatePortfolioAddressBookEntryRequest",
    "CreateNewLocateRequest": "CreateNewLocatesRequest",
    "CreateOnchainAddressBookEntryRequest": "CreateOnchainAddressGroupRequest",
    "CreateOrderPreviewRequest": "OrderPreviewRequest",
    "CreatePortfolioAllocationsRequest": "CreateAllocationRequest",
    "CreatePortfolioNetAllocationsRequest": "CreateNetAllocationRequest",
    "CreatePortfolioStakeRequest": "PortfolioStakingInitiateRequest",
    "CreatePortfolioUnstakeRequest": "PortfolioStakingUnstakeRequest",
    "CreateStakeRequest": "StakingInitiateRequest",
    "CreateTransferRequest": "CreateWalletTransferRequest",
    "CreateUnstakeRequest": "StakingUnstakeRequest",
    "CreateWithdrawalRequest": "CreateWalletWithdrawalRequest",
    "GetActivityRequest": "GetPortfolioActivityRequest",
    "GetAddressBookRequest": "GetPortfolioAddressBookRequest",
    "GetAllocationByIdRequest": "GetAllocationRequest",
    "GetCounterpartyIdRequest": "GetPortfolioCounterpartyIDRequest",
    "GetEntityActivityRequest": "GetActivityRequest",
    "GetEntityFcmBalanceRequest": "GetFcmBalanceRequest",
    "GetEntityLocateAvailabilitiesRequest": "GetLocateAvailabilitiesRequest",
    "GetEntityPaymentMethodRequest": "GetEntityPaymentMethodDetailsRequest",
    "GetEntityPositionsRequest": "ListEntityPositionsRequest",
    "GetNetAllocationsByNettingIdRequest": "GetAllocationsByClientNettingIdRequest",
    "GetPortfolioCreditInformationRequest": "GetPostTradeCreditRequest",
    "GetPortfolioWithdrawalPowerRequest": "GetWithdrawalPowerRequest",
    "GetProductCandlesRequest": "GetCandlesRequest",
    "GetTradeFinanceTieredPricingFeesRequest": "GetTFTieredPricingFeesRequest",
    "ListActivitiesRequest": "GetPortfolioActivitiesRequest",
    "ListAssetsRequest": "GetEntityAssetsRequest",
    "ListEntityActivitiesRequest": "GetEntityActivitiesRequest",
    "ListEntityFuturesSweepsRequest": "GetFuturesSweepsRequest",
    "ListEntityPaymentMethodsRequest": "GetEntityPaymentMethodsRequest",
    "ListEntityUsersRequest": "GetEntityUsersRequest",
    "ListExistingLocatesRequest": "GetExistingLocatesRequest",
    "ListInterestAccrualsForPortfolioRequest": "GetPortfolioInterestAccrualsRequest",
    "ListInterestAccrualsRequest": "GetInterestAccrualsRequest",
    "ListInvoicesRequest": "GetInvoicesRequest",
    "ListMarginCallSummariesRequest": "GetMarginSummariesRequest",
    "ListMarginConversionsRequest": "GetMarginConversionsRequest",
    "ListOpenOrdersRequest": "GetOpenOrdersRequest",
    "ListOrderFillsRequest": "GetOrderFillsRequest",
    "ListOrdersRequest": "GetOrdersRequest",
    "ListPortfolioAllocationsRequest": "GetPortfolioAllocationsRequest",
    "ListPortfolioBalancesRequest": "GetPortfolioBalancesRequest",
    "ListPortfolioFillsRequest": "GetPortfolioFillsRequest",
    "ListPortfolioTransactionsRequest": "GetPortfolioTransactionsRequest",
    "ListPortfolioUsersRequest": "GetPortfolioUsersRequest",
    "ListPortfoliosRequest": "GetPortfoliosRequest",
    "ListProductsRequest": "GetPortfolioProductsRequest",
    "ListTradeFinanceObligationsRequest": "ListTFObligationsRequest",
    "ListWalletTransactionsRequest": "GetWalletTransactionsRequest",
    "ListWalletsRequest": "GetWalletsRequest",
    "QueryTransactionValidatorsRequest": "ListTransactionValidatorsRequest",
    "RotateApiKeyRequest": "RotateAPIKeyRequest",
    "ScheduleEntityFuturesSweepRequest": "ScheduleFuturesSweepRequest",
    "SetFundingSettingsRequest": "UpdateFundingSettingsRequest",
    "UpdateOnchainAddressBookRequest": "UpdateOnchainAddressGroupRequest",
}
