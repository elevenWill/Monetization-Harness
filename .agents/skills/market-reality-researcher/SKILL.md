---
name: market-reality-researcher
description: Produce auditable external market evidence for monetization decisions by investigating exact and adjacent precedents, failures, user behavior, purchase-trigger events, real deadlines, cost of delay, buyer-originated urgency, competitors, prices, current platform policy, and case transferability. Use before Thinking Skills when a conclusion depends on current market reality; when the user asks whether a direction is viable, proven, permitted, accepted, competitive, worth entering, or likely to be bought now; when a deadline, campaign, launch, filing, rush request, penalty, or delay consequence is decision-critical; when they request cases or want to copy one; or before substantial spend when current external evidence is missing or stale. Reuse fresh scope-matched research and prefer direct project evidence when only behavior, payment, delivery, or repeatability can answer the claim.
---

# Market Reality Researcher

Produce evidence before judgment. Treat this as an **Evidence-Producing Skill**, not a Persona or Thinking Lens. Do not count it toward the normal one-or-two Thinking Skill limit, imitate a named thinker, vote with other Skills, or replace the user's transaction experiment.

Apply **Case First -> Pattern First -> Replication First**: determine what happened in the market, reconstruct the closest proven transaction and any event that triggered it, test whether its mechanism transfers, then give Thinking Skills an evidence base.

## Route the work

1. Let the orchestrator discover, resume, or bootstrap the project and read `IDEA.md` plus `STATE.md`.
2. Identify the decision and its single largest external unknown.
3. Reuse an existing `Rxxx` only when it is fresh, scope-matched, and sufficient for this decision.
4. Otherwise select `quick`, `standard`, or `deep` depth and execute the research workflow.
5. Persist research only when the repository workspace protocol authorizes a durable write.
6. Return evidence to the orchestrator before it selects Thinking Skills.

Do not research Harness usage, Skill differences, state-only resumption, recorded experiment results, execution details that do not depend on external facts, or questions already answered by fresh sufficient research.

For the end-to-end method and stopping rules, read [references/research-workflow.md](references/research-workflow.md). Read every other reference named by the applicable workflow step; they are direct one-level resources, not optional substitutes for the protocol.

## Frame a decision question

Turn the idea into falsifiable subquestions before issuing queries. Specify:

- market/geography, platform, content type, customer, payer, offer, and bought result;
- exact behavior or transaction that would prove the mode exists;
- current policy and disclosure requirements;
- user acceptance, failures, alternatives, prices, and dependencies;
- the difference between the proposed mode and likely adjacent evidence.

For query families and platform selection, read [references/query-playbook.md](references/query-playbook.md) and [references/source-strategy.md](references/source-strategy.md). Never use broad result counts, popularity, likes, followers, GMV, or hiring volume alone as demand, profit, or repeatability evidence.

When the claim depends on why someone buys now, also define the proposed `trigger event -> deadline/time window -> cost of delay -> consequence owner -> buyer/payer -> workaround -> purchase window -> trust requirement -> bought result` chain. Read [references/trigger-event-search.md](references/trigger-event-search.md) to build event-first queries and [references/deadline-signal-search.md](references/deadline-signal-search.md) to classify deadline sources. Treat anxiety, urgency language, a provider rush listing, or a calendar date as separate leads—not as proof of payment.

## Acquire evidence safely

Prefer Agent Reach when available, but treat it only as a capability layer. Follow [`docs/integrations/agent-reach.md`](../../../docs/integrations/agent-reach.md): dynamically inspect availability, run `agent-reach doctor --json` when available, use active backends, and fall back to Runtime web search, page reading, or authorized browser access. Cite original pages, not Agent Reach.

Use only public material or a login session the user explicitly authorized and controls. Do not install system software, change system configuration, obtain/export cookies, bypass access controls, log in for the user, or store credentials. Put raw temporary output in `/tmp`; never put raw HTML, whole articles, comment walls, or bulk search dumps in the workspace. Record every unvisited relevant channel as a `coverage_gap` and never claim an all-web survey.

## Match evidence to the claim

Use claim-specific authority; never apply one universal evidence ladder:

- **Policy:** current official platform rule > current regulator > official learning center/announcement > credible reporting > vendor explanation > user post > inference. Open the official source; a search snippet is only a lead.
- **Market existence:** independently verifiable transactions or continued operation > independently corroborated cases > official merchant case > operator retrospective > credible interview > vendor customer story > marketing copy > unattributed retelling.
- **Acceptance:** purchase, repeat purchase, retention, refund, or complaint behavior > verifiable operating change > a relevant body of genuine comments > structured research > isolated statements > inference.
- **Purchase trigger:** buyer-originated paid or costly action tied to a verified event > repeated buyer requests or workarounds tied to that event > official deadline plus independently observed buyer behavior > buyer statement > provider rush offer > seller urgency copy > inference.
- **User transferability:** user's paid replication > user's behavioral test > exact case with similar resources > general exact case > adjacent case > theory.

