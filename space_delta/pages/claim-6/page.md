# Claim 6 — Proposition 4.3

## Exact statement and assumptions

Under K-sparsity, for every partition `Π`—including a partition selected using
`X` and `p`—

`g(U) ≥ p(U)/(K+1) - ||g-p^Π||_TV`.

This claim quantifies over arbitrary predictive distributions `g`; exact
calibration is not assumed.

## Complete proof certificate

For a partition cell `B`, coarsening is uniform:
`p^Π(U∩B)=|U∩B|p(B)/|B|`. If `p(U∩B)=0`, the desired cell inequality is
trivial. Otherwise `|U∩B|≥1`, while
`|O∩B|≤|O|≤|F|≤K`. Hence
`|B|≤(K+1)|U∩B|`, and because `p(B)≥p(U∩B)`,

`p^Π(U∩B) ≥ p(U∩B)/(K+1)`.

Summing over cells gives `p^Π(U)≥p(U)/(K+1)`. Total variation controls every
event, so `||g-p^Π||_TV≥p^Π(U)-g(U)`. Rearrangement proves the claim.

The complete finite verifier executes the same two inequalities:

```python
p_pi = coarsen(p, pi)
assert mass(p_pi, unseen) >= mass(p, unseen) / (k + 1)
distance = tv(g, p_pi)
assert mass(g, unseen) >= mass(p, unseen) / (k + 1) - distance
```

It covers 44,390 complete models, 8,940 cell inequalities, every partition in
scope, and 43,390 models with nonzero TV.

## Native-scale measurement with exact TV

The canonical partition was evaluated for calibrated, scatter, and spike
families on 160,000 corpora: 480,000 model evaluations total. Scatter and spike
exercise nonzero TV in all 320,000 non-calibrated evaluations. Minimum slack
over all regimes was 0.588235 (calibrated), 0.588235 (scatter), and 0.888205
(spike). The implementation uses the exact cell-summed TV, not a proxy:

```python
scatter_tv = abs(budget - p_u)
spike_tv = 0.5 * (
    abs(p_u - budget) + abs(budget - p_u / unseen_size)
    + (unseen_size - 1) * p_u / unseen_size
)
```

Download the [claim contract](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_6/claim_contract.json),
[raw results](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_6/raw_results.json),
[independent checker output](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_6/independent_checker_output.json),
and [negative-control output](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_6/negative_control_output.json).

## Negative control and verdict

Removing K-sparsity with nominal `K=1`,
`p=(1/8,1/8,1/8,1/8,1/2)`, one all-universe partition, and
`U={4}` gives `g=p^Π` uniform, hence `g(U)=1/5<1/4=p(U)/(K+1)`.
The control is a strict assumption-satisfying failure of the intentionally
weakened premise.

**VERIFIED.** The cellwise proof covers every partition and every `g`; both
exact enumeration and native models materially exercise miscalibration.
