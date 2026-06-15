# NoseyMutt — Click-Level Shopify Setup Walkthrough (from ZERO)

> For a store owner who has **never** used Shopify. Read it top to bottom and do each numbered
> step in order. Every step tells you what to click, what to type, and what the choice means.
>
> **Company:** wesale · **Brand:** NoseyMutt · **Hero product:** Boredom-Buster Starter Kit ($59)
> **Budget:** $500 total. Keep the platform near $0 until a product proves it sells.
> **Source files you'll copy from:** `catalog.md` (products + copy), `brand.md` (colors/fonts),
> `pages/` (page + policy text), `setup-checklist.md` (the high-level plan this expands).
>
> ⚠️ **UI labels move.** Shopify redesigns its admin a few times a year. Button *names* and
> menu *order* may differ slightly from this guide. The **concepts** are stable — if a label is
> missing, look for the nearest equivalent or use the admin search bar (press `/` or click the
> magnifying glass at the top). Spots most likely to have shifted are flagged with 🔀.
>
> 💲 **Money rule:** the moment you spend a single dollar (domain, logo, anything), write it in
> `finance/budget.md` **before or right after** you pay. Every cost line below repeats this.

---

## What you'll need before you start (gather these first — 15 min)

Have all of this open/ready in browser tabs so you never get stuck mid-setup:

1. **A business email inbox** you control — e.g. a Gmail like `noseymutt.store@gmail.com`. You'll
   use this to sign up for Shopify, PayPal, and the dropship apps. (Customer-facing
   `hello@noseymutt.com` comes later via domain forwarding — see Phase 2.)
2. **A bank account + routing/account numbers** (US checking account). Shopify Payments deposits
   your sales here. A personal checking account is fine to start as a sole proprietor.
3. **Your tax ID** — your **SSN** (sole proprietor) or **EIN** if you've registered a business.
   Shopify Payments legally must collect this.
4. **A phone number** that can receive SMS (used for 2-factor login codes).
5. **A debit/credit card** to pay the ~$1/mo Shopify charge and the domain (~$11).
6. **A PayPal account email** (you'll create a PayPal Business account in Phase 8 — have a login
   ready or be ready to make one).
7. **A logo file** (optional). Free path: Canva or Shopify's free logo maker. A simple
   "NoseyMutt" wordmark is enough to launch. If you buy one on Fiverr (~$15), 💲 log it.
8. **Product images** — start with clean supplier photos from CJ/AliExpress. Swap in your own
   photos once the sample order arrives (own photos convert better and are ad-safe).
9. **This file, plus `catalog.md`, `brand.md`, and the `pages/` folder** open side-by-side so you
   can copy-paste copy and color codes.

**Brand quick-reference (from `brand.md`) — keep this visible:**

| Use | Color | Hex |
|---|---|---|
| Ink (text / near-black) | brown-black | `#2B2A28` |
| Cream (background) | off-white | `#FBF6EE` |
| Mustard (primary / buttons) | gold | `#F2B33D` |
| Clay (accent) | warm red | `#E8674C` |
| Sage (secondary / trust) | green | `#7E9B6E` |

- **Heading font:** Poppins (or Quicksand) · **Body font:** Inter — all free Google Fonts.
- **One-liner:** "Keep their nose busy, their brain happy."
- **Hard rule:** never make medical claims (no "treats anxiety/cures/reduces cortisol"). Market
  boredom relief, slower eating, mental stimulation, foraging fun only. This protects ad accounts.

---

# PHASE 1 — Create the Shopify account + take the $1/mo promo
**⏱️ ~30 min · 💲 ~$1 today, ~$3 total over 3 months**

