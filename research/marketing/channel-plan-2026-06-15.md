# Channel-Economics Playbook — Tiny-Budget Dropship Launch

**Date:** 2026-06-15
**Author:** Marketing agent (wesale)
**Scope:** Generic playbook for a **$20–60 impulse / problem-solving** dropship product, **US market**, no specific SKU chosen yet.
**Budget context:** $500 hard cap; paid-traffic test allotment **$100–200**; ~$100 reserve untouched until a winner is proven. (Source: `finance/budget.md`)

---

## 1. The economic frame: what "break-even" actually requires

Before channels, fix the unit economics, because they decide whether *any* paid channel closes.

**Working assumptions (flag: illustrative — replace with real numbers once a SKU is chosen):**

| Variable | Assumption | Basis |
|---|---|---|
| Retail price (AOV, 1 unit) | **$39** | Mid-point of the $20–60 impulse band; high enough that ad math can work (strategy.md bans sub-$10). |
| Landed product cost | **$11.70** (30% of retail) | strategy.md selection rule: landed cost ≤ 30–35% of retail. |
| Payment processing | ~3% ($1.17) | Standard Shopify/Stripe ~2.9% + $0.30. |
| **Gross margin per order (before ad spend)** | **~$26 (≈67%)** | $39 − $11.70 − $1.17 ≈ $26.13. |
| **Break-even CAC** | **≤ $26** | You break even on ad spend when CAC = gross margin. Profit requires CAC well below this. |
| Target CAC for healthy scale | **≤ $13 (2× MER)** | Leaves ~$13/order to fund inventory, returns, reserve. Implies needed blended ROAS ≈ **3×**. |

**The single most important number:** with ~$26 gross margin, **break-even CAC is $26 and target CAC is ~$13.** Every channel below is judged against those two lines. The budget.md kill rule (kill if cumulative ad spend > 1.5× gross margin generated) maps to a **break-even ROAS floor of ~2.2×** at this margin — anything under that on a sustained basis is a kill.

> **Assumption flag:** a single-unit AOV of $39 is thin for paid acquisition. The realistic path to profit is **lifting AOV via a 2-for / bundle / order-bump to ~$55–70**, which roughly doubles per-order margin to ~$35–45 and pulls every channel below into the green. Treat bundle/upsell construction as a *prerequisite*, not an optimization.

---

## 2. Channel-by-channel economics (2026 US benchmarks)

CAC below is modeled as **CPC ÷ landing-page conversion rate** (a click-to-purchase CVR of ~2% assumed for a decent store on cold traffic, lower for pure-impulse), cross-checked against published CPA benchmarks. All figures are *cold-traffic* unless noted.

### A. Organic TikTok / Reels (UGC, self-shot)
- **Cost:** $0 media. Cost = your time + maybe a $50–100 product sample.
- **Benchmark / mechanics:** Operators post **2–5 native videos/day**; a video clearing **1k+ views is a "signal" winner** to be recreated with variations. Realistic time-to-meaningful-sales: **30–60 days** of consistent posting. ([Ecommerce.co][8], [AutoDS][6])
- **Effective CAC:** approaches **$0** if a video pops; **infinite (time sunk, no sales)** if nothing hits. Bimodal, not a smooth curve.
- **Min viable "spend":** 30 days × 2–3 posts/day of disciplined testing.
- **Speed-to-signal:** Slow & lumpy (days→weeks), but the cheapest CAC that exists.
- **Verdict:** **Run always, in parallel with everything.** It is the only channel that can drive CAC below the paid floor, and it doubles as free creative testing for paid.

### B. Meta (Facebook/Instagram) Advantage+ / Sales campaigns
- **2026 benchmarks (ecommerce):** median **CPM ~$14.19**, avg **CPC ~$0.78**, purchase **CVR median ~1.6%**, avg **CPA ~$29.99**, avg ROAS ~1.86×. Advantage+ Shopping delivers ~**32% lower CPA** than manual. ([Get-Ryze][1], [27five][5])
- **Modeled CAC:** at $0.78 CPC and 2% store CVR → **~$39 CAC**. Published median CPA **~$30**. Either way, **above the $26 break-even line at single-unit AOV** — only closes with the bundle/AOV lift.
- **Critical constraint:** the learning phase needs **~50 optimization events/week**. At a $20–30 CPA that's **~$140–215/day** to exit learning in a week — *far beyond this budget.* ([Benly][9], [Wonderful][9b])
  - **Workaround (mandatory at this budget):** optimize for a **higher-frequency proxy event (Add-to-Cart / Initiate Checkout)**, not Purchase, so the pixel gets enough events to learn on ~$20–30/day. ([Benly][9])
