#!/usr/bin/env python3
"""Read-back summary of the NoseyMutt store build."""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from api import gql  # noqa: E402

Q = """{
  products(first:50){ nodes{ handle status totalInventory
    onlineStorePreviewUrl
    variants(first:1){ nodes{ price compareAtPrice } } } }
  collections(first:20){ nodes{ handle productsCount{ count } } }
  pages(first:50){ nodes{ handle title } }
  menus(first:20){ nodes{ handle items{ title } } }
}"""

d = gql(Q)
print("PRODUCTS")
for n in d["products"]["nodes"]:
    v = n["variants"]["nodes"][0]
    print(f"  {n['status']:7} ${v['price']:>6} (was {v['compareAtPrice']})  {n['handle']}")
print("\nCOLLECTIONS")
for n in d["collections"]["nodes"]:
    print(f"  {n['handle']:24} {n['productsCount']['count']} products")
print("\nPAGES")
for n in d["pages"]["nodes"]:
    print(f"  {n['title']:24} /pages/{n['handle']}")
print("\nMENUS")
for n in d["menus"]["nodes"]:
    print(f"  {n['handle']:10} -> {', '.join(i['title'] for i in n['items'])}")
