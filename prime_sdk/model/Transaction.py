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

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from ..enums import TransactionStatus, TransactionType
from . import (
    AssetChange,
    EstimatedNetworkFees,
    Network,
    OnchainTransactionDetails,
    ProcessRequirements,
    TransactionMetadata,
    TransferLocation,
)


@dataclass(kw_only=True)
class Transaction:
    id: str | None
    wallet_id: str | None
    portfolio_id: str | None
    type: TransactionType | None
    status: TransactionStatus | None
    symbol: str | None
    created_at: str | None
    completed_at: str | None
    amount: str | None
    transfer_from: TransferLocation | None
    transfer_to: TransferLocation | None
    network_fees: str | None
    fees: str | None
    fee_symbol: str | None
    blockchain_ids: List[str] | None
    transaction_id: str | None
    destination_symbol: str | None
    estimated_network_fees: EstimatedNetworkFees | None
    network: str | None
    estimated_asset_changes: List[AssetChange] | None
    metadata: TransactionMetadata | None
    idempotency_key: str | None
    onchain_details: OnchainTransactionDetails | None
    network_info: Network | None
    process_requirements: ProcessRequirements | None
