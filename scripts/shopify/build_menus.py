#!/usr/bin/env python3
"""Set the header (main-menu) and footer menus for NoseyMutt. Idempotent."""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from api import gql  # noqa: E402

Q_MENUS = """{ menus(first:20){ nodes{ id handle title } } }"""
Q_COLL = """query($q:String!){ collections(first:1, query:$q){ nodes{ id } } }"""
Q_PROD = """query($q:String!){ products(first:1, query:$q){ nodes{ id } } }"""
Q_PAGES = """{ pages(first:50){ nodes{ id handle } } }"""
M_UPDATE = """mutation($id:ID!,$t:String!,$h:String!,$items:[MenuItemUpdateInput!]!){ menuUpdate(id:$id,title:$t,handle:$h,items:$items){ menu{ id handle } userErrors{ field message } } }"""
M_CREATE = """mutation($t:String!,$h:String!,$items:[MenuItemCreateInput!]!){ menuCreate(title:$t,handle:$h,items:$items){ menu{ id handle } userErrors{ field message } } }"""


def errcheck(payload, key):
    ue = payload[key]["userErrors"]
    if ue:
        raise RuntimeError(f"{key} userErrors: {ue}")


def build():
    coll = gql(Q_COLL, {"q": "handle:enrichment-collection"})["collections"]["nodes"][0]["id"]
    prod = gql(Q_PROD, {"q": "handle:boredom-buster-starter-kit"})["products"]["nodes"][0]["id"]
    pages = {n["handle"]: n["id"] for n in gql(Q_PAGES)["pages"]["nodes"]}
    menus = {n["handle"]: n for n in gql(Q_MENUS)["menus"]["nodes"]}

    main_items = [
        {"title": "Home", "type": "FRONTPAGE"},
        {"title": "Shop", "type": "COLLECTION", "resourceId": coll},
        {"title": "Starter Kit", "type": "PRODUCT", "resourceId": prod},
        {"title": "About", "type": "PAGE", "resourceId": pages["about"]},
    ]
    footer_items = [
        {"title": "About", "type": "PAGE", "resourceId": pages["about"]},
        {"title": "FAQ", "type": "PAGE", "resourceId": pages["faq"]},
        {"title": "Shipping", "type": "PAGE", "resourceId": pages["shipping"]},
        {"title": "Returns", "type": "PAGE", "resourceId": pages["returns"]},
        {"title": "Contact", "type": "PAGE", "resourceId": pages["contact"]},
    ]
    targets = [("main-menu", "Main menu", main_items), ("footer", "Footer", footer_items)]
    for handle, title, items in targets:
        if handle in menus:
            d = gql(M_UPDATE, {"id": menus[handle]["id"], "t": menus[handle]["title"] or title,
                               "h": handle, "items": items}); errcheck(d, "menuUpdate")
            action = "updated"
        else:
            d = gql(M_CREATE, {"t": title, "h": handle, "items": items}); errcheck(d, "menuCreate")
            action = "created"
        print(f"  ✓ {action}  {handle:10} ({len(items)} items)")
    print("\nDone — menus set.")


if __name__ == "__main__":
    build()
