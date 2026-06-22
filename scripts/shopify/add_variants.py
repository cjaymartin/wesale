#!/usr/bin/env python3
"""Add a clean 'Color' option + variants to existing single-variant products, surgically
(renames the default 'Title/Default Title' option->value into the first color, then bulk-creates
the rest). Leaves copy/SEO/tags/status untouched. Idempotent: skips products already multi-variant.

Usage:
    python3 scripts/shopify/add_variants.py [handle ...]   # default: all defined
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from api import gql  # noqa: E402

# handle -> (price, [color display names])  — colors map 1:1 to CJ variants (see connect-progress.md)
PLAN = {
    "slow-feeder-bowl": ("27.00", ["Blue", "Pink", "Green"]),
    "lick-mat":         ("17.00", ["Blue", "Chocolate", "Green"]),
    "treat-puzzle-toy": ("22.00", ["Blue", "Hexagon Green", "Light Green", "Paw Print Blue", "Pink"]),
    "lick-plate":       ("14.00", ["Blue", "Green", "Pink", "Purple", "Yellow"]),
    "treat-ball":       ("27.00", ["Green", "Red"]),
    "rope-tug-toy":     ("19.00", ["Blue", "Multicolor"]),
}

Q = """query($q:String!){ products(first:1, query:$q){ nodes{ id handle
  options{ id name optionValues{ id name } }
  variants(first:30){ nodes{ id title } } } } }"""
M_OPT = """mutation($pid:ID!,$opt:OptionUpdateInput!){
  productOptionUpdate(productId:$pid, option:$opt, variantStrategy:LEAVE_AS_IS){
    userErrors{ field message } } }"""
M_CREATE = """mutation($pid:ID!,$v:[ProductVariantsBulkInput!]!,$s:ProductVariantsBulkCreateStrategy!){
  productVariantsBulkCreate(productId:$pid, variants:$v, strategy:$s){
    productVariants{ id title } userErrors{ field message } } }"""
M_PRICE = """mutation($pid:ID!,$v:[ProductVariantsBulkInput!]!){
  productVariantsBulkUpdate(productId:$pid, variants:$v){ userErrors{ field message } } }"""


def err(d, k):
    ue = d[k]["userErrors"]
    if ue:
        raise RuntimeError(f"{k}: {ue}")


def fetch(handle):
    n = gql(Q, {"q": f"handle:{handle}"})["products"]["nodes"]
    return n[0] if n else None


def do(handle):
    price, colors = PLAN[handle]
    p = fetch(handle)
    if not p:
        print(f"  ? {handle}: not found"); return
    pid = p["id"]
    opt = p["options"][0]
    have = {v["title"] for v in p["variants"]["nodes"]}
    standalone = (len(p["variants"]["nodes"]) == 1 and "Default Title" in have)

    # 1) rename the option name -> Color (only the name; never touch the value here)
    if opt["name"] != "Color":
        gql(M_OPT, {"pid": pid, "opt": {"id": opt["id"], "name": "Color"}})

    # 2) create missing colors; if a standalone 'Default Title' placeholder exists, remove it
    missing = [c for c in colors if c not in have]
    if missing:
        strat = "REMOVE_STANDALONE_VARIANT" if standalone else "DEFAULT"
        new = [{"optionValues": [{"optionName": "Color", "name": c}],
                "price": price, "inventoryPolicy": "DENY", "inventoryItem": {"tracked": False}}
               for c in missing]
        d = gql(M_CREATE, {"pid": pid, "v": new, "s": strat}); err(d, "productVariantsBulkCreate")

    # 3) normalise price + DENY on every variant
    allv = fetch(handle)["variants"]["nodes"]
    upd = [{"id": v["id"], "price": price, "inventoryPolicy": "DENY",
            "inventoryItem": {"tracked": False}} for v in allv]
    d = gql(M_PRICE, {"pid": pid, "v": upd}); err(d, "productVariantsBulkUpdate")
    final = [v["title"] for v in fetch(handle)["variants"]["nodes"]]
    print(f"  ✓ {handle}: {', '.join(final)}  @ ${price}")


if __name__ == "__main__":
    targets = sys.argv[1:] or list(PLAN.keys())
    for h in targets:
        if h not in PLAN:
            print(f"  ? {h}: not in PLAN"); continue
        do(h)
