"""Fixed OpenResearch entrypoint for the historical judged baseline.

This baseline does not claim to verify the paper.  It checks that the immutable
judge record and Space manifest are present and records the six historical
verdicts that subsequent child experiments must supersede.
"""

from __future__ import annotations

import hashlib
import json
import os
import platform
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / ".openresearch" / "artifacts" / "historical"
EXPECTED_SPACE_SHA = "33ec740847185e0222abba902a35182e01a96015"
EXPECTED_VERDICTS = ["toy", "inconclusive", "toy", "inconclusive", "toy", "toy"]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 16), b""):
            digest.update(chunk)
    return digest.hexdigest()


def visible_cpus() -> int:
    if hasattr(os, "sched_getaffinity"):
        return len(os.sched_getaffinity(0))
    return os.cpu_count() or 1


def main() -> None:
    started = time.perf_counter()
    record_path = ARTIFACTS / "verdict_record.json"
    manifest_path = ARTIFACTS / "protected_space_manifest.sha256"
    record = json.loads(record_path.read_text(encoding="utf-8"))
    verdicts = [claim["verdict"] for claim in record["claims"]]
    manifest_lines = [
        line for line in manifest_path.read_text(encoding="utf-8").splitlines() if line
    ]

    checks = {
        "space_id_exact": record["space_id"] == "DineshAI/iSD2q5Tius",
        "judge_sha_exact": record["sha"] == EXPECTED_SPACE_SHA,
        "judge_time_exact": record["judged_at"] == "2026-07-25T16:14:34+00:00",
        "six_claims_present": len(record["claims"]) == 6,
        "historical_verdicts_exact": verdicts == EXPECTED_VERDICTS,
        "protected_manifest_has_17_files": len(manifest_lines) == 17,
        "verdict_record_sha256": sha256(record_path)
        == "c606669bce5f393fe40091cb580e834c158270c98e91906ee3ae37a23721d272",
    }
    if not all(checks.values()):
        raise SystemExit("Historical baseline integrity failure: " + json.dumps(checks))

    result = {
        "campaign_stage": "Historical rejected baseline",
        "claim_statuses": ["BLOCKED"] * 6,
        "historical_judge_points": 4,
        "historical_judge_max_points": 12,
        "checks": checks,
        "compute": {
            "estimated_required_cores": 1,
            "selected_backend": "local",
            "selected_flavor": None,
            "process_thread_budget": 1,
            "actual_visible_logical_cpus": visible_cpus(),
            "python": platform.python_version(),
            "platform": platform.platform(),
        },
        "runtime_seconds": round(time.perf_counter() - started, 6),
        "limitations": [
            "This run audits immutable historical evidence; it verifies no paper claim.",
            "The historical checks were judged TOY or INCONCLUSIVE and remain rejected.",
        ],
    }
    print("OPENRESEARCH_EVIDENCE_BEGIN")
    print(json.dumps(result, indent=2, sort_keys=True))
    print("OPENRESEARCH_EVIDENCE_END")


if __name__ == "__main__":
    main()
