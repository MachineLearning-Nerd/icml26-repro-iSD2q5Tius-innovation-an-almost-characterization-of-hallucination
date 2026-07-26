# Claim 6 evaluation

Verdict: `VERIFIED`. Run `f01d14d8-9c3d-4888-b80f-b6615509d55f`,
SHA `ab5399c447df51aaca30462132faad7e7ae83d04`, fixed command
`uv run --frozen python -m repro_campaign.run`. It checked 44,390 complete
models, 8,940 cell inequalities, and 43,390 models with nonzero
miscalibration. Independent coarsening/TV steps passed; the non-sparse control
failed as intended.

