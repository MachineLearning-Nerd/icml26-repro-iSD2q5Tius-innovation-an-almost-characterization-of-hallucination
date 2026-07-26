# Claim 2 — Theorem 3.3

## Exact statement and assumptions

Under K-sparsity and Regular Facts, conditional on corpus `X`, if `g(U)>0`,

`Pr_p[g(H)>0 | X] ≥ 1-K/|U|`.

The right side bounds a posterior **event probability**; it is not a numerical
lower bound on the mass `g(H)`.

## Complete proof certificate

Regular Facts gives one conditional factual probability
`q=Pr[y∈F|X]` for every `y∈U`. K-sparsity gives

`|U|q = E[|F∩U| | X] ≤ K`, hence `q≤K/|U|`.

Since `g(U)>0`, choose an unseen `y*` with `g(y*)>0`. If `y*∈H`, then
`g(H)>0`; therefore

`Pr[g(H)>0|X] ≥ Pr[y*∈H|X] = 1-q ≥ 1-K/|U|`.

The exact-rational executable core is:

```python
for u in range(2, 101):
    for k in range(u):
        for q_num in range(k + 1):
            q = Fraction(q_num, u)
            assert 1 - q >= 1 - Fraction(k, u)
```

It performs 171,699 substitutions. An independent checker verifies 5,049
binomial identities
`C(u-1,k)/C(u,k)=1-k/u`. Full source:
[theorems.py](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/repro_campaign/theorems.py).

## Native-scale measurement

The spike model puts positive innovation mass on the first unseen statement.
Its observed hallucination frequency directly measures the theorem event.

| Regime `(N,K)` | Trials | Mean floor `1-K/|U|` | Spike frequency | 95% Wilson interval |
| --- | ---: | ---: | ---: | ---: |
| asymptotic `(20000,50)` | 40,000 | 0.997498 | 0.998225 | [0.997762, 0.998592] |
| moderate `(2000,100)` | 40,000 | 0.949648 | 0.958075 | [0.956067, 0.959995] |
| near boundary `(300,50)` | 40,000 | 0.830621 | 0.845875 | [0.842303, 0.849380] |

In every one of 160,000 corpora, the exact posterior
`q=(K-|O|)/|U|` satisfied `q≤K/|U|`. The paired empirical-minus-floor 95%
interval was strictly positive in all four regimes.

## Negative control and verdict

A K-sparse posterior concentrated on the model's unseen spike violates Regular
Facts and gives event probability 0 against a required 99/100. The control
fails for the intended missing assumption.

**VERIFIED.** The symbolic certificate covers every admissible model; the
native experiment independently corroborates its observable consequence.

