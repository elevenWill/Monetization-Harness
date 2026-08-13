# Local derived routing cases

These examples are authored for this Harness. Broader human-auditable behavior scenarios live in `evals/cases/`.

## New conversation-first direction

Workspace contains only `_index.md`. Input: “I keep seeing small merchants struggle to make 10–15 second commerce videos and want to investigate whether this can make money.”

Classify it as a concrete resumable monetization thread, not a generic question. Generate an internal stable slug, bootstrap only `IDEA.md` and `STATE.md` from what the user actually said, update `_index.md`, route primarily to `opportunity-finder`, and continue the substantive answer in the same turn. Do not create any Stage directory.

## Ordinary question

Input: “What is the biggest difference between Naval and Taleb?”

Classify it as No Project. Answer normally without inspecting detailed project history or writing Workspace state.

## Premature architecture

State: no customer, interviews, or payments. Request: design a database and agent architecture.

Route `assumption-challenger` + `experiment-designer`. Final judgment: the current unknown is demand/transaction, and “a full system is needed” is an assumption. Propose a timeboxed real offer.

## Repeat value

State: eight independent customers, repeat purchases, similar delivery steps. Request: continue fully manually?

Route `leverage-designer`; add `business-filter` only if repeat economics are unknown. Map steps and create one SOP/assisted asset before a full product.

## Stage regression

State says `productization`; evidence says no customer bought again after launch.

Recompute stage as `business_validation`, route `business-filter` + `experiment-designer`, and inspect the failed repeat-value assumption instead of adding features.
