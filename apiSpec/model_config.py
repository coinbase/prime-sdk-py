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
    "LocateAvailability": "LocateRequest",
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

# Rename generated class for the spec's three-field Locate schema.
LOCATE_REQUEST_CLASS = "LocateRequest"
