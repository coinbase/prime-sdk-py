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

from enum import Enum

class WalletType(Enum):
    VAULT   = "VAULT"
    TRADING = "TRADING"
    ONCHAIN = "ONCHAIN"
    OTHER   = "WALLET_TYPE_OTHER"


class WalletDepositType(Enum):
    WIRE   = "WIRE"
    SWIFT  = "SWIFT"
    CRYPTO = "CRYPTO"
    SEPA   = "SEPA"


class BalanceType(Enum):
    TRADING = "TRADING_BALANCES"
    VAULT   = "VAULT_BALANCES"
    TOTAL   = "TOTAL_BALANCES"
    UNKNOWN_BALANCE_TYPE = "UNKNOWN_BALANCE_TYPE"
    PRIME_CUSTODY_BALANCES = "PRIME_CUSTODY_BALANCES"


class NetworkType(Enum):
    NETWORK_TYPE_UNSPECIFIED = "NETWORK_TYPE_UNSPECIFIED"
    NETWORK_TYPE_EVM = "NETWORK_TYPE_EVM"
    NETWORK_TYPE_SOLANA = "NETWORK_TYPE_SOLANA"


class OrderSide(Enum):
    BUY  = "BUY"
    SELL = "SELL"


class OrderType(Enum):
    MARKET = "MARKET"
    LIMIT  = "LIMIT"
    TWAP   = "TWAP"
    BLOCK  = "BLOCK"
    VWAP   = "VWAP"
    STOP_LIMIT = "STOP_LIMIT"
    RFQ = "RFQ"


class TimeInForce(Enum):
    GOOD_UNTIL_DATE_TIME      = "GOOD_UNTIL_DATE_TIME"
    GOOD_UNTIL_CANCELLED       = "GOOD_UNTIL_CANCELLED"
    IMMEDIATE_OR_CANCEL        = "IMMEDIATE_OR_CANCEL"
    FILL_OR_KILL               = "FILL_OR_KILL"
    UNKNOWN_TIME_IN_FORCE      = "UNKNOWN_TIME_IN_FORCE"


class SizeType(Enum):
    ALLOCATION_SIZE_TYPE_UNKNOWN = "ALLOCATION_SIZE_TYPE_UNKNOWN"
    BASE = "BASE"
    QUOTE = "QUOTE"
    PERCENT = "PERCENT"


class ActivityLevel(Enum):
    ACTIVITY_LEVEL_ALL = "ACTIVITY_LEVEL_ALL"
    ACTIVITY_LEVEL_ENTITY = "ACTIVITY_LEVEL_ENTITY"
    ACTIVITY_LEVEL_PORTFOLIO = "ACTIVITY_LEVEL_PORTFOLIO"


class AggregationType(Enum):
    UNKNOWN_BALANCE_TYPE = "UNKNOWN_BALANCE_TYPE"
    TRADING_BALANCES = "TRADING_BALANCES"
    VAULT_BALANCES = "VAULT_BALANCES"
    TOTAL_BALANCES = "TOTAL_BALANCES"
    PRIME_CUSTODY_BALANCES = "PRIME_CUSTODY_BALANCES"
    UNIFIED_TOTAL_BALANCES = "UNIFIED_TOTAL_BALANCES"


class UnstakeEstimateType(Enum):
    UNSPECIFIED = "UNSPECIFIED"
    LIVE = "LIVE"
    INTERIM = "INTERIM"


class UnstakeType(Enum):
    UNSTAKE_TYPE_UNSPECIFIED = "UNSTAKE_TYPE_UNSPECIFIED"
    UNSTAKE_TYPE_PARTIAL = "UNSTAKE_TYPE_PARTIAL"
    UNSTAKE_TYPE_FULL = "UNSTAKE_TYPE_FULL"
