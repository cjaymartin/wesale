# NoseyMutt — Go-Live Checklist (follow when ready to start selling)

This takes the store from **trial (password-locked)** to **live and taking real orders**.
A human (or an agent driving the browser) can follow this top to bottom. Anything marked
**[needs you]** requires a human decision, a card, or bank/ID info.

## Store facts (current)
- Shopify store: **34zb0n-hp.myshopify.com** — admin: https://admin.shopify.com/store/34zb0n-hp
- Shopify account (owner): **noseymuttstore@gmail.com** (C.Jay Martin) — sign in with Google
- Plan: **trial** (3-day, no card on file) → must pick a paid plan to go live
- Store name is currently **"My Store"** → change to **NoseyMutt** (step 1)
- Admin API token (for scripts) lives in `wesale/.env` (SHOPIFY_ADMIN_TOKEN). `python3 scripts/shopify/api.py ping` to verify.
- CJ is linked (account noseymuttstore@gmail.com, CJ shopId 2606221241263535400); all 7 active products connected with inventory sync ON.

## 0. Pre-flight (do first, ~10 min) — mostly free
- [ ] **Store name → NoseyMutt**: Settings → General → Store details → Store name = "NoseyMutt". Also set sender email / customer-facing email.
- [ ] **Verify catalog**: `python3 scripts/shopify/verify.py` — confirm 5 active core SKUs + 3 upsells, drafts still draft (travel-bowl, lick-mat-refill-3pack).
- [ ] **Logo + theme**: new store uses the default theme. Re-apply branding — upload logo from `storefront/brand-assets/` (Online Store → Themes → Customize → header logo). Set brand colors. (See `NoseyMutt-Shopify-Setup-Guide.docx`.)
- [ ] **Policies**: confirm Shipping, Returns, Privacy, Contact pages exist (they do — built via API) and are linked in the footer menu. Settings → Policies: paste refund/privacy/TOS (Shopify can generate templates).
- [ ] **Standards/branding email**: Settings → Notifications → sender = a noseymutt address you control.

## 1. Pick a plan + add card **[needs you]**
- [ ] Admin → **Settings → Plan** (or the "Select a plan" button). Choose **Basic** (~$39/mo; often $1/mo for first 3 months promo).
- [ ] Enter card. (This is the first real cost. Budget impact: ~$39/mo or $1 promo.)

## 2. Payments **[needs you]** — so you can actually collect money
- [ ] Settings → **Payments** → activate **Shopify Payments** (needs business type, EIN/SSN, bank account for payouts). US-based.
- [ ] If Shopify Payments isn't an option, enable **PayPal** and/or a third-party gateway.
- [ ] Do a **test transaction** (Shopify Payments test mode, or a $1 real order you refund).

## 3. Shipping rates — don't lose margin or scare buyers
- [ ] Settings → **Shipping and delivery** → General profile.
- [ ] Recommended for launch: **Free shipping** (bake ~$5 into prices; CJ China→US is cheap on the chosen methods) OR a flat **$4.99**.
- [ ] Remove/disable any carrier-calculated rates. One simple domestic (US) zone with one rate.
- [ ] Note: CJ ships from China (most SKUs) / US warehouse (Treat Ball). Delivery ~8–15 days (China lines) / 3–7 days (US). Set buyer expectations on the Shipping page + product pages.

## 4. Taxes (US) **[needs you]**
- [ ] Settings → **Taxes and duties** → United States. Let Shopify Tax auto-calc; register for sales tax only where you have nexus (start: your home state). Low priority at launch volume but set the region.

## 5. Custom domain (optional, recommended) **[needs you]**
- [ ] Settings → **Domains** → Buy (`noseymutt.com` if available, ~$11–15/yr) or Connect an existing one.
- [ ] Set it primary; verify SSL is issued. Until then the store runs on 34zb0n-hp.myshopify.com.

## 6. Final QA before unlocking
- [ ] Click through every **active** product — images, price, variants, "Add to cart" works.
- [ ] Confirm draft products (travel-bowl, lick-mat-refill-3pack) are **not** visible.
- [ ] Place a **full test order** end-to-end (checkout → CJ receives it). With CJ inventory sync ON + inventoryPolicy=DENY, out-of-stock variants won't oversell.
- [ ] Confirm the order appears in **CJ → Orders** and can be paid/fulfilled. (You front the CJ cost; CJ ships to the customer.)
- [ ] Check order confirmation + shipping notification emails look right.

## 7. Remove the password = GO LIVE **[needs you — irreversible-ish]**
- [ ] Online Store → **Preferences** → scroll to **Password protection** → **uncheck "Restrict access"** → Save.
- [ ] The store is now public and selling. 🎉

## 8. Day-1 after launch
- [ ] Submit sitemap to Google Search Console; verify the domain.
- [ ] Turn on the marketing channels from the marketing plan (cheap-first: SEO blog, Pinterest, TikTok organic, then small paid tests). See `marketing/` docs.
- [ ] Watch the first orders; fulfill via CJ promptly; confirm tracking flows back to Shopify.

## Rough first costs
- Shopify Basic: ~$39/mo (or $1/mo promo 3 mo) · Domain: ~$12/yr · CJ: pay-per-order (product + shipping, you keep the margin) · Ads: optional, start small.

## Starter Kit ($59) — fulfillment **[action needed]**
The kit (bowl + lick mat + snuffle) is built in Shopify and ACTIVE, but it is **not connected to a
single CJ product**. CJ's "combined product" (one CJ SKU that ships all 3) is **not a self-serve
action** in this account — it's a CJ Prime / support-assisted feature (no "Combine" option exists in
My Products → Added Products row actions; only Packaging/Cart/Collection/Delete).
Two ways to handle kit orders:
- **Manual (works today):** when a kit sells, place **3 CJ orders** to the customer's address —
  Slow Feeder Bowl + Calm-Down Lick Mat + Snuffle Mat (~$21 CJ cost vs $59 retail). Fine for low volume.
- **Automated (set up later):** ask **CJ support** to create a combined SKU for these 3, then connect it
  to the kit in CJ → Store Products; OR install a Shopify bundle app that splits the bundle into its 3
  components so CJ auto-imports each. Until then, consider **drafting the kit** if you don't want manual orders.

## Open follow-ups (not blockers)
- Rope Tug Toy is single-color (CJ variant-cache wouldn't refresh). To offer rope colors: re-run CJ **Specific Sync** after a longer wait, then re-add colors in Shopify + connect (see `scripts/cj/connect-progress.md`).
- Snuffle retail is $32 but new CJ cost is only $7.25 — consider testing a lower price (e.g. $24–27) for conversion.
