# V0 evaluations

The V0 eval surface consists of human-readable scenario specifications in `cases/`, hand-simulated golden traces in `results/`, and a standard-library validator in `run_evals.py`.

This intentionally does not implement an LLM runner or another agent loop. Codex is the runtime. The traces make route, challenge, stage, evidence, action, correction, persistence, and resumption expectations auditable in Git.

Run:

```bash
python3 evals/run_evals.py
```

For a live forward test, start a fresh Codex task in this repository, provide a case's State and Input without its Expected behavior, and compare the response with the corresponding result. Case 09 is the mandatory core acceptance test: a response that begins database/agent architecture design fails V0.

`case-10` additionally verifies that the fixture can be resumed from repository content alone. Repository-wide static checks and an isolated real run of `scripts/new_project.py` are performed by:

```bash
python3 scripts/validate_repo.py
```
