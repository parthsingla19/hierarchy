"""
Your solution. See README.md — build it part by part. No server, no API calls.
"""

import json
from collections import defaultdict


def main():
    with open("accounts.json") as f:
        accounts = json.load(f)
    with open("activity.json") as f:
        activity = json.load(f)
    orphans = []
    balances = defaultdict(int)
    for txn in activity:
        acc_id = txn["account_id"]
        orphan = True
        for account_id, account_info in accounts.items():
            if account_id == acc_id:
                orphan = False
                balances[acc_id] += txn["amount_cents"]
                break
        if orphan:
            orphans.append(acc_id)
    print(balances)
    print(orphans)


if __name__ == "__main__":
    main()
