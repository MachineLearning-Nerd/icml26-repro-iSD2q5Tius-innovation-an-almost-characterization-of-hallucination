# Prior exact-certificate summary

This summary has been superseded by the current
[judge-readable scorecard](#/00-scorecard) and six inlined claim pages. It
remains current scientific evidence—not a historical rejected verifier—but the
new pages are the canonical review path because they expose the proof and code
directly. The live score before the new candidate is **6/12**.

Source: arXiv:2605.26808v1, retrieved 2026-07-26 with SHA-256
`62a56be95a07594b408b3f3f263d39d72259def46969e4df1c7c0bfcdba0bb49`.
Current cumulative evidence run: `f01d14d8-9c3d-4888-b80f-b6615509d55f`;
Git SHA `ab5399c447df51aaca30462132faad7e7ae83d04`.
Fixed command: `uv run --frozen python -m repro_campaign.run`.
Pinned environment: Python 3.13.7 and Marimo 0.23.15 from `uv.lock`.
Compute: estimated one core, supervised local CPU, process budget one, eight
logical CPUs visible; 10 seconds wall time and 7.837742 seconds verifier time.
The checks are deterministic; seeds and sampling intervals do not apply.

## Claim 1 — Observation 3.2

Exact statement: `g(H)>0 -> g(U)>0`. Because corpus statements are sampled from
the true distribution, `O subseteq F`; therefore `H subseteq U` and
`g(H)<=g(U)`.

- Primary evidence: generic elementwise certificate plus 2,736,552 complete
  denominator-four models (`1<=|Omega|<=8`), zero counterexamples.
- Independent checker: 3,279 bit-mask relations and 21,324 point-mass bases.
- Control: removing `O subseteq F` gives `g(H)=1`, `g(U)=0`, the intended fail.

## Claim 2 — Theorem 3.3

Exact statement: under K-sparsity and Regular Facts, if `g(U)>0`, then
`Pr[g(H)>0 | X] >= 1-K/|U|`.

Important correction: `1-K/|U|` bounds the posterior probability of the event
`g(H)>0`; it is not a lower bound on the numerical mass `g(H)`. The historical
assessment conflated these two quantities.

- Primary evidence: 171,699 exact `q<=K/|U|` symbolic checks and 3,662 complete
  symmetric-posterior models; 734 attained the worst-case equality.
- Independent checker: 5,049 binomial identities
  `C(u-1,K)/C(u,K)=1-K/u`.
- Control: a K-sparse but non-Regular posterior yields event probability 0
  against required `99/100`, the intended fail.

## Claim 3 — Proposition 3.4

Exact statement: exact partition calibration `g=p^Pi` and `p(U)>0` imply
`g(U)>0`. A positive unseen `p`-mass provides a witness whose partition cell,
and hence coarsened point mass, is positive.

- Primary evidence: all 56,105 denominator-three
  distribution/observed-set/partition models through `|Omega|=6`.
- Independent checker: 56,105 explicit unseen-witness and cell checks.
- Control: keeping `p(U)=1/2` but removing calibration allows `g(U)=0`.

## Claim 4 — Theorem 4.1

Exact statement: for every strict `delta in (K/|U|,1)`,
`Pr[g(H)>=g(U)(1-K/(delta|U|)) | X] >= 1-delta`.

- Primary evidence: 2,359 exact expectation-bound substitutions and 4,508
  complete symmetric-posterior models.
- Non-vacuity: every tested factor was strictly positive. The rejected baseline
  used the excluded endpoint `delta=K/|U|`, making its factor zero.
- Control: removing Regular Facts gives event probability 0 against required
  `9/10`.

## Claim 5 — Theorem 4.2

Exact statement:
`Pr[g(H)>=g(U)/(K+1) | X] >= 1-K/|U|`.

- Primary evidence: 4,500 exact scatter/spike cases and 5,862 complete
  symmetric-posterior models.
- Independent sharpness certificate: uniform `g` on `K+1` unseen statements
  attains `g(H)=g(U)/(K+1)` in every uniform K-subset world.
- Control: strengthening the denominator from `K+1` to `K` makes the event
  probability 0 against required `1/4`.

## Claim 6 — Proposition 4.3

Exact statement: for every partition Pi,
`g(U)>=p(U)/(K+1)-||g-p^Pi||_TV`.

- Primary evidence: 44,390 complete finite models, 8,940 cell inequalities,
  and 43,390 models with nonzero TV miscalibration.
- Independent checker: cellwise coarsening
  `p^Pi(U)>=p(U)/(K+1)` plus TV variational inequality
  `TV>=p^Pi(U)-g(U)`.
- Control: removing `|supp(p)|<=K` yields `g(U)=1/5 < 1/4`, the intended fail.

## Downloads and limitations

For each `N` in 1–6, the evaluator can download the claim contract, raw result,
independent checker output, negative-control output, verifier, source audit,
method, evaluation, and limitations from `.openresearch/artifacts/claim_N/`.
The shared full implementations are
[Claim 1](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/repro_campaign/claim1.py),
[its independent checker](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/repro_campaign/independent_claim1.py),
[Claims 2–6](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/repro_campaign/theorems.py),
and the [fixed entrypoint](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/repro_campaign/run.py);
the environment is pinned by [uv.lock](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/uv.lock).

The finite sweeps are explicitly scoped corroboration, never universal proofs.
Universal validity rests on the independently reconstructed symbolic/set/
probability derivations. These claims concern the paper's abstract Language
Model definition, not a particular neural architecture. No empirical LLM
performance claim is being substituted.

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | this page | [yes](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_1/verifier.py) | yes | [raw JSON](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_1/raw_results.json) | [pass](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_1/independent_checker_output.json) | [expected fail](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_1/negative_control_output.json) | yes | VERIFIED |
| 2 | this page | [yes](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_2/verifier.py) | yes | [raw JSON](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_2/raw_results.json) | [pass](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_2/independent_checker_output.json) | [expected fail](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_2/negative_control_output.json) | yes; event-probability correction | VERIFIED |
| 3 | this page | [yes](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_3/verifier.py) | yes | [raw JSON](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_3/raw_results.json) | [pass](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_3/independent_checker_output.json) | [expected fail](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_3/negative_control_output.json) | yes | VERIFIED |
| 4 | this page | [yes](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_4/verifier.py) | yes | [raw JSON](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_4/raw_results.json) | [pass](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_4/independent_checker_output.json) | [expected fail](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_4/negative_control_output.json) | yes; strict non-vacuous delta | VERIFIED |
| 5 | this page | [yes](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_5/verifier.py) | yes | [raw JSON](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_5/raw_results.json) | [pass](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_5/independent_checker_output.json) | [expected fail](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_5/negative_control_output.json) | yes | VERIFIED |
| 6 | this page | [yes](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_6/verifier.py) | yes | [raw JSON](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_6/raw_results.json) | [pass](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_6/independent_checker_output.json) | [expected fail](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/.openresearch/artifacts/claim_6/negative_control_output.json) | yes; nonzero TV exercised | VERIFIED |

Historical pages from judged SHA `33ec740847185e0222abba902a35182e01a96015`
remain reachable under navigation labels beginning **Historical rejected
baseline**. They are preserved evidence, not the current verifier.
The three overwritten entry files are also retained byte-for-byte under
`historical/judged-33ec740/`, with hashes recorded in the release manifest.
See the [final release report](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/release/final_release_report.md)
and [evaluator-blind review](https://huggingface.co/spaces/DineshAI/iSD2q5Tius/resolve/main/release/evaluator_blind_red_team.md).
