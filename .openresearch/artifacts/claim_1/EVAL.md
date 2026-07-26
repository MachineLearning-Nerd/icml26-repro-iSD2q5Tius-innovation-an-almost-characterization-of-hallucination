# Claim 1 evaluation contract

Verdict: `VERIFIED`.

Evidence-producing run: `b965e058-dca8-4e8d-82ff-fcc01a75eb06`.
Evidence-producing Git SHA: `4bc947424e0e591a06d91d886f514dd158101b08`.
Fixed command: `uv run --frozen python -m repro_campaign.run`.
Environment: Python 3.13.7, `uv.lock`, Marimo 0.23.15.
Compute: supervised local CPU; estimated one required core; process thread
budget one; eight logical CPUs visible; 10 seconds OpenResearch duration and
4.105397 seconds verifier runtime.

The run checked 2,736,552 complete-domain rational models, found zero
counterexamples, independently checked 3,279 set relations and 21,324
point-mass bases, and observed the intended negative-control failure
`g(H)=1, g(U)=0` after removing `O subseteq F`.

The fixed command executes the primary certificate, independent checker,
negative control, historical regression, and exact raw-fixture regeneration.
Any mismatch exits nonzero. Full evidence is printed between
`OPENRESEARCH_EVIDENCE_BEGIN` and `OPENRESEARCH_EVIDENCE_END`.

