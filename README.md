# wesale

A drop-ship business, built and operated as a small autonomous company. Claude acts as CEO; specialized sub-agents handle research, sourcing, marketing, and storefront build-out.

## Mission

Find a profitable drop-ship niche, source reliable suppliers, stand up a storefront, and reach profitability as fast as possible on a **total budget of $500**.

## Operating principles

1. **Profit fast, spend slow.** Every dollar is tracked in [`finance/`](finance/). Validate demand before paying for inventory commitments or premium tooling.
2. **Research before commitment.** No niche is chosen, and no money is spent, until the research folders justify it.
3. **One source of truth.** Decisions and their rationale live in [`docs/`](docs/). Raw findings live in [`research/`](research/).
4. **Agents do the legwork.** Reusable agent briefs live in [`agents/`](agents/); their outputs land in [`research/`](research/).

## Structure

| Folder | Purpose |
|---|---|
| [`agents/`](agents/) | Briefs / prompts for the specialized sub-agents (niche research, supplier sourcing, marketing, storefront). |
| [`research/`](research/) | Findings: candidate niches, dropship/supplier availability, marketing channels, competitor analysis. |
| [`storefront/`](storefront/) | Storefront build-out — platform choice, theme, product pages, eventually code. |
| [`marketing/`](marketing/) | Channel plans, ad creative, content calendar, launch playbook. |
| [`finance/`](finance/) | Budget ledger ($500 cap), unit economics, P&L. |
| [`docs/`](docs/) | Strategy, decisions (ADRs), and the running playbook. |

## Status

- **Phase:** 1 — brand chosen (**NoseyMutt**), MVP store package built, ready to assemble in Shopify
- **Budget remaining:** $500.00 / $500.00 (see [`finance/budget.md`](finance/budget.md))
- **Brand:** **NoseyMutt** (`noseymutt.com` available) — Enrichment / Anti-Boredom dog brand. Flagship "Boredom-Buster Starter Kit" $59 (~73% blended margin), sourced single-supplier from CJ to ship as one parcel.
- **Storefront:** Full paste-ready package in [`storefront/`](storefront/) (brand, catalog+copy, policies, go-live checklist, browser preview). Stack: Shopify Basic + DSers/CJ.
- **From-zero guides ready:** [`storefront/shopify-setup-walkthrough.md`](storefront/shopify-setup-walkthrough.md) (no Shopify account needed yet) and [`marketing/meta-ads-setup-walkthrough.md`](marketing/meta-ads-setup-walkthrough.md) (no Meta account needed yet).
- **Cheap traffic engine:** [`marketing/cheaper-channels.md`](marketing/cheaper-channels.md) (Pinterest, TikTok/Reels, gifting, email) + [`marketing/seo-strategy.md`](marketing/seo-strategy.md) (blog/SEO). Start these *before* paid ads.
- **Next:** build the store (Shopify walkthrough) → start organic/SEO → place the CJ sample order through the live store → run the $90 Meta test.

## Roadmap

- [ ] **Phase 0 — Research:** niche candidates, supplier availability, channel feasibility, competitor scan.
- [ ] **Phase 1 — Selection:** pick 1 niche + 2–3 hero products with a defensible margin and a clear traffic path.
- [ ] **Phase 2 — Build:** stand up storefront, list hero products, set up payments + tracking.
- [ ] **Phase 3 — Launch:** small paid test + organic, measure CAC vs. margin.
- [ ] **Phase 4 — Scale or pivot:** double down on winners, kill losers.
