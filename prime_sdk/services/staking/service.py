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

from prime_sdk.client import Client
from prime_sdk.utils import to_body_dict
from .create_stake import (
    CreateStakeRequest,
    CreateStakeResponse
)
from .create_unstake import (
    CreateUnstakeRequest,
    CreateUnstakeResponse
)
from .create_portfolio_stake import (
    CreatePortfolioStakeRequest,
    CreatePortfolioStakeResponse
)
from .create_portfolio_unstake import (
    CreatePortfolioUnstakeRequest,
    CreatePortfolioUnstakeResponse
)
from .claim_wallet_staking_rewards import (
    ClaimWalletStakingRewardsRequest,
    ClaimWalletStakingRewardsResponse
)
from .query_transaction_validators import (
    QueryTransactionValidatorsRequest,
    QueryTransactionValidatorsResponse
)


class StakingService:
    def __init__(self, client: Client):
        self.client = client

    def create_stake(self, request: CreateStakeRequest) -> CreateStakeResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/staking/initiate"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateStakeResponse(**response.json())

    def create_unstake(self, request: CreateUnstakeRequest) -> CreateUnstakeResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/staking/unstake"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreateUnstakeResponse(**response.json())

    def create_portfolio_stake(self, request: CreatePortfolioStakeRequest) -> CreatePortfolioStakeResponse:
        path = f"/portfolios/{request.portfolio_id}/staking/initiate"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreatePortfolioStakeResponse(**response.json())

    def create_portfolio_unstake(self, request: CreatePortfolioUnstakeRequest) -> CreatePortfolioUnstakeResponse:
        path = f"/portfolios/{request.portfolio_id}/staking/unstake"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return CreatePortfolioUnstakeResponse(**response.json())

    def claim_wallet_staking_rewards(self, request: ClaimWalletStakingRewardsRequest) -> ClaimWalletStakingRewardsResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/staking/claim_rewards"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return ClaimWalletStakingRewardsResponse(**response.json())

    def query_transaction_validators(self, request: QueryTransactionValidatorsRequest) -> QueryTransactionValidatorsResponse:
        path = f"/portfolios/{request.portfolio_id}/staking/transaction-validators/query"
        body = to_body_dict(request)
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return QueryTransactionValidatorsResponse(**response.json())
