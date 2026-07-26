#!/usr/bin/env python3
"""Standalone wrapper for the primary Claim 1 verifier."""

import json

from repro_campaign.claim1 import verify_claim1


if __name__ == "__main__":
    print(json.dumps(verify_claim1(), indent=2, sort_keys=True))

