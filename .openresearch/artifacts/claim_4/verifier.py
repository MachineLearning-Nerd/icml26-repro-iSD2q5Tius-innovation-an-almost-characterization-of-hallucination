#!/usr/bin/env python3
import json
from repro_campaign.theorems import claim4
if __name__ == "__main__":
    print(json.dumps(claim4(), indent=2, sort_keys=True))

