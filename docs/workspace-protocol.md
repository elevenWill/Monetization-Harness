# Workspace and resumption protocol

## Mutation triggers

Write project files only when at least one durable item changes:

- new evidence-backed fact or transaction;
- new or materially changed experiment;
- explicit decision;
- assumption status becomes supported, weakened, or invalidated;
- stage, status, next gate, largest unknown, or material risk changes.

Do not write for brainstorming, casual questions, a Skill opinion, or a proposed decision the user has not accepted.

## Write sequence

1. Determine the stage owning the material.
2. Allocate stable IDs by searching the whole project.
3. Write the detailed evidence/object in that stage directory.
4. Update the current snapshot and links in `STATE.md`.
5. Update `workspace/_index.md` when stage, status, next gate, or date changes.
6. Re-read changed files and verify every FACT has evidence and every link resolves.

Use ISO dates (`YYYY-MM-DD`) and repository-relative Markdown links. Redact secrets and personal data.

## Root invariant

A project root may contain only:

- `IDEA.md`
- `STATE.md`
- `01-opportunity/` through `08-scaling/`
- `99-archive/`

Put uncertain analysis in the current stage's `analysis/`, never at the project root.

## Resuming without chat history

1. Read `workspace/_index.md` to locate the project.
2. Read the project's `IDEA.md` and `STATE.md` completely.
3. Open only the linked materials needed for the current gate.
4. Restate the current goal, stage, largest unknown, active experiment, and next action.
5. Identify missing or stale fields as uncertainty; do not fill them from imagination.
6. Continue from the recorded next action or explain why new evidence changes it.

If these steps cannot recover the project, `STATE.md` is incomplete and must be repaired before proceeding.
