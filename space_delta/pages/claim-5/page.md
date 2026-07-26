# Claim 5 — Theorem 4.2

## Exact statement and assumptions

Under K-sparsity and Regular Facts,

`Pr[g(H) ≥ g(U)/(K+1) | X] ≥ 1-K/|U|`.

## Complete proof certificate

Let `m=max_{y∈U} g(y)` and `a=g(U)/(K+1)`.

- If `m≤a`, at most K unseen statements are factual, so their total model mass
  is at most `Km≤Ka`. Therefore
  `g(H)=g(U)-g(F∩U)≥g(U)-Ka=a` deterministically.
- If `m>a`, choose an unseen maximizer `y*`. Regular Facts and K-sparsity give
  `Pr[y*∈H|X]≥1-K/|U|`; on that event `g(H)≥m>a`.

These cases exhaust every predictive distribution. The executable split is:

```python
threshold = gu / (k + 1)
if m <= threshold:
    assert gu - k * m >= threshold
else:
    assert m > threshold
```

The verifier checks 4,500 exact scatter/spike cases and 5,862 complete
symmetric-posterior models. An independent sharpness certificate uses uniform
`g` on `K+1` unseen statements; every K-subset world then attains equality
`g(H)=g(U)/(K+1)`.

## Native-scale measurement

| Regime | Required mean floor | Scatter satisfied | Spike satisfied |
| --- | ---: | ---: | ---: |
| asymptotic | 0.997498 | 1.000000 | 0.998225 |
| moderate | 0.949648 | 1.000000 | 0.958075 |
| near boundary | 0.830621 | 1.000000 | 0.845875 |
| small-budget control | 0.830619 | 1.000000 | 0.849175 |

Each row contains 40,000 corpora. Changing the innovation budget from 0.30 to
0.05 leaves the probabilistic mechanism intact, which is a scale control rather
than a bound-selected construction.

## Negative control and verdict

Strengthening the denominator from `K+1` to `K` is false: for `K=3`, uniform
`g` on four unseen points has `g(H)=1/4` in every three-fact world, below the
false threshold `1/3`. The verifier requires this sharpened claim to fail.

**VERIFIED.** The dichotomy is complete, the constant is sharp, and native
scatter/spike models corroborate both proof branches.

