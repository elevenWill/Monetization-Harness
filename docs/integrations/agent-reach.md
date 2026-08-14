# Agent Reach Integration

Agent Reach is an optional, preferred internet capability layer for Market Reality Research. It can help the Runtime reach supported platforms and collect original content. It is not the research method, does not determine evidence quality, and is not itself a source to cite.

The `market-reality-researcher` owns question decomposition, claim-specific source selection, exact-versus-adjacent classification, contradiction search, case reconstruction, and transferability. Agent Reach only supplies available access paths.

## Dynamic use

When current external evidence is required:

1. Check whether the `agent-reach` command/capability is available in the current Runtime.
2. If available, run:

   ```bash
   agent-reach doctor --json
   ```

3. Parse the current result rather than assuming any backend is installed, configured, authenticated, or healthy.
4. Select only an active backend appropriate to the target platform and decision question.
5. Use Agent Reach-supported channels for original content.
6. For unsupported or inactive channels, fall back to available Codex Web Search, webpage reading, or browser capability.
7. Open and cite the original webpage or platform item. Do not cite Agent Reach or its diagnostic output as evidence for a market claim.

Do not hard-code the set of supported platforms or backend behavior. Installation, authentication, platform access, and service behavior can change.

## Unavailable or partial coverage

Agent Reach unavailability must not fail the whole study. Use Runtime fallbacks and record:

```yaml
channels_actually_accessed:
  - <channel and access method>
coverage_gaps:
  - channel: <relevant but inaccessible platform>
    reason: <not installed, inactive backend, authentication unavailable, access denied, or unsupported>
    decision_impact: <what evidence is missing>
```

Never claim a full-web or all-platform investigation. A search-engine snippet may identify a lead but does not prove that a login-dependent post, full thread, or comments were read.

## Authorized login state

For Xiaohongshu, Reddit, X, and other login-dependent platforms:

- use only a session the user explicitly authorized and controls;
- do not obtain, inspect, export, copy, or persist browser cookies;
- do not ask tools to reveal tokens or credentials;
- do not log into an account for the user or bypass access controls;
- do not install system software or change system configuration without explicit user authorization;
- record an inaccessible platform as a coverage gap.

Never write Cookie, Token, credentials, payment privacy, or sensitive personal data to this repository.

## Temporary and durable data

Place raw command output, fetched pages, exports, and intermediate search results under `/tmp`. Treat them as temporary working material.

Persist only compact, auditable research records:

- original URL and title;
- publisher/platform and source type;
- publication date when available;
- access/check date;
- narrow claim and brief necessary excerpt or faithful paraphrase;
- the FACT/ASSUMPTION supported or contradicted;
- authority, verification, freshness, scope match, and direction;
- accessed channels and coverage gaps.

Do not persist whole HTML pages, full articles, long comment walls, or bulk result dumps. Respect platform terms, access controls, copyright, and quotation limits.

## Failure behavior

- If a backend fails, try an in-scope Runtime fallback and record the gap.
- If an official rule cannot be opened, do not promote a snippet or vendor interpretation to policy FACT.
- If a critical login-only channel is inaccessible, narrow the verdict or use `research_blocked` when the gap prevents the decision.
- If current research is still fresh and scope-matched, reuse it; do not run Agent Reach to display capability.

## Audit snapshot

On 2026-08-14, the locally inspected Agent Reach distribution reported version `v1.5.0`, the upstream repository [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach), and an MIT license. This is an audit snapshot, not a pinned dependency or a guarantee that the same version, backends, commands, authentication state, or platform coverage will exist at runtime. Always perform the dynamic availability and doctor checks above.
