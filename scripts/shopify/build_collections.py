#!/usr/bin/env python3
"""Create the 3 NoseyMutt collections and assign products. Idempotent by handle."""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from api import gql  # noqa: E402

COLLECTIONS = [
    {"handle": "enrichment-collection", "title": "The Enrichment Collection",
     "desc": "Everything to keep their nose busy and their brain happy — bowls, mats, snuffle toys, and refills.",
     "members": "ALL"},
    {"handle": "bundles-kits", "title": "Bundles & Kits",
     "desc": "Save when you bundle. Our enrichment kits in one box.",
     "members": ["boredom-buster-starter-kit"]},
    {"handle": "refills", "title": "Refills",
     "desc": "Keep the games fresh — refill and rotate.",
     "members": ["lick-mat-refill-3pack"]},
]

Q_PRODUCTS = """{ products(first:50){ nodes{ id handle } } }"""
Q_FIND = """query($q:String!){ collections(first:1, query:$q){ nodes{ id handle } } }"""
M_CREATE = """mutation($i:CollectionInput!){ collectionCreate(input:$i){ collection{ id handle } userErrors{ field message } } }"""
M_ADD = """mutation($id:ID!, $ids:[ID!]!){ collectionAddProducts(id:$id, productIds:$ids){ collection{ id } userErrors{ field message } } }"""
Q_PUBS = """{ publications(first:20){ nodes{ id name } } }"""
M_PUBLISH = """mutation($id:ID!, $pid:ID!){ publishablePublish(id:$id, input:{publicationId:$pid}){ userErrors{ field message } } }"""


def errcheck(payload, key):
    ue = payload[key]["userErrors"]
    if ue:
        raise RuntimeError(f"{key} userErrors: {ue}")


def build():
    pmap = {n["handle"]: n["id"] for n in gql(Q_PRODUCTS)["products"]["nodes"]}
    pub = next((n["id"] for n in gql(Q_PUBS)["publications"]["nodes"] if n["name"] == "Online Store"), None)
    for c in COLLECTIONS:
        found = gql(Q_FIND, {"q": f"handle:{c['handle']}"})["collections"]["nodes"]
        if found:
            cid = found[0]["id"]; action = "exists "
        else:
            d = gql(M_CREATE, {"i": {"title": c["title"], "handle": c["handle"],
                                     "descriptionHtml": f"<p>{c['desc']}</p>"}})
            errcheck(d, "collectionCreate")
            cid = d["collectionCreate"]["collection"]["id"]; action = "created"
        members = list(pmap.values()) if c["members"] == "ALL" else [pmap[h] for h in c["members"]]
        d = gql(M_ADD, {"id": cid, "ids": members}); errcheck(d, "collectionAddProducts")
        if pub:
            gql(M_PUBLISH, {"id": cid, "pid": pub})
        print(f"  ✓ {action}  {c['handle']:22} ({len(members)} products)")
    print("\nDone — 3 collections.")


if __name__ == "__main__":
    build()
