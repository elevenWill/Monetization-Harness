# Persona source to monetization lens mapping

This mapping was derived from the local repositories under `/Users/lei/Downloads/0813/` at the pinned commits recorded in each Skill's `SOURCE.md`. Source snapshots retain the original MIT licenses, examples, research, workflow, limitations, and attribution.

| Source persona | Domain Skill | Retained core models | Use in this Harness | Explicitly removed |
| --- | --- | --- | --- | --- |
| Paul Graham | `opportunity-finder` | Look for problems, make something people want, iterative discovery, do things that do not scale, founder/domain familiarity | Find observed pain, tolerated manual work, existing spend, and service-first opportunity candidates | Persona voice, founder worship, assumption that venture-scale software is required |
| Slavoj Žižek | `assumption-challenger` | Expose presuppositions, desire versus stated goal, contradiction, fantasy/function, rebuild after critique | Detect FACT/ASSUMPTION collapse, wrong questions, research/building as avoidance, and means becoming ends | Roleplay, jargon-heavy performance, critique without a next action |
| Duan Yongping | `business-filter` | Business model as first filter, right thing before execution, return to origin, circle of competence, validated followership, long horizon | Identify payer, bought result, alternatives, timing, durable revenue logic, repeatability, and reasons not to proceed | Stock-picking advice, persona voice, treating long-term intuition as evidence |
| Nassim Nicholas Taleb | `experiment-designer` | Ruin/ergodicity, asymmetric and convex exposure, barbell, via negativa, skin in the game, turkey problem | Cap downside, avoid irreversible bets, prefer manual/pre-sale/concierge tests, require behavioral or cash evidence | Aggressive persona voice, unsupported certainty, risk critique without an executable test |
| Naval Ravikant | `leverage-designer` | Specific knowledge, accountability, permissionless code/media leverage, productize yourself, compounding, judgment | After repeated value, map repetition into SOPs, automation, code/media assets, and lower marginal delivery cost | Premature “build once, sell forever” advice, lifestyle philosophy, persona voice |

## Applicability boundaries

- Source material is cognitive context, not evidence about the user's market.
- The five rows above are the complete Persona-to-Thinking-Skill mapping. `market-reality-researcher` is an evidence-producing capability, not a Persona-derived Thinking Skill or a sixth lens; it has no `SOURCE.md` Persona provenance and does not count against lens limits. The Why-Now Gate and Buying Situation protocol are orchestrator/domain logic, not a Persona or a new Skill.
- Source few-shot examples are preserved under `examples/source/`; Harness-specific examples are labeled `examples/local/`.
- Each wrapper narrows the original Persona Skill to a decision lens and overrides original roleplay instructions.
- Original Persona source files remain unmodified snapshots. Do not edit or repurpose anything under the five Skills' `references/source/` or `examples/source/` trees as market research, and never cite Persona material as an external-market FACT. `references/domain-core.md`, local examples, `SKILL.md`, and `SOURCE.md` are derived or newly authored.
- The orchestrator depends on domain Skill names, never persona names, so later lenses can be added without changing the state protocol.
- External market sources and Agent Reach results belong in scoped `Rxxx`/`Cxxx` artifacts under the owning project Stage. Their provenance, freshness, coverage, and claim support follow `docs/object-protocol.md` and `docs/workspace-protocol.md`, not this Persona mapping.

## Extraction detail

### Paul Graham → opportunity-finder

- Source workflow retained: classify whether current facts are needed, investigate users/product/organic pull when needed, then reframe toward a more fundamental problem. The wrapper narrows this to direct-access inventory → observed workaround → candidate → ranked investigation → one reality-contact action.
- Apply when there is no credible customer/problem pair. Avoid after a payer and repeated problem are already evidenced unless deliberately discovering a separate opportunity.
- Source few-shot: `.agents/skills/opportunity-finder/examples/source/demo-conversation-2026-04-07.md`.
- Source references: six research files under `.agents/skills/opportunity-finder/references/source/references/research/`, including writings, conversations, expression DNA, external critique, decisions, and timeline.

### Žižek → assumption-challenger

- Source workflow retained: surface claim → presupposition → desire/function → contradiction → more accurate reconstruction. The wrapper adds explicit FACT/ASSUMPTION comparison and requires a reality-contact action.
- Apply to unsupported certainty, means/ends inversion, and avoidance disguised as building/research. Avoid personality diagnosis, jargon performance, and critique that does not alter a decision.
- Source few-shot: `.agents/skills/assumption-challenger/examples/source/demo-inputs.md` and `real-use-cases.md`.
- Source references: `anti-patterns.md`, `concepts.md`, `patterns.md`, and `quotes.md` under the preserved source tree.

### Duan Yongping → business-filter

- Source workflow retained: business model first → right direction before execution → return to origin → competence boundary → long-horizon/repetition check → correct quickly. The wrapper translates this into payer/result/trigger/alternative/money/repeatability fields.
- Apply when a problem/offer or first transaction exists. Avoid using the lens as proof about emerging markets, stock advice, or a substitute for payment experiments.
- Source few-shot: `.agents/skills/business-filter/examples/source/conversations/demo.md`.
- Source references: six research files covering writings, conversations, expression, criticism, decisions, and timeline.

### Taleb → experiment-designer

- Source workflow retained: inspect tail/ruin, fragility, historical stability traps, incentive/skin in the game, and asymmetric exposure. The wrapper always ends with a bounded ethical experiment record.
- Apply to every major commitment and to evidence acquisition under uncertainty. Avoid aggressive certainty, harmful/deceptive tests, and risk critique without an operational alternative.
- Source few-shot: `.agents/skills/experiment-designer/examples/source/demo-conversation.md`.
- Source references: the original research overview plus five Chinese research files on the thought system, conversations, expression, criticism, and major decisions.

### Naval → leverage-designer

- Source workflow retained: identify leverage type, marginal cost, permission needs, compounding, specific knowledge, and aligned accountability. The wrapper adds a repeat-value entry gate and step-by-step baseline/rollback measurement.
- Apply after repeat purchase or stable repeated paid delivery. Avoid using “permissionless leverage” to skip business validation.
- Source few-shot: `.agents/skills/leverage-designer/examples/source/demo-conversation.md`.
- Source references: preserved works/system-thinking, conversations, expression DNA, and quality-validation files.

Exact repository URLs, commits, extraction dates, licenses, filenames, and modification status live in each wrapper's `SOURCE.md`.
