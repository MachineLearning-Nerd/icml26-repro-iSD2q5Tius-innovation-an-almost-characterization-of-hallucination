# Claim 5 evaluation

Verdict: `VERIFIED`. Run `f01d14d8-9c3d-4888-b80f-b6615509d55f`,
SHA `ab5399c447df51aaca30462132faad7e7ae83d04`, fixed command
`uv run --frozen python -m repro_campaign.run`. It checked 4,500 exact
scatter/spike cases and 5,862 complete symmetric-domain models. The K+1
sharpness certificate passed and the false denominator-K control failed.
