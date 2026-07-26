# Current verification

## Claim 1 contract: hallucination implies innovation

Verdict: **VERIFIED**.

The exact source statement is: for every valid finite statement universe,
corpus-generated observed set, true support, and predictive distribution,
`g(H)>0` implies `g(U)>0`. The source anchors are Definition 3.1 and Observation
3.2 in arXiv:2605.26808v1.

The current verifier replaces the historical circular `FactModel` assignment
with a generic set-inclusion certificate, a declared complete finite-domain
sweep, an independent bit-mask checker, and an assumption-violating negative
control.

### Assumption audit

The corpus is sampled from the true distribution, so every observed statement
is factual: `O subseteq F`. Consequently,
`H = Omega\F subseteq Omega\O = U`. For every probability distribution `g`,
measure monotonicity gives `g(H) <= g(U)`, hence `g(H)>0 -> g(U)>0`.
K-sparsity, Regular Facts, calibration, and a neural architecture are not
assumptions of Observation 3.2.

### Raw result

| Check | Exact result |
| --- | ---: |
| Complete rational models (`1 <= |Omega| <= 8`, denominator 4) | 2,736,552 |
| Positive-hallucination cases | 1,844,256 |
| Counterexamples | 0 |
| Independent set relations | 3,279 |
| Independent point-mass bases | 21,324 |
| Negative control after removing `O subseteq F` | `g(H)=1`, `g(U)=0` (expected failure) |

Evidence-producing run: `b965e058-dca8-4e8d-82ff-fcc01a75eb06`.
Git SHA: `4bc947424e0e591a06d91d886f514dd158101b08`.
Fixed command: `uv run --frozen python -m repro_campaign.run`.
Pinned environment: Python 3.13.7 from `uv.lock` (Marimo 0.23.15).
Compute estimate/selection: one core, supervised local CPU; process budget one,
eight logical CPUs visible. Runtime: 10 seconds OpenResearch duration,
4.105397 seconds verifier runtime. No stochastic seeds or intervals apply.

Downloads:
[claim contract](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/evidence/claim_1/claim_contract.json),
[primary verifier](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/evidence/claim_1/verifier.py),
[raw JSON](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/evidence/claim_1/raw_results.json),
[independent checker output](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/evidence/claim_1/independent_checker_output.json),
and
[negative-control output](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/evidence/claim_1/negative_control_output.json).

Limitations: the finite sweep is scoped corroboration. Universal force comes
from the generic elementwise set certificate and measure monotonicity, not
extrapolation. The paper defines a Language Model as an abstract map to a
distribution, so substituting a particular neural model would test a narrower,
different claim.

Historical pages remain preserved and will be labeled **Historical rejected
baseline** in the candidate navigation.

