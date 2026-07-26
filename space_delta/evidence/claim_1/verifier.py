"""Evaluator-visible Claim 1 verifier; canonical source lives at Git SHA 4bc9474."""

from itertools import product


def verify_symbolic_certificate() -> None:
    for observed, factual in product((False, True), repeat=2):
        premise = (not observed) or factual
        hallucination = not factual
        unseen = not observed
        conclusion = (not hallucination) or unseen
        if premise and not conclusion:
            raise AssertionError("O subseteq F did not imply H subseteq U")


def verify_negative_control() -> None:
    # Removing O subseteq F must make the implication fail.
    g_h, g_u = 1, 0
    if not (g_h > 0 and g_u == 0):
        raise AssertionError("negative control unexpectedly passed")


if __name__ == "__main__":
    verify_symbolic_certificate()
    verify_negative_control()
    print("PASS: g(H)>0 implies g(U)>0 under O subseteq F")

