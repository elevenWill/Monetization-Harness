# 10 — Refresh stale platform policy before publishing

## Preconditions

- The project links an old `Rxxx` policy finding for a named platform, region,
  and AI-generated short-video content type.
- The research is stale for the imminent publishing decision.

## User message

> 平台规则可能更新了，我准备下周开始发视频，按之前的规则做就行吗？

## Expected observable behavior

- The Market Reality Gate invokes `market-reality-researcher` before release advice.
- Runtime opens the current official platform rule or official rule center; a
  search snippet, vendor explanation, or old media summary is only a lead.
- The updated finding records platform, region, content type, official URL,
  published date when available, `checked_at`, and current status.
- Old policy evidence is retained as history and marked stale or superseded; any
  conflict is recorded rather than silently overwritten.
- Publishing advice reflects the current official finding and unresolved coverage gaps.

## Failure conditions

- Reuses stale policy because it already exists in the workspace.
- Gives current compliance advice from model memory, a search snippet, or vendor content.
- Deletes historical policy evidence or omits the checked date and scope.
