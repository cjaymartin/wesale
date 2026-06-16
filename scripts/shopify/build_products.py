#!/usr/bin/env python3
"""Create/update the NoseyMutt catalog via the Admin GraphQL API. Idempotent by handle.

Run:  python3 scripts/shopify/build_products.py
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from api import gql  # noqa: E402

VENDOR = "NoseyMutt"
PTYPE = "Dog Enrichment"

PRODUCTS = [
    {
        "handle": "boredom-buster-starter-kit",
        "title": "The Boredom-Buster Starter Kit — Slow Feeder + Lick Mat + Snuffle Toy",
        "price": "59.00", "compare": "69.00",
        "tags": ["bundle", "starter-kit", "enrichment", "best-seller"],
        "seo_title": "Dog Enrichment Starter Kit — Slow Feeder, Lick Mat & Snuffle Toy | NoseyMutt",
        "seo_desc": "Stop boredom at the source. NoseyMutt's Boredom-Buster Starter Kit bundles a slow-feeder bowl, lick mat, and snuffle toy to slow fast eaters and tire out busy brains. Save $10.",
        "html": """<p>Bored dogs dig, bark, chew, and inhale their dinner in nine seconds flat. The Boredom-Buster Starter Kit gives their nose and brain a real job — three ways.</p>
<ul>
<li><strong>🥣 Slow-Feeder Bowl</strong> — turns a 9-second gulp-fest into a 9-minute puzzle. Easier on the tummy, harder on the boredom.</li>
<li><strong>👅 Lick Mat</strong> — spread on peanut butter or wet food, stick it to the wall, and buy yourself a calm 15 minutes (bath time, nail trims, Zoom calls).</li>
<li><strong>🐽 Snuffle Toy</strong> — hide kibble and let their nose do what it was born to do. Foraging = a tired, satisfied dog.</li>
</ul>
<p>Built for gulpers, diggers, and "my dog is bored and I feel guilty" parents. <strong>Save $10</strong> vs. buying separately.</p>
<ul>
<li>3-piece enrichment system — bowl + lick mat + snuffle toy</li>
<li>Slows fast eaters &amp; busts boredom (less chewing, barking, digging)</li>
<li>Food-safe silicone &amp; fabric — dishwasher-friendly bowl &amp; mat</li>
<li>Ships as one box · 30-day happy-dog guarantee</li>
</ul>""",
    },
    {
        "handle": "slow-feeder-bowl",
        "title": "Slow-Feeder Enrichment Bowl — Turn Gulping Into a Game",
        "price": "27.00", "compare": "34.00",
        "tags": ["enrichment", "slow-feeder", "bowl"],
        "seo_title": "Slow Feeder Dog Bowl — Stop Fast Eating & Gulping | NoseyMutt",
        "seo_desc": "For dogs that inhale dinner. NoseyMutt's slow-feeder bowl slows fast eaters, eases gulping and bloat, and turns mealtime into a puzzle. Lightweight, dishwasher-safe.",
        "html": """<p>If your dog finishes dinner before you've sat down, this is for them. The raised-maze design forces them to work for each bite — slowing fast eaters, easing bloat and gulping, and turning a 9-second scarf-down into a satisfying brain game.</p>
<ul>
<li>Slows fast eaters &amp; eases gulping/bloat</li>
<li>Non-slip base, dishwasher-friendly</li>
<li>Lightweight food-safe silicone/plastic — won't chip, crack, or break a toe (not ceramic)</li>
</ul>""",
    },
    {
        "handle": "lick-mat",
        "title": "Calm-Down Lick Mat — 15 Minutes of Peace, Stuck to the Wall",
        "price": "17.00", "compare": "22.00",
        "tags": ["enrichment", "lick-mat", "calming"],
        "seo_title": "Dog Lick Mat with Suction — Calm Grooming & Alone-Time | NoseyMutt",
        "seo_desc": "Smear it, stick it, walk away. NoseyMutt's suction lick mat keeps dogs busy and settled during baths, nail trims, and alone-time. Food-safe, freezer- and dishwasher-friendly.",
        "html": """<p>Spread on peanut butter, yogurt, or wet food, press the suction base to any smooth surface, and let the licking begin. Repetitive licking keeps dogs busy and settled during baths, nail trims, vet visits, alone-time, and your work calls.</p>
<ul>
<li>Suction base sticks to wall, floor, or tub</li>
<li>Freezer-friendly for longer sessions</li>
<li>Food-safe silicone, dishwasher-safe</li>
<li>Great for grooming &amp; alone-time</li>
</ul>""",
    },
    {
        "handle": "snuffle-toy",
        "title": "Snuffle Foraging Toy — Let Their Nose Do the Work",
        "price": "25.00", "compare": "32.00",
        "tags": ["enrichment", "snuffle", "foraging"],
        "seo_title": "Dog Snuffle Mat / Foraging Toy — Boredom Buster | NoseyMutt",
        "seo_desc": "A dog's nose is its superpower. NoseyMutt's snuffle foraging toy hides kibble so dogs sniff, forage, and tire out — a mental workout that beats a walk. Machine-washable.",
        "html": """<p>A dog's nose is its superpower — and using it is more tiring than a walk. Tuck kibble or treats into the folds and let your dog forage, sniff, and problem-solve their way to every piece.</p>
