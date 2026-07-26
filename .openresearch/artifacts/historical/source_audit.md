# Source audit

- Paper: *Innovation: An Almost Characterization of Hallucination*
- arXiv: `2605.26808v1`
- Retrieved URL: `https://ar5iv.labs.arxiv.org/html/2605.26808`
- Retrieval date: `2026-07-26` (Asia/Kolkata)
- User-Agent: `OpenResearch-Reproduction/1.0 (claim audit; contact via repository)`
- SHA-256: `62a56be95a07594b408b3f3f263d39d72259def46969e4df1c7c0bfcdba0bb49`
- Retrieved bytes: `357117`
- Official empirical repository commit inspected:
  `9a6c7a2dcca668055b8ec152344ea1d85d121896`
- Official repository Python requirement: `>=3.13`

## Exact anchors and quantifiers

The relevant HTML anchors are `#S2.Thmtheorem3` (K-sparsity),
`#S2.Thmtheorem4` (Regular Facts), `#S3.Thmtheorem1` (Definition 3.1),
`#S3.Thmtheorem2` (Observation 3.2), `#S3.Thmtheorem3` (Theorem 3.3),
`#S3.Thmtheorem4` (Proposition 3.4), `#S4.Thmtheorem1` (Theorem 4.1),
`#S4.Thmtheorem2` (Theorem 4.2), and `#S4.Thmtheorem3`
(Proposition 4.3).

Theorem 3.3 states
`Pr_{p~D_world}[g(H)>0 | X] >= 1-K/|U|` when `g(U)>0`; it does **not**
state `g(H) >= 1-K/|U|`. The imported judge claim paraphrase conflates a
posterior probability with a hallucination-mass lower bound. Current work must
test the exact source theorem while explaining this mismatch.

Theorem 4.1 quantifies over every `delta in (K/|U|,1)` and bounds the
posterior probability of
`g(H) >= g(U)(1-K/(delta|U|))` by at least `1-delta`.
The strict lower endpoint is necessary for a positive, non-vacuous factor.

Theorem 4.2 bounds the posterior probability of
`g(H) >= g(U)/(K+1)` by at least `1-K/|U|`.

Proposition 4.3 quantifies over every partition `Pi`, including partitions
chosen as a function of the corpus and true distribution, and states
`g(U) >= p(U)/(K+1) - ||g-p^Pi||_TV`.

