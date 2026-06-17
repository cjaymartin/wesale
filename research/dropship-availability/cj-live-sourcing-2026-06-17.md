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

## Recommendation
1. **Source the soft goods (lick mat, snuffle, treat puzzle, travel bowl) in the CJ app** —
   the API can't find them; the app's visual search can. Prefer **CJ US-WH** and the **same supplier
   as the bowl** where possible (single-parcel kit).
2. **Connect** either in the CJ app, or via the MCP `create_product_connection` once CJ's shared
   server frees up (retry later).
3. The bowl above is ready to connect now (PID + variant IDs listed).
