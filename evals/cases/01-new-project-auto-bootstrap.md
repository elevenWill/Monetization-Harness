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
- Because the question depends on a public market and the project has no market
  evidence, Runtime runs a bounded quick market reconnaissance before the
  Thinking Skills. If that real research completes in the same turn, it is a
  separate durable mutation: create a non-empty
  `01-opportunity/research/R001-*.md`, link it from `STATE.md`, and do not create
  any unrelated stage directory.
- `opportunity-finder` is the primary lens; `assumption-challenger` is added only
  if needed to challenge trend-implies-demand reasoning.
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
- Gives a market-feasibility direction without the required quick scan or writes
  a research artifact without actually completing research.
- Creates a second project despite one clearly matching the topic.
- Stops after persistence instead of continuing the conversation.
