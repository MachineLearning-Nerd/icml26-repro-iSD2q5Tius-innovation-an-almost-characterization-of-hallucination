# Claim 4 — Theorem 4.1

## Exact statement and assumptions

Under K-sparsity and Regular Facts, for every strict
`δ∈(K/|U|,1)`,

`Pr[g(H) ≥ g(U)(1-K/(δ|U|)) | X] ≥ 1-δ`.

The strict interval is load-bearing: it makes the displayed rate factor
positive. The historical baseline used the excluded endpoint and obtained a
vacuous zero bound.

## Complete proof certificate

Let `Z=g(F∩U)`, so `g(H)=g(U)-Z`. Under Regular Facts, every unseen statement
has factual probability `q`, and K-sparsity yields `q≤K/|U|`. Consequently

`E[Z|X] = q g(U) ≤ K g(U)/|U|`.

Markov's inequality gives
`Pr[Z > K g(U)/(δ|U|) | X] ≤ δ`. On the complementary event,
`g(H)≥g(U)(1-K/(δ|U|))`, proving the claim.

The verifier checks the exact substitution and the strict domain:

```python
delta = Fraction(d_num, 12)
if not Fraction(k, u) < delta < 1:
    continue
t = 1 - Fraction(k, 1) / (delta * u)
assert 0 < t < 1
lower = (1 - Fraction(k, u) - t) / (1 - t)
assert lower == 1 - delta
```

There are 2,359 exact substitutions plus 4,508 complete symmetric-posterior
models; every tested factor is non-vacuous.

## Native-scale measurement

Scatter satisfied the inequality in 100% of every admissible regime/δ pair.
Spike frequencies were 0.998225, 0.958075, 0.845875, and 0.849175. For
`δ=0.30`, these all exceeded the required 0.70; for `δ=0.15`, only the
asymptotic and moderate regimes were admissible and both exceeded 0.85.
Near-boundary `δ=0.15` was explicitly excluded because no trial satisfied
`δ>K/|U|`. Every exact conditional probability margin was strictly positive.

Download the [claim contract](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_4/claim_contract.json),
[raw results](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_4/raw_results.json),
[independent checker output](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_4/independent_checker_output.json),
and [negative-control output](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_4/negative_control_output.json).

## Negative control and verdict

Removing Regular Facts and concentrating the posterior on the model's spike
gives event probability 0 against required 9/10. The control fails as intended.

**VERIFIED.** The Markov derivation proves the quantified result, while both
exact finite enumeration and native-scale runs exercise only admissible,
strictly positive bounds.
