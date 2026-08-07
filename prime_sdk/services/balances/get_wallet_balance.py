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

from dataclasses import dataclass

from ...base_request import BaseRequest
from ...base_response import BaseResponse
from ...model import GetWalletBalanceRequest as _GetWalletBalanceRequest
from ...model import GetWalletBalanceResponse as _GetWalletBalanceResponse


@dataclass(kw_only=True)
class GetWalletBalanceRequest(BaseRequest, _GetWalletBalanceRequest):
    """
    Get Wallet Balance

    Attributes:
        portfolio_id: Portfolio ID
        wallet_id: Wallet ID
    """


@dataclass
class GetWalletBalanceResponse(BaseResponse, _GetWalletBalanceResponse):
    """
    Attributes:
        balance.symbol: The display symbol for the asset
        balance.amount: The total amount in whole units with full precision. Includes the
            `holds` amount.
        balance.holds: Amount that is currently held in obligation to an open order's
            position or a pending withdrawal
        balance.bonded_amount: Amount that is currently locked due to bonding/staking,
            potentially subject to an unbonding period, in whole units
        balance.reserved_amount: Amount that must remain in the wallet due to the protocol,
            in whole units
        balance.unbonding_amount: Amount that is in the process of unbonding, in whole units
        balance.unvested_amount: Unrealized amount subject to a vesting schedule, in whole
            units
        balance.pending_rewards_amount: Pending bonding/staking rewards that have not yet
            been realized, in whole units
        balance.past_rewards_amount: Previously realized bonding/staking rewards, in whole
            units
        balance.bondable_amount: Amount available for bonding/staking, in whole units
        balance.withdrawable_amount: Amount available to withdraw, in whole units
        balance.fiat_amount: The total amount in fiat unit
        balance.unbondable_amount: Amount available for unbonding/unstaking, in whole units
        balance.claimable_rewards_amount: ETH staking rewards currently available to claim,
            in whole units. This field is returned only in GetWalletBalance responses for
            ETH wallets. It is omitted or empty for portfolio-level responses and for non-
            ETH assets; use pending_rewards_amount where applicable.
    """
