# Changelog

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
