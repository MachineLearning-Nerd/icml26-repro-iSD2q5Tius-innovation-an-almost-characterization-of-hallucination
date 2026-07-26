# Evaluator-blind pre-publication review

Review date: 2026-07-26. The valid review used a fresh download of the exact
currently judged Space revision
`d97b9033c6272a5a315afb3fe6ceccbe2c5a43d8` and overlaid only the explicit
89-file candidate allowlist. Repository history, OpenResearch logs, and
unpublished branch knowledge were not used to fill scientific conclusions.

An earlier staging command was discarded before review because its JSON
iterator stopped without overlaying the new pages and its shell variable
shadowed the command search path. It produced no scientific conclusion. The
valid review below restarted in a fresh directory.

## Files opened from the canonical path

1. `README.md`
2. `logbook.json`
3. `pages/index.md`
4. `pages/00-scorecard/page.md`
5. `pages/claim-1/page.md`
6. `pages/claim-2/page.md`
7. `pages/claim-3/page.md`
8. `pages/claim-4/page.md`
9. `pages/claim-5/page.md`
10. `pages/claim-6/page.md`
11. `pages/methods/page.md`
12. `.openresearch/artifacts/native_scale/raw_results.json`
13. `release/upload_manifest.sha256`

README's first navigation link was `#/00-scorecard`; `logbook.json` also put
`pages/00-scorecard/page.md` first. Nine current pages preceded every entry
whose title begins exactly **Historical rejected baseline**.

## Claim-by-claim conclusions

| Claim | Exact claim and assumptions found | Proof found | Executable code inline | Native data inline | Control found | Blind conclusion |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | complete `O⊆F ⇒ H⊆U` proof | yes | 160,000 checks | remove `O⊆F` | VERIFIED |
| 2 | yes; event probability distinguished from mass | complete Regular-Facts posterior proof | yes | rates, floors, CIs | remove Regular Facts | VERIFIED |
| 3 | yes; every partition | positive unseen witness proof | yes | 160,000 identities | remove calibration | VERIFIED |
| 4 | yes; strict `δ∈(K/|U|,1)` | complete Markov derivation | yes | admissible deltas only | remove Regular Facts | VERIFIED |
| 5 | yes | exhaustive max-mass dichotomy | yes | scatter/spike table | false denominator K | VERIFIED |
| 6 | yes; every partition and arbitrary g | cellwise lemma plus TV event bound | yes | exact-TV slacks | remove sparsity | VERIFIED |

The reviewer did not need linked source files to understand or assess any
claim. Links provide full implementations and raw data as supplementary
downloads.

## Mechanical results

- Exact old candidate file paths checked: 93
- Old paths missing from the staged candidate: 0
- Current navigation pages before historical entries: 9
- Complete canonical claim pages: 6/6
- Manifest hash failures: 0
- Native raw status: PASS
- Native raw scope: 160,000 corpora, maximum universe 20,000
- Leaderboard discovery tags present: yes
- Historical judged entry hashes: pass
- Secret-prefix scan: pass

## Remaining risks

No evaluator-visible evidence cell is missing. The remaining risk is external
judge interpretation: the universal certificates are reconstructed symbolic
proofs rather than Lean/Coq objects, and the paper's model is abstract rather
than a neural architecture. Those limitations are explicit on the methods
page. The reviewer found no basis to downgrade any claim to toy or blocked from
the candidate alone.
