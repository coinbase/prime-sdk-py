# Changelog

## [1.9.0] - 2026-JUL-24

### Added

#### New API Endpoints

**Api Keys Service**
- **`rotate_api_key()`**: Rotate the Prime API key (`POST /v1/api-keys/rotate`)

**Financing Service**
- **`get_xm_liquidation()`**: Get cross margin liquidation details (`GET /v1/entities/{entity_id}/cross_margin/liquidation`)
- **`list_xm_liquidations()`**: List cross margin liquidation history (`GET /v1/entities/{entity_id}/cross_margin/liquidations`)

#### New & Updated Models
- **`XMSummary`**, **`XMLiquidationDetail`**, **`XMLiquidationSummary`**, **`XMLiquidatedAsset`**: Cross margin liquidation types
- **`CustomStablecoinAsset`**, **`CustomStablecoinRewardDetails`**, **`ValidatorAllocation`**: New supporting models
- **`RewardMetadata`**: Added `custom_stablecoin_reward_details`
- **`TravelRuleParty`**: Added `vasp_address`
- **`StakingInputs`**: Added `end_date` and `validator_allocations`
- **`CreateStakeRequest`** / **`CreateUnstakeRequest`**: Added `metadata` (`WalletStakingMetadata`)
- **`CreatePortfolioUnstakeRequest`**: Added `validator_provider`

#### New Enums
- **`RewardSubtype`**, **`ValidatorProvider`**, **`TransactionType`** (includes new `MERGE_STAKE` value and `RewardSubtype.CUSTOM_STABLECOIN_REWARD`)

### Changed

- **`Credentials`**: Only `accessKey`, `passphrase`, and `signingKey` are required in `PRIME_CREDENTIALS`. `portfolioId`, `entityId`, and `svcAccountId` are optional (from JSON and/or `PRIME_PORTFOLIO_ID` / `PRIME_ENTITY_ID`).

## [1.8.0] - 2026-JUN-01

### Changed

- Repository canonical home is [coinbase/prime-sdk-py](https://github.com/coinbase/prime-sdk-py). No intentional API or code changes compared to 1.7.1.

## [1.7.1] - 2026-MAY-11

### Fixed

- Corrected `set_funding_settings` endpoint path from `/funding/settings` to `/funding_settings` to match the updated API spec.

## [1.7.0] - 2026-MAY-11

### Breaking Changes

- `RiskNettingInfo.nodal_margin_requirement` renamed to `dco_margin_requirement` to match the updated API spec (`XMRiskNettingInfo.dco_margin_requirement`). Code accessing the old field name must be updated.

### Added

- Financing Service has four new beta endpoints
  - `get_cross_margin_risk_parameters` — `GET /v1/entities/{entity_id}/cross_margin/risk_parameters`
  - `get_cross_margin_prime_overview` — `GET /v2/entities/{entity_id}/cross_margin/prime`
  - `set_funding_settings` — `POST /v1/entities/{entity_id}/funding/settings`
  - `get_market_data` — `GET /v1/entities/{entity_id}/market_data`
- New models: `ActiveLiquidationSummary`, `ValidatorUnstakePreview`, `CrossMarginRiskParameters`, `TierPairRateEntry`, `CrossMarginPrimeMarginSummary`, `CrossMarginPrimeSpotEquityBreakdown`, `CrossMarginPrimeFuturesEquityBreakdown`, `CrossMarginPrimeRiskNettingInfo`, `CrossMarginPrimeXMPosition`, `PrimeXMMarginRequirementBreakdown`, `PrimeXMOffsetCreditBreakdown`, `PrimeXMMarginCallThresholds`, `PrimeXMMarginThreshold`, `MarketData`
- New enums: `XMLiquidationStatus`, `PrimeXMControlStatus`, `PrimeXMMarginLevel`, `PrimeXMMarginRequirementType`, `PrimeXMHealthStatus`, `PrimeXMMarginThresholdType`
- `WalletType.QC` enum value added to match spec
- `AssetNetwork` updated with `network_scoped_symbol`, `min_withdrawal_amount`, `max_withdrawal_amount`, and `min_deposit_amount` fields
- `CrossMarginOverview` updated with `active_liquidation` field
- `CrossMarginSummary` updated with `consumed_margin_limit` field
- `PreviewUnstakeResponse` updated with `wallet_id`, `wallet_address`, `current_timestamp`, and `validators` fields
- `CreateQuoteRequest` updated with optional `quote_duration_ms` field (RFQ timeout in ms, mirrors FIX tag 8090)
- `CreateQuoteResponse` updated with `quote_duration_ms` echo field
- `Client.request` now accepts an optional `version` parameter (default `"v1"`) to support versioned API paths

## [1.6.0] - 2026-MAR-30

### Added

- Advanced Transfers Service has four new endpoints
  - listAdvancedTransfers
  - createAdvancedTransfer
  - cancelAdvancedTransfer
  - listAdvancedTransferTransactions
- Transactions Service has a new endpoint
  - getTransactionTravelRuleData
- Futures Service has a new endpoint
  - getFcmEquity
- New models: `AdvancedTransfer`, `FundMovement`, `BlindMatchMetadata`, `RewardMetadata`, `CommissionDetailTotal`, `ProcessRequirements`
- Updated `TransferLocation` with `address` and `account_identifier` fields
- Updated `TransactionMetadata` with `reward_metadata` field
- Updated `Order` with `product_type` and `commission_detail_total` fields
- Updated `Transaction.process_requirements` from `str` to `ProcessRequirements`
