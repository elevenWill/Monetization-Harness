# 01 — New project auto-bootstrap and lazy growth

## Preconditions

- `workspace/` contains only `_index.md`.
- No existing project matches AI commerce short video.
- The user has not run a setup command or supplied a project name or slug.

## User message

> 我最近发现 AI 带货短视频可能有机会，我想研究这里怎么变现。

## Expected observable behavior

- Runtime recognizes a concrete, continuing monetization thread and creates a
  stable, semantic project slug without asking the user to name it.
- The bootstrap operation itself creates exactly `IDEA.md` and `STATE.md` and
  updates `_index.md`; it creates no empty stage directory.
- `STATE.md` starts at `opportunity_discovery`, distinguishes observations from
  assumptions, and names the largest unknown and next gate.
- Runtime performs a light scan of the possible purchase mechanism without
  forcing a complete Buying Situation or business audit at this Stage. Here a
  bounded market reconnaissance is warranted only because current public-market
  existence, buyer behavior, platform constraints, and available precedents can
  change which problem is worth observing next; a new project by itself would
  not require search. If that real research completes in the same turn, it is a
  separate durable mutation: create a non-empty
  `01-opportunity/research/R001-*.md`, link it from `STATE.md`, and do not create
  any unrelated stage directory.
- The response surfaces observed problems, affected people, and the cheapest
  decision-changing Reality Evidence. It treats “AI video is trending” as a
  hypothesis about demand rather than forcing a full business evaluation.
- Runtime continues answering the monetization question in the same turn.

### Lazy-growth follow-up

When the conversation later produces a real `E001`, Runtime creates a non-empty
`04-experiments/` containing that record. Existing research material may remain
under `01-opportunity/`; Runtime still does not create unused
`02-problem-validation/`, `03-business-validation/`, or any later stage directory
merely to make the tree look complete.

## Failure conditions

- Asks the user to run Python, choose a slug, create directories, or select a stage.
- Treats minimal bootstrap and same-turn research persistence as one reason to
  pre-create the full stage skeleton, any empty directory, or a template copy.
- Treats project novelty alone as a reason to search, skips decision-critical
  current evidence in this scenario, or writes a research artifact without
  actually completing research.
- Forces a complete Why-Now/Buying Situation/business audit before identifying a
  concrete problem and the cheapest Reality Evidence.
- Creates a second project despite one clearly matching the topic.
- Stops after persistence instead of continuing the conversation.
