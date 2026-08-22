# Persona source to monetization lens mapping

This mapping was derived from the local repositories under `/Users/lei/Downloads/0813/` at the pinned commits recorded in each Skill's `SOURCE.md`. Source snapshots retain the original MIT licenses, examples, research, workflow, limitations, and attribution.

| Source persona | Domain Skill | Retained core models | Use in this Harness | Explicitly removed |
| --- | --- | --- | --- | --- |
| Paul Graham | `opportunity-finder` | Pre-pitch existence, schlep inversion, love-versus-like, manual-crank discovery, messy precedent transitions | Redirect discovery toward avoided recurring work, intense minority pull, and Reality contact that permits surprise | Persona voice, founder worship, generic evidence bookkeeping, venture-scale software assumptions |
| Slavoj Žižek | `assumption-challenger` | Presupposition extraction, practical function, decaffeinated outcomes, contradiction-to-exposure reconstruction | Detect when the question or activity preserves the exposure it claims to seek, then reconstruct the decision | Roleplay, jargon, personality diagnosis, generic FACT/Stage checks, critique without action |
| Duan Yongping | `business-filter` | Origin test, validated-late entry, thesis ledger/immediate correction, long-horizon mechanism invariance | Test whether the intelligible business reason authorizing continuation still survives and deserves durable commitment | Stock advice, persona voice, generic business canvas, transferability/readiness duplicated from Core |
| Nassim Nicholas Taleb | `experiment-designer` | Ruin precedence, convex exposure, reserved-core barbell, subtraction, hidden tails, consequence symmetry | Change the geometry of evidence exposure when one time-path failure, correlation, or regime break controls survivability | Persona aggression, generic experiment checklist, cheap-test slogans, risk critique without a safe alternative |
| Naval Ravikant | `leverage-designer` | Value-kernel boundary, judgment-mechanism split, replication-mode choice, compounding residue, accountability loop | Reproduce proven value without erasing consequential judgment or the feedback that improves it | Premature “build once, sell forever,” AI/code-as-leverage, business validation, lifestyle philosophy, persona voice |

## Applicability boundaries

- Source material is cognitive context, not evidence about the user's market.
- The five rows above are the complete Persona-to-Thinking-Skill mapping. `market-reality-researcher` is an evidence-producing capability, not a Persona-derived Thinking Skill or a sixth lens; it has no `SOURCE.md` Persona provenance and does not count against lens limits. The Why-Now Gate and Buying Situation protocol are orchestrator/domain logic, not a Persona or a new Skill.
- Source few-shot examples are preserved under `examples/source/`; Harness-specific examples are labeled `examples/local/`.
- Each wrapper narrows the original Persona Skill to a decision lens and overrides original roleplay instructions.
- Original Persona source files remain unmodified snapshots. Do not edit or repurpose anything under the five Skills' `references/source/` or `examples/source/` trees as market research, and never cite Persona material as an external-market FACT. `references/domain-core.md`, local examples, `SKILL.md`, and `SOURCE.md` are derived or newly authored.
- The orchestrator depends on domain Skill names, never persona names, so later lenses can be added without changing the state protocol.
- External market sources found through Agent Reach, AnySearch, or Runtime fallbacks belong in scoped `Rxxx`/`Cxxx` artifacts under the owning project Stage. Their provenance, freshness, coverage, and claim support follow `docs/object-protocol.md` and `docs/workspace-protocol.md`, not this Persona mapping; acquisition capability is not evidence authority.

## Extraction detail

### Paul Graham → opportunity-finder

- Source moves retained: pre-pitch behavior, schlep blindness, intense narrow pull,
  hand-cranked discovery, and behavior-forced transitions hidden by clean success
  stories. Shared evidence classification and Candidate normalization remain in
  the wrapper/Core rather than the Lens operators.
- Apply when there is no credible participant/audience plus problem or repeated-value pattern. Avoid after a payer and repeated value are already evidenced unless deliberately discovering a separate opportunity.
- Source few-shot: `.agents/skills/opportunity-finder/examples/source/demo-conversation-2026-04-07.md`.
- Source references: six research files under `.agents/skills/opportunity-finder/references/source/references/research/`, including writings, conversations, expression DNA, external critique, decisions, and timeline.

### Žižek → assumption-challenger

- Source moves retained: presupposition extraction, the practical function of
  behavior after intellectual critique, “X without X,” and contradiction rebuilt
  into bounded exposure. FACT/ASSUMPTION comparison remains Harness Core.
- Apply to unsupported certainty, means/ends inversion, and avoidance disguised as building/research. Avoid personality diagnosis, jargon performance, and critique that does not alter a decision.
- Source few-shot: `.agents/skills/assumption-challenger/examples/source/demo-inputs.md` and `real-use-cases.md`.
- Source references: `anti-patterns.md`, `concepts.md`, `patterns.md`, and `quotes.md` under the preserved source tree.

### Duan Yongping → business-filter

- Source moves retained: return to the intelligible origin, use validated late
  entry to avoid pioneer errors, preserve the dated thesis, correct immediately
  when it fails, and distinguish temporary opportunity from persistent mechanism.
  User readiness/transferability is now a Core hard gate, not Lens differentiation.
- Apply when a problem/offer or first transaction exists. Avoid using the lens as proof about emerging markets, stock advice, or a substitute for payment experiments.
- Source few-shot: `.agents/skills/business-filter/examples/source/conversations/demo.md`.
- Source references: six research files covering writings, conversations, expression, criticism, decisions, and timeline.

### Taleb → experiment-designer

- Source moves retained: time-path ruin precedence, convex exposure, ring-fenced
  core, subtraction before intervention, hidden regime tails, and consequence
  symmetry. Thresholds, evidence capture, and generic cheap tests remain Core.
- Apply to every major commitment and to evidence acquisition under uncertainty. Avoid aggressive certainty, harmful/deceptive tests, and risk critique without an operational alternative.
- Source few-shot: `.agents/skills/experiment-designer/examples/source/demo-conversation.md`.
- Source references: the original research overview plus five Chinese research files on the thought system, conversations, expression, criticism, and major decisions.

### Naval → leverage-designer

- Source moves retained: isolate the repeated value kernel, preserve specific
  judgment, choose the replication mode from the work geometry, require reusable
  compounding residue, and keep amplified failures accountable.
- Apply after repeat purchase or stable repeated paid delivery. Avoid using “permissionless leverage” to skip business validation.
- Source few-shot: `.agents/skills/leverage-designer/examples/source/demo-conversation.md`.
- Source references: preserved works/system-thinking, conversations, expression DNA, and quality-validation files.

Exact repository URLs, commits, extraction dates, licenses, filenames, and modification status live in each wrapper's `SOURCE.md`.
