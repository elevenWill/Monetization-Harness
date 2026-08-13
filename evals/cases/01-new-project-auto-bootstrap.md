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
- The new project contains exactly `IDEA.md` and `STATE.md`; `_index.md` is
  updated, and no empty stage directory is created.
- `STATE.md` starts at `opportunity_discovery`, distinguishes observations from
  assumptions, and names the largest unknown and next gate.
- `opportunity-finder` is the primary lens; `assumption-challenger` is added only
  if needed to challenge trend-implies-demand reasoning.
- Runtime continues answering the monetization question in the same turn.

### Lazy-growth follow-up

When the conversation later produces a real `E001`, Runtime creates a non-empty
`04-experiments/` containing that record. It still does not create unused
`01-opportunity/`, `02-problem-validation/`, `03-business-validation/`, or any
later stage directory merely to make the tree look complete.

## Failure conditions

- Asks the user to run Python, choose a slug, create directories, or select a stage.
- Creates the full stage skeleton, any empty directory, or a template copy.
- Creates a second project despite one clearly matching the topic.
- Stops after persistence instead of continuing the conversation.
