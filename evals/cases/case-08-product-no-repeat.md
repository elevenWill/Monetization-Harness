---
id: case-08
title: Productization without repeat purchase
expected_stage: business_validation
expected_skills:
  - business-filter
  - experiment-designer
require_challenge: true
require_evidence_split: true
require_action: true
require_correction: true
require_persistence: true
expected_stage_change: true
---

# CASE 08 — Stage regression

## State

- Stored stage is `productization`.
- Product launched.
- No customer purchased again.

## Input

> 产品上线了，但没有人重复购买。下一版应该加什么功能？

## Expected behavior

Regress to `business_validation`, invalidate the repeat-value assumption, and test why the bought result did not recur. Do not add features by default.

## Failure conditions

- Treats stages as one-way.
- Generates a feature roadmap.