For every policy FACT record `platform`, `region`, `content_type`, `published_at`, `checked_at`, `official_url`, and `status`. For time-sensitive research also retain `accessed_at`. Time-qualify claims; do not hard-code policies, prices, capabilities, traffic rules, or competitor status as permanent.

## Keep exact and adjacent evidence separate

Set source `scope_match` to exactly one of:

```text
exact | adjacent | weak_analogy | irrelevant
```

Use one case verification status:

```text
exact_verified | exact_corroborated | exact_reported
adjacent_verified | adjacent_reported | vendor_claim_only
stale_case | contradicted | insufficient_evidence
```

`exact_verified` requires an exact business form, real actor, explicit time and platform, behavioral or transaction evidence, and evidence beyond vendor promotion. A vendor-only customer story is `vendor_claim_only`: the defensible FACT is that the vendor published the claim, not that the claimed result occurred.

Never let an adjacent case prove an exact mode. If only adjacent cases exist, state:

> 当前只找到了相邻模式，尚未找到足以证明该精确方案已被市场验证的案例。

Reconstruct reusable cases with [references/case-reconstruction.md](references/case-reconstruction.md), then evaluate transferability with [references/transferability-check.md](references/transferability-check.md).

## Search against survivorship bias

Every standard study must seek all five evidence groups:

1. positive or successful cases;
2. failures or negative signals;
3. current official policy for each target platform;
4. user behavior and acceptance;
5. competitors, prices, or substitutes.

Search explicitly for failure, shutdown, refund, complaint, ban, throttling, violation, low conversion, no viewers, distrust, poor results, losses, abandonment, pitfalls, and failed replacement of humans. When no negative case appears, record `no negative case found in current coverage`; never infer that no risk exists.

When why-now is decision-critical, additionally seek the event source, buyer-originated rush behavior, actual consequence of delay, consequence owner, workaround, purchase window, accepted rush price or other costly action, trust barrier, delivery failure/liability, and recurrence. Search a non-urgent control query. Distinguish `hard_external`, `hard_internal`, `rolling_operational`, `opportunity_window`, `soft_social`, `seller_created`, `fabricated`, `none`, and `unknown`; never recommend fabricated scarcity.

## Select research depth

- **quick:** Default for a decision-capped go/no-go check or experiment preparation when one current external fact must be resolved. Predeclare the decision, query/time cap, and stop rule. Target only the minimum authoritative constraint, closest case/negative signal, price or substitute evidence, and explicit gaps needed for that decision.
- **standard:** For an explicit viability landscape, case request, or material direction whose named decision cannot be resolved by a quick check or direct field evidence. Target at least three independent case candidates, ideally one or two exact cases; at least two negative sources; one current official policy source per target platform; acceptance signals from at least two independent channel types; and real price/transaction signals. These are coverage targets, not a license to fill quotas with weak analogies. Stop conclusion escalation when no exact case is found.
- **deep:** For an explicit deep study, major commitment, or multi-platform entry. Add multilingual and multi-period searches, major competitors, business models, unit economics, acquisition, delivery, policy history, positive and negative feedback, failure modes, transfer conditions, and a minimal replication design. Do not implement scheduled monitoring in V0.

## Record auditable objects

Use stable project IDs `R001`, `R002`, ... for a decision-scoped RESEARCH object and `C001`, `C002`, ... only for cases with durable reuse value. Use local source IDs `R001-S01`, `R001-S02`, ... inside a research record. Do not create a Case per page.

An `Rxxx` must contain:

```text
Research question; Scope; Market / geography; Target platforms; Content type;
Started / checked date; Research depth; Queries used; Channels actually accessed;
Coverage gaps; Sources; Supporting evidence; Contradicting evidence; Exact cases;
Adjacent cases; Negative cases; Policy findings; User acceptance signals;
Competitor and pricing signals; Verdict; Remaining unknowns; Recheck condition
```

Each source must contain:

```text
id; title; url; publisher; platform; source_type; published_at; accessed_at;
market; claim; supports; contradicts; authority; verification; freshness;
scope_match; direction; notes
```

Use only these source-quality classifications:

```yaml
authority: official | first_party | independent_third_party | user_generated | vendor_marketing | unknown
verification: directly_observed | independently_corroborated | single_source_reported | unverified
freshness: current | aging | stale | unknown
scope_match: exact | adjacent | weak_analogy | irrelevant
direction: supports | contradicts | mixed | neutral
```

