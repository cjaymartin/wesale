# Meta Ads — Zero-to-Live Setup Walkthrough (NoseyMutt)

**Date:** 2026-06-15
**For:** wesale / NoseyMutt — enrichment dog brand
**Goal:** Go from *no Meta advertising presence at all* → a live, ~$90 Add-to-Cart-optimized creative test for the **Boredom-Buster Starter Kit ($59)**, exactly per `research/marketing/channel-plan-2026-06-15.md` §3 Phase 1.
**Reader assumption:** You have a personal Facebook login and nothing else (no Page, no Business portfolio, no ad account, no Pixel).

> **Naming warning (read once):** Meta renames things constantly. As of mid-2026: *Business Manager* is now called **Meta Business Portfolio** (the container for your assets); you manage it inside **Meta Business Suite** at `business.facebook.com`. The *Facebook Pixel* is now called a **dataset** inside **Events Manager**. *Detailed Targeting* audiences are increasingly replaced by **Advantage+ audience**. If a button name below doesn't match what you see, look for the nearest equivalent — the *flow* is stable even when labels drift. ([Leadsie — Business Suite vs Portfolio](https://www.leadsie.com/blog/meta-business-manager-vs-meta-business-suite-differences))

---

## TL;DR for the CEO

- **Realistic time, zero → live test:** **~3–5 hours of hands-on work spread across 5–10 calendar days.** The hands-on clicking is only a few hours; the calendar drag is **business verification (5–15 business days)** and **ad-account review of your first campaign (up to ~24h)**. You can launch the $90 test *before* business verification finishes, but expect a low starting spend limit (~$25–50/day).
- **All-in test cost:** **~$90 media** (Phase 1) + **$0 in mandatory tooling** (Shopify Facebook & Instagram channel, Pixel/dataset, and Conversions API are all free) + the **time** above. Phase 2 (if Phase 1 passes its gate) adds ~$60–110. Total paid exposure stays inside the **$100–200 test allotment** in `finance/budget.md`; reserve stays untouched until a SCALE verdict.
- **Log every charge** as a new row in `finance/budget.md` (Ledger). Meta bills in chunks as you hit a billing threshold, not once at the end — log each charge.

---

## Phase 0 — Prerequisites (gather before you click anything)

Do not start the setup until ALL of these are true. Missing one will stall you mid-flow.

