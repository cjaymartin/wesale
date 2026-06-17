#!/usr/bin/env python3
"""Add the 3 approved upsell products + set oversell protection (inventoryPolicy=DENY)
on the whole active catalog. Idempotent by handle."""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from api import gql  # noqa: E402

VENDOR = "NoseyMutt"
PTYPE = "Dog Enrichment"

UPSELLS = [
    {
        "handle": "lick-plate", "price": "14.00", "compare": "18.00",
        "title": "Lick & Calm Plate — Slow-Lick Treat Surface",
        "tags": ["enrichment", "lick", "upsell", "order-bump"],
        "seo_title": "Dog Lick Plate — Slow-Lick Calming Treat Surface | NoseyMutt",
        "seo_desc": "A second lick surface to rotate with your lick mat. Spread, freeze, and let them work for it — keeps the licking game fresh and the dog calm.",
        "html": """<p>Rotate a fresh lick surface into the mix. Spread on peanut butter or wet food, freeze it, and let your dog settle into a long, calming lick — perfect for bath time, alone-time, and crate training.</p>
<ul>
<li>A second lick format — rotate it with your lick mat so the game never gets boring</li>
<li>Freezer-friendly for longer sessions</li>
<li>Food-safe silicone, dishwasher-safe</li>
</ul>""",
    },
    {
        "handle": "treat-ball", "price": "27.00", "compare": "34.00",
        "title": "Roll & Forage Treat Ball — Adjustable Difficulty",
        "tags": ["enrichment", "treat-dispensing", "foraging", "upsell"],
        "seo_title": "Dog Treat-Dispensing Ball — Adjustable Foraging Toy | NoseyMutt",
        "seo_desc": "Load it, set the difficulty, and let your dog nudge and roll to release each piece. Rewards problem-solving and slows speed-eaters.",
        "html": """<p>Load it with kibble or treats, set the difficulty, and let your dog nudge, roll, and chase to release each piece. A moving target that rewards problem-solving and burns mental energy.</p>
<ul>
<li>Adjustable difficulty grows with your dog</li>
<li>Rolling, foraging fun — slows speed-eaters</li>
<li>Durable, easy to refill and rinse</li>
<li>Pairs with the snuffle &amp; puzzle toys for rotation</li>
</ul>""",
    },
    {
        "handle": "rope-tug-toy", "price": "19.00", "compare": "25.00",
        "title": "Tough Rope Tug Toy — Chew, Tug & Play",
        "tags": ["chew", "tug", "upsell"],
        "seo_title": "Tough Dog Rope Tug Toy — Chew & Play for Big Dogs | NoseyMutt",
        "seo_desc": "A rugged cotton rope for tug, fetch, and solo chewing — helps clean teeth and burn energy. Big and tough for medium-to-large dogs.",
        "html": """<p>A rugged, oversized cotton rope built for tug-of-war, fetch, and solo chewing. Helps clean teeth, burn energy, and give the jaws a job.</p>
<ul>
<li>Big &amp; tough — made for medium-to-large dogs</li>
<li>Tug, fetch, or solo chew</li>
<li>Natural cotton; helps clean teeth as they gnaw</li>
</ul>""",
    },
]

Q_FIND = """query($q:String!){ products(first:1, query:$q){ nodes{ id handle variants(first:1){nodes{id}} } } }"""
Q_ALL = """{ products(first:50){ nodes{ handle id variants(first:1){ nodes{ id } } } } }"""
M_CREATE = """mutation($p:ProductCreateInput!){ productCreate(product:$p){ product{ id handle variants(first:1){nodes{id}} } userErrors{ field message } } }"""
M_VARIANT = """mutation($pid:ID!, $v:[ProductVariantsBulkInput!]!){ productVariantsBulkUpdate(productId:$pid, variants:$v){ userErrors{ field message } } }"""
Q_PUBS = """{ publications(first:20){ nodes{ id name } } }"""
M_PUBLISH = """mutation($id:ID!, $pid:ID!){ publishablePublish(id:$id, input:{publicationId:$pid}){ userErrors{ field message } } }"""
Q_COLL = """query($q:String!){ collections(first:1, query:$q){ nodes{ id } } }"""
M_ADD = """mutation($id:ID!, $ids:[ID!]!){ collectionAddProducts(id:$id, productIds:$ids){ userErrors{ field message } } }"""


def errcheck(p, k):
    ue = p[k]["userErrors"]
    if ue:
        raise RuntimeError(f"{k}: {ue}")


def build():
    pub = next((n["id"] for n in gql(Q_PUBS)["publications"]["nodes"] if n["name"] == "Online Store"), None)
    coll = gql(Q_COLL, {"q": "handle:enrichment-collection"})["collections"]["nodes"][0]["id"]
    new_ids = []
    for p in UPSELLS:
        found = gql(Q_FIND, {"q": f"handle:{p['handle']}"})["products"]["nodes"]
        common = {"title": p["title"], "handle": p["handle"], "descriptionHtml": p["html"],
                  "productType": PTYPE, "vendor": VENDOR, "tags": p["tags"], "status": "ACTIVE",
                  "seo": {"title": p["seo_title"], "description": p["seo_desc"]}}
        if found:
            pid = found[0]["id"]; vid = found[0]["variants"]["nodes"][0]["id"]; action = "exists "
        else:
            d = gql(M_CREATE, {"p": common}); errcheck(d, "productCreate")
            node = d["productCreate"]["product"]; pid = node["id"]; vid = node["variants"]["nodes"][0]["id"]
            action = "created"
        gql(M_VARIANT, {"pid": pid, "v": [{"id": vid, "price": p["price"], "compareAtPrice": p["compare"],
                                           "inventoryItem": {"tracked": False}, "inventoryPolicy": "DENY"}]})
        if pub:
            gql(M_PUBLISH, {"id": pid, "pid": pub})
        new_ids.append(pid)
        print(f"  ✓ {action} ${p['price']:>6}  {p['handle']}")
    gql(M_ADD, {"id": coll, "ids": new_ids})
    print("  ✓ added 3 upsells to The Enrichment Collection")

    # Oversell protection: set inventoryPolicy=DENY on EVERY product's default variant
    print("\nSetting inventoryPolicy=DENY on all products (oversell protection):")
    for n in gql(Q_ALL)["products"]["nodes"]:
        vid = n["variants"]["nodes"][0]["id"]
        gql(M_VARIANT, {"pid": n["id"], "v": [{"id": vid, "inventoryPolicy": "DENY"}]})
        print(f"  ✓ DENY  {n['handle']}")


if __name__ == "__main__":
    build()
