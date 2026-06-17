#!/usr/bin/env python3
"""Explore raw CJ search results for several terms to find real product naming."""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cj_api  # noqa: E402

TERMS = ["lick mat", "snuffle mat", "slow feeder bowl", "collapsible dog bowl",
         "treat ball dog", "dog puzzle feeder", "snuffle ball"]


def run():
    for t in TERMS:
        d = cj_api.search(t, page_size=12)
        lst = (d.get("data") or {}).get("list") or []
        print(f"\n=== '{t}'  ({len(lst)} results) ===")
        for it in lst:
            name = (it.get("productNameEn") or it.get("productName") or "")[:60]
            cat = (it.get("categoryName") or "")[:20]
            price = str(it.get("sellPrice", ""))
            pid = it.get("pid", "")
            print(f"   ${price:>11} [{cat:20}] {name}  ({pid})")


if __name__ == "__main__":
    run()
