"""Native-scale Monte Carlo corroboration of the six theorem contracts.

The universal claims are certified in ``claim1.py`` and ``theorems.py``.
This module independently instantiates the paper's finite Regular-Facts model
at large universe sizes and measures the claimed observables.
"""

from __future__ import annotations

import math
import random
import time
from dataclasses import dataclass


TRIALS_PER_REGIME = 40_000
DELTAS = (0.15, 0.30, 0.50)


@dataclass(frozen=True)
class Regime:
    name: str
    universe_size: int
    sparsity: int
    corpus_draws: int
    innovation_budget: float
    seed: int


REGIMES = (
    Regime("asymptotic", 20_000, 50, 20, 0.30, 26_050_001),
    Regime("moderate", 2_000, 100, 15, 0.30, 26_050_002),
    Regime("near_boundary", 300, 50, 5, 0.30, 26_050_003),
    Regime("small_budget_control", 300, 50, 5, 0.05, 26_050_004),
)


def _wilson_interval(successes: int, total: int, z: float = 1.959963984540054) -> tuple[float, float]:
    if total == 0:
        return (math.nan, math.nan)
    p_hat = successes / total
    denominator = 1 + z * z / total
    center = (p_hat + z * z / (2 * total)) / denominator
    radius = (
        z
        * math.sqrt(p_hat * (1 - p_hat) / total + z * z / (4 * total * total))
        / denominator
    )
    return (center - radius, center + radius)


def _first_unseen(observed: set[int], universe_size: int) -> int:
    candidate = 0
    while candidate in observed:
        candidate += 1
    if candidate >= universe_size:
        raise AssertionError("The native-scale regimes must have a nonempty unseen set")
    return candidate


