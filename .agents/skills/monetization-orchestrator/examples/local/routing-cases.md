# Local derived routing cases

These examples are authored for this Harness. Full executable records live in `evals/`.

## Premature architecture

State: no customer, interviews, or payments. Request: design a database and agent architecture.

Route `assumption-challenger` + `experiment-designer`. Final judgment: the current unknown is demand/transaction, and “a full system is needed” is an assumption. Propose a timeboxed real offer.

## Repeat value

State: eight independent customers, repeat purchases, similar delivery steps. Request: continue fully manually?

Route `leverage-designer`; add `business-filter` only if repeat economics are unknown. Map steps and create one SOP/assisted asset before a full product.

## Stage regression

State says `productization`; evidence says no customer bought again after launch.

Recompute stage as `business_validation`, route `business-filter` + `experiment-designer`, and inspect the failed repeat-value assumption instead of adding features.