Explain why each source can support the named claim. Do not collapse these dimensions into a numeric confidence score.

Keep Purchase Trigger findings inside the existing `Rxxx` schema: record event-first queries under `Queries used`, deadline and behavior sources under `Sources`, supported and contradicted trigger links under evidence sections, and missing consequence, owner, budget, reachability, trust, or transaction links under `Coverage gaps` and `Remaining unknowns`. Do not invent a new Research depth, source-quality enum, or research verdict for trigger work.

Use one research verdict:

```text
exact_precedent_verified | exact_precedent_reported | adjacent_precedent_only
market_signal_exists | insufficient_evidence | contradicted_by_evidence
policy_conditional | policy_blocked | research_blocked | stale_research
```

The full Case schema is in [references/case-reconstruction.md](references/case-reconstruction.md). When persistence is authorized, resolve the exact canonical Stage path from `docs/workspace-protocol.md` and create the first artifact with it in the same write—for example, `01-opportunity/research/R001-market-reality-scan.md` for `opportunity_discovery` or `02-problem-validation/research/R002-problem-market-evidence.md` for `problem_validation`. Never abbreviate a Stage directory. Create `cases/Cxxx-*.md` only when warranted. Never add `MARKET.md`, `RESEARCH.md`, `CASES.md`, or `SOURCES.md` to a project root; never create empty directories.

## Produce the Closest Proven Playbook

Do not return a link pile or a feeling-based viability score. Report separately whether anyone has done it, policy allows it, behavior supports it, cases transfer, and the current user has the required conditions.

When purchase timing materially affects the decision, also report separately: the candidate trigger, deadline type and source, cost and owner of delay, observed buyer behavior, purchase window, payer reachability, trust barrier, recurrence, delivery liability, and every unverified link. A real deadline without buyer behavior is not a purchase trigger; high urgency can still be unbuyable.

Use this response shape when research materially informs the answer:

```markdown
## 当前判断
<precedent/verdict status and decisive evidence>

## 已被验证的部分
- <evidence-backed transactions, behavior, or policy facts>

## 尚未被验证的部分
- <remaining assumptions>

## 最接近的成功模式
<who uses it, who pays, bought result, acquisition, delivery, conditions, limits>

## 不能直接照抄的部分
- <unique resources, geography, platform, or time differences>

## 平台与合规约束
- <platform + region + content type + checked date>

## 反面证据
- <failures, complaints, penalties, or conversion problems>

## 当前最小复现实验
<Cxxx mechanism copied, omitted advantages, migration assumption, cap, pass/fail/stop>

## 研究覆盖
- 已访问：
- 未访问：
- 最新检查时间：
```

If no exact case exists, use `Exact Proven Playbook: 未找到`, name the `Closest Adjacent Playbook`, and state the decisive difference. The next experiment should replicate the closest verified transaction mechanism, not justify a full build.

## Use the examples

- Read [examples/local/digital-human-commerce.md](examples/local/digital-human-commerce.md) for the complete digital-human short-video commerce flow.
- Read [examples/local/adjacent-case-trap.md](examples/local/adjacent-case-trap.md) when evidence differs by format, platform, market, customer, or transaction.
- Read [examples/local/vendor-claim-trap.md](examples/local/vendor-claim-trap.md) for promotional outcome claims.
- Read [examples/local/policy-conflict.md](examples/local/policy-conflict.md) for stale or conflicting platform rules.
- Read [examples/local/no-exact-precedent.md](examples/local/no-exact-precedent.md) when searches find signals but no exact proven case.
- Read [examples/local/deadline-opportunity.md](examples/local/deadline-opportunity.md) for a potentially recurring operational deadline.
- Read [examples/local/fake-urgency.md](examples/local/fake-urgency.md) when urgency originates from seller copy, scarcity, or a countdown.
- Read [examples/local/urgent-but-unbuyable.md](examples/local/urgent-but-unbuyable.md) when a real urgent consequence may be blocked by trust, access, procurement, or liability.
- Read [examples/local/digital-human-deadline.md](examples/local/digital-human-deadline.md) when campaign timing is claimed to create demand for digital-human short videos.

## Guardrails

Respect terms of service and copyright. Quote only what is necessary and brief; retain original URL and access date. Extract commercial mechanisms, not brands, likenesses, copy, or protected assets. Public GMV does not prove profit; external cases do not prove the current user can reproduce them; research never replaces a bounded real transaction experiment. Do not fabricate deadlines, inventory, capacity, buyer posts, accepted quotes, payments, penalties, or scarcity, and do not recommend deceptive urgency as a test.