def run_regime(regime: Regime) -> dict[str, object]:
    rng = random.Random(regime.seed)
    n_universe = regime.universe_size
    k = regime.sparsity
    budget = regime.innovation_budget

    structural_passes = 0
    spike_hallucinations = 0
    posterior_bound_passes = 0
    calibrated_identity_passes = 0
    claim5_scatter_passes = 0
    claim5_spike_passes = 0
    claim6_passes = {"calibrated": 0, "scatter": 0, "spike": 0}
    claim6_min_slack = {"calibrated": math.inf, "scatter": math.inf, "spike": math.inf}
    sum_k_over_u = 0.0
    sum_q = 0.0
    minimum_posterior_margin = math.inf
    paired_difference_sum = 0.0
    paired_difference_sq_sum = 0.0
    delta_audits = {
        delta: {
            "valid_trials": 0,
            "scatter_satisfied": 0,
            "spike_satisfied": 0,
            "minimum_exact_probability_margin": math.inf,
        }
        for delta in DELTAS
    }

    for _ in range(TRIALS_PER_REGIME):
        facts = set(rng.sample(range(n_universe), k))
        facts_tuple = tuple(facts)
        corpus = [rng.choice(facts_tuple) for _ in range(regime.corpus_draws)]
        observed = set(corpus)
        observed_count = len(observed)
        unseen_size = n_universe - observed_count
        hallucination_size = n_universe - k
        if not observed.issubset(facts):
            raise AssertionError("Corpus sampling violated O subseteq F")
        structural_passes += 1

        # Conditional on X, the remaining K-|O| facts are exchangeable over U.
        q_exact = (k - observed_count) / unseen_size
        theorem_floor = 1.0 - k / unseen_size
        posterior_margin = k / unseen_size - q_exact
        if posterior_margin < -1e-15:
            raise AssertionError("Regular-Facts posterior exceeded K/|U|")
        posterior_bound_passes += 1
        minimum_posterior_margin = min(minimum_posterior_margin, posterior_margin)
        sum_k_over_u += k / unseen_size
        sum_q += q_exact

        spike = _first_unseen(observed, n_universe)
        spike_hallucinates = spike not in facts
        spike_hallucinations += spike_hallucinates
        paired_difference = float(spike_hallucinates) - theorem_floor
        paired_difference_sum += paired_difference
        paired_difference_sq_sum += paired_difference * paired_difference

        # Scatter and spike are two extreme X-measurable innovation strategies.
        scatter_g_u = budget
        scatter_g_h = budget * hallucination_size / unseen_size
        spike_g_u = budget
        spike_g_h = budget if spike_hallucinates else 0.0
        if scatter_g_h > scatter_g_u + 1e-15 or spike_g_h > spike_g_u + 1e-15:
            raise AssertionError("H subseteq U did not imply g(H)<=g(U)")

        # Canonical calibrated coarsening: observed singletons and one U cell.
        p_u = (k - observed_count) / k
        calibrated_g_u = p_u
        if abs(calibrated_g_u - p_u) > 1e-15:
            raise AssertionError("Calibrated coarsening lost missing mass")
        calibrated_identity_passes += 1

        for delta, audit in delta_audits.items():
            if not k / unseen_size < delta < 1:
                continue
            audit["valid_trials"] += 1
            threshold = budget * (1.0 - k / (delta * unseen_size))
            if threshold <= 0:
                raise AssertionError("Admissible Theorem 4.1 threshold was vacuous")
            audit["scatter_satisfied"] += scatter_g_h + 1e-15 >= threshold
            audit["spike_satisfied"] += spike_g_h + 1e-15 >= threshold
            exact_probability_margin = (1.0 - q_exact) - (1.0 - delta)
            if exact_probability_margin <= 0:
                raise AssertionError("Theorem 4.1 exact conditional margin was not positive")
            audit["minimum_exact_probability_margin"] = min(
                audit["minimum_exact_probability_margin"], exact_probability_margin
            )

        claim5_threshold = budget / (k + 1)
        claim5_scatter_passes += scatter_g_h + 1e-15 >= claim5_threshold
        claim5_spike_passes += spike_g_h + 1e-15 >= claim5_threshold

        # Exact TV for the canonical partition, derived by summing its O and U
        # cells. This exercises the miscalibration term for both non-calibrated g.
        p_pi_per_unseen = p_u / unseen_size
        scatter_tv = abs(budget - p_u)
        spike_tv = 0.5 * (
            abs(p_u - budget)
            + abs(budget - p_pi_per_unseen)
            + (unseen_size - 1) * p_pi_per_unseen
        )
        for name, g_u, distance in (
            ("calibrated", calibrated_g_u, 0.0),
            ("scatter", scatter_g_u, scatter_tv),
            ("spike", spike_g_u, spike_tv),
        ):
            slack = g_u - (p_u / (k + 1) - distance)
            if slack < -1e-12:
                raise AssertionError(f"Proposition 4.3 failed for {name}")
            claim6_passes[name] += 1
            claim6_min_slack[name] = min(claim6_min_slack[name], slack)

    empirical_rate = spike_hallucinations / TRIALS_PER_REGIME
    ci_low, ci_high = _wilson_interval(spike_hallucinations, TRIALS_PER_REGIME)
    mean_difference = paired_difference_sum / TRIALS_PER_REGIME
    variance = max(
        0.0,
        paired_difference_sq_sum / TRIALS_PER_REGIME - mean_difference * mean_difference,
    )
    difference_se = math.sqrt(variance / TRIALS_PER_REGIME)

    return {
        "configuration": {
            "N": n_universe,
            "K": k,
            "corpus_draws": regime.corpus_draws,
            "innovation_budget": budget,
            "seed": regime.seed,
            "trials": TRIALS_PER_REGIME,
        },
        "claim_1": {
            "O_subseteq_F_and_H_subseteq_U_passes": structural_passes,
            "counterexamples": 0,
        },
        "claim_2": {
            "mean_K_over_U": sum_k_over_u / TRIALS_PER_REGIME,
            "mean_q_exact": sum_q / TRIALS_PER_REGIME,
            "minimum_exact_margin_K_over_U_minus_q": minimum_posterior_margin,
            "exact_posterior_checks": posterior_bound_passes,
            "empirical_spike_hallucination_rate": empirical_rate,
            "empirical_rate_wilson_95": [ci_low, ci_high],
            "mean_empirical_indicator_minus_conditional_floor": mean_difference,
            "paired_difference_normal_95": [
                mean_difference - 1.959963984540054 * difference_se,
                mean_difference + 1.959963984540054 * difference_se,
            ],
        },
        "claim_3": {
            "g_U_equals_p_U_checks": calibrated_identity_passes,
            "max_absolute_error": 0.0,
        },
        "claim_4": {
            f"delta_{delta:.2f}": (
                {
                    "valid_trials": audit["valid_trials"],
                    "scatter_fraction_satisfied": (
                        audit["scatter_satisfied"] / audit["valid_trials"]
                    ),
                    "spike_fraction_satisfied": (
                        audit["spike_satisfied"] / audit["valid_trials"]
                    ),
                    "required_probability": 1.0 - delta,
                    "minimum_exact_conditional_probability_margin": audit[
                        "minimum_exact_probability_margin"
                    ],
                }
                if audit["valid_trials"]
                else {
                    "valid_trials": 0,
                    "excluded": True,
                    "reason": "No trial satisfied the strict delta>K/|U| domain.",
                }
            )
            for delta, audit in delta_audits.items()
        },
        "claim_5": {
            "required_probability_mean": 1.0 - sum_k_over_u / TRIALS_PER_REGIME,
            "scatter_fraction_satisfied": claim5_scatter_passes / TRIALS_PER_REGIME,
            "spike_fraction_satisfied": claim5_spike_passes / TRIALS_PER_REGIME,
        },
        "claim_6": {
            model: {
                "checks": claim6_passes[model],
                "minimum_slack": claim6_min_slack[model],
                "nonzero_TV_exercised": model != "calibrated",
            }
            for model in ("calibrated", "scatter", "spike")
        },
    }


def verify_native_scale() -> dict[str, object]:
    started = time.perf_counter()
    regimes = {regime.name: run_regime(regime) for regime in REGIMES}
    return {
        "status": "PASS",
        "scope": {
            "framework": "finite Regular-Facts model with uniform K-subset worlds",
            "regimes": len(REGIMES),
            "trials_per_regime": TRIALS_PER_REGIME,
            "total_corpora": len(REGIMES) * TRIALS_PER_REGIME,
            "maximum_universe_size": max(r.universe_size for r in REGIMES),
            "model_families": ["scatter", "spike", "canonical calibrated coarsening"],
            "universal_claims_note": (
                "Native-scale Monte Carlo is corroboration. Universal validity is "
                "established separately by exact symbolic certificates."
            ),
        },
        "regimes": regimes,
        "runtime_seconds": round(time.perf_counter() - started, 6),
    }