- **Min viable spend:** ~$20–30/day for 5–7 days per test cell.
- **Speed-to-signal:** Fast (CTR/CPC/ATC readable in 2–3 days; ~$50–80 in).
- **Verdict:** **Best paid channel for speed-to-signal on a small budget**, but only profitable with AOV lift + proxy-event optimization. This is the **primary paid test channel.**

### C. Pinterest Ads
- **2026 benchmarks:** **CPC ~$0.50–$1.50** (often cheaper than Meta), CPM ~$3–$5, promoted-pin CVR **2–4%** (5–8% home/decor), strong on **search/purchase intent**. ([Coupler.io][2], [Pinwell][2b])
- **Modeled CAC:** $0.75 CPC ÷ 3% CVR → **~$25 CAC** — right at break-even, *better than Meta* for the right (visual, home/kitchen/beauty/gift) niche.
- **Min viable spend:** ~$10–20/day.
- **Speed-to-signal:** Slower than Meta (lower volume, longer consideration), readable in ~1–2 weeks.
- **Verdict:** **Strong backup paid channel** — cheaper clicks + intent — but only if the product is visual/aesthetic and female-skewing. Weaker for gadgets/problem-solvers aimed at men.

### D. Google Shopping
- **2026 benchmarks:** Shopping **CPC ~$0.30–$1.50**, ecommerce CVR ~0.5–1%, ecommerce **CPA commonly $15–$45**, ROAS 3–8× on well-built accounts. ([Bir.ch][3], [Groas][3b])
- **Modeled CAC:** strong intent can deliver **$15–30 CAC**, *but* requires a product feed, brand/cold competition, and these are **search-intent** buys — works for products people actively shop for, **not impulse/unknown novelty.**
- **Min viable spend:** ~$15–25/day; needs a clean product feed (Merchant Center) — setup overhead.
- **Speed-to-signal:** Medium; needs volume to learn.
- **Verdict:** **Defer.** Best CAC of the intent channels, but impulse/novelty products have little existing search demand, and feed setup is friction. Revisit only if the chosen SKU is a *known, searched* category.

