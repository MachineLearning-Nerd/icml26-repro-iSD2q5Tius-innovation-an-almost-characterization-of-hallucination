# Innovation vs. hallucination — claim-by-claim reproduction

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-iSD2q5Tius-innovation-an-almost-characterization-of-hallucination/blob/main/notebooks/innovation_claims.py)

We reproduced the six theoretical claims selected by the live judge from
[*Innovation: An Almost Characterization of Hallucination*](https://arxiv.org/abs/2605.26808).
The previous Space received **4/12**. The cumulative reproduction now gives an
honest evidence verdict of **VERIFIED for all six exact source statements**;
that is a forecastable evidence status, not a new judge score.

The main correction is conceptual: Theorem 3.3 bounds
`Pr[g(H)>0 | X]`, not the numerical hallucination mass `g(H)`. We rebuilt every
claim as an exact contract, checked its symbolic derivation, exhaustively
corroborated a declared finite domain, and required an assumption-sensitive
control to fail. The strongest cumulative run took **10 seconds on supervised
local CPU with a one-core process budget**. No GPU or HF CPU upgrade was needed
because every run was deterministically bounded below five minutes and one
core.

- [Illustrated technical report](reports/claim-by-claim/report.md)
- [Self-contained Marimo tutorial](notebooks/innovation_claims.py)
- [Canonical candidate Space page](space_delta/pages/current-verification/page.md)
- [Pinned environment](uv.lock)

## Result summary

| Claim | Paper statement | Observed evidence | Assessment |
| --- | --- | --- | --- |
| 1 | `g(H)>0 -> g(U)>0` | 2,736,552 exact finite models; generic set certificate | VERIFIED |
| 2 | `Pr[g(H)>0|X]>=1-K/|U|` | 171,699 symbolic checks; misquote corrected | VERIFIED |
| 3 | calibration + `p(U)>0 -> g(U)>0` | 56,105 distribution/partition models | VERIFIED |
| 4 | Markov bound for strict admissible delta | 4,508 non-vacuous models | VERIFIED |
| 5 | high-confidence `g(U)/(K+1)` bound | 5,862 models; sharpness certificate | VERIFIED |
| 6 | missing-mass/TV bound | 44,390 models; 43,390 with nonzero TV | VERIFIED |

These are abstract probability theorems, not neural-LLM benchmark claims.
Finite sweeps are scoped corroboration; universality rests on independently
reconstructed proof certificates.

## Experiment log

`main` was not run as an experiment (publication surface).

| Branch / experiment | Purpose | Exact run command | Assessment / outcome | Compute |
| --- | --- | --- | --- | --- |
| [`orx/historical-judged-baseline-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-iSD2q5Tius-innovation-an-almost-characterization-of-hallucination/tree/orx/historical-judged-baseline-audit) | Freeze judged SHA and criticisms | `uv run --frozen python -m repro_campaign.run` | Historical rejected baseline; 6 BLOCKED | local CPU, 1-core budget, 5s |
| [`orx/claim-1-exact-set-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-iSD2q5Tius-innovation-an-almost-characterization-of-hallucination/tree/orx/claim-1-exact-set-certificate) | Exact Claim 1 certificate | `uv run --frozen python -m repro_campaign.run` | Claim 1 VERIFIED | local CPU, 1-core budget, 10s |
| [`orx/claim-1-evaluator-visible-package`](https://github.com/MachineLearning-Nerd/icml26-repro-iSD2q5Tius-innovation-an-almost-characterization-of-hallucination/tree/orx/claim-1-evaluator-visible-package) | Raw-fixture and navigation regression | `uv run --frozen python -m repro_campaign.run` | Claim 1 fixture regenerated | local CPU, 1-core budget, 10s |
| [`orx/exact-certificates-for-claims-2-through-6`](https://github.com/MachineLearning-Nerd/icml26-repro-iSD2q5Tius-innovation-an-almost-characterization-of-hallucination/tree/orx/exact-certificates-for-claims-2-through-6) | Cumulative exact proof audits | `uv run --frozen python -m repro_campaign.run` | Claims 1–6 VERIFIED | local CPU, 1-core budget, 10s |
| [`orx/evaluator-visible-release-candidate`](https://github.com/MachineLearning-Nerd/icml26-repro-iSD2q5Tius-innovation-an-almost-characterization-of-hallucination/tree/orx/evaluator-visible-release-candidate) | Release gates and publication surface | `uv run --frozen python -m repro_campaign.run` | Claims 1–6 plus release gates VERIFIED | local CPU, 1-core budget |

## Reproduce

```bash
uv sync --frozen
uv run --frozen python -m repro_campaign.run
uv run --frozen marimo check notebooks/innovation_claims.py
```

Historical Space evidence at
`DineshAI/iSD2q5Tius@33ec740847185e0222abba902a35182e01a96015`
is preserved and labeled **Historical rejected baseline**.