<ul>
<li>Mental workout that actually tires dogs out</li>
<li>Slows eating, builds foraging instinct</li>
<li>Machine-washable, folds flat</li>
<li>Great boredom-buster for alone-time</li>
</ul>""",
    },
    {
        "handle": "treat-puzzle-toy",
        "title": "Treat-Dispensing Puzzle Toy — Make Them Work For It",
        "price": "22.00", "compare": "28.00",
        "tags": ["enrichment", "puzzle", "treat-dispensing"],
        "seo_title": "Dog Treat-Dispensing Puzzle Toy — Mental Enrichment | NoseyMutt",
        "seo_desc": "Load it, drop it, watch the wheels turn. NoseyMutt's treat-dispensing puzzle toy makes dogs nudge and roll for every piece — adjustable difficulty, slows speed-eaters.",
        "html": """<p>Fill it with kibble or treats and let your dog nudge, roll, and paw to release each piece. Adjustable difficulty keeps clever dogs challenged and slows down speed-eaters.</p>
<ul>
<li>Adjustable difficulty</li>
<li>Slows eating, builds focus</li>
<li>Durable &amp; easy to clean</li>
<li>Pairs with the snuffle toy for rotation</li>
</ul>""",
    },
    {
        "handle": "travel-bowl",
        "title": "Collapsible Travel Enrichment Bowl — Foraging On The Go",
        "price": "15.00", "compare": "20.00",
        "tags": ["enrichment", "travel", "bowl"],
        "seo_title": "Collapsible Travel Dog Bowl — Foraging On The Go | NoseyMutt",
        "seo_desc": "Clips to the leash, pops open for snack hunts anywhere. NoseyMutt's collapsible travel bowl has a textured base for on-the-go foraging. Food-safe silicone, folds flat.",
        "html": """<p>A pocketable silicone bowl with a textured base that turns any rest stop into a mini foraging game. Folds flat, clips to a leash or bag with the carabiner, and rinses clean.</p>
<ul>
<li>Folds flat, clips on with carabiner</li>
<li>Textured base for on-the-go foraging</li>
<li>Food-safe silicone, easy rinse</li>
<li>Light enough to forget it's there</li>
</ul>""",
    },
    {
        "handle": "lick-mat-refill-3pack",
        "title": "Refill & Rotate — Lick Mat Variety 3-Pack",
        "price": "19.00", "compare": "24.00",
        "tags": ["refill", "lick-mat", "consumable"],
        "seo_title": "Dog Lick Mat Variety 3-Pack — Refill & Rotate | NoseyMutt",
        "seo_desc": "New textures = new fun. NoseyMutt's 3-pack of different-textured lick mats keeps the licking game fresh. Food-safe, freezer- and dishwasher-friendly.",
        "html": """<p>Dogs love novelty. This 3-pack of different-textured mats keeps the licking game fresh — rotate a new pattern each week to re-spark interest and stretch every session longer. Same food-safe, freezer-friendly, dishwasher-safe silicone.</p>
<ul>
<li>3 different textures to rotate</li>
<li>Keeps lick sessions novel &amp; longer</li>
<li>Food-safe, freezer- and dishwasher-friendly</li>
</ul>""",
    },
]

Q_FIND = """query($q:String!){ products(first:1, query:$q){ nodes{ id handle variants(first:1){nodes{id}} } } }"""
M_CREATE = """mutation($p:ProductCreateInput!){ productCreate(product:$p){ product{ id handle variants(first:1){nodes{id}} } userErrors{ field message } } }"""
M_UPDATE = """mutation($p:ProductUpdateInput!){ productUpdate(product:$p){ product{ id handle variants(first:1){nodes{id}} } userErrors{ field message } } }"""
M_VARIANT = """mutation($pid:ID!, $v:[ProductVariantsBulkInput!]!){ productVariantsBulkUpdate(productId:$pid, variants:$v){ userErrors{ field message } } }"""
Q_PUBS = """{ publications(first:20){ nodes{ id name } } }"""
M_PUBLISH = """mutation($id:ID!, $pid:ID!){ publishablePublish(id:$id, input:{publicationId:$pid}){ userErrors{ field message } } }"""


def errcheck(payload, key):
    ue = payload[key]["userErrors"]
    if ue:
        raise RuntimeError(f"{key} userErrors: {ue}")


def online_store_pub():
    for n in gql(Q_PUBS)["publications"]["nodes"]:
        if n["name"] == "Online Store":
            return n["id"]
    return None


def build():
    pub = online_store_pub()
    print(f"Online Store publication: {'found' if pub else 'NOT FOUND'}\n")
    for p in PRODUCTS:
        found = gql(Q_FIND, {"q": f"handle:{p['handle']}"})["products"]["nodes"]
        common = {
            "title": p["title"], "handle": p["handle"], "descriptionHtml": p["html"],
            "productType": PTYPE, "vendor": VENDOR, "tags": p["tags"], "status": "ACTIVE",
            "seo": {"title": p["seo_title"], "description": p["seo_desc"]},
        }
        if found:
            pid = found[0]["id"]
            vid = found[0]["variants"]["nodes"][0]["id"]
            d = gql(M_UPDATE, {"p": {**common, "id": pid}}); errcheck(d, "productUpdate")
            action = "updated"
        else:
            d = gql(M_CREATE, {"p": common}); errcheck(d, "productCreate")
            node = d["productCreate"]["product"]
            pid = node["id"]; vid = node["variants"]["nodes"][0]["id"]
            action = "created"
        # price + no inventory tracking on the default variant
        d = gql(M_VARIANT, {"pid": pid, "v": [{
            "id": vid, "price": p["price"], "compareAtPrice": p["compare"],
            "inventoryItem": {"tracked": False},
        }]}); errcheck(d, "productVariantsBulkUpdate")
        # publish to Online Store
        if pub:
            d = gql(M_PUBLISH, {"id": pid, "pid": pub}); errcheck(d, "publishablePublish")
        print(f"  ✓ {action:8} ${p['price']:>6}  {p['handle']}")
    print(f"\nDone — {len(PRODUCTS)} products.")


if __name__ == "__main__":
    build()
