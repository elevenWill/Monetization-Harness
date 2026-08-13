---
id: case-03
title: One paid lawyer delivery
expected_stage: transaction_validation
expected_skills:
  - business-filter
  - experiment-designer
require_challenge: false
require_evidence_split: true
require_action: true
require_correction: true
require_persistence: true
expected_stage_change: true
---

# CASE 03 — First lawyer payment

## State

- Previously `experiment_validation`.
- `transactions.total = 0` before the message.

## Input

> 一个律师已经给我 500 元让我整理案件资料。

## Expected behavior

Record one transaction as FACT/TRANSACTION, move to transaction validation, and test independent repeatability. Do not jump to SaaS.

## Failure conditions

- Treats one payment as repeat demand.
- Routes directly to leverage or productization.
- Fails to persist the new transaction and state change.
