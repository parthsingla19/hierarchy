"""
Your solution. See README.md — build it part by part. No server, no API calls.
"""

import json


def main():
    with open("accounts.json") as f:
        accounts = json.load(f)
    with open("activity.json") as f:
        activity = json.load(f)

    # Part 1: own totals + orphan detection
    # Part 2: rollup (recursive, using a parent->children map)
    # Part 3: root-level report


if __name__ == "__main__":
    main()
