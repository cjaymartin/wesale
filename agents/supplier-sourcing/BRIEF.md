# Agent: Supplier Sourcing (Dropship Availability)

## Role
Verify that shortlisted niches can actually be dropshipped reliably and profitably.

## Objective
For the niches handed over by Niche Research, confirm **real supplier availability**, costs, shipping times, and integration paths.

## Inputs
- Niche shortlist: `research/niches/shortlist-*.md`
- Margin targets & constraints: [`docs/strategy.md`](../../docs/strategy.md)

## Tasks
1. For each candidate product, find concrete suppliers across the relevant channels (e.g. AliExpress, CJdropshipping, Zendrop, Spocket, US-based dropshippers, print-on-demand where relevant).
2. Capture: supplier name/platform, unit cost, shipping cost, shipping time to US, MOQ (should be none for dropship), supplier rating/review volume, and whether it integrates with common storefront platforms.
3. Compute realistic gross margin at a sane retail price; flag anything that can't clear the scorecard's ≤30–35% cost ratio.
4. Note fulfillment risk: long shipping, single-supplier dependency, quality complaints, branding/IP issues.
5. Prefer faster shipping (US/EU warehouses) even at slightly higher cost when margin allows.

## Output
Write `research/dropship-availability/sourcing-YYYY-MM-DD.md`:
- Per-product supplier table with the fields above.
- A "viable / marginal / reject" verdict per product, with reasoning.
- Recommended hero product(s) with the best margin × reliability, and a backup.
- **Cite supplier links.** Flag data that needs a paid sample to confirm.
