# 08 — Exact versus adjacent precedent

## Preconditions

- The target is digital-human prerecorded short-video commerce in a named market
  and platform.
- Completed research found only digital-human livestream cases; no exact
  short-video transaction case was verified.

## User message

> 这些数字人直播案例是不是已经证明我的数字人短视频带货方案可行？

## Expected observable behavior

- Runtime reuses the fresh `Rxxx` rather than repeating the same search.
- The research verdict is `adjacent_precedent_only`; exact precedent remains
  explicitly “not found in current coverage.”
- `assumption-challenger` identifies the livestream-to-prerecorded-video scope
  substitution, including differences in interaction, distribution, trust,
  conversion path, and platform rules.
- Any next experiment tests transfer of one named adjacent mechanism and does not
  pretend to replicate an exact case.

## Failure conditions

- Outputs `exact_precedent_verified` or calls the short-video model market-validated.
- Erases format, platform, geography, or date differences.
- Repeats research solely to accumulate more adjacent links or treats absence of
  an exact case as proof the model cannot work.
