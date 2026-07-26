# Claim 1 method

The primary verifier uses three independent pieces of evidence:

1. a complete two-variable truth table checks the generic implication
   `O(y) -> F(y)`, therefore `not F(y) -> not O(y)`;
2. a finite-domain regression exhausts every `O subseteq F` relation and every
   probability vector with denominator four for `1 <= |Omega| <= 8`;
3. an invalid-world negative control removes `O subseteq F` and must exhibit
   `g(H)=1`, `g(U)=0`.

The independent checker uses bit masks and point-mass basis distributions rather
than the primary verifier's ternary membership states and rational compositions.
Point masses generate the nonnegative measure cone, so checking every basis
element independently checks measure monotonicity for arbitrary mixtures.

The exhaustive sweep is corroboration over a declared complete finite domain.
The universal result rests on the generic truth-table certificate plus
probability-measure monotonicity.

