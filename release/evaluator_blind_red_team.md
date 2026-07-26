# Evaluator-blind pre-publication review

Review date: 2026-07-26. Candidate source: a fresh checkout of judged Space
revision `33ec740847185e0222abba902a35182e01a96015` with only the explicit
text allowlist overlaid. Repository knowledge and OpenResearch run logs were
not used to fill evidence gaps.

## Traversal

The review began at `README.md`, followed its canonical link to
`pages/current-verification/page.md`, and used `logbook.json` plus
`pages/index.md` to confirm that current verification is the first navigation
item. The page itself identified all evidence locations.

Files opened:

- `README.md`
- `logbook.json`
- `pages/index.md`
- `pages/current-verification/page.md`
- for each claim number 1 through 6:
  `.openresearch/artifacts/claim_N/claim_contract.json`,
  `raw_results.json`, `independent_checker_output.json`,
  `negative_control_output.json`, and `verifier.py`

Total files opened: 34. The reviewer also checked link targets without using
their content: `source_audit.md`, `method.md`, `EVAL.md`, `limitations.md`,
the shared `repro_campaign/*.py` implementation, `pyproject.toml`, and
`uv.lock`.

## Conclusions

- All six exact source claims and quantifiers were located on the canonical
  page.
- Assumptions and their numerical audits were inline for all six claims.
- Raw numerical results, executable verifiers, independent checks, and failing
  controls were directly linked.
- The fixed command, environment, evidence-producing Git SHA, CPU estimate,
  actual visible CPU allocation, and runtime were inline.
- Every old judged path remained in the candidate. The only intentionally
  replaced paths were `README.md`, `logbook.json`, and `pages/index.md`; their
  exact prior bytes were preserved under `historical/judged-33ec740/`.
- The rejected verifier was reachable only under the exact label
  **Historical rejected baseline** and was not the default verification page.

No evidence conclusion was inaccessible after traversal. No navigation or
science fix was required after this repeated clean-room overlay review.
