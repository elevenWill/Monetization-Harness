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

The bootstrap operation itself creates no object artifact. If the same first message contains a separate durable event such as a real payment, finish the minimal bootstrap and then persist that event under the lazy-materialization rules.

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

## Mutation triggers

Write project files only when at least one durable item changes:

- a new project is established;
- new evidence-backed fact or transaction;
- new or materially changed experiment;
- explicit decision;
- assumption status becomes supported, weakened, or invalidated;
- stage, status, next gate, largest unknown, or material risk changes.

Do not write for brainstorming, casual questions, a Skill opinion, an unaccepted suggestion, paraphrase churn, or every conversational detail.

## Lazy materialization

`STATE.md` is the sole authority for the current Stage. A directory means only that related durable work exists historically. Stage directories may be absent, non-contiguous, and retained after Stage regression.

Create a Stage directory only in the same operation that writes its first real artifact. Create a nested directory such as `analysis/`, `observations/`, or `evidence/` only together with a file that belongs there. Empty Stage or nested directories are invalid.

Examples:

```text
# bootstrap
IDEA.md
STATE.md

# first opportunity artifact
IDEA.md
STATE.md
01-opportunity/O001.md

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

## Write sequence

1. Confirm a mutation trigger and project ownership.
2. Classify the durable change and determine its owning Stage.
3. Decide whether it needs a standalone artifact. A compact snapshot change may update only `STATE.md`; a transaction, experiment, or evidence record normally needs an artifact.
4. Allocate stable IDs by searching the whole project. For a standalone artifact, create the owning directory and file atomically in the same change.
5. Update the current snapshot and links in `STATE.md`. Reconcile all active assumption statuses, decision bases, counters, risks, and next actions with the new evidence; time-qualify older statements whose original context must be preserved.
6. Update `workspace/_index.md` when a project is created or stage, status, next gate, or date changes. Reconcile a missing or stale row discovered during an otherwise-triggered write; do not create a duplicate project.
7. Re-read changed files. Verify every FACT names or links evidence, links resolve, counters and present-tense summaries agree, the root invariant holds, and no empty directories were introduced.

Use ISO dates (`YYYY-MM-DD`) and repository-relative Markdown links. Redact secrets and personal data. Do not silently rewrite `IDEA.md`; preserve a material direction change and its reasons in the appropriate Stage history.

## Root invariant

A real project root must contain:

- `IDEA.md`
- `STATE.md`

Beyond those files, the root may contain only already-used standard Stage directories:

- `01-opportunity/` through `08-scaling/`
- `99-archive/`

These directories are optional, need not be continuous, and must not be empty. `workspace/_index.md` is the Runtime-maintained project registry; it is not a project. A repository with no real projects needs only `workspace/_index.md` under `workspace/`.

## Resuming without chat history

1. Read `workspace/_index.md` to locate likely projects.
2. Inspect candidate `IDEA.md` and `STATE.md` files and resolve one semantic match.
3. Read the matched project's `IDEA.md` and `STATE.md` completely.
4. Open only linked materials needed for the current gate.
5. Restate the current goal, Stage, largest unknown, active experiment, and next action.
6. Identify missing or stale fields as uncertainty; do not fill them from imagination.
7. Continue from the recorded next action or explain why new evidence changes it.

If these steps cannot recover the project, `STATE.md` is incomplete. Repair it only from existing evidence or user-confirmed information.