- [ ] **Personal Facebook account** that you can log into (this becomes the *admin* of everything — do **not** create a fake/second personal account; that's the #1 ban trigger).
- [ ] **Business email** — ideally `hello@noseymutt.com` (free via registrar forwarding, see `brand.md`). Used for the Business portfolio + Events Manager notifications. A Gmail works to start but a domain email looks more legitimate to Meta's automated trust checks.
- [ ] **Payment card** in the business's name (credit card preferred over debit; PayPal also accepted). ([Get-Ryze — billing setup](https://www.get-ryze.ai/blog/meta-ads-billing-payment-setup-beginner-guide))
- [ ] **Live Shopify store** at `noseymutt.com` with the **Boredom-Buster Starter Kit** published, an **order-bump/bundle live to push AOV toward $55–70** (channel-plan pre-flight requirement), and **realistic shipping times disclosed** on the product page + checkout (brand guardrail + ad-policy requirement).
- [ ] **Domain verified-able** — you own `noseymutt.com` DNS (needed for domain verification in Events Manager so *you*, not a reseller, control the Pixel on your domain).
- [ ] **3–5 ad creatives ready** (video preferred; per channel-plan §5 templates). Each must obey the **no-health-claim** guardrail (see Phase 12). Aspect: 9:16 (1080×1920) for Reels/Stories + a 1:1 (1080×1080) fallback.
- [ ] **Brand assets:** NoseyMutt logo (square, ≥320×320 for the Page profile), a cover image, and the palette from `brand.md` (Mustard `#F2B33D` CTA, Cream `#FBF6EE` bg).
- [ ] **Business info for verification:** legal business name, address, phone. wesale should have a registered entity (or sole-prop equivalent) whose name **matches exactly** what you'll enter — mismatches fail verification. ([AGrowth — verify your business](https://agrowth.io/blogs/facebook-ads/how-to-verify-your-business-on-meta))

**Time:** assembling these = ~1–2h (most should already exist from the store build). **Cost:** $0 new here.

---

## Phase 1 — Create the NoseyMutt Facebook Page

A Page is required: ads run *from* a Page, and the Instagram link hangs off it.

1. Log into your **personal** Facebook at `facebook.com`.
2. Go to **`facebook.com/pages/create`** (or click the **+ (Create)** menu top-right → **Page**).
3. **Page name:** type `NoseyMutt` exactly (matches `brand.md`).
4. **Category:** type and select **`Pet Supplies`** (add a secondary like *Brand* or *Product/Service* if offered).
5. **Bio:** paste the one-liner — *"Keep their nose busy, their brain happy. Enrichment toys & feeders for bored dogs."*
6. Click **Create Page**.
7. Add **Profile picture** = NoseyMutt logo; **Cover photo** = a branded hero image. Why: an empty Page looks like a throwaway/scam account and raises your ban risk on a new ad account.
8. Add **Website** = `https://noseymutt.com`, and an **Action button** = *Shop now* → `noseymutt.com`.

**Time:** ~20 min. **Cost:** $0.

> Don't run ads via the personal "Boost Post" button. Everything below routes ads through the Business portfolio so you control the Pixel, audiences, and billing properly.

---

## Phase 2 — Create the Business Portfolio (formerly Business Manager)

This is the container that owns the Page, the ad account, and the dataset.

1. Go to **`business.facebook.com`** and log in with the same personal account.
2. In the **top-left dropdown** (the portfolio switcher), scroll to the bottom and click **Create a business portfolio**. ([Meta Help — create a business portfolio](https://www.facebook.com/business/help/1710077379203657))
3. **Business portfolio name:** `wesale` (your company) — *not* the brand. (One portfolio can hold multiple brands later.)
4. **Your name** and **business email:** enter your real name and `hello@noseymutt.com`.
5. Click **Create**, then **open the confirmation email** Meta sends and click the verification link. Until you confirm the email, some actions are blocked.
6. Open **Settings** (gear icon) → this is **Business settings**, where you'll add every asset below.
7. In **Business settings → Accounts → Pages → Add → Add a Page**, find **NoseyMutt** and add it. (If the "add" fails because you're the personal owner, choose *Claim a Page* / *Request access* as offered.) ([3naves — connect assets](https://www.3naves.com/blog-en/how-to-create-your-business-portfolio-in-meta-and-connect-all-your-assets.htm))

**Time:** ~15 min (plus waiting for the email). **Cost:** $0.

---

## Phase 3 — Create the Ad Account (currency + timezone are PERMANENT)

1. In **Business settings → Accounts → Ad accounts → Add → Create a new ad account**.
2. **Ad account name:** `NoseyMutt — Main`.
3. **Time zone:** ⚠️ **PERMANENT. Choose your real reporting timezone now** (e.g. `America/New_York` if you run US East, or whatever you'll read reports in). The default is **Pacific (PST)** — change it before saving or all your day-parting/reports will be off. You cannot edit it later; fixing it means deleting and re-creating the account. ([Meta Help — ad account time zone](https://en-gb.facebook.com/business/help/754049591334898))
4. **Currency:** ⚠️ **PERMANENT. Choose `USD`** (your budget, margins, and benchmarks in the channel-plan are all USD). Cannot be changed later. ([Leadsie — create ad account](https://www.leadsie.com/blog/how-to-create-meta-business-manager-and-facebook-ad-account))
5. Confirm **this ad account belongs to your own business** (not a client/agency) when prompted.
6. Click **Create**.
7. Still in Business settings → **Ad accounts → Assign people →** add **yourself** with **full control (manage)**.

**Time:** ~10 min. **Cost:** $0 (you're not charged until ads deliver).

---

## Phase 4 — Add a Payment Method + Set a Spending Limit

1. Open **Ads Manager** (`adsmanager.facebook.com`) → **☰ menu → Billing & payments** (or **Business settings → Payments**).
2. **Payment settings → Add payment method →** add your business **credit card** (preferred; debit/PayPal also accepted). Set it as **primary**; add a **backup** card if you have one (failed payments depress your spend-limit growth and can flag the account). ([Get-Ryze — billing setup](https://www.get-ryze.ai/blog/meta-ads-billing-payment-setup-beginner-guide))
3. **Expect a low starting limit:** brand-new accounts often start with a **per-account or daily spend cap as low as $25–$50** as fraud prevention. This is normal and *enough* for a $15/day test. It rises automatically as you pay invoices on time and complete business verification. ([Get-Ryze — spending limits](https://www.get-ryze.ai/blog/meta-ads-account-spending-limit-and-budget-tracking-best-practices))
4. **Set an account spending limit** (a hard stop across the whole account): in **Billing → Payment settings → Account spending limit**, set **`$200`**. Why: this is a *hard cap that protects your $500 budget* — even if a campaign misbehaves, Meta stops all delivery at $200 until you raise it. It maps to the test allotment in `budget.md`.
5. Note how Meta bills: it charges when you hit a **billing threshold** (starts small, e.g. ~$25, and steps up) **or** on your monthly bill date — whichever comes first. So you'll see several small charges, not one $90 charge. **Log each one in `finance/budget.md`.**

**Time:** ~15 min. **Cost:** $0 now (first charge lands once ads start delivering).

---

## Phase 5 — Connect Instagram

NoseyMutt's ads will run on Instagram (Reels/feed) too, so link the IG account.

1. First, make sure **@noseymutt** exists on Instagram and is set to a **Business/Professional** account (in the IG app: *Settings → Account type → Switch to Professional → Business*).
2. In **Business settings → Accounts → Instagram accounts → Add → Connect your Instagram account**, log in with the **@noseymutt** credentials and accept permissions. ([Duplex Ventures — Business Suite 2026 guide](https://duplex-ventures.com/how-to-use-meta-business-suite-guide/))
3. In **Business settings → Accounts → Instagram accounts**, click the account → **Connect assets → connect the NoseyMutt Page** so ads can use either identity.

**Time:** ~10 min (more if you still need to create the IG account). **Cost:** $0.

---

## Phase 6 — Install the Pixel/Dataset via Shopify's Facebook & Instagram Channel

This is the easiest, least error-prone path: let Shopify create/connect the **dataset (Pixel)** and turn on **Conversions API** automatically. Do NOT also hand-paste a pixel into the theme — that causes double-counting.

1. In **Shopify admin → Settings → Apps and sales channels → Shopify App Store**, install **Facebook & Instagram** (by Meta). ([Shopify — Meta Pixel setup](https://www.shopify.com/blog/72787269-relax-advertising-on-facebook-just-got-a-lot-easier))
2. Open the channel → **Connect account** → log into Facebook with the same admin account → grant access to the **wesale** Business portfolio, the **NoseyMutt** Page, the **ad account**, and Instagram.
3. **Choose / create your dataset (Pixel):** select **Create new** (Shopify will make a NoseyMutt dataset) or pick an existing one. Name it `NoseyMutt`.
4. **Data sharing level:** set to **Maximum**. This is the setting that fully turns on the **Conversions API (server-side) with advanced matching** — it's what makes ATC/Purchase tracking survive iOS/ad-blocker loss. ([Stormy AI — Pixel + CAPI for Shopify 2026](https://stormy.ai/blog/meta-pixel-conversions-api-shopify-tutorial-2026))
5. Accept Meta's terms; finish the connect flow.

**What this gives you automatically:** Shopify fires the standard events — **ViewContent, AddToCart, InitiateCheckout, Purchase** — via *both* browser Pixel and server-side CAPI, with **event deduplication** (matching `event_id`) so a single order isn't counted twice. ([Stormy AI](https://stormy.ai/blog/meta-pixel-conversions-api-shopify-tutorial-2026), [wetracked — CAPI on Shopify](https://www.wetracked.io/post/set-up-facebook-conversion-api-on-shopify))

**Time:** ~20 min. **Cost:** $0.

> **Phase 9 (Conversions API) is already done by this step.** Because the Shopify channel set data sharing to *Maximum*, CAPI is on — no separate gateway/app needed. Verify it in Phase 8.

---

## Phase 7 — Verify Your Business + Verify Your Domain

Two different verifications. Do both.

**Domain verification** (so *you* control the Pixel on `noseymutt.com`):
1. In **Events Manager → ☰ → Brand safety / Business settings → Domains → Add** → enter `noseymutt.com`.
2. Choose the **DNS TXT record** method, copy the TXT value, add it in your domain registrar's DNS, then click **Verify**. (Shopify-hosted domains can also use the meta-tag method via the theme.)

**Business verification** (raises spend limits + unlocks restricted features):
3. In **Business settings → Security Center → Start verification** (admin only). Submit your legal business name, address, phone, and an official doc (incorporation cert / business license / tax registration) whose name **matches exactly** what you entered. ([AGrowth — verify your business](https://agrowth.io/blogs/facebook-ads/how-to-verify-your-business-on-meta))
4. **Timeline: 5–15 business days.** You can **launch the $90 test without waiting** for this, but verification lifts your spend cap and reduces "is this a real business?" review friction, so start it now in parallel. ([AGrowth](https://agrowth.io/blogs/facebook-ads/how-to-verify-your-business-on-meta))

> 2026 note: Meta increasingly requires **advertiser identity verification** (and codified that every ad account must map to a verifiable entity). Expect to be asked for ID at some point even for low spend — have it ready. ([AuditSocials — legitimacy check 2026](https://www.auditsocials.com/blog/meta-ad-account-legitimacy-verification-requirement-2026))

**Time:** ~20 min to submit; **5–15 business days** to clear (async — keep going). **Cost:** $0.

---

## Phase 8 — Verify Add-to-Cart + Purchase Events Fire (DO NOT SKIP)

The entire channel-plan optimizes on **Add-to-Cart**. If ATC doesn't fire, the test is dead on arrival.

1. Open **Events Manager** (`business.facebook.com/events_manager`) → select the **NoseyMutt dataset**.
2. Install the **Meta Pixel Helper** Chrome extension. Open `noseymutt.com` in that browser.
3. **Test the real funnel manually:** view the Boredom-Buster Kit product page → click **Add to cart** → begin checkout. Watch Pixel Helper light up **ViewContent → AddToCart → InitiateCheckout**.
4. In Events Manager → **Test events** tab, enter your site URL and repeat the funnel; confirm each event appears **in real time**, tagged **Browser + Server** (Server = CAPI is working). ([Stormy AI](https://stormy.ai/blog/meta-pixel-conversions-api-shopify-tutorial-2026))
5. **Purchase:** place one real test order (use a discount code; you can refund). Confirm a **Purchase** event arrives, also Browser + Server. (You're not optimizing for Purchase in Phase 1, but it must work for Phase 2 validation.)
6. In the **Overview** tab, confirm **deduplication** shows no glaring double-counting (Browser and Server events for the same order collapse into one).

**Definition of "passing":** AddToCart and Purchase both appear in **Test events**, both show a **Server** source, and Pixel Helper shows no duplicate-pixel errors.

**Time:** ~20–30 min (incl. one test order). **Cost:** the test order's product/ship cost (refundable) — log it in `budget.md` if not refunded.

---

## Phase 9 — Conversions API (confirm only — already enabled)

You enabled CAPI in **Phase 6** by setting data sharing to **Maximum**; you confirmed it in **Phase 8** (events tagged *Server*). **No extra app or "Conversions API Gateway" is needed** for this budget. If, and only if, Phase 8 showed *Browser only* (no Server events), go back to the Shopify Facebook & Instagram channel → **Settings → Data sharing → set to Maximum → reconnect**. ([wetracked — CAPI on Shopify](https://www.wetracked.io/post/set-up-facebook-conversion-api-on-shopify))

**Time:** 0–10 min. **Cost:** $0.

---

## Phase 10 — Build the $90 Test Campaign (exactly per channel-plan §3 Phase 1)

> **The design (do not deviate):** 3 ad creatives × 1 broad US ad set, **$15/day total**, **optimized for Add-to-Cart** (proxy event — Purchase volume is too low to learn on at this budget), **Advantage+ audience**, broad placements. Read after **~$90 / ~6 days**. (channel-plan §3 Phase 1)

### 10a. Campaign level
1. **Ads Manager → Create**.
2. **Objective: Sales.** (This is the only objective that lets you optimize for AddToCart/Purchase conversion events. *Engagement/Traffic would optimize for cheap clicks, not buyers.*)
3. Name: `NoseyMutt — P1 Creative Test — ATC`.
4. **Advantage+ Shopping vs. manual sales campaign:** choose a **manual sales campaign** for Phase 1 so you can *force optimization on Add-to-Cart* and isolate 3 creatives cleanly. (Advantage+ Shopping defaults toward Purchase and auto-mixes creative, which hides the per-creative signal you need.) You'll still use Advantage+ *audience* at the ad-set level.
5. **Budget: Campaign budget optimization (Advantage campaign budget) = $15.00/day.** This is the whole test's spend; CBO spreads it across the creatives.
6. Leave special ad categories **OFF** (pet products are not a special category — do **not** tick Housing/Employment/Credit/Politics).

### 10b. Ad set level (one ad set)
7. Name: `Broad US — ATC`.
8. **Conversion location: Website.**
9. **Performance goal / optimize for: Maximize number of Add-to-Cart conversions.** (Pick **AddToCart** as the conversion event — NOT Purchase. This is the non-negotiable proxy-event move from channel-plan §3: ATC fires ~5–10× more often, so the algorithm can exit learning on ~$15/day.)
10. **Dataset:** select the **NoseyMutt** dataset.
11. **Audience: broad.** Turn **Advantage+ audience ON** and leave suggestions empty (let Meta find buyers). Set only:
    - **Location:** United States.
    - **Age:** 25–55 (dog-parent skew; adjust per your creatives). **Gender:** All.
    - **No detailed interest targeting** — broad is the channel-plan spec and works better with the ATC signal.
12. **Placements: Advantage+ placements (automatic)** — let Meta serve Reels, Feed, Stories everywhere. Cheaper and more learning data at this budget.

### 10c. Ads (3 creatives — can extend to 5)
13. Create **3 separate ads** in this one ad set, each a different creative angle from channel-plan §5:
    - **Ad A — Problem→Solution demo (PAS):** show the gulping/boredom problem → the Kit solving it. Hook in first 1–2s.
    - **Ad B — "I was today years old" discovery:** fast satisfying demo of slow-feeder + snuffle + lick mat.
    - **Ad C — Before/After:** chaos/bored dog → calm, busy dog using the Kit.
    - *(Optional Ad D/E if you have them — up to 5 total; CBO will still find the winner.)*
14. **Identity:** NoseyMutt **Page** + **@noseymutt** Instagram.
15. **Primary text / headline:** benefit-focused, **no health claims** (see Phase 12). Example headline: *"Eat slower. Sniff more. Wreck less."* CTA button: **Shop Now** → the Boredom-Buster Kit product URL (`noseymutt.com/products/boredom-buster-starter-kit`).
16. **URL parameters:** add `utm_source=meta&utm_medium=cpc&utm_campaign=p1_atc_test` for clean attribution.
17. **Publish.** First-time ads on a new account go to **review (usually <24h, sometimes a few hours)** before delivery.

**Time:** ~45–60 min to build. **Cost (media):** **$15/day × 6 days = ~$90.** Log charges in `budget.md`.

---

## Phase 11 — Kill / Scale Decision Rules (what to watch, where)

**Where to read it:** Ads Manager, **ad level**, columns customized to show: **Link CTR, Cost per Add-to-Cart, Adds to Cart, Amount spent, CPM, Impressions.** Add **Purchases + ROAS** columns too (for Phase 2). Set the date range to the campaign's life.

### Phase 1 gate — read after ~$90 / ~3–4 days (channel-plan §3 Phase 1)
Primary metrics: **Link CTR** and **cost-per-ATC**.

| Outcome | Trigger | Action |
|---|---|---|
| **GO to Phase 2 (signal)** | **Link CTR ≥ 1.2%** AND **cost-per-ATC ≤ ~$3** on at least one creative | Kill the losers; keep the winner(s). Proceed. |
| **KILL the product/creative** | **Link CTR < 0.8%** across all 3 **OR** cost-per-ATC **> $6 with 0–1 ATC** | **Stop now.** Do **not** spend the rest. Iterate creative or move to the next SKU. |
| **Murky middle** | CTR 0.8–1.2% / ATC $3–6 | Iterate the hooks on the best creative; re-test once before deciding. |

> Don't touch budgets/audiences in the first **~3 days** — you'll reset Meta's learning phase. Let it run to ~$90.

### Phase 2 — conversion validation ($60–110, ~4–5 days) — only if Phase 1 passed
1. Kill losing creatives; **scale the winner to $20–25/day.**
2. Switch optimization toward **Purchase** (keep ATC only if Purchase volume is too thin to learn on).
3. Read against the **budget.md kill rule: kill if cumulative ad spend > 1.5× gross margin generated** (≈ break-even ROAS floor ~2.2× at this margin).

| Outcome | Trigger | Action |
|---|---|---|
| **SCALE** | blended **ROAS ≥ 2.2×** trending to 3×, CAC ≤ ~$26 with AOV lift | Product validated. **Tap reserve**, raise budget **+20–30% every 3 days** (never bigger jumps — protects learning). |
| **HOLD / ITERATE** | ROAS 1.5–2.2× | Margin/AOV problem, not demand. Fix bundle/price/order-bump, re-test once. |
| **KILL** | ROAS < 1.5% after $60+ in Phase 2, **or** cumulative spend > 1.5× margin generated | Dead. Stop, log, move to next candidate. |

**Total paid exposure across both phases:** ~$150–200 — inside the test allotment; **reserve stays untouched until a SCALE verdict.**

---

## Phase 12 — Account-Ban & Policy Pitfalls (critical for a brand-new account)

A new ad account has **zero trust**. One policy strike on day 1 can disable the account. Avoid these:

**A. Health/medical claims — the #1 risk for a dog brand (and a hard brand guardrail).**
- ❌ Never: "treats/cures anxiety," "reduces cortisol," "stops destructive behavior," "weight loss," "calms separation anxiety," "vet-recommended" (unless literally true + documented). Health/wellness claims are among Meta's most-enforced categories and enforcement is now largely automated/pre-human. ([Accelerated Digital Media — health ad restrictions 2026](https://www.accelerateddigitalmedia.com/insights/guide-to-social-media-health-ad-restrictions-2026/))
- ✅ Allowed (NoseyMutt voice): "busts boredom," "slows fast eaters," "mental stimulation," "foraging fun," "less chewing, barking, digging," "winds them down." (Matches `brand.md` guardrails.)

**B. Personal-attributes policy — easy accidental violation.**
- Meta forbids ad copy that *implies it knows something about the viewer*. Second-person "your dog has a problem" phrasing can trip it.
- ❌ "Is YOUR dog anxious and destructive?" / "Does your dog have a behavior problem?"
- ✅ Reframe as benefit-focused/general: "Bored dogs dig and chew — give their nose a job." / "Enrichment that tires busy brains." ([Gripas — claims & personal-attributes policy 2026](https://gripasmarketing.com/meta-ads-claims-personal-policy/))

**C. Trademark/IP in creative & catalog.** Never show or name **KONG / Nina Ottosson / Outward Hound** (already a catalog rule). Using a competitor's branded product image in an ad = takedown + strike.

**D. New-account warm-up / spend ramp (don't trip fraud systems):**
- Keep the **account spending limit at $200** (Phase 4) — a hard ceiling that also signals "modest, legit advertiser."
- **Don't dump budget on day 1.** $15/day is ideal: it's a believable new-advertiser spend and stays under your ~$25–50 starting limit. ([Get-Ryze — spending limits](https://www.get-ryze.ai/blog/meta-ads-account-spending-limit-and-budget-tracking-best-practices))
- After a SCALE verdict, **raise budget +20–30% every ~3 days**, never doubling — big jumps look like account takeover *and* reset the learning phase.
- **One admin, one consistent device/location.** Logging in from many IPs/devices, or adding a brand-new "personal" profile just to run ads, is a top ban trigger.
- **Pay invoices on time.** A single failed payment depresses your spend-limit growth and flags the account. ([Get-Ryze — billing](https://www.get-ryze.ai/blog/meta-ads-billing-payment-setup-beginner-guide))
- **Complete business + domain verification** (Phase 7) — verified accounts get higher limits and softer review treatment. ([AGrowth](https://agrowth.io/blogs/facebook-ads/how-to-verify-your-business-on-meta))
- **Have a Page presence first** (Phase 1) — ads from an empty Page get scrutinized harder.
- If an ad is rejected: **edit the copy** (usually the fix is removing an implied health/personal claim) and resubmit; don't spam-duplicate rejected ads — repeated violations escalate to account-level restriction.

---

## Definition of Done / Ready to Launch Checklist

Launch the $90 test only when EVERY box is ticked:

- [ ] NoseyMutt **Facebook Page** live with logo, cover, bio, Shop-now button.
- [ ] **@noseymutt Instagram** is a Business account, connected to the Page + portfolio.
- [ ] **wesale Business portfolio** created; email confirmed.
- [ ] **Ad account** created with **USD** currency + correct **timezone** (verified permanent settings are right).
- [ ] **Payment method** added (+ backup); **account spending limit = $200** set.
- [ ] **Shopify Facebook & Instagram channel** connected; **data sharing = Maximum**.
- [ ] **NoseyMutt dataset (Pixel)** created and connected.
- [ ] **AddToCart + Purchase** events confirmed firing in **Events Manager → Test events**, both tagged **Server** (CAPI live), no duplicate-pixel errors.
- [ ] **Domain `noseymutt.com` verified**; **business verification submitted** (pending is OK to launch).
- [ ] Store has a **live bundle/order-bump** lifting AOV toward $55–70, and **shipping times disclosed**.
- [ ] **3–5 creatives** ready, each **policy-clean** (no health claims, no personal-attribute phrasing, no competitor IP).
- [ ] Campaign built: **Sales objective, $15/day CBO, ad set optimizing for AddToCart, broad US + Advantage+ audience, Advantage+ placements, 3+ ads**, UTMs added.
- [ ] **Phase 1 kill/scale gates** written down where you'll read them; **column set** in Ads Manager shows Link CTR + Cost-per-ATC.
- [ ] **`finance/budget.md` updated** with the planned $90 test line *and* a reminder to log each Meta charge as it bills.

---

## Time + Cost Summary by Phase

| Phase | Hands-on time | Calendar wait | Cost |
|---|---|---|---|
| 0 Prerequisites | 1–2h | — | $0 new |
| 1 Facebook Page | 20 min | — | $0 |
| 2 Business portfolio | 15 min | email confirm | $0 |
| 3 Ad account | 10 min | — | $0 |
| 4 Payment + spend limit | 15 min | — | $0 (charges later) |
| 5 Instagram | 10 min | — | $0 |
| 6 Shopify channel + Pixel/CAPI | 20 min | — | $0 |
| 7 Business + domain verification | 20 min | **5–15 business days** (async) | $0 |
| 8 Verify ATC + Purchase events | 20–30 min | — | refundable test order |
| 9 Confirm CAPI | 0–10 min | — | $0 |
| 10 Build $90 campaign | 45–60 min | <24h ad review | **~$90 media** |
| 11 Decision rules | ongoing | 6 days run | (in the $90) |
| 12 Policy guardrails | (built in) | — | $0 |
| **Total** | **~3–5h hands-on** | **~5–10 days** (verification + ad review run in parallel) | **~$90 all-in test** |

**Reminder:** log every Meta charge in `finance/budget.md` (Ledger) as it bills. Test exposure target: **~$90 Phase 1**, ≤ **$200** total across both phases, **reserve untouched until SCALE**.

---

## Sources (Meta help-center + 2026 guides; flag = label likely to change)

- Business portfolio (was "Business Manager") — [Meta Business Help: Create a business portfolio](https://www.facebook.com/business/help/1710077379203657) · [Leadsie: Suite vs Portfolio](https://www.leadsie.com/blog/meta-business-manager-vs-meta-business-suite-differences) · [Duplex Ventures 2026 guide](https://duplex-ventures.com/how-to-use-meta-business-suite-guide/)
- Ad account currency/timezone permanence — [Meta Business Help: ad account time zone](https://en-gb.facebook.com/business/help/754049591334898) · [Leadsie: create ad account](https://www.leadsie.com/blog/how-to-create-meta-business-manager-and-facebook-ad-account)
- Connect assets (Page/IG) — [3naves: connect your assets](https://www.3naves.com/blog-en/how-to-create-your-business-portfolio-in-meta-and-connect-all-your-assets.htm)
- Billing, payment, spending limits, new-account warm-up — [Get-Ryze: billing setup](https://www.get-ryze.ai/blog/meta-ads-billing-payment-setup-beginner-guide) · [Get-Ryze: spending limits](https://www.get-ryze.ai/blog/meta-ads-account-spending-limit-and-budget-tracking-best-practices)
- Pixel/dataset + Conversions API via Shopify — [Shopify: Meta Pixel setup](https://www.shopify.com/blog/72787269-relax-advertising-on-facebook-just-got-a-lot-easier) · [Stormy AI: Pixel + CAPI for Shopify 2026](https://stormy.ai/blog/meta-pixel-conversions-api-shopify-tutorial-2026) · [wetracked: CAPI on Shopify](https://www.wetracked.io/post/set-up-facebook-conversion-api-on-shopify)
- Business/identity verification — [AGrowth: verify your business on Meta](https://agrowth.io/blogs/facebook-ads/how-to-verify-your-business-on-meta) · [AuditSocials: legitimacy check 2026](https://www.auditsocials.com/blog/meta-ad-account-legitimacy-verification-requirement-2026)
- Ad policy (health claims + personal attributes) — [Meta Transparency: Advertising Standards](https://transparency.meta.com/policies/ad-standards/) · [Accelerated Digital Media: health ad restrictions 2026](https://www.accelerateddigitalmedia.com/insights/guide-to-social-media-health-ad-restrictions-2026/) · [Gripas: claims & personal-attributes policy](https://gripasmarketing.com/meta-ads-claims-personal-policy/)

> **Change-watch flags:** "Business Manager" → now **Business Portfolio**; "Pixel" → now **dataset** in Events Manager; "Detailed Targeting" → now **Advantage+ audience**; "Advantage+ Shopping" UI shifts often; 2026 introduced stricter **advertiser identity verification** and new **monthly-invoicing/direct-debit** billing options. Re-check exact button labels against the live UI before each step.
