- Previous live judged score: `4/12`
- Conservative projected score range after the proposed change: `8–12/12`
- Best-supported possible new score: `12/12` (**forecast, not a judge result**)

# Final release report

Current total score: **4/12**. Conservative projected total score range:
**8–12/12**. Best-supported possible total: **12/12**, strictly a forecast
until the live evaluator records a verdict.

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
| --- | ---: | ---: | --- | --- | --- |
| 1 | 1 | 2 | HIGH | VERIFIED | Generic set certificate, 2,736,552 exact models, independent implementation, and assumption-removal control. Remaining risk is evaluator interpretation. |
| 2 | 0 | 2 | HIGH | VERIFIED | Exact source audit corrects the event-probability misquote; symbolic, symmetric-posterior, and binomial certificates agree. Remaining risk is acceptance of the corrected reading. |
| 3 | 1 | 2 | HIGH | VERIFIED | Witness proof and all 56,105 declared finite models agree; noncalibrated control fails. Remaining risk is evaluator interpretation. |
| 4 | 0 | 2 | HIGH | VERIFIED | Strict admissible deltas make all 4,508 bounds non-vacuous; expectation proof and non-Regular control agree. Remaining risk is evaluator interpretation. |
| 5 | 1 | 2 | HIGH | VERIFIED | Case-split proof, 5,862 models, sharpness certificate, and false-constant control agree. Remaining risk is evaluator interpretation. |
| 6 | 1 | 2 | HIGH | VERIFIED | Cellwise/TV proof, 44,390 models including 43,390 nonzero-TV cases, and non-sparse control agree. Remaining risk is evaluator interpretation. |

All six claims changed in evidence status relative to the prior judge surface:
Claims 1, 3, 5, and 6 replace toy evidence; Claims 2 and 4 replace inconclusive,
misdirected or vacuous checks. No claim remains BLOCKED. No LOW-confidence
route sequence is required.

## Release evidence

- Winning scientific branch:
  `orx/exact-certificates-for-claims-2-through-6`
- Winning scientific Git SHA:
  `ab5399c447df51aaca30462132faad7e7ae83d04`
- Fixed command: `uv run --frozen python -m repro_campaign.run`
- Pinned environment: Python 3.13.7, `uv.lock`
- Scientific cumulative run:
  `f01d14d8-9c3d-4888-b80f-b6615509d55f`
- Scientific verifier runtime: 7.837742 seconds; supervised local job wall
  time: 10 seconds
- Compute estimate: one core; selected backend local; selected HF flavor none;
  actual process budget one; eight logical CPUs visible
- Total completed OpenResearch wall time before the release regression:
  35 seconds; Hugging Face compute cost $0

The experiment tree is a single descending lineage: immutable historical
audit → exact Claim 1 certificate → evaluator-visible Claim 1 package →
cumulative exact Claims 2–6 → evaluator-visible release candidate. Each child
reruns all accepted checks.

## Preservation and visibility

The fresh candidate overlay contains all 17 judged paths. Fourteen remain
byte-identical in place. The three intentionally replaced entry files are
retained byte-for-byte under `historical/judged-33ec740/`; all five historical
claim pages remain unchanged and reachable. The clean-room traversal opened 34
files from the canonical entrypoint and found every required claim artifact.
The six-row visibility matrix is inline on the current verification page with
no missing cells.

The exact upload allowlist contains 79 UTF-8 text files after including this
report and the red-team record. `release/upload_manifest.sha256` hashes every
payload except itself. Secret-prefix scanning, unique-target checks, JSON
validation, and historical entry hash checks pass.

## Reproduction and audit commands

```bash
uv sync --frozen
uv run --frozen python -m repro_campaign.run
uv run --frozen marimo check notebooks/innovation_claims.py
xmllint --noout reports/claim-by-claim/images/*.svg
orx exp run 4c71c890-5d27-4417-8397-76c0b206d9e4 --backend local
orx exp wait 4c71c890-5d27-4417-8397-76c0b206d9e4 --timeout 480
orx logs <release-run-id>
```

Startup and provenance commands also included `orx projects --json`,
`orx runs defa40af-003c-4438-9239-91355dc1da84`, `orx exp status`,
`orx exp desc`, `git status --short`, `git branch -a`, `git rev-parse HEAD`,
`git ls-remote`, `df -h`, `env | cut -d= -f1`, explicit-User-Agent paper
retrieval, exact Space checkout, strict verdict filtering by `space_id`, and
SHA-256 verification.

## Publication action

After the cumulative release regression and all gates pass, upload only the
79 allowlisted UTF-8 files through the Hugging Face commit API to the existing
Space `DineshAI/iSD2q5Tius`, preserving all other files. Then download the exact
published revision, verify its manifest and canonical traversal, push the
polished README/report/notebook surface to GitHub `main`, confirm the remote
SHA with `git ls-remote`, and mark the paper awaiting the live judge.
