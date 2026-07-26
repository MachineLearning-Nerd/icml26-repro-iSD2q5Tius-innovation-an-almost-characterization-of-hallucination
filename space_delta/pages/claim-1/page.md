# Claim 1 — Observation 3.2

## Exact statement and assumptions

Let `O=set(X)`, `U=Ω\O`, `F=supp(p)`, and `H=Ω\F`. For every predictive
distribution `g`, `g(H)>0` implies `g(U)>0`. The data-generating framework gives
`O⊆F`; K-sparsity, Regular Facts, calibration, and a neural architecture are
not assumptions of this observation.

## Complete proof certificate

Taking complements in `O⊆F` gives `H=Ω\F⊆Ω\O=U`. Probability measures are
monotone, hence `g(H)≤g(U)`. Strict positivity of the left side forces strict
positivity of the right side. This is the entire universal argument.

The executable certificate checks every truth-table row satisfying the premise:

```python
for observed, factual in product((False, True), repeat=2):
    premise = (not observed) or factual       # O(y) -> F(y)
    conclusion = factual or (not observed)   # H(y) -> U(y)
    if premise and not conclusion:
        raise AssertionError("O subset F did not imply H subset U")
```

Full source: [claim1.py](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/repro_campaign/claim1.py).

## Independent and native evidence

- Complete rational sweep: 2,736,552 models for `1≤|Ω|≤8`, every valid `O⊆F`
  membership and every denominator-four probability vector; zero
  counterexamples and 1,844,256 positive-hallucination cases.
- Independent implementation: 3,279 bit-mask relations and 21,324 point-mass
  bases; zero counterexamples.
- Native scale: `O⊆F` and `H⊆U` in 160,000/160,000 corpora through
  `|Ω|=20,000`.

Download the [claim contract](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_1/claim_contract.json),
[raw results](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_1/raw_results.json),
[independent checker output](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_1/independent_checker_output.json),
and [negative-control output](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_1/negative_control_output.json).

## Negative control and verdict

Removing `O⊆F` permits `Ω=O={0}`, `F=∅`, and point-mass `g`, yielding
`g(H)=1` and `g(U)=0`; the verifier requires this control to fail.

**VERIFIED.** The finite runs are corroboration; the set-inclusion certificate
proves the universally quantified statement.
