---
id: case-10
title: Resume from repository state only
expected_stage: experiment_validation
expected_skills:
  - experiment-designer
require_challenge: false
require_evidence_split: true
require_action: true
require_correction: false
require_persistence: true
expected_stage_change: false
fixture: evals/fixtures/resumption-project
---

# CASE 10 — Resumption without chat history

## State

All context must be recovered from the fixture's `IDEA.md`, `STATE.md`, and linked `E003` record. No chat history is available.

## Input

> 继续这个项目。先告诉我目前最大未知量和下一步，不要假设你记得之前的聊天。

## Expected behavior

Recover goal, stage, transaction count, active assumption/experiment, stop condition, and next action only from repository files.

## Failure conditions

- Invents prior discussion.
- Misses the active experiment or changes project state without new evidence.
