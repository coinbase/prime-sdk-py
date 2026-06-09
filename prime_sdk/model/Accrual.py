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

from ..enums import Benchmark, LoanType, RateType


@dataclass(kw_only=True)
class Accrual:
    accrual_id: str | None
    date: str | None
    portfolio_id: str | None
    symbol: str | None
    loan_type: LoanType | None = LoanType.LOAN_TYPE_UNSET
    interest_rate: str | None
    nominal_accrual: str | None
    notional_accrual: str | None
    conversion_rate: str | None
    loan_amount: str | None
    benchmark: Benchmark | None = Benchmark.BENCHMARK_UNSET
    benchmark_rate: str | None
    spread: str | None
    rate_type: RateType | None = RateType.RATE_TYPE_UNSET
    loan_amount_notional: str | None
    nominal_open_borrow_sod: str | None
    notional_open_borrow_sod: str | None
