# Judge-readable scorecard — six exact contracts

**Live score before this candidate: 6/12.** That is the judge result for Space
revision `d97b9033c6272a5a315afb3fe6ceccbe2c5a43d8`, judged
2026-07-26T12:34:04Z. The table below is a scientific evidence assessment and
a score forecast, not a new judge result.

Paper source: arXiv:2605.26808v1, retrieved 2026-07-26, SHA-256
`62a56be95a07594b408b3f3f263d39d72259def46969e4df1c7c0bfcdba0bb49`.
Fixed command: `uv run --frozen python -m repro_campaign.run`.

| Claim | Exact contract | Proof certificate | Native-scale corroboration | Control | Evidence status |
| --- | --- | --- | --- | --- | --- |
| 1, Obs. 3.2 | `g(H)>0 => g(U)>0` | `O⊆F => H⊆U => g(H)≤g(U)` | 160,000/160,000 structural checks | remove `O⊆F`: `g(H)=1,g(U)=0` | **VERIFIED** |
| 2, Thm. 3.3 | `Pr[g(H)>0|X]≥1-K/|U|` under K-sparsity and Regular Facts | `q|U|=E|F∩U|≤K`; spike on any positive-mass unseen point | spike rates 0.998225/0.958075/0.845875 vs floors 0.997498/0.949648/0.830621 | non-Regular posterior gives 0 vs 0.99 | **VERIFIED** |
| 3, Prop. 3.4 | exact calibration and `p(U)>0 => g(U)>0` | positive unseen witness has a positive-mass partition cell | `g(U)=p(U)` exactly in 160,000 canonical calibrated runs | remove calibration: `p(U)=1/2,g(U)=0` | **VERIFIED** |
| 4, Thm. 4.1 | for every `δ∈(K/|U|,1)`, probability at least `1-δ` of the stated rate bound | Markov applied to unseen factual mass | every admissible regime/δ passed; every factor strictly positive | remove Regular Facts: 0 vs required 0.9 | **VERIFIED** |
| 5, Thm. 4.2 | probability at least `1-K/|U|` that `g(H)≥g(U)/(K+1)` | exhaustive scatter/spike dichotomy | scatter 1.0; spike 0.998225/0.958075/0.845875 | false denominator `K` fails sharply | **VERIFIED** |
| 6, Prop. 4.3 | for every partition `Π`, `g(U)≥p(U)/(K+1)-TV(g,p^Π)` | cellwise coarsening lemma plus TV event inequality | 480,000 model evaluations; nonzero TV exercised in 320,000 | remove K-sparsity: `1/5<1/4` | **VERIFIED** |

The native run used four deterministic seeds, 40,000 corpora per regime,
`N∈{300,2000,20000}`, `K∈{50,100}`, and scatter, spike, and calibrated model
families. The exact proof certificates—not Monte Carlo extrapolation—establish
the universal quantifiers.

Formal native run: `52ea83c1-e3c6-4452-9381-4e2a0864f88a`, Git
`7e40a42329bbb30590625f8f2b60d33550493dea`, Hugging Face `cpu-upgrade`,
one-core estimate and one-thread process, 64 logical CPUs visible, 6.414696 s
native simulation and 20.161143 s cumulative verifier. Raw native JSON:
[download](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/native_scale/raw_results.json).

