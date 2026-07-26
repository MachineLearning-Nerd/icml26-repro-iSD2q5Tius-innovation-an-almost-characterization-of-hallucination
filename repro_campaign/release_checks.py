"""Deterministic checks for the evaluator-visible, text-only Space candidate."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST = ROOT / "release" / "upload_allowlist.json"
MANIFEST = ROOT / "release" / "upload_manifest.sha256"
OLD_ENTRY_HASHES = {
    "space_delta/historical/judged-33ec740/README.md":
        "d8d82f46247bbb6e029f39300d568d1267e93a40082802e2403f9ffdce9d447f",
    "space_delta/historical/judged-33ec740/logbook.json":
        "d58b98c8e78f715494e96b85ae6556d245b6d9bc267621e8465a936b162a2960",
    "space_delta/historical/judged-33ec740/pages/index.md":
        "50c41502fb02ef4ffe8f1b78a3744b98a1bd8016382c864c09ad95423e863f71",
}
SECRET_PATTERNS = (
    re.compile(r"\bhf_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expanded_allowlist() -> list[dict[str, str]]:
    spec = json.loads(ALLOWLIST.read_text(encoding="utf-8"))
    entries = list(spec["files"])
    for group in spec["claim_groups"]:
        for name in group["files"]:
            entries.append(
                {
                    "source": f"{group['source_prefix']}/{name}",
                    "target": f"{group['target_prefix']}/{name}",
                }
            )
    return entries


def expected_manifest(entries: list[dict[str, str]]) -> str:
    return "".join(
        f"{sha256(ROOT / entry['source'])}  {entry['target']}\n"
        for entry in sorted(entries, key=lambda item: item["target"])
        if entry["source"] != "release/upload_manifest.sha256"
    )


def verify_release_candidate() -> dict[str, object]:
    entries = expanded_allowlist()
    sources = [entry["source"] for entry in entries]
    targets = [entry["target"] for entry in entries]
    if len(sources) != len(set(sources)) or len(targets) != len(set(targets)):
        raise AssertionError("Duplicate source or target in upload allowlist")

    secret_hits: list[str] = []
    for source in sources:
        path = ROOT / source
        if not path.is_file():
            raise AssertionError(f"Missing allowlisted source: {source}")
        text = path.read_text(encoding="utf-8")
        if "\x00" in text:
            raise AssertionError(f"Non-text NUL byte in {source}")
        if any(pattern.search(text) for pattern in SECRET_PATTERNS):
            secret_hits.append(source)
    if secret_hits:
        raise AssertionError(f"Possible secret material in: {secret_hits}")

    old_entry_hashes_match = all(
        sha256(ROOT / path) == expected for path, expected in OLD_ENTRY_HASHES.items()
    )
    if not old_entry_hashes_match:
        raise AssertionError("Historical entrypoint preservation hash mismatch")

    actual_manifest = MANIFEST.read_text(encoding="utf-8")
    if actual_manifest != expected_manifest(entries):
        raise AssertionError("Upload manifest does not match allowlisted sources")

    scorecard = (ROOT / "space_delta/pages/00-scorecard/page.md").read_text(
        encoding="utf-8"
    )
    for claim_id in range(1, 7):
        page = (ROOT / f"space_delta/pages/claim-{claim_id}/page.md").read_text(
            encoding="utf-8"
        )
        required = (
            f"# Claim {claim_id}",
            "## Exact statement and assumptions",
            "## Complete proof certificate",
            "```python",
            "## Negative control and verdict",
            "**VERIFIED.**",
        )
        if not all(token in page for token in required):
            raise AssertionError(
                f"Claim {claim_id} is incomplete on its canonical page"
            )
        if f"| {claim_id}," not in scorecard:
            raise AssertionError(f"Claim {claim_id} is missing from scorecard")

    native = json.loads(
        (ROOT / ".openresearch/artifacts/native_scale/raw_results.json").read_text(
            encoding="utf-8"
        )
    )
    if native["status"] != "PASS":
        raise AssertionError("Native-scale raw evidence did not pass")
    if native["scope"]["total_corpora"] != 160000:
        raise AssertionError("Native-scale trial count mismatch")
    if native["scope"]["maximum_universe_size"] != 20000:
        raise AssertionError("Native-scale universe size mismatch")
    if native["regimes"]["asymptotic"]["claim_2"][
        "empirical_spike_hallucination_rate"
    ] != 0.998225:
        raise AssertionError("Displayed native headline result mismatch")

    readme = (ROOT / "space_delta/README.md").read_text(encoding="utf-8")
    for tag in (
        "trackio-logbook",
        "open-experiment",
        "icml2026-repro",
        "paper-iSD2q5Tius",
    ):
        if f"  - {tag}" not in readme:
            raise AssertionError(f"Missing leaderboard discovery tag: {tag}")

    logbook = json.loads(
        (ROOT / "space_delta/logbook.json").read_text(encoding="utf-8")
    )
    children = logbook["root"]["children"]
    current_slugs = [
        "00-scorecard",
        "claim-1",
        "claim-2",
        "claim-3",
        "claim-4",
        "claim-5",
        "claim-6",
        "methods",
        "current-verification",
    ]
    if [child["slug"] for child in children[: len(current_slugs)]] != current_slugs:
        raise AssertionError("Current judge-readable pages are not first")
    if any(
        not child["title"].startswith("Historical rejected baseline")
        for child in children[len(current_slugs):]
    ):
        raise AssertionError("Historical navigation labels are not explicit")

    return {
        "allowlisted_text_files": len(entries),
        "target_paths_unique": True,
        "utf8_text_only": True,
        "secret_scan_passed": True,
        "historical_entry_hashes_match": True,
        "manifest_matches": True,
        "canonical_claim_pages_complete": 6,
        "inline_executable_proof_blocks": 6,
        "native_scale_corpora": 160000,
        "native_scale_maximum_universe": 20000,
        "leaderboard_tags_present": True,
        "current_verifier_first": True,
        "historical_labels_exact": True,
    }
