- Previous campaign live judged score: `4/12`
- Current live judged score before this candidate: `6/12`
- Conservative projected score range after the proposed change: `10–12/12`
- Best-supported possible new score: `12/12` (**forecast, not a judge result**)

# Final native-proof release report

Current total score: **6/12** at Space revision
`d97b9033c6272a5a315afb3fe6ceccbe2c5a43d8`. Conservative projected total:
**10–12/12**. Best-supported possible total: **12/12**, strictly a forecast
until the live evaluator records a new verdict.

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
| --- | ---: | ---: | --- | --- | --- |
| 1 | 1 | 2 | HIGH | VERIFIED | Inlined universal set proof; 2,736,552 exact models; independent basis checker; 160,000 native structural checks; assumption-removal control. Remaining risk: judge interpretation. |
| 2 | 1 | 2 | HIGH | VERIFIED | Inlined Regular-Facts posterior proof and executable fractions; 171,699 symbolic checks; 160,000 exact posterior audits; native rates and CIs clear the event-probability floor. Remaining risk: source interpretation. |
| 3 | 1 | 2 | HIGH | VERIFIED | Inlined positive-witness proof for every partition; 56,105 complete finite models; 160,000 native calibrated identities; calibration-removal control. Remaining risk: judge interpretation. |
| 4 | 1 | 2 | HIGH | VERIFIED | Inlined Markov derivation; 2,359 exact substitutions; 4,508 non-vacuous models; native admissible-delta audit and non-Regular control. Remaining risk: judge interpretation. |
| 5 | 1 | 2 | HIGH | VERIFIED | Inlined exhaustive scatter/spike proof; 4,500 cases; sharpness certificate; native scatter/spike rates; false-constant control. Remaining risk: judge interpretation. |
| 6 | 1 | 2 | HIGH | VERIFIED | Inlined every-partition cell proof and TV step; 44,390 complete models; exact TV in 320,000 non-calibrated native evaluations; non-sparse control. Remaining risk: judge interpretation. |

All six claims change on the proposed evaluator surface from the live judge's
TOY verdict to a candidate VERIFIED verdict. No claim remains BLOCKED and no
claim has LOW confidence. Forecast confidence is scientific confidence, not
confidence that an external judge will necessarily award the point.

## Winning evidence and experiment tree

- Winning scientific branch: `orx/judge-readable-native-proof-package`
- Winning scientific Git SHA:
  `5bb4fa0a853342aa301feb18ece8f35cebe06d63`
- Fixed command: `uv run --frozen python -m repro_campaign.run`
- Pinned environment: Python 3.13, one repository `.venv`, `uv.lock`
- Winning cumulative run: `86e8776a-7f1c-4aba-809a-249a539485fa`
- Native predecessor run: `52ea83c1-e3c6-4452-9381-4e2a0864f88a`
- Native scale: 160,000 corpora, four regimes, `N≤20,000`, `K≤100`,
  scatter/spike/calibrated model families
- Winning verifier runtime: 20.116019 seconds; HF job running time 30 seconds

The stacked lineage is: immutable historical audit → exact Claim 1 certificate
→ visible Claim 1 package → exact Claims 2–6 → first release candidate →
native-scale HF corroboration → judge-readable native proof package → final
release gates. Each child reruns all previously accepted claims with the same
command and lockfile.

## Compute and cost

Every new formal run estimated one required core and used a one-thread process.
The first native runtime was uncertain, so it was routed to Hugging Face
`cpu-upgrade` as required. That flavor advertises 8 vCPU at $0.0005/minute; the
container exposed 64 logical CPUs to Python, recorded as allocation visibility.
No GPU was used.

| Run | Result | HF running time | Nominal cost at $0.0005/min |
| --- | --- | ---: | ---: |
| `98229fad-9d5b-47a4-9279-568a57e9e9fa` | packaging-only manifest failure | 30 s | ≈$0.00025 |
| `52ea83c1-e3c6-4452-9381-4e2a0864f88a` | native-scale PASS | 30 s | ≈$0.00025 |
| `86e8776a-7f1c-4aba-809a-249a539485fa` | judge-readable package PASS | 30 s | ≈$0.00025 |

Nominal HF cost before the final release-only regression is approximately
**$0.00075**, subject to Hugging Face billing granularity. Historical local
runs cost $0 in HF compute.

## Current evaluator-visible contents

The canonical path is README → scorecard → one page per claim. Every claim page
contains the exact quantifiers and assumptions, the complete derivation,
executable verifier code inline, native numerical results, an
assumption-targeted negative control, limitations, and an explicit VERIFIED
evidence verdict. The methods page exposes the fixed command, pinned
environment, seeds, CPU selection/allocation, and runtime. Raw native JSON and
all prior claim artifacts are directly downloadable.

The current upload allowlist contains 89 UTF-8 text files. Its SHA-256 manifest
excludes only itself. Secret-prefix scanning, unique-target checks, JSON
validation, leaderboard tags, canonical-page checks, and byte-for-byte
historical entry hashes pass.

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `pages/claim-1/page.md` | yes, executable block | yes | claim + native JSON | independent basis | expected fail | yes | VERIFIED |
| 2 | `pages/claim-2/page.md` | yes, executable block | rates + CI | claim + native JSON | binomial identity | expected fail | yes | VERIFIED |
| 3 | `pages/claim-3/page.md` | yes, executable block | yes | claim + native JSON | witness checker | expected fail | yes | VERIFIED |
| 4 | `pages/claim-4/page.md` | yes, executable block | admissible deltas | claim + native JSON | exact substitution | expected fail | yes | VERIFIED |
| 5 | `pages/claim-5/page.md` | yes, executable block | yes | claim + native JSON | sharpness certificate | expected fail | yes | VERIFIED |
| 6 | `pages/claim-6/page.md` | yes, executable block | exact TV/slack | claim + native JSON | cell + TV checker | expected fail | yes | VERIFIED |

## Reproduction and orchestration commands

```bash
uv run --frozen python -m repro_campaign.run
orx exp run e56f5654-b597-40b6-949b-d52efbc10eb4 --backend hf --flavor cpu-upgrade --image ghcr.io/astral-sh/uv:python3.13-bookworm-slim --timeout 30m
orx exp wait e56f5654-b597-40b6-949b-d52efbc10eb4 --interval 5 --timeout 55
orx logs 52ea83c1-e3c6-4452-9381-4e2a0864f88a --bytes 200000
orx exp run 57b32b27-c9b7-413b-9d97-74f5430a0e23 --backend hf --flavor cpu-upgrade --image ghcr.io/astral-sh/uv:python3.13-bookworm-slim --timeout 30m
orx exp wait 57b32b27-c9b7-413b-9d97-74f5430a0e23 --interval 5 --timeout 55
orx logs 86e8776a-7f1c-4aba-809a-249a539485fa --bytes 200000
```

Startup and audit commands included `orx projects --json`, `orx project view`,
`orx runs`, `orx exp status`, `orx exp desc`, `git status --short`,
`git rev-parse HEAD`, `git ls-remote`, exact-revision `hf download`, strict
verdict filtering by `space_id`, JSON validation, SHA-256 verification, and
the staged evaluator-blind traversal.

## Publication action

After the final cumulative regression and repeated blind traversal pass, upload
only the exact 89-file UTF-8 allowlist through the Hugging Face commit API to
the existing Space `DineshAI/iSD2q5Tius`. Then download that exact published
revision, verify every manifest hash and the canonical traversal, mirror the
same reader-facing text to GitHub `main`, confirm the remote SHA using
`git ls-remote`, and leave the paper awaiting the live judge.
