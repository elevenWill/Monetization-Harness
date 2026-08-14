# Adjacent Case Trap

## Scenario

The user proposes AI-avatar recorded short-video commerce on a target platform in China. Research finds credible digital-human livestream commerce on another platform and human-presented short-video commerce on the target platform, but no exact AI-avatar recorded short-video transaction case.

## Correct classification

```yaml
livestream_case:
  scope_match: adjacent
  verification_status: adjacent_verified
  mismatch:
    - content format
    - interaction and retention mechanism
    - traffic entry point
human_short_video_case:
  scope_match: adjacent
  verification_status: adjacent_verified
  mismatch:
    - presenter and trust mechanism
research_verdict: adjacent_precedent_only
```

Do not merge two adjacent cases into one exact precedent. Each proves only its own scoped claim.

## Required response

```text
Exact Proven Playbook:
未找到

Closest Adjacent Playbook:
<the transaction structure supported by the strongest adjacent case>

关键差异:
<the unverified bridge from livestream to recorded video, or human trust to disclosed AI presenter>
```

State what adjacent evidence does support—for example, that merchants pay for a digital-human livestream service or that short-form product demonstrations can acquire transactions. Keep the combined proposition as an ASSUMPTION.

## Next evidence

Design a bounded experiment that isolates the unverified bridge. Preserve the proven product, channel, offer, and checkout where possible; change only the presenter/content mechanism. Compare actual high-intent or payment behavior and predeclare stop conditions.

## Failure mode

Incorrect:

> Both halves work elsewhere, so the combined mode is market-validated.

Correct:

> Adjacent mechanisms exist, but the exact combination lacks a verified precedent in current coverage.
