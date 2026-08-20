# Innovation vs. hallucination — claim-by-claim reproduction

## Collection classification and audit boundary

This repository is a **legacy/source workspace** for *Innovation: An Almost Characterization of Hallucination*
(arXiv `2605.26808`, OpenReview `iSD2q5Tius`). It is preserved
separately from the standardized canonical record at
[`icml26-innovation-hallucination`](https://github.com/MachineLearning-Nerd/icml26-innovation-hallucination).

The claim results and scores recorded below are historical results of this
workspace. They are not new paper-level verifications performed while
organizing the collection. The collection audit did not run the scientific
implementation; the canonical record documents its own scoped status and
limitations.

### How the historical claim evidence is produced

The claim table and experiment log below are the authoritative mapping from
each paper claim to its producer, command, control, and evidence artifact. In
this workspace, the six claim modules and native-proof/checker routes produce claim-specific evidence pages and raw artifacts, with the claim table below connecting each verdict to its producer.

The former `orx/*` branches are historical workstreams, not additional final
publication claims. Their purposes and tips are preserved in
[`BRANCH_AUDIT.md`](BRANCH_AUDIT.md). Citation and author acknowledgment
details are in [`CITATION.cff`](CITATION.cff) and
[`AUTHOR_THANK_YOU.md`](AUTHOR_THANK_YOU.md).

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-iSD2q5Tius-innovation-an-almost-characterization-of-hallucination/blob/main/notebooks/innovation_claims.py)

We reproduced the six theoretical claims selected by the live judge from
[*Innovation: An Almost Characterization of Hallucination*](https://arxiv.org/abs/2605.26808).
The original Space received **4/12**; after the first evidence release, the
live judge recorded **6/12**. The cumulative native-proof release is now judged
**12/12 (six VERIFIED claims, quality HIGH)** at Space revision
[`1454c59e`](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/commit/1454c59e31063fb5bec1d97886836ab66e59daa3).

The main correction is conceptual: Theorem 3.3 bounds
`Pr[g(H)>0 | X]`, not the numerical hallucination mass `g(H)`. We rebuilt every
claim as an exact contract, checked its symbolic derivation, exhaustively
corroborated a declared finite domain, and required an assumption-sensitive
control to fail. We then sampled **160,000 corpora** across four regimes up to
`|Ω|=20,000`. The strongest cumulative verifier took **20.116 seconds** on
Hugging Face `cpu-upgrade` with a one-thread process; no GPU was used.

- [Illustrated technical report](reports/claim-by-claim/report.md)
- [Self-contained Marimo tutorial](notebooks/innovation_claims.py)
- [Canonical candidate scorecard](space_delta/pages/00-scorecard/page.md)
- [Published logbook](https://huggingface.co/spaces/DineshAI/iSD2q5Tius)
- [Challenge leaderboard](https://icml-2026-agent-repro-challenge.static.hf.space/leaderboard.html)
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

Native headline measurements for the spike model were 0.998225, 0.958075,
and 0.845875 against theorem floors 0.997498, 0.949648, and 0.830621.
Scatter satisfied Claims 4–5 pointwise in every native trial; exact calibrated
identity checks passed 160,000/160,000 times; Claim 6 exercised nonzero exact TV
in 320,000 model evaluations.

## Experiment log

`main` was not run as an experiment (publication surface).

| Branch / experiment | Purpose | Exact run command | Assessment / outcome | Compute |
| --- | --- | --- | --- | --- |
| [`orx/historical-judged-baseline-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-iSD2q5Tius-innovation-an-almost-characterization-of-hallucination/tree/orx/historical-judged-baseline-audit) | Freeze judged SHA and criticisms | `uv run --frozen python -m repro_campaign.run` | Historical rejected baseline; 6 BLOCKED | local CPU, 1-core budget, 5s |
| [`orx/claim-1-exact-set-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-iSD2q5Tius-innovation-an-almost-characterization-of-hallucination/tree/orx/claim-1-exact-set-certificate) | Exact Claim 1 certificate | `uv run --frozen python -m repro_campaign.run` | Claim 1 VERIFIED | local CPU, 1-core budget, 10s |
| [`orx/claim-1-evaluator-visible-package`](https://github.com/MachineLearning-Nerd/icml26-repro-iSD2q5Tius-innovation-an-almost-characterization-of-hallucination/tree/orx/claim-1-evaluator-visible-package) | Raw-fixture and navigation regression | `uv run --frozen python -m repro_campaign.run` | Claim 1 fixture regenerated | local CPU, 1-core budget, 10s |
| [`orx/exact-certificates-for-claims-2-through-6`](https://github.com/MachineLearning-Nerd/icml26-repro-iSD2q5Tius-innovation-an-almost-characterization-of-hallucination/tree/orx/exact-certificates-for-claims-2-through-6) | Cumulative exact proof audits | `uv run --frozen python -m repro_campaign.run` | Claims 1–6 VERIFIED | local CPU, 1-core budget, 10s |
| [`orx/evaluator-visible-release-candidate`](https://github.com/MachineLearning-Nerd/icml26-repro-iSD2q5Tius-innovation-an-almost-characterization-of-hallucination/tree/orx/evaluator-visible-release-candidate) | Release gates and publication surface | `uv run --frozen python -m repro_campaign.run` | Claims 1–6 plus release gates VERIFIED | local CPU, 1-core budget |
| [`orx/native-scale-inline-proof-release`](https://github.com/MachineLearning-Nerd/icml26-repro-iSD2q5Tius-innovation-an-almost-characterization-of-hallucination/tree/orx/native-scale-inline-proof-release) | 160,000-corpus native corroboration | `uv run --frozen python -m repro_campaign.run` | Claims 1–6 VERIFIED; native audit PASS | HF `cpu-upgrade`, 1 thread, 37s wall |
| [`orx/judge-readable-native-proof-package`](https://github.com/MachineLearning-Nerd/icml26-repro-iSD2q5Tius-innovation-an-almost-characterization-of-hallucination/tree/orx/judge-readable-native-proof-package) | Inline proofs, code, numbers, controls | `uv run --frozen python -m repro_campaign.run` | 6 canonical pages and 89 release gates PASS | HF `cpu-upgrade`, 1 thread, 37s wall |
| [`orx/final-native-proof-release-gates`](https://github.com/MachineLearning-Nerd/icml26-repro-iSD2q5Tius-innovation-an-almost-characterization-of-hallucination/tree/orx/final-native-proof-release-gates) | Final blind traversal and release regression | `uv run --frozen python -m repro_campaign.run` | Published revision judged 12/12, quality HIGH | HF `cpu-upgrade`, 1 thread, 37s wall |

## Reproduce

```bash
uv sync --frozen
uv run --frozen python -m repro_campaign.run
uv run --frozen marimo check notebooks/innovation_claims.py
```

Historical Space evidence at
`DineshAI/iSD2q5Tius@33ec740847185e0222abba902a35182e01a96015`
is preserved and labeled **Historical rejected baseline**.
