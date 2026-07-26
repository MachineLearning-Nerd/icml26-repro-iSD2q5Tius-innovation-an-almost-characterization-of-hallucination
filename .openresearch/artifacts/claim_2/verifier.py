#!/usr/bin/env python3
import json
from repro_campaign.theorems import claim2
if __name__ == "__main__":
    print(json.dumps(claim2(), indent=2, sort_keys=True))

