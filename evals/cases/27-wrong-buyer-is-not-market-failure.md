# 27 — Wrong buyer is not market failure

## Preconditions

- An offer experiment contacted 10 people at target companies.
- Evidence now shows that all 10 were individual contributors without purchasing
  authority, budget influence, or responsibility for the stated consequence.
- Some saw the offer and price, but no intended decision-maker was exposed.

## User message

> 我联系了 10 个人，后来才发现他们都不是采购人，也不负责这个结果。没人买，是不是市场不行？

## Expected observable behavior

- Runtime classifies the completed experiment as `invalid`, not
  `demand_failure`, because the qualified intended-buyer minimum was zero.
- It records the first broken selected step as buyer qualification/decision
  relevance and distinguishes this observable break from an unsupported causal
  claim about the market.
- The market-demand and price assumptions remain unresolved. Stage is reviewed
  from the full evidence and is not automatically promoted or rolled back by the
  result label.
- The repaired test names the consequence owner, buyer/payer role, qualification
  and exclusion rules, concrete sources or filters, a bounded sample, and the
  evidence required before counting exposure.

## Failure conditions

- Treats employees at a target company as qualified buyers merely because they
  saw a message.
- Declares market, demand, price, or urgency failure from the zero purchases.
- Repeats the same list with more volume without changing qualification or access
  to a decision-relevant role.
