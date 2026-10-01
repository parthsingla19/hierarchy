# Account Hierarchy Rollup

Pure script. No server, no API calls. Read two JSON files, join and roll up.
This mirrors "read JSON files, do back-and-forth ETL" — the actual BikeMap
task description.

## Files
- `accounts.json` — account_id -> {name, parent_id}. parent_id is null for a
  root (top-level) account.
- `activity.json` — list of {account_id, ts, amount_cents}. Represents
  revenue/usage events attributed directly to one account.
- `report.py` — your file.

Run: `python report.py`

## Part 1 — Own totals + orphan detection
For each account, sum the amount_cents of activity events directly
attributed to it (not descendants — just that account's own events).

Some activity may reference an account_id that doesn't exist in
accounts.json — report those separately as orphans, exclude them from totals.

Print each account's own total, sorted by account_id. Then print the orphan
account_ids.

Expected own totals:
    acc_child1: 2000
    acc_child2: 1500
    acc_grandchild1: 500
    acc_root1: 1000
    acc_root2: 3000
Expected orphans: acc_ghost

## Part 2 — Rollup (the new pattern)
Every account's "rollup total" = its own total + the rollup total of every
one of its direct children (which already includes THEIR children, and so
on — this is recursive).

Build a parent -> [children] map from accounts.json first. Then compute each
account's rollup. Think about the order: you can't compute a parent's
rollup until you know all its children's rollups — what does that tell you
about whether to use recursion or a specific processing order?

Expected rollups:
    acc_grandchild1: 500        (leaf — no children — own total only)
    acc_child1: 2500             (own 2000 + grandchild1's 500)
    acc_child2: 1500             (leaf)
    acc_root1: 5000              (own 1000 + child1's 2500 + child2's 1500)
    acc_root2: 3000              (leaf)

## Part 3 — Org-level report
Print just the ROOT accounts (parent_id is null) with their full rollup
total, sorted by name.

Expected:
    Org A: 5000
    Org B: 3000

## Edge cases to consider
- An account with no activity at all (own total 0, but may still have a
  nonzero rollup from children).
- What if accounts.json had a cycle (an account is its own ancestor)? Not
  present in this data, but say out loud how you'd detect/guard it.
