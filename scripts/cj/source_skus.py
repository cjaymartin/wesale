#!/usr/bin/env python3
"""Search CJ for the best source product per NoseyMutt SKU. Prints concise candidates."""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cj_api  # noqa: E402

# (our SKU handle, search queries, must-contain-any keywords) — filter hard to real items
SKUS = [
    ("slow-feeder-bowl", ["slow feeder bowl", "dog maze bowl", "anti gulping dog bowl"],
     ["slow", "feeder", "maze", "gulp"]),
    ("lick-mat", ["lick mat dog", "dog licking mat", "pet lick pad"],
     ["lick"]),
    ("snuffle-toy", ["snuffle mat dog", "dog sniffing mat", "snuffle ball pet"],
     ["snuffle", "sniff", "forag", "nose work"]),
    ("treat-puzzle-toy", ["dog treat dispenser ball", "pet puzzle iq toy", "treat dispensing dog toy"],
     ["treat", "puzzle", "iq", "dispens"]),
    ("travel-bowl", ["collapsible dog bowl", "foldable pet travel bowl", "silicone folding dog bowl"],
     ["collaps", "fold", "travel"]),
]
PET = ("dog", "pet", "cat", "puppy", "doggie")


def fmt(item):
    name = (item.get("productNameEn") or item.get("productName") or "")[:58]
    pid = item.get("pid", "")
    price = item.get("sellPrice", "")
    listed = item.get("listedNum", item.get("addMarkStatus", ""))
    cat = (item.get("categoryName") or "")[:24]
    return f"      ${str(price):>10}  listed:{str(listed):>5}  [{cat:24}] {name}  (pid {pid})"


def relevant(item, must_any):
    name = (item.get("productNameEn") or item.get("productName") or "").lower()
    cat = (item.get("categoryName") or "").lower()
    is_pet = any(p in name for p in PET) or "pet" in cat
    hit = any(k in name for k in must_any)
    return is_pet and hit


def run():
    for handle, queries, must_any in SKUS:
        print(f"\n=== {handle} ===")
        seen = set()
        hits = []
        for q in queries:
            d = cj_api.search(q, page_size=20)
            lst = (d.get("data") or {}).get("list") or []
            if not d.get("result"):
                print(f"   query '{q}': ERROR {d.get('message')}")
                continue
            for it in lst:
                if it.get("pid") in seen or not relevant(it, must_any):
                    continue
                seen.add(it.get("pid"))
                hits.append(it)
        if not hits:
            print("   (no relevant pet matches via keyword search)")
        for it in hits[:6]:
            print(fmt(it))


if __name__ == "__main__":
    run()
