# Conversation-first workspace protocol

The workspace is Codex's durable memory for resumable monetization threads. It is not a database the user must initialize or maintain. The user starts by talking; Runtime owns discovery, bootstrap, resumption, lazy directory creation, and indexing.

## Project discovery

For each substantive monetization message:

1. Decide whether the topic is a concrete thread worth resuming. General knowledge, Harness questions, generic one-off discussions, and passing brainstorms remain No Project and cause no writes.
2. Read `workspace/_index.md`, enumerate actual `workspace/*/` project roots, and inspect complete `IDEA.md` and `STATE.md` files for plausible candidates. The registry is navigation, not proof that no unindexed project exists.
3. Resume a single clear semantic match using customer, problem, goal, offer, distinctive evidence, current context, and recency. Do not match on one keyword or create a duplicate for a rephrased topic.
4. If multiple projects remain plausible and a wrong choice could corrupt durable state, analyze provisionally without writing. Ask which project only when ownership is necessary.
5. If no project matches and the conversation establishes a concrete direction worth continuing, bootstrap automatically and continue the answer in the same turn.

## Automatic bootstrap

Generate a meaningful lowercase ASCII short-kebab-case slug from the idea. Treat it as an internal stable ID that the user does not need to choose. If the slug already names the same topic, resume it; for a genuinely different collision, use the first free deterministic numeric suffix. Do not rename an existing directory when only the project's display name changes.

Bootstrap creates exactly:

```text
workspace/<slug>/
├── IDEA.md
└── STATE.md
```

It also adds a row to `workspace/_index.md`. It does not copy a template, create a Stage directory, or require a script, slug, goal flag, or manual Stage selection.

`IDEA.md` records only the user's initial idea, current goal, currently believed customer, and initial decision-relevant assumptions. `STATE.md` records the evidence-derived Stage (normally `opportunity_discovery` when no stronger gate is met), active status, transaction counts, current goal, facts, assumptions, decisions, largest unknown, next gate, next action, material risk, active experiment, last change, and links. Use `unknown` for missing information. Set transaction counts to `0` only when the conversation supports zero; otherwise use `unknown`.

The bootstrap operation itself creates no object artifact. If the same first message contains a separate durable event such as a real payment, finish the minimal bootstrap and then persist that event under the lazy-materialization rules. The same separation applies to market research and Buying Situations: bootstrap still creates only `IDEA.md` and `STATE.md`; if the Market Reality Gate then produces real research in the same turn, persist it afterward as an independent write that creates the current Stage's non-empty `research/` directory and first `Rxxx` artifact together. If trigger analysis produces a real `BSxxx`, create its non-empty `buying-situations/` path in a separate subsequent write rather than as bootstrap scaffolding.

Use this minimum file contract; omit unsupported detail rather than adding speculative prose:

```markdown
<!-- IDEA.md -->
---
project: "<stable-slug>"
display_name: "<faithful short name>"
created_at: "<YYYY-MM-DD>"
status: active
---

# Idea

## 初始想法
<what the user actually expressed>

## 当前目标
<user-grounded goal or unknown>

## 目前认为的用户
<user-grounded customer or unknown>

## 当前关键假设
<stable-ID summaries or unknown>
```

```markdown
<!-- STATE.md -->
---
project: "<stable-slug>"
stage: <evidence-derived-stage>
status: active
updated_at: "<YYYY-MM-DD>"
transactions:
  total: <supported-count-or-unknown>
  repeat_customers: <supported-count-or-unknown>
next_gate: <gate-or-unknown>
---

# Current State

## 当前目标
## 已确认事实 FACTS
## 当前假设 ASSUMPTIONS
## 当前决定 DECISIONS
## 最大未知量
## 当前最大风险
## 当前实验
## Next Gate
## 当前下一步
## 为什么这是下一步
## 最近一次状态变化
## 相关材料
```

Allocate stable IDs only for decision-relevant claims that are actually persisted. A FACT summarized at bootstrap must name its evidence (for example, a dated direct user statement); a runtime inference stays an ASSUMPTION or analysis.

After real market research exists, `STATE.md` may add a compact `market_evidence` block. When the block is present, it must also include corresponding Markdown headings for current external evidence, latest research, closest verified pattern, policy status, and coverage gaps. Do not include these optional fields or headings as empty bootstrap boilerplate. The block should link the latest `Rxxx`, state the matched market/platform/content/decision scope, checked date, freshness status, exact-precedent status, and material gaps.

After a real Buying Situation is being analyzed, `STATE.md` may also add this compact snapshot. Omit the entire block from bootstrap and from projects with no active trigger analysis. Use one allowed enum value per field and `unknown` for unsupported values; keep detailed evidence in the linked `BSxxx` object.