### E. Marketplaces (Amazon / Etsy / eBay)
- **2026 fees:** Etsy ~**10–12% all-in** ($0.20 listing + 6.5% txn + 3%+$0.25 processing); Amazon **referral 8–15%** (most categories 15%) + FBA — total often **30–45% of price.** ([Webgility][4], [Printify][4b])
- **CAC:** "free" organic marketplace traffic exists, but **fees eat 10–45% of revenue** — at 30% landed cost, Amazon's 30–45% take can erase the entire margin. Etsy's ~11% is survivable for *handmade/personalized/aesthetic* goods only (generic dropship is against Etsy policy and against strategy.md's branded/IP caution).
- **Speed-to-signal:** Slow (ranking takes time); demand validation is muddied by marketplace search.
- **Verdict:** **Not for the launch test.** Fees + policy risk + slow ranking. Possible *later* channel for a proven Etsy-appropriate product. Marketplaces validate that demand exists but don't teach you a repeatable CAC.

### F. Influencer / UGC seeding
- **2026 rates:** nano (1k–10k) **$25–$300/video**, micro (10k–100k) **$200–$2,500/video**; **UGC-with-no-posting $30–$250** (40–60% cheaper than in-feed); pure **gifting/seeding** = cost of the sample only. ([Tomoson][7], [InfluencerMarketingHub][7b])
- **CAC:** unpredictable per-post; the *cheap* play is **gifting** (send product free to 10–20 nano creators, ask for an honest post) — cost = ~$120–200 in samples, zero media. Convert the best-performing creator clips into **Spark Ads** to lower paid CAC later.
- **Speed-to-signal:** Slow (outreach + shipping + posting lag = 2–4 weeks).
- **Verdict:** **Cheap creative engine, not a primary channel.** Use seeding to *generate native UGC assets* that feed organic + Meta, rather than as a standalone acquisition bet.

### Channel summary table

| Channel | Modeled CAC | vs $26 break-even | Min viable spend | Speed-to-signal | Role |
|---|---|---|---|---|---|
| Organic TikTok/Reels | ~$0 (bimodal) | ✅ (or no sales) | $0 + sample | Slow/lumpy | **Always-on, free CAC floor** |
| **Meta Adv+ (proxy event)** | ~$30–39 | ⚠️ needs AOV lift | $20–30/day | **Fast (2–3 d)** | **PRIMARY paid test** |
| **Pinterest** | ~$25 | ⚠️/✅ if visual | $10–20/day | Medium | **BACKUP paid** |
| Google Shopping | $15–30 | ✅ but intent-only | $15–25/day + feed | Medium | Defer (no impulse demand) |
| Marketplaces | fees 11–45% | ❌ margin risk | listing fees | Slow | Defer / later |
| Influencer seeding | sample cost | ✅ as asset source | $120–200 samples | Slow | Creative engine, not channel |

---

## 3. The $100–200 launch-test framework (concrete)

**Channel:** Meta (Advantage+ Shopping or a lean ABO sales campaign), **optimized for Add-to-Cart** (proxy event) so the pixel can learn on a small budget. Pinterest held as backup.

**Pre-flight (no media spend):** store live with a working bundle/order-bump to push AOV toward $55–70; pixel + ATC/IC + Purchase events firing; 3–4 creatives ready (see §5).

### Phase 1 — Creative signal test ($90, ~6 days)
- **3 ad creatives × 1 broad US ad set (age/gender per product), $15/day total**, ATC-optimized, Advantage+ audience.
- **Read after ~$90 / 3–4 days.** Primary metric: **CTR (link)** and **cost-per-ATC**.
- **Decision gates:**
  - **CTR ≥ 1.2%** (vs ~1.55% Meta ecommerce avg — we accept a bit below since it's cold/untested) AND **cost-per-ATC ≤ ~$3** → creative has signal → go Phase 2.
  - **CTR < 0.8%** across all 3 OR **cost-per-ATC > $6** with **0–1 ATC** → **KILL this product/creative.** Do not spend the remaining budget. Iterate creative or move to next SKU.

### Phase 2 — Conversion validation ($60–110, ~4–5 days)
- Kill losing creatives, **scale the winner to $20–25/day**, switch optimization toward **Purchase** (or keep ATC if volume too low).
- **Read against the kill/scale rule (from budget.md): kill if cumulative ad spend > 1.5× gross margin generated.**
- **Decision gates:**
  - **SCALE:** blended **ROAS ≥ 2.2×** (break-even at this margin) trending toward **3×**, CAC ≤ ~$26 with AOV lift in play → product validated. Tap reserve to scale at +20–30%/3 days; protect the learning phase (no big budget jumps).
  - **HOLD/ITERATE:** ROAS 1.5–2.2× → margin/AOV problem, not demand → fix bundle/price/upsell, re-test once.
  - **KILL:** ROAS < 1.5× after $60+ in Phase 2, or cumulative spend > 1.5× margin generated → dead. Stop, log, move to next candidate.

**Total exposure:** ~$150–200 across both phases — inside the test allotment, reserve untouched until a SCALE verdict.

> **Why ATC-as-proxy is non-negotiable here:** at ~$30 CPA, hitting 50 *purchase* events/week needs ~$140+/day (out of budget). ATC events are ~5–10× more frequent, letting the algorithm learn on $15–25/day. ([Benly][9])

---

## 4. Organic / free starter plan (to drive CAC below the paid floor)

Run from **day 1, in parallel** with the paid test — this is where real margin lives.

- **TikTok + Instagram Reels + YouTube Shorts:** post the **same** native, self-shot video to all three (cross-post, zero marginal cost). **2–3 videos/day for 30 days.** ([Ecommerce.co][8])
- **Content mix per week:** problem→solution demos (40%), "POV / you need this" hooks (20%), before/after or satisfying-use clips (20%), trending-audio remixes (10%), creator/review-style (10%).
- **Winner rule:** any video **>1k views in 24h** → save the audio, recreate 3–5 variants, double down. ([AutoDS][6])
- **Seeding loop:** gift product to **10–20 nano creators** (~$120–200 in samples, already a budgeted line) for honest UGC; license the best clip for **Spark Ads** to cut paid CAC. ([InfluencerMarketingHub][7b])
- **SEO/free basics:** keyworded product + collection titles/meta, a Pinterest business account with 5–10 rich pins/day (free, compounding, intent traffic), and an **email/SMS capture** (popup + abandoned-cart flow) so repeat purchases lower blended CAC.
- **Expectation flag:** organic realistically takes **30–60 days** to produce steady sales — it's the durable CAC-killer, not the day-1 revenue source. ([Ecommerce.co][8])

---

## 5. Reusable creative-angle templates (hook + value prop)

Plug the chosen product into these. Hooks in first 1–2 seconds, native/unpolished, captioned.

**Template 1 — Problem → Agitation → Product ("PAS")**
- *Hook:* "If you [specific recurring annoyance], stop scrolling."
- *Value prop:* "This [product] fixes it in [X seconds] — no [tools/skills/mess] needed."
- *Best for:* problem-solver SKUs on Meta + organic. Map to ATC test creatives.

**Template 2 — "I was today years old" / discovery**
- *Hook:* "I can't believe this only costs [$X]."
- *Value prop:* Fast demo of the satisfying result → "Grab yours before it sells out again."
- *Best for:* impulse/novelty, TikTok organic, Spark Ads from seeded creators.

**Template 3 — Before/After transformation**
- *Hook:* Show the messy/broken "before" on screen instantly.
- *Value prop:* "Here's the same thing 10 seconds later" → reveal → "link in bio."
- *Best for:* visually demoable products; doubles as the Pinterest pin and the Meta video.

---

## 6. Key assumptions & risks (flagged)

1. **AOV $39 / 67% margin is illustrative.** Real SKU must be re-run through §1. At single-unit AOV, **no paid channel reliably clears break-even** — the bundle/upsell is a prerequisite, not optional.
2. **Store CVR of 2% on cold paid traffic is optimistic for an unbranded dropship store**; could be 0.8–1.5%, which pushes Meta CAC to $40–50 and makes the AOV lift even more critical.
3. **Benchmarks are blended-industry averages**, not category-specific; actual CPC/CPM swing ±50% by niche and rise 40–60% in Q4. ([TikTok benchmarks][2])
4. **$100–200 is below Meta's learning-phase threshold for Purchase optimization** — the proxy-event workaround is what makes the test viable, but it tests *interest*, not full purchase efficiency. A SCALE verdict still needs validation at higher spend from reserve.
5. **Marketplaces and Google Shopping are deferred, not dismissed** — both can beat Meta on CAC for the *right* product type (Etsy-appropriate handmade; or a searched, known category).

---

## Sources
- Meta 2026 benchmarks: [Get-Ryze][1] https://www.get-ryze.ai/blog/meta-ads-cost-benchmarks-by-industry-2026 · [27five][5] https://www.27five.com/blog/meta-ads-benchmarks-ecommerce-2026/
- TikTok 2026 benchmarks: [Lebesgue/Trendtrack][2] https://www.trendtrack.io/blog-post/tiktok-vs-meta-cpm · https://lebesgue.io/tiktok-ads/tiktok-ads-benchmarks-for-ctr-cr-and-cpm
- Pinterest 2026: [Coupler.io][2] https://blog.coupler.io/ppc-statistics/ · [Pinwell][2b] https://pinwellmedia.com/pinterest-cpc-benchmarks-by-industry/
- Google Shopping 2026: [Bir.ch][3] https://bir.ch/blog/google-ads-cost-breakdown · [Groas][3b] https://www.groas.com/post/google-ads-cpc-cpa-benchmarks-by-industry-2026-complete-data-guide
- Marketplace fees 2026: [Webgility][4] https://www.webgility.com/blog/marketplace-fees-amazon-ebay-etsy-walmart · [Printify][4b] https://printify.com/blog/amazon-seller-fees/
- Influencer/UGC rates 2026: [Tomoson][7] https://tomoson.com/tiktok-influencer-rates · [InfluencerMarketingHub][7b] https://influencermarketinghub.com/micro-influencer-rates/
- Organic TikTok strategy 2026: [Ecommerce.co][8] https://ecommerce.co/blog/tiktok-organic-dropshipping-strategy · [AutoDS][6] https://www.autods.com/blog/dropshipping-tips-strategies/tiktok-dropshipping/
- Meta learning phase 2026: [Benly][9] https://benly.ai/learn/meta-ads/learning-phase-optimization · [Wonderful][9b] https://www.usewonderful.com/blog/meta-ads-learning-phase-50-conversions-per-week-help-center
