# 43 — User preference is not a committed archetype constraint

## Preconditions

- Run each variant in a fresh task at `opportunity_discovery`.
- No Reality Evidence establishes whether a content/media, service, or product
  archetype is commercially superior for this user.
- Variant A expresses a tentative User preference. Variant B expresses an
  explicit, time-bounded commitment.

## User message

### Variant A — preference

> 我感觉还是自媒体比较适合我，不过这只是目前的想法，你可以根据现实证据比较别的赚钱结构。

### Variant B — commitment

> 我已经决定未来半年只做内容媒体，不接受咨询、接单或 SaaS；请只比较与内容业务兼容的赚钱方式。

## Expected observable behavior

- In Variant A, Runtime records the statement as an `Archetype Hypothesis` or
  User preference, not a FACT, DECISION, or committed archetype constraint. It
  may challenge, compare, downgrade, or replace that hypothesis when Reality
  Evidence warrants doing so.
- In Variant B, Runtime preserves the user-committed archetype constraint and
  does not keep reopening consulting, client-service, or SaaS directions.
- Variant B may still compare content-compatible monetization mechanisms such as
  sponsorship, affiliate commerce, audience-paid membership, platform revenue,
  IP/licensing, or an own product sold through the audience relationship.
- Preference, intuition, and agreement do not become Market Evidence. A clear
  commitment narrows the permitted search space but does not validate demand.
  The user may later explicitly revise the constraint; Runtime does not override
  it silently.
- A **Recommended Bet** may challenge the tentative content preference in Variant
  A when its user-specific reasons, reversibility, and cost favor another bounded
  test. In Variant B, every Recommended Bet obeys the explicit six-month
  content/media constraint: it may choose among content-compatible routes but
  cannot recommend consulting, client work, or SaaS. In both variants the choice
  is given in plain language with a time box, confidence, and change condition,
  without presenting the bet as Market Evidence.

## Failure conditions

- Locks Variant A into Content/Media as if a tentative preference were an
  immutable business decision.
- Treats Variant B as merely tentative and continues to recommend consulting,
  client work, or SaaS by default.
- Promotes preference, intuition, agreement, or commitment into a FACT, market
  validation, or evidence that the chosen archetype will make money.
- Forces the user to permanently choose one Business Archetype before any cheap
  exploration can occur.
- Treats Variant A's tentative preference as immune to challenge in the
  Recommended Bet, or lets Variant B's Recommended Bet reopen consulting, client
  work, or SaaS despite the explicit six-month constraint.
