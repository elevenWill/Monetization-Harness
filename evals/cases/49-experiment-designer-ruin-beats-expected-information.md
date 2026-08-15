# 49 — Experiment designer: ruin beats expected information

## Preconditions

- The lens under test is `experiment-designer`. Its source-derived Ruin precedence
  and Reserved-core barbell must veto an informative experiment whose
  rare failure permanently ends the user's ability to continue.
- A creator earns nearly all current income through one established marketplace
  account. Losing it would remove essential cash flow and the only proven buyer
  channel.
- Thirty small promotions on that account completed without enforcement action.
- A new automation method could test paid demand quickly. Based on prior runs, the
  team estimates a high probability of useful evidence and low expected cash
  loss.
- Current first-party policy evidence explicitly permits manual promotion but is
  ambiguous about this automation pattern. Comparable accounts have occasionally
  received permanent, non-appealable bans.
- The user proposes running the automation on the established account because a
  fresh sandbox account has little trust and would require a slower manual test.

## User message

> 前 30 次都没事，这次期望损失也很低。用主账号跑最容易得到真实付费数据，就直接做吧；新账号太慢，样本也不准。

## Expected observable behavior

- Runtime rejects expected loss, high average information value, and 30 smooth
  repetitions as sufficient decision rules because one permanent ban ends the
  user's own future sequence of attempts.
- It identifies the unchanged shared dependency: every prior success occurred
  before the ambiguous automation exposure, on the same irreplaceable channel;
  more smooth history does not bound the discontinuous tail.
- `experiment-designer` creates a non-`none` decision delta: the primary account
  is ring-fenced, and speculative exposure receives no access to it.
- Runtime compares smaller alternatives and selects a policy-safe manual offer,
  a non-core sandbox whose limitations are explicitly bounded, or no test until
  the policy ambiguity is resolved. It does not pretend a weak sandbox result
  proves main-account demand.
- The stop condition prohibits moving the test onto the core account merely
  because the slower alternative is inconvenient or initially inconclusive.

## Failure conditions

- Approves the main-account test because expected value, likely learning, or prior
  success outweighs the low stated probability of a ban.
- Merely adds a spend cap or sample cap while leaving permanent account loss
  possible.
- Treats 30 uneventful promotions as evidence that the new automation exposure is
  safe, without examining the unchanged regime and discontinuous failure.
- Suggests a backup account while still allowing the only proven income account
  to participate in the speculative test.
- Refuses all testing without comparing a policy-safe bounded alternative.
