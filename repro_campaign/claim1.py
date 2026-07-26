"""Exact verifier for Definition 3.1 and Observation 3.2."""

from __future__ import annotations

from itertools import product
from typing import Iterator


def compositions(total: int, parts: int) -> Iterator[tuple[int, ...]]:
    """Yield all weak integer compositions, using no numerical library."""
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, parts - 1):
            yield (first, *rest)


def verify_symbolic_certificate() -> dict[str, object]:
    """Check the generic one-element truth table behind H ⊆ U."""
    rows = []
    for observed, factual in product((False, True), repeat=2):
        premise = (not observed) or factual  # O(y) -> F(y)
        hallucination = not factual
        unseen = not observed
        conclusion = (not hallucination) or unseen  # H(y) -> U(y)
        rows.append(
            {
                "observed": observed,
                "factual": factual,
                "premise_O_implies_F": premise,
                "conclusion_H_implies_U": conclusion,
            }
        )
        if premise and not conclusion:
            raise AssertionError("O⊆F did not imply H⊆U")
    return {
        "universal_element_truth_table": rows,
        "valid_rows_checked": sum(row["premise_O_implies_F"] for row in rows),
        "derived_set_relation": "H = Omega\\F subseteq U = Omega\\O",
        "measure_rule": "For every nonnegative probability measure g, H subseteq U implies g(H) <= g(U)",
        "strict_implication": "g(H)>0 implies g(U)>0",
    }


def verify_complete_finite_domain(max_omega: int = 8, denominator: int = 4) -> dict[str, object]:
    """Exhaust every O⊆F and rational distribution on Ω in the stated domain."""
    models = 0
    positive_hallucination_cases = 0
    for size in range(1, max_omega + 1):
        # 0: observed fact; 1: unobserved fact; 2: hallucination.
        for membership in product(range(3), repeat=size):
            unseen = tuple(i for i, state in enumerate(membership) if state != 0)
            hallucinations = tuple(i for i, state in enumerate(membership) if state == 2)
            for weights in compositions(denominator, size):
                models += 1
                g_u_num = sum(weights[i] for i in unseen)
                g_h_num = sum(weights[i] for i in hallucinations)
                if g_h_num > g_u_num:
                    raise AssertionError("Monotonicity failed on a valid O⊆F instance")
                if g_h_num > 0:
                    positive_hallucination_cases += 1
                    if g_u_num == 0:
                        raise AssertionError("Observation 3.2 failed")
    return {
        "scope": {
            "omega_sizes": [1, max_omega],
            "all_O_subseteq_F_pairs": True,
            "all_probability_vectors": f"integer weights / {denominator}",
        },
        "models_checked": models,
        "positive_hallucination_cases": positive_hallucination_cases,
        "counterexamples": 0,
    }


def verify_negative_control() -> dict[str, object]:
    """Remove O⊆F and require the theorem to fail for the intended reason."""
    omega = {0}
    observed = {0}
    factual: set[int] = set()
    hallucinations = omega - factual
    unseen = omega - observed
    g = {0: 1}
    g_h = sum(g[y] for y in hallucinations)
    g_u = sum(g[y] for y in unseen)
    implication_holds = not (g_h > 0 and g_u == 0)
    if implication_holds:
        raise AssertionError("Negative control unexpectedly passed")
    return {
        "assumption_removed": "O subseteq F (training statements are factual)",
        "Omega": [0],
        "O": [0],
        "F": [],
        "g_H": g_h,
        "g_U": g_u,
        "expected_failure_observed": True,
        "failure_reason": "The observed statement is declared non-factual, so H is not a subset of U.",
    }


def verify_claim1() -> dict[str, object]:
    symbolic = verify_symbolic_certificate()
    exhaustive = verify_complete_finite_domain()
    control = verify_negative_control()
    return {
        "claim": 1,
        "status": "VERIFIED",
        "exact_source_result": "g(H)>0 implies g(U)>0",
        "symbolic_certificate": symbolic,
        "complete_finite_domain": exhaustive,
        "negative_control": control,
        "limitations": [
            "The exhaustive sweep is complete only for the explicitly stated finite rational domain.",
            "Universality comes from the checked set-inclusion truth table and probability-measure monotonicity rule, not extrapolation from the sweep.",
            "The paper's Language Model definition is an abstract mapping to a distribution; a neural LLM is not an additional theorem assumption.",
        ],
    }

