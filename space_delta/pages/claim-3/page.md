# Claim 3 — Proposition 3.4

## Exact statement and assumptions

For any true distribution `p`, corpus `X`, and partition `Π`, if the model is
exactly calibrated (`g=p^Π`) and the missing mass is positive (`p(U)>0`), then
`g(U)>0`.

## Complete proof certificate

Because `p(U)>0`, there is `y*∈U` with `p(y*)>0`. Let `B*` be its partition
cell. Then `p(B*)≥p(y*)>0`, so the coarsened distribution has
`g(y*)=p^Π(y*)=p(B*)/|B*|>0`. As `y*∈U`, `g(U)≥g(y*)>0`.

The verifier constructs every set partition and checks the implication:

```python
for pi in partitions(n):
    g = coarsen(p, pi)
    assert mass(g, unseen) > 0
    witness = next(i for i in unseen if p[i] > 0)
    block = next(block for block in pi if witness in block)
    assert mass(p, block) > 0 and g[witness] > 0
```

This exhausts all 56,105 denominator-three
distribution/observed-set/partition models through `|Ω|=6`; an independent
witness checker repeats all 56,105 checks.

## Native-scale measurement

For the canonical partition of observed singletons plus one `U` cell,
`p^Π(U)=p(U)` algebraically. The implementation rebuilt this calibrated model
on 160,000 corpora across four regimes and obtained
`|g(U)-p(U)|=0.0` in every run.

Download the [claim contract](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_3/claim_contract.json),
[raw results](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_3/raw_results.json),
[independent checker output](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_3/independent_checker_output.json),
and [negative-control output](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_3/negative_control_output.json).

## Negative control and verdict

With `p=(1/2,1/2)`, `O={0}`, and positive missing mass, removing exact
calibration permits `g=(1,0)` and `g(U)=0`. The control is therefore a strict
assumption-targeted failure.

**VERIFIED.** The witness proof handles every partition; the native canonical
construction is additional non-toy corroboration, not the universal argument.
