#!/usr/bin/env python3
"""Standalone wrapper for the independent Claim 1 checker."""

import json

from repro_campaign.independent_claim1 import independent_check


if __name__ == "__main__":
    print(json.dumps(independent_check(), indent=2, sort_keys=True))

