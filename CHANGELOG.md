# Changelog

## [1.10.0] - 2026-AUG-07

### Breaking Changes

These responses previously used incorrect field names or shapes in the Python SDK. They now match the OpenAPI spec (and the live API). Update any code that reads the old attributes:

- **`CreatePortfolioAllocationsResponse`** / **`CreatePortfolioNetAllocationsResponse`**: success/allocation fields are nested under `body` (e.g. `response.body.allocation_id` instead of `response.allocation_id`).
- **`GetEntityLocateAvailabilitiesResponse`**: `locate_availability` renamed to `locates`.
- **`GetOrderEditHistoryResponse`**: `edits` replaced by `order_id`, `edit_history`, and deprecated `order_edit_history`.
- **`GetWalletDepositInstructionsResponse`**: removed top-level `instructions`; use `crypto_instructions` and `fiat_instructions` (`CryptoInstructions` / `FiatInstructions` models).
- **`ListPortfolioBalancesRequest`** and **`ListEntityPaymentMethodsRequest`**: removed the `pagination` field. The OpenAPI spec does not document cursor pagination for these endpoints.
- **Cursor+limit paginated requests** (`ListEntityBalancesRequest`, `ListWeb3WalletBalancesRequest`, `ListInvoicesRequest`, `ListAggregateEntityPositionsRequest`, `ListEntityPositionsRequest`, `ListWalletAddressesRequest`, and `GetEntityPositionsRequest`): `pagination` is now typed as `CursorLimitPaginationParams` (cursor and limit only) instead of `PaginationParams`, matching the spec.

### Changed

- **Models**: `prime_sdk/model.py` is now a compatibility shim over generated dataclasses in `prime_sdk/generated/models.py`. Run `make update-spec` to refresh models from the OpenAPI specification. Existing imports and field names are preserved via `apiSpec/model_config.py` and `prime_sdk/model_manual.py`.
- **Service models**: Service `*Request` and `*Response` dataclasses now inherit field definitions and docstrings from generated models (via local `as _Internal...` aliases), matching the TypeScript SDK pattern.
- **Request docstrings**: All service `*Request` classes now inherit OpenAPI-derived docstrings from generated stub models. JSON-body requests document path/query parameters alongside body fields.
- **Generated path/query parameters**: Request models in `prime_sdk/generated/models.py` now include path and query parameter fields (not just docstrings), including body-backed requests such as `CreateOrderRequest` and `CreatePortfolioAddressBookEntryRequest` (tagged with `metadata={"location": "path"|"query"}`). Service `*Request` subclasses no longer hand-redeclare fields such as `portfolio_id` or `wallet_id` when those are already on the generated base class, and keep only SDK-specific extras such as `allowed_status_codes` and `pagination`.
- Path parameters on body-backed requests now use the same soft-required convention as other generated fields (`field(default=None, ...)` instead of a required `field_name: str` on the service subclass).
- **Examples**: Wallet example scripts fall back to `PRIME_WALLET_ID` and `PRIME_ONCHAIN_WALLET_ID` when `--wallet-id` is omitted; see `.env.example` and README.
- Service `*Request` classes now inherit SDK control fields (`allowed_status_codes`, `pagination`) from base mixins instead of declaring them per file. Pagination tier (full vs cursor+limit) is determined from the OpenAPI spec at generation time.
- **`GetMarketDataRequest`** and **`ListXMLiquidationsRequest`**: replaced raw `cursor`/`limit`/`sort_direction` fields with the standard `pagination: PaginationParams` field.

### Fixed

- **`BaseResponse`**: Nested dataclass hydration now unwraps optional type annotations.
- **`to_body_dict`**: SDK control fields tagged with `metadata={"control": True}` (such as `allowed_status_codes` and `pagination`) and path/query fields tagged with `metadata={"location": "path"|"query"}` are no longer serialized into JSON request bodies.

### Added

- **`make update-spec`**, **`make gen-models`**, **`make check-models`**, and **`make promote-titles`** Makefile targets for spec and model regeneration.
- **Generated request-body models**: Inline OpenAPI path request bodies are emitted into `prime_sdk/generated/models.py` (e.g. `CreateOrderRequest`, `OrderPreviewRequest`).
- **New optional request fields** on body-backed requests that inherit generated models, including `peg_offset_type`, `offset`, `wig_level`, and `is_buy_exact` on `CreateOrderRequest`.
- **`tests/test_model_compat.py`**: Guards backward-compatible model surface across spec updates.
- **`tests/test_service_model_compat.py`**: Guards backward-compatible service request/response field surfaces.
- **`BaseRequest`**, **`BasePaginatedRequest`**, and **`BaseCursorLimitPaginatedRequest`** mixins in `prime_sdk/base_request.py` to centralize `allowed_status_codes` and pagination fields on service `*Request` classes.
- **`CursorLimitPaginationParams`** in `prime_sdk/utils.py` for endpoints that support cursor and limit pagination without `sort_direction`.
- Pagination support on **`ListOpenOrdersRequest`** and **`GetEntityPositionsRequest`**, which the spec documents but the SDK previously omitted.

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
