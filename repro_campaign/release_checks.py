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

    page = (ROOT / "space_delta/pages/current-verification/page.md").read_text(
        encoding="utf-8"
    )
    for claim_id in range(1, 7):
        required = (
            f"## Claim {claim_id}",
            f".openresearch/artifacts/claim_{claim_id}/verifier.py",
            f".openresearch/artifacts/claim_{claim_id}/raw_results.json",
            f".openresearch/artifacts/claim_{claim_id}/independent_checker_output.json",
            f".openresearch/artifacts/claim_{claim_id}/negative_control_output.json",
        )
        if not all(token in page for token in required):
            raise AssertionError(f"Claim {claim_id} is incomplete on canonical page")

    logbook = json.loads(
        (ROOT / "space_delta/logbook.json").read_text(encoding="utf-8")
    )
    children = logbook["root"]["children"]
    if children[0]["slug"] != "current-verification":
        raise AssertionError("Current verification is not first in navigation")
    if any(
        not child["title"].startswith("Historical rejected baseline")
        for child in children[1:]
    ):
        raise AssertionError("Historical navigation labels are not explicit")

    return {
        "allowlisted_text_files": len(entries),
        "target_paths_unique": True,
        "utf8_text_only": True,
        "secret_scan_passed": True,
        "historical_entry_hashes_match": True,
        "manifest_matches": True,
        "canonical_claim_rows_complete": 6,
        "current_verifier_first": True,
        "historical_labels_exact": True,
    }