```yaml
purchase_trigger:
  status: not_started | hypothesis | partial | evidenced | paid | repeated | invalidated
  active_buying_situation: BS001
  trigger_event: unknown
  deadline_type: hard_external | hard_internal | rolling_operational | opportunity_window | soft_social | seller_created | fabricated | none | unknown
  deadline_window: unknown
  cost_of_delay: unknown
  consequence_owner: unknown
  purchase_window: unknown
  trust_barrier: unknown
  low_trust_entry: unknown
  latest_evidence: unknown
```

The `|` alternatives document enums; a real `STATE.md` contains one value. The snapshot status describes the project's current Purchase Trigger Gate:

- `not_started`: a real `BSxxx` has been selected for Why-Now analysis, but evidence collection for its trigger chain has not begun; omit the block entirely when no Buying Situation exists;
- `hypothesis`: an active Buying Situation is proposed but its trigger chain is unverified;
- `partial`: some links in the trigger-to-purchase chain have evidence, but a decision-critical link remains `unknown`;
- `evidenced`: the material trigger, time window, consequence, owner, buyer/payer, trust, and reachability links are supported, but this Project has no qualifying payment in the situation;
- `paid`: at least one qualifying completed payment is linked;
- `repeated`: materially comparable Buying Situations have produced independent repeat transaction evidence;
- `invalidated`: evidence or a declared disconfirmation condition breaks a necessary link in the active situation.

It does not replace the `BSxxx` object's more granular status or its evidence links. Follow [`purchase-trigger-protocol.md`](purchase-trigger-protocol.md) for the field meanings and Why-Now rules.

## Mutation triggers

Write project files only when at least one durable item changes:

- a new project is established;
- new evidence-backed fact or transaction;
- completed decision-relevant market research, a reusable external case, or a material change in research freshness or coverage;
- a decision-relevant Buying Situation is first persisted, materially changes status, or gains trigger, Cost-of-Delay, trust, reachability, or transaction evidence;
- a new accepted experiment, a materially changed experiment plan, or a completed experiment result;
- explicit decision;
- assumption status becomes supported, weakened, or invalidated;
- stage, status, next gate, largest unknown, or material risk changes.

Do not write for brainstorming, casual questions, a Skill opinion, an unaccepted suggestion, paraphrase churn, or every conversational detail.

## Lazy materialization

`STATE.md` is the sole authority for the current Stage. A directory means only that related durable work exists historically. Stage directories may be absent, non-contiguous, and retained after Stage regression.

Create a Stage directory only in the same operation that writes its first real artifact. Create a nested directory such as `analysis/`, `observations/`, `evidence/`, `research/`, `cases/`, or `buying-situations/` only together with a file that belongs there. Empty Stage or nested directories are invalid.

Use this exact mapping; these directory names are protocol identifiers and must not be shortened or reworded:

| Stage | Canonical directory |
| --- | --- |
| `opportunity_discovery` | `01-opportunity/` |
| `problem_validation` | `02-problem-validation/` |
| `business_validation` | `03-business-validation/` |
| `experiment_validation` | `04-experiments/` |
| `transaction_validation` | `05-transactions/` |
| `leverage_discovery` | `06-leverage/` |
| `productization` | `07-productization/` |
| `scaling` | `08-scaling/` |

`99-archive/` stores archived material and is not an active Stage mapping. A path such as `02-problem/` is invalid even when its meaning seems clear.

Store each completed decision-relevant external investigation as `Rxxx-<short-name>.md` under the owning Stage's `research/` directory. It must record the research question, scope, market/geography, target platforms, content type, checked date, depth, queries, channels actually accessed, coverage gaps, sources, supporting and contradicting evidence, exact/adjacent/negative cases, policy findings, market signals, verdict, remaining unknowns, and recheck condition. Source entries normally remain inside the research artifact using stable local IDs such as `R001-S01`; do not create a file for every page or raw search result.

Create `Cxxx-<short-name>.md` under the owning Stage's `cases/` directory only when a success or failure case has durable comparative value. A CASE must link its supporting `Rxxx` and local source IDs, distinguish exact from adjacent precedent, record verification and transferability limits, and state its relevance to the current project. Finding a page does not by itself justify a CASE artifact.

Create `BSxxx-<short-name>.md` under the owning Stage's `buying-situations/` directory only when a concrete Buying Situation is actually being analyzed and is decision-relevant. It must use the complete schema in [`object-protocol.md`](object-protocol.md), link its evidence, use `unknown` rather than invented field values, and distinguish buyer anxiety from a real Trigger Event and Cost of Delay. The Why-Now Gate is cross-stage; the artifact belongs to the Stage whose decision it informs, not automatically to `03-business-validation/`.

Examples:

```text
# bootstrap
IDEA.md
STATE.md

# first opportunity artifact
IDEA.md
STATE.md
01-opportunity/O001.md

# first market scan after bootstrap
IDEA.md
STATE.md
01-opportunity/research/R001-market-reality-scan.md

# first reusable case from that scan
IDEA.md
STATE.md
01-opportunity/research/R001-market-reality-scan.md
01-opportunity/cases/C001-verified-precedent.md

# first Buying Situation, once business-validation work is real
IDEA.md
STATE.md
03-business-validation/buying-situations/BS001-campaign-video-deadline.md

# first experiment; intermediate directories need not exist
IDEA.md
STATE.md
01-opportunity/O001.md
04-experiments/E001.md

# first payment
IDEA.md
STATE.md
01-opportunity/O001.md
04-experiments/E001.md
05-transactions/T001.md
```

Never create `01-opportunity/` merely because `stage: opportunity_discovery`, and never backfill missing directories for visual completeness.

An Experiment plan, its completed result, and its aggregate Evidence Ledger stay
in the same `Exxx` artifact under `04-experiments/`. Completion does not create a
new object ID, project-root result file, lead table, or funnel directory. Existing
plan-only experiments require no migration; apply the completion contract in
[`object-protocol.md`](object-protocol.md) only when a completed/result section is
recorded.

## Write sequence

1. Confirm a mutation trigger and project ownership.
2. Classify the durable change and determine its owning Stage. The Market Reality Gate and Why-Now Gate are not Stages; research and Buying Situations belong to the Stage whose decision they inform.
3. Decide whether it needs a standalone artifact. A compact snapshot change may update only `STATE.md`; a transaction, experiment, completed decision-relevant RESEARCH record, or real decision-relevant Buying Situation normally needs an artifact. Create a standalone CASE only when it is reusable beyond one research summary.
4. Allocate stable IDs by searching the whole project. For a standalone artifact, create the owning directory and file atomically in the same change.
5. Update the current snapshot and links in `STATE.md`. Reconcile the active experiment's status/result, all active assumption statuses, evidence-backed facts, user-committed decision bases, transaction counters, Stage entry evidence, largest unknown, risks, and next actions. When present, also reconcile market scope, checked date, latest-research link, freshness, policy status, exact-precedent status, coverage gaps, and the optional Purchase Trigger snapshot. Time-qualify older statements whose original context must be preserved; mark superseded or stale research explicitly rather than leaving its conclusion current. An Experiment result code alone does not promote or roll back the Stage.
6. Update `workspace/_index.md` when a project is created or stage, status, next gate, or date changes. Reconcile a missing or stale row discovered during an otherwise-triggered write; do not create a duplicate project.
7. Re-read changed files. Verify every FACT names or links evidence; every RESEARCH and CASE has scope, checked date, supporting source IDs or links, contradictory evidence, and coverage limits; every `BSxxx` uses an allowed status and Deadline type and marks missing fields `unknown`; links resolve; counters and present-tense summaries agree; the root invariant holds; and no empty directories were introduced.

Use ISO dates (`YYYY-MM-DD`) and repository-relative Markdown links. Redact secrets and personal data. Do not silently rewrite `IDEA.md`; preserve a material direction change and its reasons in the appropriate Stage history.

## Root invariant

A real project root must contain:

- `IDEA.md`
- `STATE.md`

Beyond those files, the root may contain only already-used standard Stage directories:

- `01-opportunity/` through `08-scaling/`
- `99-archive/`

These directories are optional, need not be continuous, and must not be empty. `workspace/_index.md` is the Runtime-maintained project registry; it is not a project. A repository with no real projects needs only `workspace/_index.md` under `workspace/`.

Do not add `MARKET.md`, `RESEARCH.md`, `CASES.md`, `SOURCES.md`, `DEADLINE.md`, `HUMAN-NATURE.md`, `URGENCY.md`, `BUYING-SITUATIONS.md`, or equivalent research/source/urgency files at the project root. `research/`, `cases/`, and `buying-situations/` are optional nested Stage directories and must be created only with their first real artifact.

## Resuming without chat history

1. Read `workspace/_index.md` to locate likely projects.
2. Inspect candidate `IDEA.md` and `STATE.md` files and resolve one semantic match.
3. Read the matched project's `IDEA.md` and `STATE.md` completely.
4. Open only linked materials needed for the current gate, including the latest relevant `Rxxx`/`Cxxx` when external evidence matters and the active `BSxxx` when why-now evidence matters; verify scope and freshness before reuse.
5. Restate the current goal, Stage, largest unknown, active experiment, active Buying Situation when present, and next action.
6. Identify missing or stale fields, market coverage, and Purchase Trigger evidence as uncertainty; do not fill them from imagination or treat an inaccessible channel as searched.
7. Continue from the recorded next action or explain why new evidence changes it.

If these steps cannot recover the project, `STATE.md` is incomplete. Repair it only from existing evidence or user-confirmed information.
