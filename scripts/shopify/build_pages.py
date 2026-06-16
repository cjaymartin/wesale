#!/usr/bin/env python3
"""Create the NoseyMutt content pages. Idempotent by handle."""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from api import gql  # noqa: E402

PAGES = [
    {"handle": "about", "title": "About", "body": """<h2>We're NoseyMutt — and we're a little obsessed with bored dogs.</h2>
<p>It started with a dog who ate dinner like it was a race and treated the couch like a chew toy whenever she got bored. Walks helped. But the thing that <em>actually</em> tired her out? Letting her use her nose — sniffing, foraging, and working for her food.</p>
<p>Turns out a dog's nose is its superpower. Ten minutes of sniffing and problem-solving can do more for a busy brain than a long walk. So we built NoseyMutt: simple, food-safe enrichment gear that turns mealtime and downtime into a game — slowing fast eaters, busting boredom, and giving your dog's brain a real job.</p>
<p>No gimmicks, no medical promises — just smart, well-made tools that make for a calmer dog and a happier home.</p>
<p><strong>Keep their nose busy, their brain happy. 🐽</strong></p>
<p>Questions, photos of your nosey mutt, or just want to say hi? <a href="mailto:hello@noseymutt.com">hello@noseymutt.com</a></p>"""},
    {"handle": "faq", "title": "FAQ", "body": """<h3>How fast will my order arrive?</h3>
<p>Orders process in 1–3 business days and typically arrive within 5–12 business days. You'll get tracking by email as soon as it ships.</p>
<h3>Does the Starter Kit ship in one box?</h3>
<p>Yes — whenever possible we ship the bundle together in a single package.</p>
<h3>What size should I get?</h3>
<p>Small/Medium suits most dogs up to ~50 lbs; choose Large for bigger breeds or fast, powerful eaters. When in doubt, size up.</p>
<h3>Are the products safe? What are they made of?</h3>
<p>The bowl, lick mat, and travel bowl are food-safe silicone/plastic. The snuffle toy is machine-washable fabric. Always supervise your dog with any enrichment item, and replace anything that becomes damaged.</p>
<h3>Is this a chew toy?</h3>
<p>No — these are enrichment and slow-feeding tools, not indestructible chews. Heavy chewers should be supervised.</p>
<h3>Will this calm my dog down?</h3>
<p>Enrichment gives dogs a mental job, and a mentally tired dog tends to be a calmer, less destructive dog. We're not vets and don't make medical claims — for behavioral or health concerns, talk to your vet.</p>
<h3>Can I wash them?</h3>
<p>Yes. The bowl and lick mat are dishwasher-friendly; the snuffle toy is machine-washable. Freeze the lick mat with food on it to make sessions last longer.</p>
<h3>How do I reach you?</h3>
<p><a href="mailto:hello@noseymutt.com">hello@noseymutt.com</a> — we reply within 24 hours.</p>"""},
    {"handle": "shipping", "title": "Shipping Policy", "body": """<p><strong>Where we ship:</strong> United States (48 contiguous states to start).</p>
<p><strong>Processing time:</strong> Orders are processed within 1–3 business days.</p>
<p><strong>Delivery time:</strong> Most orders arrive within 5–12 business days after processing. Items in a bundle ship together in one package whenever possible; occasionally an item may arrive separately.</p>
<p><strong>Shipping cost:</strong> Free standard shipping on US orders over $35. Orders under $35 are a flat $4.95.</p>
<p><strong>Tracking:</strong> You'll get a tracking number by email as soon as your order ships. Allow 1–2 days for tracking to update.</p>
<p><strong>Delays:</strong> Carrier or customs delays can occasionally add a few days. If your order hasn't arrived in the window above, email us and we'll sort it out fast.</p>
<p>Questions? <a href="mailto:hello@noseymutt.com">hello@noseymutt.com</a> — we reply within 24 hours.</p>"""},
    {"handle": "returns", "title": "Returns & Refunds", "body": """<h2>Our 30-Day Happy-Dog Guarantee</h2>
<p>If your dog isn't more entertained — or something arrives wrong or damaged — we'll make it right within 30 days of delivery.</p>
<p><strong>Damaged, defective, or wrong item:</strong> Email <a href="mailto:hello@noseymutt.com">hello@noseymutt.com</a> with your order number and a quick photo or video. We'll send a free replacement or a full refund — no need to ship anything back in most cases.</p>
<p><strong>Changed your mind / not the right fit:</strong> Contact us within 30 days. Unused items in original condition can be returned; the customer covers return shipping for non-defective returns. Once we confirm the item's condition, we'll refund the product price.</p>
<p><strong>Refunds:</strong> Approved refunds are issued to your original payment method within 5–10 business days of approval.</p>
<p><strong>Not covered:</strong> Normal wear from heavy chewing (these are enrichment tools, not indestructible chew toys), or damage from misuse.</p>
<p>Start a return or claim: <a href="mailto:hello@noseymutt.com">hello@noseymutt.com</a>.</p>"""},
    {"handle": "contact", "title": "Contact", "templateSuffix": "contact",
     "body": """<p>Questions about an order, sizing, or your nosey mutt? Send us a message below or email <a href="mailto:hello@noseymutt.com">hello@noseymutt.com</a> — we reply within 24 hours (Mon–Fri).</p>"""},
]

Q_PAGES = """{ pages(first:50){ nodes{ id handle } } }"""
M_CREATE = """mutation($p:PageCreateInput!){ pageCreate(page:$p){ page{ id handle } userErrors{ field message } } }"""
M_UPDATE = """mutation($id:ID!, $p:PageUpdateInput!){ pageUpdate(id:$id, page:$p){ page{ id handle } userErrors{ field message } } }"""


def errcheck(payload, key):
    ue = payload[key]["userErrors"]
    if ue:
        raise RuntimeError(f"{key} userErrors: {ue}")


def build():
    existing = {n["handle"]: n["id"] for n in gql(Q_PAGES)["pages"]["nodes"]}
    for p in PAGES:
        body = {"title": p["title"], "handle": p["handle"], "body": p["body"], "isPublished": True}
        if "templateSuffix" in p:
            body["templateSuffix"] = p["templateSuffix"]
        if p["handle"] in existing:
            d = gql(M_UPDATE, {"id": existing[p["handle"]], "p": body}); errcheck(d, "pageUpdate")
            action = "updated"
        else:
            d = gql(M_CREATE, {"p": body}); errcheck(d, "pageCreate")
            action = "created"
        print(f"  ✓ {action}  /pages/{p['handle']}")
    print(f"\nDone — {len(PAGES)} pages.")


if __name__ == "__main__":
    build()
