# CJ Live Sourcing & Integration Status — 2026-06-17

## Connection state
- CJ ↔ Shopify: **linked** (store authorized on CJ side).
- CJ REST API: **working** from this machine (token in `.env`, 1 req/sec).
- CJ MCP server: **authenticated** (API Key) but **unreliable** — the shared MCP endpoint
  (`developers.cjdropshipping.cn`) returns `Too Many Requests, one ip limit 3 users` on nearly every
  call (CJ's per-IP user cap on their shared server, not our pacing). This blocks MCP-driven
  search + `create_product_connection` right now.

## Key limitation discovered
CJ's REST product search **matches only a single keyword token** and ignores the rest:
- "lick mat" / "snuffle mat" → matched only "mat" → floor/cooling mats (junk)
- "snuffle ball" → matched only "ball" → random balls (junk)
- "slow feeder bowl" / "collapsible dog bowl" → matched "bowl" → **real pet bowls** ✓

⇒ The API reliably finds **bowls**, but **cannot surface lick mats, snuffle mats, treat puzzles, or
travel bowls** by keyword. Those are best sourced **visually in the CJ app** (photos, reviews,
warehouse, shipping calculator).

## VERIFIED source — Slow-Feeder Bowl (hero component)
- **Product:** Household Silicone Slow-feeding Dog Bowl
- **CJ PID:** `2606130757481633800` · **SPU:** `CJYD2933018`
- **Price:** $3.34–5.31 (variant-dependent) · weight 440–805 g
- **Variants (3):**
  - `CJYD293301801AZ` Soothing Licking Bowl — $3.34 (vid 2606130757481634600)
  - `CJYD293301802BY` Square Mat — $5.31 (vid 2606130757481635200)
  - `CJYD293301803CX` Soothing Licking Bowl + Sucker — $3.62 (vid 2606130757481635900)
- **Margin @ $27 retail:** ~80–88% gross. ✅ Excellent.
- Backup bowls: `2606120626181635400` ($2.99), `2606130342141605800` ($2.07).

## FINAL launch lineup (5 SKUs) — verified CJ sources
User browsed CJ and found real products; verified via API. Dropped Travel Bowl + Refill 3-Pack
(no good CJ source / contrived) → drafted in Shopify.

| Shopify SKU | Retail | CJ product (verified) | CJ PID | CJ cost | Margin |
|---|---|---|---|---|---|
| Boredom-Buster Starter Kit | $59 | (bowl+lickmat+snuffle) | — | ~$21 | ~63% |
| Slow Feeder Bowl | $27 | Slow Feeder Dog Bowl Silicone | `1834432475368935424` | $2.48 | ~91% |
| Lick Mat | $17 | Dog Licking Mat Peanut Lick Pad | `1402533508353757184` | $1.52–4.27 | ~82% |
| Snuffle Mat | $32 | Pet Dog Snuffle Mat Foraging Toy | `2020069592964943873` | $16.51 | ~48% |
| Treat Puzzle Toy | $22 | Pet Puzzle Slow Dispensing Feeder | `1574CAB1-85D2-4B0E-9B53-FD1B23763674` | $2.88 | ~87% |

Snuffle is the cost outlier ($16.51, only 21 listings) — repriced to $32 for margin; consider a
cheaper snuffle later.

## Upsell candidates (verified) — pending add
| Name | CJ PID | CJ cost | Suggested retail | Margin | Notes |
|---|---|---|---|---|---|
| Silicone Licking Plate (2nd lick format) | `2604210343391628100` | $1.83 | $14 | ~87% | ⭐ New order-bump; recovers the AOV play |
| Adjustable Treat-Dispensing Ball | `2060273901891014657` | $13.60 | $27 | ~50% | On-theme foraging, rolling format |
| Dog Rope Tug Toy (XXL) | `2034564711125245954` | $7.41 | $19 | ~61% | 83 listings (most popular); broad cross-sell, off strict theme |
| Chase Buddy motion ball | `2047228520268357633` | $9.90 | $29 | ~66% | ⚠️ likely battery-powered → violates no-electronics guardrail (ship/ad risk) |

## Recommendation
1. Connect the 5 core CJ products (PIDs above) in the CJ app (or MCP when its shared server frees).
2. Build the kit single-supplier/same-warehouse where possible (single parcel).
