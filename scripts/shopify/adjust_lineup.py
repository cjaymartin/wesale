#!/usr/bin/env python3
"""Lock the launch lineup: draft the 2 dropped SKUs, reprice the snuffle. Idempotent."""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from api import gql  # noqa: E402

Q_FIND = """query($q:String!){ products(first:1, query:$q){ nodes{ id handle status variants(first:1){nodes{id}} } } }"""
M_UPDATE = """mutation($p:ProductUpdateInput!){ productUpdate(product:$p){ product{ id status } userErrors{ field message } } }"""
M_VARIANT = """mutation($pid:ID!, $v:[ProductVariantsBulkInput!]!){ productVariantsBulkUpdate(productId:$pid, variants:$v){ userErrors{ field message } } }"""


def errcheck(p, k):
    ue = p[k]["userErrors"]
    if ue:
        raise RuntimeError(f"{k}: {ue}")


def find(handle):
    n = gql(Q_FIND, {"q": f"handle:{handle}"})["products"]["nodes"]
    return n[0] if n else None


# 1) draft the two dropped SKUs
for h in ["travel-bowl", "lick-mat-refill-3pack"]:
    p = find(h)
    if not p:
        print(f"  ? {h}: not found"); continue
    d = gql(M_UPDATE, {"p": {"id": p["id"], "status": "DRAFT"}}); errcheck(d, "productUpdate")
    print(f"  ✓ drafted  {h}")

# 2) reprice the snuffle to $32 (compare-at $39)
p = find("snuffle-toy")
if p:
    vid = p["variants"]["nodes"][0]["id"]
    d = gql(M_VARIANT, {"pid": p["id"], "v": [{"id": vid, "price": "32.00", "compareAtPrice": "39.00"}]})
    errcheck(d, "productVariantsBulkUpdate")
    print("  ✓ snuffle-toy repriced -> $32 (was-compare $39)")

print("\nLineup locked: Kit, Bowl, Lick Mat, Snuffle ($32), Treat Puzzle = 5 active SKUs.")
