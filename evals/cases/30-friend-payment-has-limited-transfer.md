# 30 — Friend payment has limited transfer

## Preconditions

- The first and only 300 CNY payment is real and delivery occurred; a redacted
  provider record supplies the amount, currency, paid date, payer/customer
  labels, completion status, and payment evidence required for one `Txxx`.
- The payer is a close friend who wants to support the user; the experiment did
  not exclude relationship-biased buyers or establish ordinary purchase intent.
- No independent buyer has paid, and repeatability is unproven.

## User message

> 我朋友给了我 300 元买了一次服务，他也确实收到了交付。是不是已经证明陌生客户也会买？

## Expected observable behavior

- Runtime records the real payment as a `Txxx` transaction and linked FACT with
  honest relationship provenance; it does not erase it because the evidence is
  confounded.
- It states that one supported transaction can move the project to
  `transaction_validation` while providing weak or no evidence that independent
  buyers will purchase or that demand repeats.
- The offer experiment is `inconclusive` about independent-market demand unless
  the predeclared protocol made relationship bias a known invalidating defect;
  in that case `invalid` is acceptable. The result code does not erase the
  payment record.
- The next test keeps the result, price, and terms materially comparable but uses
  independently sourced, qualified buyers and predeclared exclusion rules.

## Failure conditions

- Calls the transaction fake, refuses to record it, or records it without the
  relationship provenance.
- Generalizes one friendship payment to independent demand, repeatability, or a
  viable business.
- Creates payment evidence only inside the experiment result instead of a linked
  transaction/FACT, or jumps to productization.