> **What this phase does:** opens your store and locks in the cheap promo so the platform costs
> almost nothing during the test window.
>
> **Verified pricing (June 2026, from [shopify.com/pricing](https://www.shopify.com/pricing)):**
> 3 days free, then **$1/month for 3 months** on a standard plan, then **Basic = $39/mo monthly
> or $29/mo if paid annually**. Second tier is now called **"Grow"** ($105/mo), and the top tier
> **"Advanced"** ($399/mo). Card processing on Basic = **2.9% + 30¢** online with Shopify Payments,
> and a **2% extra fee only if you use a third-party gateway** instead of Shopify Payments.
> 🔀 Shopify renamed the middle plan from "Shopify" to "Grow" recently — don't be confused if
> older guides say "Shopify plan."

1. Open a browser and go to **`shopify.com`**.
2. Click **"Start free trial"** (top-right). 🔀 It may say "Start free trial" or "Get started."
3. Shopify shows a few quick setup questions (e.g., "Where would you like to sell?", "What do you
   want to sell?"). Answer honestly — pick **"I'm just starting"** and **"Online store"**. These
   only customize hints; they don't lock you into anything. You can click **Skip** on most of them.
4. **Create your login.** Enter your business email from the prerequisites, then either continue
   with email (you'll set a password) or use "Continue with Google." Use the **business** email,
   not a personal one you'll lose access to.
5. Shopify creates a temporary store URL like `noseymutt-xxxx.myshopify.com`. **This is normal** —
   it's your permanent back-end address. Customers will see `noseymutt.com` once you connect the
   domain in Phase 2. Do **not** waste time trying to change the `.myshopify.com` part; it can't be
   changed later, but it's invisible to customers.
6. You're now in the **Shopify admin** (your dashboard). The left sidebar has Home, Orders,
   Products, Customers, Marketing, Discounts, Content, Analytics, and **Settings** (bottom-left).
   Take 60 seconds to notice where Settings is — you'll use it constantly.
7. **Choose the plan / take the promo.** Go to **Settings → Plan** (or click the "Select a plan"
   / "Choose a plan" banner Shopify shows during the trial). 🔀 May appear as a top banner.
8. Pick the **Basic** plan. On the plan page you should see the **"$1/month for 3 months"** offer
   applied automatically. If you're asked for **monthly vs. yearly billing**, choose **Monthly**.
   ⚠️ **Critical gotcha:** the $1 promo applies to **monthly** billing only. If you pick **annual**
   now, you forfeit the $1 deal and get charged ~$348 upfront. Choose **Monthly** during the
   promo; you can switch to annual later *if* you prove a winner.
9. Enter your card. You'll be charged **$1** (or $0 today + $1/mo). Confirm the screen says
   "**$1/month for 3 months**, then $39/month." If it shows full price with no $1, **stop** — close
   and re-open via `shopify.com` "Start free trial" so the promo attaches. (The promo is for **new
   accounts only**.)
10. 💲 **Log it now** in `finance/budget.md`: `Shopify Basic — $1/mo promo (×3 = ~$3 total)`.
11. **Set your store name + basics.** Go to **Settings → General**. Set **Store name =** `NoseyMutt`.
    Set the **store currency = USD** and **store address** (your real address; required for tax and
    payments — it is not shown publicly).

**Common mistakes to avoid in Phase 1:**
- Signing up with an email you'll abandon. Use a permanent business inbox.
- Choosing annual billing during the promo (kills the $1 deal).
- Panicking about the `myshopify.com` URL — it's just the backend; customers never see it.
- Buying any paid app or upsell during signup. Everything we need has a **free tier**.

---

# PHASE 2 — Buy / connect the domain `noseymutt.com`
**⏱️ ~20–40 min (DNS can take up to 48h to fully propagate) · 💲 ~$11/yr**

> **What this phase does:** points the web address customers type (`noseymutt.com`) at your
> Shopify store, and sets up `hello@noseymutt.com` email forwarding.
>
> ⚠️ **Before you pay:** confirm `noseymutt.com` is still available and run a quick free **USPTO
> trademark search** ([tmsearch.uspto.gov](https://tmsearch.uspto.gov)) for "NoseyMutt" in pet
> classes. If a live mark conflicts, stop and pick a new name before spending anything.

**Option A — Buy the domain through Shopify (easiest, slightly pricier ~$15/yr):**
1. Go to **Settings → Domains**.
2. Click **"Buy new domain."**
3. Type `noseymutt.com` and press search. If available, click **Buy**, confirm the price
   (~$15/yr), and pay. Shopify auto-connects it — **no DNS steps needed**. This is the
   zero-hassle path; the extra few dollars buys you skipping the technical part.
4. 💲 Log the domain cost in `finance/budget.md`.

**Option B — Buy cheaper elsewhere (~$10–11/yr at Cloudflare/Namecheap) and connect it:**
1. At your registrar (Cloudflare Registrar is at-cost ~$10.44/yr; Namecheap often ~$7 first year),
   register `noseymutt.com`. 💲 Log the cost.
2. Back in Shopify: **Settings → Domains → "Connect existing domain."**
3. Type `noseymutt.com`, click **Next**. Shopify shows you two DNS records to add:
   - an **A record** pointing `@` to Shopify's IP (Shopify shows the exact IP, e.g. `23.227.38.x`).
   - a **CNAME** pointing `www` to `shops.myshopify.com`.
4. In a second tab, open your registrar's **DNS settings** and add those exact two records. Save.
5. Back in Shopify, click **Verify connection.** It may say "pending" for a few minutes to 48h —
   that's normal DNS propagation. Leave it; check back later.

**Set the primary domain + email forwarding (both options):**
6. In **Settings → Domains**, make sure `noseymutt.com` is set as the **primary domain** (the
   address customers see). Enable **"Redirect all traffic to this domain"** so the `www` and
   `myshopify.com` versions all forward to the clean `noseymutt.com`.
7. **Email:** at your registrar (or in Shopify's domain settings if you bought through Shopify),
   set up a **forwarding rule** so `hello@noseymutt.com` forwards to your business Gmail. This
   gives you a professional support address for free. Test it by emailing `hello@noseymutt.com`
   from your phone and confirming it lands in Gmail.

**Common mistakes to avoid in Phase 2:**
- Paying without checking trademark first.
- Forgetting to set `noseymutt.com` as **primary** — your store will still show the ugly
  `myshopify.com` URL to customers.
- Expecting DNS to work instantly. Give it up to 48h before troubleshooting.
- Skipping email forwarding — ad platforms and Shopify Payments expect a real on-domain contact.

---

# PHASE 3 — Install + customize the free Dawn theme
**⏱️ ~45–60 min · 💲 $0**

> **What this phase does:** sets your store's look — colors, fonts, logo — using Shopify's free,
> fast, well-supported **Dawn** theme (the default on every new store; powers 268k+ stores as of
> 2026). Do **not** buy a paid theme during validation.

1. Go to **Online Store → Themes** (left sidebar; if you don't see "Online Store," it's under
   **Sales channels** — click the **+** to add the Online Store channel first). 🔀
2. Dawn is usually pre-installed as your **current theme**. If not, scroll to **"Theme library"** →
   **"Add theme" / "Visit theme store" → free themes → Dawn → Add**. Confirm Dawn is your live
   theme.
3. Click **Customize** next to Dawn. This opens the **theme editor**: a live preview in the middle,
   a section list on the left, and settings on the right.
4. **Set brand colors.** In the editor, click the **Theme settings** icon (a paint-roller / gear at
   the bottom-left of the editor) → **Colors**. Dawn uses "color schemes" (reusable swatches).
   Set up at least these, using the hex codes from `brand.md`:
   - **Scheme 1 (default page):** Background `#FBF6EE` (Cream), Text `#2B2A28` (Ink),
     Buttons/Solid `#F2B33D` (Mustard), Button label `#2B2A28` (Ink so the gold button text is
     readable).
   - **Scheme 2 (accent sections):** Background `#2B2A28` or `#E8674C` (Clay) for contrast bands,
     with Cream text.
   - Use **Sage `#7E9B6E`** for trust/secondary elements (badges, "free shipping" bars).
   To enter a hex: click the color swatch → type the 6-character code (no `#` needed in some
   fields) → Enter.
5. **Set fonts.** Theme settings → **Typography**. Set **Headings = Poppins** (or Quicksand if
   Poppins isn't listed) and **Body = Inter**. Click the font picker → search the name → select.
   These are free Google Fonts already bundled in Shopify's font library.
6. **Add the logo.** Theme settings → **Logo** (sometimes under "Header"). Click **Select image**,
   upload your NoseyMutt wordmark PNG (transparent background looks best). Set a sensible **logo
   width** (~120–160px). If you have no logo yet, leave the text store name showing — you can add
   the logo later.
7. **Favicon** (the tiny browser-tab icon). Theme settings → **Favicon** → upload a small square
   version of the logo/glyph (32×32 works).
8. **Buttons / corners.** Theme settings → **Buttons** (or "Inputs"). A slightly **rounded** corner
   radius matches NoseyMutt's friendly, rounded brand. Keep it subtle.
9. Click **Save** (top-right). Nothing is public yet — the store still has a password page
   (Phase 13 removes it).

**Common mistakes to avoid in Phase 3:**
- Picking a button color so light the text disappears. Gold button + dark Ink label = readable.
- Buying a premium theme "to look professional." Dawn converts fine; spend that money on ads.
- Forgetting to **Save** — the editor doesn't auto-publish.
- Using huge logo widths that break the mobile header.

---

# PHASE 4 — Create the products from `catalog.md`
**⏱️ ~1–2 h (7 products) · 💲 $0**

> **What this phase does:** builds your product pages with exact titles, descriptions, prices, and
> variants. Copy the text straight from `catalog.md`. Build them in priority order: **(1) Starter
> Kit first** (it's the hero — all ads point here), then Slow-Feeder Bowl, Lick Mat, Snuffle Toy,
> Treat Puzzle, Travel Bowl, then the Refill 3-Pack last.
>
> **For each product:** Products → **Add product**, then fill the fields below. Click **Save** when
> done with each.

### 4A. The hero — Boredom-Buster Starter Kit (do this one first)

1. **Products → Add product.**
2. **Title** field — paste:
   `The Boredom-Buster Starter Kit — Slow Feeder + Lick Mat + Snuffle Toy`
3. **Description** (the big rich-text box) — paste the full description block from `catalog.md`
   (the "Bored dogs dig, bark, chew..." paragraph plus the three 🥣/👅/🐽 bullet lines and the
   "Save $10" line). Use the toolbar to make the three items a **bulleted list** and bold the lead
   words. Then add the four "above the fold" bullets as a second bulleted list (3-piece system /
   slows fast eaters / food-safe silicone / ships as one box · 30-day guarantee).
4. **Media** (images) — click **Add** and upload 5–8 clean product images. Drag the best
   lifestyle/hero shot to **first position** (that's the thumbnail). Add a short video if you have
   one. *(Use supplier images now; swap in your own once the sample arrives.)*
5. **Pricing** section:
   - **Price =** `59.00`
   - **Compare-at price =** `69.00` (this shows the slashed $69 so the $59 reads as a deal).
   - Leave **"Charge tax on this product"** checked (tax handled later in Settings).
   - **Cost per item** — optional; enter your landed cost once the sample confirms it
     (`[SAMPLE-NEEDED]`, est. ~$16). This drives the profit-margin readout; not customer-visible.
6. **Inventory:** uncheck **"Track quantity"** (the supplier holds stock, not you — you don't want
   Shopify marking it sold out). 🔀 Labeled "Track quantity" or "Inventory tracking." Make sure
   **"Continue selling when out of stock"** is on if tracking stays on.
7. **Shipping:** keep **"This is a physical product"** checked. Weight is optional for now.
8. **Variants** — this product has two option sets. Scroll to **Variants** → **Add options like
   size or color**:
   - Option 1 name: `Size` · values: `Small/Medium`, `Large` (Small/Medium is the default).
   - Option 2 name: `Color` · values: `Mustard`, `Sage`, `Clay` (match what the supplier actually
     stocks — delete any color the supplier doesn't carry).
   Shopify generates the combinations. You can leave one price ($59) across all variants. ⚠️ Only
   add colors/sizes the supplier truly has, or you'll oversell something you can't fulfill.
9. **Search engine listing (SEO)** — scroll to the bottom, click **Edit website SEO**:
   - **Page title =** `Dog Enrichment Starter Kit — Slow Feeder, Lick Mat & Snuffle Toy | NoseyMutt`
   - **Meta description =** the SEO description from `catalog.md` ("Stop boredom at the source…").
   - **URL handle =** `boredom-buster-starter-kit`.
10. **Status** (top-right) — set to **Active** so it can be published (the password page still
    hides the whole store until launch). Assign it to the **Online Store** sales channel.
11. **Save.**

### 4B–4F. The other six products — same steps, data from `catalog.md`

Repeat steps 1–11 for each, using the exact fields below. All have **Size S/M + L** and
**Color Mustard/Sage/Clay** variants *except the Refill 3-Pack* (no variants). Set
**"Track quantity" off** on all.

| # | Title (from catalog) | Handle | Price | Compare-at | SEO title |
|---|---|---|---|---|---|
| 2 | Slow-Feeder Enrichment Bowl — Turn Gulping Into a Game | `slow-feeder-bowl` | 27.00 | 34.00 | Slow Feeder Dog Bowl — Stop Fast Eating & Gulping \| NoseyMutt |
| 3 | Calm-Down Lick Mat — 15 Minutes of Peace, Stuck to the Wall | `lick-mat` | 17.00 | 22.00 | Dog Lick Mat with Suction — Calm Grooming & Alone-Time \| NoseyMutt |
| 4 | Snuffle Foraging Toy — Let Their Nose Do the Work | `snuffle-toy` | 25.00 | 32.00 | Dog Snuffle Mat / Foraging Toy — Boredom Buster \| NoseyMutt |
| 5 | Treat-Dispensing Puzzle Toy — Make Them Work For It | `treat-puzzle-toy` | 22.00 | 28.00 | Dog Treat-Dispensing Puzzle Toy — Mental Enrichment \| NoseyMutt |
| 6 | Collapsible Travel Enrichment Bowl — Foraging On The Go | `travel-bowl` | 15.00 | 20.00 | Collapsible Travel Dog Bowl — Foraging On The Go \| NoseyMutt |
| 7 | Refill & Rotate — Lick Mat Variety 3-Pack | `lick-mat-refill-3pack` | 19.00 | 24.00 | Dog Lick Mat Variety 3-Pack — Refill & Rotate \| NoseyMutt |

For each, paste the matching **Description**, **Bullets**, and **Hook** from `catalog.md` into the
description box.

⚠️ **Product 5 (Treat Puzzle) compliance gotcha:** source a **generic shape only** — never a KONG,
Nina Ottosson, or Outward Hound design or name. Don't use their brand names anywhere in the
listing or images.

⚠️ **Lick Mat / Travel Bowl are under $10 landed but priced $17/$15 retail — fine.** The brand rule
"nothing sold standalone under $10" refers to *retail price*; these are all above $10. Just never
price a single item below $10.

**Common mistakes to avoid in Phase 4:**
- Leaving **Track quantity ON** — Shopify will mark items sold out since you hold no stock.
- Forgetting the **compare-at price** — you lose the visual "sale" anchor.
- Adding variant colors/sizes the supplier can't fulfill.
- Skipping SEO fields — fill them now while the copy is in front of you.
- Saving products as **Draft** and forgetting to set **Active**.

---

# PHASE 5 — Build the collections
**⏱️ ~15 min · 💲 $0**

> **What this phase does:** groups products into shoppable categories used by the menu and
> homepage. Per `catalog.md` you need three.

1. **Products → Collections → Create collection.**
2. **Collection 1 — "The Enrichment Collection"** (your main shop / featured collection):
   - **Title =** `The Enrichment Collection`
   - **Collection type =** **Manual** (you pick products) is simplest with 7 SKUs. (Automated =
     auto-includes by rule/tag; not needed yet.)
   - Add **all 7 products**.
   - Add a short description ("Everything to keep their nose busy and brain happy.").
   - Set the SEO/handle to `enrichment-collection`. **Save.**
3. **Collection 2 — "Bundles & Kits":** Manual; add the **Boredom-Buster Starter Kit** (and future
   kits). Handle `bundles-kits`. **Save.**
4. **Collection 3 — "Refills":** Manual; add the **Refill & Rotate 3-Pack**. Handle `refills`.
   **Save.**

**Common mistakes:** forgetting to actually **add products** after creating the collection (empty
collection = blank page); making collections Automated with no matching tags (also blank).

---

# PHASE 6 — Create pages + legal policies
**⏱️ ~45 min · 💲 $0**

> **What this phase does:** adds the content + legal pages that customers (and ad platforms +
> Shopify Payments) require. Copy text from the `pages/` folder.

**Content pages:**
1. **Content → Pages → Add page.** Create each of these, pasting body text from the matching file:
   - **About** ← `pages/about.md`
   - **FAQ** ← `pages/faq.md`
   - **Shipping** ← `pages/shipping-policy.md` (must state realistic dropship delivery times)
   - **Returns** ← (use the returns text in `pages/returns-policy.md`)
   - **Contact** — give it the title "Contact." In the page **template** dropdown (right sidebar)
     choose **"page.contact"** so Shopify renders a working contact form. 🔀 Template name may be
     "contact" — pick the contact one. Add `hello@noseymutt.com` in the body too.
   Set each page **Visible** and **Save**.

**Legal policies (auto-generated templates):**
2. Go to **Settings → Policies** (🔀 sometimes "Settings → Legal" or under "Checkout"). You'll see
   fields for **Refund policy, Privacy policy, Terms of service, Shipping policy, Contact
   information.**
3. For each, click **"Create from template"** to insert Shopify's standard template, then **edit**
   to match NoseyMutt specifics from `pages/legal-contact.md` (company name, contact email,
   realistic shipping windows, 30-day guarantee). **Save.** These auto-link in the footer at
   checkout — required for Shopify Payments approval and ad approval.

⚠️ Read each template before publishing — the defaults have placeholder blanks (`[business
name]`, addresses, response times) you must fill in.

**Header + footer navigation:**
4. **Content → Menus** (🔀 "Navigation"). Edit the **Main menu** (header) to:
   `Home` · `Shop` (→ The Enrichment Collection) · `Starter Kit` (→ the hero product) · `About`.
5. Edit the **Footer menu** to include: **Shipping, Returns, FAQ, Contact, Privacy Policy, Terms of
   Service, Refund Policy** (link the policy items to the policy pages — Shopify lists them when you
   click "Add menu item → Policies").

**Common mistakes:** leaving template placeholders un-filled; forgetting to set the Contact page to
the contact **template** (no form otherwise); not linking policies in the footer.

---

# PHASE 7 — Build the homepage sections
**⏱️ ~45 min · 💲 $0**

> **What this phase does:** assembles the front page from Dawn "sections." Follow
> `pages/homepage.md` for the exact section order and copy. You're back in **Online Store →
> Themes → Customize**, with the **Home page** selected in the top page-dropdown.

Recommended Dawn sections, top to bottom (add via **"Add section"** in the left panel):
1. **Header** (already there) — logo, menu, cart. Optionally add an **announcement bar** above it:
   "Free US shipping over $35 · 30-day happy-dog guarantee" in Mustard.
2. **Image banner / Hero** — headline `Keep their nose busy, their brain happy.`, subtext about
   busting boredom, and a **button → the Boredom-Buster Starter Kit**. Upload a strong dog photo.
3. **Featured collection** — point it at **The Enrichment Collection** so the grid of products
   shows. Set it to show all/most products.
4. **Featured product** (optional) — feature the **Starter Kit** with its Add-to-Cart.
5. **Rich text / "Why enrichment"** — short brand story (sniff/forage/slow-eat), warm and plain.
6. **Multicolumn** — 3 icons/benefits: "Slows fast eaters," "Busts boredom," "Ships as one box."
7. **Collage / image-with-text** — show the three kit pieces (bowl + mat + snuffle).
8. **Reviews** — leave a placeholder; the reviews app (later, optional) injects here. Seed reviews
   honestly with sample-order photos; **never fabricate**.
9. **Newsletter signup** — captures emails for later.
10. **Footer** — auto-shows the footer menu/policies from Phase 6.

After arranging, click **Save**. Then click the **mobile preview icon** (phone icon at top of
editor) and check it top-to-bottom — **most of your traffic is mobile**.

**Common mistakes:** hero button not linking to the Starter Kit; featured collection pointing at
the wrong (or empty) collection; never checking mobile; walls of text (keep it punchy per
`brand.md` voice).

---

# PHASE 8 — Set up Shopify Payments + PayPal
**⏱️ ~15–20 min · 💲 $0 (fees come out of each sale, not your budget)**

> **What this phase does:** lets you actually take money. Shopify Payments is the cheapest option
> here — **2.9% + 30¢** and **no extra platform fee**. A third-party-only gateway would add **2%**
> on Basic, so we use Shopify Payments as primary and PayPal as a secondary express button.

1. Go to **Settings → Payments.**
2. Under **Shopify Payments**, click **"Complete account setup"** (or "Activate"). 🔀
3. Fill in the business details:
   - **Business type:** "Individual / Sole proprietor" (unless you have an LLC/EIN).
   - **Personal details + SSN/EIN**, business address, product description ("dog enrichment
     products").
   - **Bank account:** routing + account number where payouts deposit.
4. **Save / Submit.** Shopify verifies in seconds to a couple of days. Until verified, you can keep
   building.
5. **Add PayPal as secondary.** On the same Payments page, find the **PayPal** row → **Activate /
   Set up** → log in with (or create) a **PayPal Business** account using your business email →
   authorize. This adds the yellow PayPal express button at checkout (lifts conversion).
6. ⚠️ **Do NOT enable any third-party credit-card gateway** (Stripe-direct, Authorize.net, etc.) —
   on Basic that triggers the extra **2%** fee. Shopify Payments + PayPal only.
7. **Test mode for QA:** later, in **Settings → Payments → Shopify Payments → Manage → "Use test
   mode,"** you can simulate orders without real charges (used in Phase 12). Remember to turn test
   mode **OFF** before launch.

**Common mistakes:** wrong bank numbers (payouts fail silently); enabling a third-party gateway and
eating the 2% fee; leaving test mode ON at launch (real customers can't pay); using a personal
PayPal that limits business receiving.

---

# PHASE 9 — Shipping settings (free over $35, else $4.95)
**⏱️ ~20–30 min · 💲 $0**

> **What this phase does:** matches your shipping policy — **free shipping on orders $35+**, flat
> **$4.95** under that, **US-only** to start.

1. Go to **Settings → Shipping and delivery.**
2. Under **Shipping** → your **General profile** → **Manage rates** (🔀 "General shipping rates").
3. You'll see a **Domestic** zone. Confirm it covers the **United States** (create/edit a zone
   named "United States" containing the US if needed). Remove or leave other countries out — start
   **US-only**.
4. In the US zone, **Add rate** twice:
   - **Rate A — Free shipping:** name `Free Shipping`, price `0`. Click **"Add conditions" → Based
     on order price**, set **Minimum = $35.00**, no maximum. (Free when subtotal ≥ $35.)
   - **Rate B — Flat rate:** name `Standard Shipping`, price `4.95`. Add condition **Based on order
     price → Maximum = $34.99** (so it only shows on orders under $35).
5. **Save.** Now carts ≥$35 see "Free Shipping," carts <$35 see "$4.95."
6. **Delivery estimate / transit time:** because you dropship, make the wait clear. Add a line like
   "Ships in 1–3 business days; delivery in 7–15 business days" on product pages and in the
   Shipping policy. (Honest ETAs protect ad accounts and reduce disputes.)

**Common mistakes:** overlapping price conditions so both rates show (set the $4.95 max to $34.99,
free min to $35); leaving worldwide zones on (you'll get orders you can't cheaply fulfill); hiding
the real delivery time (causes chargebacks and ad bans).

---

# PHASE 10 — Connect CJdropshipping + DSers, turn on auto-fulfill
**⏱️ ~45–60 min · 💲 $0 (free apps; you pay suppliers per order from revenue)**

> **What this phase does:** wires order routing to your supplier so fulfillment "runs itself"
> (auto-order + tracking sync). You can use **CJdropshipping** (better US shipping times, you have
> prior CJ experience) and/or **DSers** (AliExpress). Both are free Shopify apps. The Starter Kit
> must be built from **one CJ supplier / same warehouse (ideally CJ US-WH)** so it ships as **one
> parcel** — set that up on the CJ side.

**Install CJdropshipping (primary, per the plan):**
1. In Shopify admin, go to **Apps** (left sidebar) → **"Shopify App Store"** → search
   **"CJdropshipping."** 🔀 The exact listing may be "CJdropshipping" or "Droplink by CJ."
2. Click **Add app → Install**, then **authorize** it to access your store.
3. Create/log in to your **CJdropshipping account** (use your business email).
4. In CJ, **link/authorize** your Shopify store (CJ → Authorization → Shopify). Confirm the store
   shows as connected.
5. **Map each product to a CJ supplier listing:** in CJ, search the product, pick a supplier (for
   the Kit, choose items from the **same warehouse**, ideally **CJ US-WH**), and link it to the
   matching Shopify product. This tells CJ which supplier SKU to order when a sale comes in.
6. **Set pricing to the retail in `catalog.md`** — do **not** rely on CJ's auto-markup. Your
   Shopify prices ($59/$27/$17/etc.) are already set; just make sure CJ doesn't overwrite them on
   sync (turn off "sync price" or set it to keep your price).

**Install DSers (optional secondary, for AliExpress items):**
7. **Apps → Shopify App Store → "DSers."** Add app → Install → authorize.
8. In DSers, **link your AliExpress account** (DSers walks you through it / a Chrome extension).
9. **Import/map** any AliExpress-sourced SKUs to Shopify products. (Free plan covers thousands of
   products and includes auto tracking sync — plenty for launch.)

**Turn on auto-order + tracking sync (the "runs itself" layer):**
10. In **CJ** (and/or DSers) **Settings**, enable:
    - **Auto-order / auto-place order** — when a paid Shopify order arrives, it's auto-created with
      the supplier (you fund it; for full auto you can keep a CJ wallet balance).
    - **Auto-sync tracking** — supplier tracking numbers flow back to Shopify and email the
      customer automatically.
11. ⚠️ **Scope check:** auto-fulfill handles **order routing + tracking only**. Ads, customer
    service, and returns stay **manual** — don't expect the app to answer customers.
12. **Verify the mapping:** in Phase 12 you'll place a test order and confirm it appears as a
    draft/order inside CJ/DSers. If it doesn't, the product isn't mapped — fix the mapping.

**Common mistakes:** building the Kit from multiple warehouses (ships as several parcels = bad CSAT
and cost); letting CJ auto-markup overwrite your retail prices; forgetting to fund the CJ wallet so
auto-order can actually pay the supplier; assuming auto-fulfill covers customer service.

---

# PHASE 11 — Set the Refill 3-Pack as a checkout order-bump
**⏱️ ~20 min · 💲 $0 (free app tier)**

> **What this phase does:** offers "Add a Refill 3-Pack and save 20%" at checkout behind any
> bowl/kit purchase — seeds the repeat-purchase habit and lifts average order value.
>
> **Recommended free app:** **ReConvert** (free plan covers ~49 orders/month — fine for a
> validation test) or **Selleasy** (free plan up to ~100 orders/month, full cart + post-purchase
> upsells). Either works; **Selleasy's free tier is the most generous** if you want headroom.
> (Avoid "Releasit COD" for this — its free plan only works on development stores, not live
> merchant stores.)

1. **Apps → Shopify App Store →** search **"Selleasy"** (or **"ReConvert"**) → **Add app →
   Install** → authorize. Stay on the **Free** plan.
2. In the app, **create a new offer/funnel**:
   - **Type:** checkout / cart order-bump (or post-purchase upsell if checkout bump isn't on the
     free tier).
   - **Trigger:** when cart contains the **Starter Kit** *or* any **bowl** product.
   - **Offer product:** the **Refill & Rotate Lick Mat Variety 3-Pack**.
   - **Discount:** **20% off** the 3-pack, with copy "Add a Refill 3-Pack and save 20%."
3. **Save / publish** the offer and toggle it **Active**.
4. You'll verify it actually appears during the Phase 12 test checkout.

**Common mistakes:** accidentally upgrading to a paid plan you don't need; setting the trigger so
broad it shows on the refill page itself; forgetting to publish/activate the offer; not testing
that the discount actually applies.

---

# PHASE 12 — Pre-launch QA + a test order
**⏱️ ~45–60 min · 💲 $0 (use test mode / Bogus Gateway)**

> **What this phase does:** catches the embarrassing/expensive bugs before real customers (or ad
> dollars) hit the store.

**A. Page-by-page check (do on mobile AND desktop):**
1. Every product page shows: correct **price**, **compare-at**, **variants**, **images**,
   **Add-to-Cart**, and a visible **delivery ETA**.
2. **Collections** load and aren't empty.
3. **Menus** work: Home / Shop / Starter Kit / About all go to the right place.
4. **Footer** links to all policies + Contact; **Contact form** sends (email yourself a test).
5. **Homepage** hero button goes to the Starter Kit; reviews/benefit sections render.

**B. Place a real end-to-end test order:**
6. Turn on **Settings → Payments → Shopify Payments → Manage → Use test mode** (or use the **Bogus
   Gateway**). 🔀
7. Add the **Starter Kit** to cart. Confirm the **order-bump (Refill 3-Pack, 20% off)** appears —
   add it.
8. Go to checkout. Confirm shipping shows **Free** (since the cart is >$35) — and separately test a
   small cart **under $35** to confirm **$4.95** shows.
9. Use a Shopify **test card number** (e.g. `4242 4242 4242 4242`, any future expiry, any CVC) to
   complete the order.
10. Confirm: order appears in **Orders**; the **order-confirmation email** arrives; and the order
    **routes to a draft inside CJ/DSers** (proves auto-fulfill mapping works).
11. **Refund/cancel** the test order, then **turn test mode OFF.**

**C. Trust + recovery basics:**
12. Turn ON the native **abandoned-cart email**: **Settings → Checkout →** scroll to **Abandoned
    checkouts → enable automatic emails**. 🔀 (Free; recovers lost sales.)
13. Confirm trust elements are visible on the product page (secure checkout, 30-day guarantee, free
    shipping over $35).

**Common mistakes:** leaving **test mode ON** at launch (real cards rejected); test order **not**
appearing in CJ/DSers (mapping broken — fix before launch); order-bump not showing; only testing on
desktop; forgetting to enable abandoned-cart recovery.

---

# PHASE 13 — Remove the password page → go LIVE
**⏱️ ~5 min · 💲 $0**

> **What this phase does:** opens the doors. Until now a password page hid the store from the
> public. Do this **only after Phase 12 passes** and **test mode is OFF.**

1. Go to **Online Store → Preferences.** 🔀 (Password setting may live under **Themes → Customize**
   or **Online Store → Preferences** depending on admin version.)
2. Scroll to **Password protection** and **uncheck "Restrict access to visitors with the
   password."**
3. **Save.** The store is now **LIVE** at `noseymutt.com`.
4. Final live sanity check: open `noseymutt.com` in a **private/incognito** window on your phone —
   confirm it loads with no password prompt, the Starter Kit buys correctly, and checkout works.
5. 💲 Confirm `finance/budget.md` reflects all spend to date (Shopify promo + domain + any logo).

**Common mistakes:** removing the password while **test mode is still on** (customers can't pay);
not doing a final incognito check; forgetting to confirm the domain (Phase 2) finished
propagating before announcing the store.

---

## Definition of done — final go-live checklist

Tick every box before you point any traffic at the store:

**Account & domain**
- [ ] Shopify Basic on the **$1/mo-for-3-months** promo (monthly billing), spend logged.
- [ ] `noseymutt.com` connected and set as **primary**; `hello@noseymutt.com` forwards to inbox.

**Look & content**
- [ ] Dawn theme live with NoseyMutt colors (Cream bg, Ink text, Mustard buttons) + Poppins/Inter.
- [ ] Logo + favicon set; homepage sections built; mobile checked.

**Products & merchandising**
- [ ] All 7 products Active with correct title, description, price, **compare-at**, variants, SEO,
      images; **inventory tracking OFF**.
- [ ] 3 collections built and **not empty** (Enrichment / Bundles & Kits / Refills).
- [ ] Refill 3-Pack live as a **checkout order-bump** (Selleasy/ReConvert free tier), 20% off.

**Pages & policies**
- [ ] About, FAQ, Shipping, Returns, Contact (with form) pages live.
- [ ] Privacy, Terms, Refund, Shipping policies generated **and** edited (no placeholders).
- [ ] Header + footer menus correct; policies linked in footer.

**Payments & shipping**
- [ ] Shopify Payments active (bank + tax ID); PayPal secondary on; **no third-party gateway**.
- [ ] Free shipping ≥$35 / $4.95 under; US-only; delivery ETA stated.

**Fulfillment**
- [ ] CJ (and/or DSers) connected; products mapped; Kit = **one warehouse/one parcel**.
- [ ] Auto-order + auto-tracking ON; CJ wallet funded; retail prices preserved.

**QA & launch**
- [ ] Test order completed end-to-end; routed to CJ/DSers draft; order-bump appeared; refunded.
- [ ] **Test mode OFF**; abandoned-cart email ON.
- [ ] Password page **removed**; incognito mobile check passed → **store LIVE**.
- [ ] All spend recorded in `finance/budget.md` (target ~$13–30 to launch; ~$470+ reserved for
      sample order + ad test).

---

## Running cost summary (log each in `finance/budget.md`)

| Item | When | Cost | Note |
|---|---|---|---|
| Shopify Basic ($1/mo promo) | Phase 1 | ~$1/mo × 3 = **~$3** | Monthly billing only; reverts to $39/mo (or $29 annual) after 3 mo |
| Domain `noseymutt.com` | Phase 2 | **~$10–15/yr** | Cheaper at Cloudflare/Namecheap (~$10–11); ~$15 if bought via Shopify |
| Logo (optional) | Prereqs | **$0–15** | Free via Canva/Shopify logo maker, or ~$15 Fiverr |
| Dropship apps (CJ, DSers) | Phase 10 | **$0** | Free; you pay suppliers per order from revenue |
| Order-bump app (Selleasy/ReConvert) | Phase 11 | **$0** | Free tier |
| Reviews / consent / pixels | (later) | **$0** | All free tiers |
| **Total to launch** | | **~$13–30** | Leaves ~$470+ for sample order + ad test |

⚠️ **Decision checkpoint ~2026-09-15:** before the 3-month promo ends and Shopify bills full price,
either (a) you have a proven winner → switch to **annual Basic ($29/mo)**, or (b) **pause/cancel**.
Set a calendar reminder.

---

## Sources (verified June 2026 — flag if changed)

- Shopify plans, prices, free trial, $1/mo×3 promo, transaction & 3rd-party fees —
  [shopify.com/pricing](https://www.shopify.com/pricing)
- $1/mo-for-3-months promo mechanics (monthly-only; new accounts only) —
  [pagefly.io/blogs/shopify/shopify-1-dollar](https://pagefly.io/blogs/shopify/shopify-1-dollar),
  [demandsage.com/shopify-free-trial](https://www.demandsage.com/shopify-free-trial/)
- Basic fees (2.9%+30¢ Shopify Payments; 2% third-party on Basic) —
  [firstpier.com/resources/how-much-does-shopify-take-per-sale](https://www.firstpier.com/resources/how-much-does-shopify-take-per-sale)
- Dawn theme is the free default; color schemes + typography editor —
  [blackbeltcommerce.com/customizing-dawn-theme-shopify](https://www.blackbeltcommerce.com/customizing-dawn-theme-shopify/)
- DSers free plan, install + auto order/tracking —
  [apps.shopify.com/dsers](https://apps.shopify.com/dsers),
  [bettamax.com/dsers-review](https://bettamax.com/dsers-review/)
- CJdropshipping free Shopify app, connect + auto-fulfill —
  [cjdropshipping.com/integrations/shopify](https://cjdropshipping.com/integrations/shopify)
- Free order-bump/upsell apps (Selleasy ~100 orders/mo free; ReConvert ~49 orders/mo free;
  Releasit free = dev stores only) —
  [aftersell.com/blog/best-9-shopify-checkout-upsell-apps-to-boost-aov-in-2026-aftersell](https://www.aftersell.com/blog/best-9-shopify-checkout-upsell-apps-to-boost-aov-in-2026-aftersell)

**What may have changed since writing (re-verify at setup):**
- 🔀 The middle Shopify plan was renamed **"Shopify" → "Grow"** ($105/mo); naming could shift again.
- 🔀 The **$1/mo×3** promo length/terms change periodically (sometimes 3 days free + $1×3, sometimes
  "90 days"). Confirm the exact offer on the pricing page at signup and that it's **monthly-only**.
- 🔀 Admin labels (Online Store vs. Sales channels, Policies vs. Legal, Menus vs. Navigation,
  password location) get reorganized regularly — use the admin search bar if a label is missing.
- 🔀 Free-tier order limits on upsell apps change; confirm the current free cap before relying on it.
