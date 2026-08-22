# Market Search Capability Routing

Agent Reach and AnySearch are optional acquisition capabilities for Market
Reality Research. Neither is the research method, an evidence-quality label, or
a source to cite. The `market-reality-researcher` owns question decomposition,
claim-to-source fit, contradiction search, exact-versus-adjacent classification,
case reconstruction, and transferability. Cite the original page or platform
item that was opened and checked, never the acquisition capability.

## Route by evidence surface

Choose the minimum capable route for the claim. Do not call both capabilities
ceremonially or treat one as a universal primary and the other as a fallback.

| Evidence need | Default capability | Why / boundary |
| --- | --- | --- |
| Login-dependent or platform-native posts, comments, feeds, profiles, subtitles, and community behavior on supported platforms | **Agent Reach** | It can use platform-specific CLIs, APIs, or an authorized user-controlled browser session. Search-engine snippets cannot substitute for reading the item or comments. |
| GitHub repositories, issues, PRs, commits, and code context | **Agent Reach** | Prefer `gh` or the active code-search backend for repository-native fields and history. |
| Broad current Web discovery, news, official pages, public cases, competitors, or several independent queries | **AnySearch** | Use general search or `batch_search`; it is suited to real-time public-Web discovery and parallel query families. |
| Finance, academic, health, legal, security, code, business, social-media, or another supported structured domain | **AnySearch vertical** | Run `get_sub_domains` first, then supply every required parameter. Vertical results are leads until the original source is opened. |
| A known public HTML, JSON, text, or Markdown URL | **AnySearch `extract`** | Use for full-page extraction when supported. It does not handle PDF, DOC/DOCX, images, audio/video, archives, or streaming media; use the relevant Runtime reader instead. |
| RSS, video/audio transcripts, or a platform item whose metadata/comments matter | **Agent Reach** | Use the channel-native reader or transcript path rather than flattening the item into generic Web text. |
| Policy plus observed enforcement/acceptance | **Combine** | AnySearch can discover and open the current official rule; Agent Reach can inspect relevant platform-native behavior or enforcement reports. Keep policy and behavior claims separate. |
| Transaction-bearing playbook or multi-platform acceptance study | **Combine when roles are independent** | Use AnySearch for broad transaction surfaces, official sources, prices, and public cases; use Agent Reach for platform-native offers, operator continuity, comments, and community behavior. Partition query families instead of duplicating every query. |

AnySearch's `social_media` or other vertical search can discover public indexed
leads, but it does not prove that a login-dependent post, full thread, or comment
set was read. Agent Reach platform data can expose behavior, but it does not
replace broad Web, official, structured-domain, or cross-publisher coverage.

## Dynamic selection

When current external evidence is decision-critical:

1. Reuse fresh, scope-matched research when it already answers the claim.
2. Name the claim and the evidence surface qualified to answer it.
3. If the surface is Agent Reach-native, check whether `agent-reach` is available,
   run `agent-reach doctor --json`, and use only the reported active backend.
4. If the surface is AnySearch-suitable, use its configured runtime directly.
   For a vertical or overlapping domain, run `get_sub_domains` before search and
   provide every required parameter. Use hybrid `batch_search` when the query
   genuinely spans general Web and structured vertical intents.
5. Use one capability when it can answer the claim with adequate coverage. Use
   both only when they cover independent evidence roles, a decision-critical
   corroboration gap, or public-Web discovery followed by platform-native
   verification.
6. Open the original sources, record their source lineage, and do not double-count the
   same press release or syndicated claim returned by two capabilities.

Record the actual acquisition path in the existing query log:

```text
query text; date run; capability; channel/backend; scope intent;
useful source IDs; result limitation or coverage gap
```

Capability choice affects access and coverage, not `authority`, `verification`,
`freshness`, `scope_match`, or `direction`.

## Combination patterns

- **Official policy:** AnySearch general/vertical search -> open the current
  official page -> Agent Reach only if platform-native enforcement or user
  behavior is a separate material claim.
- **User acceptance:** AnySearch maps public actors and reports -> Agent Reach
  reads claim-relevant posts/comments on the target platform -> preserve sample
  and login coverage limits.
- **Closest Proven Playbook:** AnySearch finds buyer briefs, price pages,
  procurement, reporting, and operator cases -> Agent Reach verifies repository,
  social, video, or community traces needed to reconstruct acquisition,
  delivery, acceptance, continuation, or failure.
- **Negative evidence:** split failure queries across broad Web/reporting and the
  platform-native communities where complaints, abandonment, refunds, or
  enforcement are observable; do not equate two retrieval paths with two
  independent evidence lineages.

## Unavailable or partial coverage

- If Agent Reach is unavailable, continue with AnySearch and other Runtime
  Web/page/browser tools for public indexed evidence. Preserve login-only posts,
  comments, feeds, and platform metadata as coverage gaps.
- If AnySearch is unavailable, continue with Agent Reach for supported surfaces
  and its available Web/code/readers. Preserve unsupported structured-domain,
  broad-Web, or extraction coverage as gaps rather than issuing invented
  AnySearch commands.
- If both are unavailable or blocked, use available Runtime Web Search, page
  reading, PDF/document readers, or authorized browser access.
- If a decision-critical surface remains inaccessible, narrow the verdict or use
  `research_blocked`; capability failure must not be disguised as negative market
  evidence.

Never claim a full-Web or all-platform investigation. A provider outage, quota
limit, authentication failure, unsupported file type, or unvisited relevant
channel belongs in `coverage_gaps` with its decision impact.

## Authorization, privacy, and credentials

For login-dependent platforms, use only a session the user explicitly authorized
and controls. Do not obtain, inspect, export, copy, or persist browser cookies;
log in for the user; bypass access controls; install system software; or change
system configuration without explicit authority.

AnySearch sends search queries, extracted URLs, and any configured API key to its
service. Do not send passwords, personal data, trade secrets, private project
facts, or other sensitive material. Anonymous access may be used when available.
Never save a newly issued key without explicit user approval, and never write
Cookie, Token, credentials, payment privacy, or sensitive personal data to this
repository.

## Temporary and durable data

Place raw command output, fetched pages, exports, and intermediate search results
under `/tmp`. Persist only compact source metadata, narrow claims, necessary
excerpts or faithful paraphrases, evidence classifications, actual access paths,
and coverage gaps. Do not persist whole HTML pages, full articles, long comment
walls, or bulk result dumps.

## Audit snapshot

On 2026-08-22, local inspection found Agent Reach with active platform-specific
backends reported dynamically by `agent-reach doctor --json`, and AnySearch Skill
version `3.1.0` with a configured Python CLI. These are audit snapshots, not
pinned dependencies or guarantees about future availability, authentication,
commands, supported domains, quotas, or backend behavior. Always select from the
capabilities actually available at runtime.
