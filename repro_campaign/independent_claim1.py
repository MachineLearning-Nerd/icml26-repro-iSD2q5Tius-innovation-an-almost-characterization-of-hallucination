"""Independent bit-mask checker for Claim 1.

This intentionally does not import the primary verifier.
"""

from __future__ import annotations


def independent_check(max_omega: int = 7) -> dict[str, object]:
    checked_relations = 0
    checked_point_masses = 0
    for size in range(1, max_omega + 1):
        universe = (1 << size) - 1
        for factual in range(universe + 1):
            observed = factual
            while True:
                checked_relations += 1
                hallucinations = universe ^ factual
                unseen = universe ^ observed
                if hallucinations & ~unseen:
                    raise AssertionError("Independent H⊆U relation failed")
                # Point masses span the nonnegative cone; check each basis vector.
                for bit in range(size):
                    checked_point_masses += 1
                    g_h = (hallucinations >> bit) & 1
                    g_u = (unseen >> bit) & 1
                    if g_h > g_u:
                        raise AssertionError("Independent measure monotonicity failed")
                if observed == 0:
                    break
                observed = (observed - 1) & factual
    return {
        "implementation": "independent bit-mask subset enumeration plus point-mass basis",
        "omega_sizes": [1, max_omega],
        "relations_checked": checked_relations,
        "point_masses_checked": checked_point_masses,
        "counterexamples": 0,
        "status": "PASS",
    }

