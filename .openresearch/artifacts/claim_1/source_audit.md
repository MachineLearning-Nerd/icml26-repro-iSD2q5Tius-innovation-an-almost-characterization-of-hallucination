# Claim 1 source audit

Definition 3.1 defines innovation as `g(U)>0`, where
`U = Omega \ set(X)`. Observation 3.2 states that for any language model
predictive distribution `g`, `g(H)>0` in a world `p` implies `g(U)>0`.

The only substantive model assumption used is inherited from the data-generating
framework: observed statements are sampled from `p`, so `O=set(X)` is a subset
of `F=supp(p)`. Therefore `H=Omega\F` is a subset of `U=Omega\O`.
K-sparsity, Regular Facts, calibration, corpus size, and neural architecture are
not assumptions of this observation.

The paper defines a Language Model abstractly as a map from corpora to
probability distributions. Requiring a particular neural LLM would change the
claim rather than make this theorem check more faithful.

