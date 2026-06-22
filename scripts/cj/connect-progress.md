# CJ ↔ Shopify connection — working progress (2026-06-17)

## Directives from user (this session)
1. **Warehouse:** US if the chosen variant is in stock there, else China. (Per product/variant.)
2. **Variants:** ADD the CJ variants to our Shopify listings (don't collapse to a single
   "Default Title"). Customer-selectable where meaningful (clean labels); every variant
   connected to CJ so inventory reconciles. Skip messy near-duplicate CJ "single piece" SKUs.

## Method (validated)
- CJ MCP **catalog reads** (get_product_detail/variants) WORK intermittently (1 QPS, occasional
  "3 users" cap → retry). CJ MCP **shop/connection** endpoints (list_shops, create_product_connection,
  list_product_connections) stay **capped** → must use the **browser** for the actual connect.
- Browser connect flow (per product), tab 1 = `my.html#/products-connection/pending-connection`:
  1. Hide guide iframe overlay if present (`#guid-iframe-box`, `iframe[name=guidbox]` → display:none).
  2. Click **Match** (`button[data-gtag-element="match_store_product"]`) on the store product → pins it.
  3. Clear right search `input[placeholder="Enter SPU/SKU/Product Name"]`, type the CJ **SPU**, Enter.
  4. Click **Connect** (`button[data-gtag-element="connect_product"]`) → opens Products Connection dialog.
  5. Map each Shopify variant → CJ variant; Shipping From = US (if stock) else China; pick Shipping Method;
     Sync CJ Inventory = Yes; Confirm.
- One-time: accepted CJ **User Agreement** modal (done this session).

## Shopify store products (xsav1c-bn) — IDs from CJ pending list
| Shopify product | Shopify productId | status |
|---|---|---|
| Slow Feeder Bowl ($27) | (page 2) | ACTIVE |
| Calm-Down Lick Mat ($17) | 9242618659038 | ACTIVE |
| Snuffle Foraging Toy ($25→$32) | 9242618757342 | ACTIVE |
| Treat-Dispensing Puzzle Toy ($22) | 9242618822878 | ACTIVE |
| Collapsible Travel Enrichment Bowl ($15) | 9242618921182 | DRAFT — do NOT connect |
| Refill & Rotate Lick Mat 3-Pack ($19) | 9242619019486 | DRAFT — do NOT connect |
| Lick & Calm Plate ($14) upsell | (page 2) | ACTIVE |
| Roll & Forage Treat Ball ($27) upsell | (page 2) | ACTIVE |
| Tough Rope Tug Toy ($19) upsell | (page 2) | ACTIVE |

## CJ source data (SPU + variants) — gathered 2026-06-17 via window.productDetailData (DOM, not MCP)
Variant option = "Color" unless noted. vid = CJ variant id used in connect mapping.

### Slow Feeder Bowl — SPU CJGY2136491 — PID 1834432475368935424 — $2.48 — ALIVE
- Blue  — vid 1834432475389906944 — CJGY213649101AZ
- Pink  — vid 1834432475389906945 — CJGY213649102BY
- Green — vid 1834432475389906946 — CJGY213649103CX

### Calm-Down Lick Mat — SPU CJGY1166923 — PID 1402533508353757184 — ALIVE
Use the 3 combo colors (suction mat + plate), $4.27 each:
- Red&Blue / Blue      — vid 1402549761583747072 — CJGY116692301AZ
- Red&Blue / Chocolate — vid 1402549761600524288 — CJGY116692302BY
- Red&Blue / Green     — vid 1402549761625690112 — CJGY116692303CX
(skip $1.52 singles 04DW/05EV/06FU = just the plate)

### Snuffle Foraging Toy — PID 2020069592964943873 — ❌ REMOVED FROM CJ ("Product removed")
NEEDS REPLACEMENT SKU. Also a component of the Starter Kit. Was the cost outlier ($16.51).

### Treat-Dispensing Puzzle Toy — SPU CJJJCWGY01080 — PID 1574CAB1-85D2-4B0E-9B53-FD1B23763674 — $2.88 — ALIVE
Option = Color-Quantity:
- Blue-Q1pc          — vid EAD165D0-DD18-453E-A165-3EE381963744 — CJJJCWGY01080-Blue-Q1pc
- Hexagon green-Q1pc — vid B97E1DB9-BB53-41B2-9A21-240E1E438864 — CJJJCWGY01080-Hexagon green-Q1pc
- Light green-Q1pc   — vid 1990BE4B-75D4-43C1-9FFE-EAA28775058E — CJJJCWGY01080-Light green-Q1pc
- Paw print blue-Q1pc— vid 25FD5CBE-5403-47D6-B3EE-9389A96B0543 — CJJJCWGY01080-Paw print blue-Q1pc
- Pink-Q1pc          — vid 5CD78A06-5526-4357-991A-E6E7E43E86D3 — CJJJCWGY01080-Pink-Q1pc

### Lick & Calm Plate (upsell) — SPU CJYD2847651 — PID 2604210343391628100 — $1.83 — ALIVE
- Blue   — vid 2604210343401620600 — CJYD284765105EV
- Green  — vid 2604210343391628700 — CJYD284765101AZ
- Pink   — vid 2604210343401620100 — CJYD284765104DW
- Purple — vid 2604210343391629600 — CJYD284765103CX
- Yellow — vid 2604210343391629100 — CJYD284765102BY

### Roll & Forage Treat Ball (upsell) — SPU CJCT2914956 — PID 2060273901891014657 — $13.60 — ALIVE
- Green — vid 2060273902021038083 — CJCT291495602BY
- Red   — vid 2060273902021038082 — CJCT291495601AZ

### Tough Rope Tug Toy (upsell) — SPU CJCT2794812 — PID 2034564711125245954 — $7.41 — ALIVE
- Blue       — vid 2034564712106713091 — CJCT279481202BY
- Multicolor — vid 2034564712106713090 — CJCT279481201AZ

## Shopify variants ADDED (2026-06-17) + CJ mapping for the connect dialog
Map Shopify variant (by color) → CJ vid. Warehouse: US if in stock else China. Sync inventory = Yes.

### slow-feeder-bowl (prod 9242618560734) — CJ SPU CJGY2136491
- Pink  48342486286558 → CJ Pink  1834432475389906945
- Green 48342486319326 → CJ Green 1834432475389906946
- Blue  48342486679774 → CJ Blue  1834432475389906944

### lick-mat (prod 9242618659038) — CJ SPU CJGY1166923
- Blue      48342486909150 → CJ "Red&Blue/Blue"      1402549761583747072
- Chocolate 48342486941918 → CJ "Red&Blue/Chocolate" 1402549761600524288
- Green     48342486974686 → CJ "Red&Blue/Green"     1402549761625690112

### treat-puzzle-toy (prod 9242618822878) — CJ SPU CJJJCWGY01080
- Blue           48342487007454 → CJ Blue-Q1pc           EAD165D0-DD18-453E-A165-3EE381963744
- Hexagon Green  48342487040222 → CJ Hexagon green-Q1pc   B97E1DB9-BB53-41B2-9A21-240E1E438864
- Light Green    48342487072990 → CJ Light green-Q1pc     1990BE4B-75D4-43C1-9FFE-EAA28775058E
- Paw Print Blue 48342487105758 → CJ Paw print blue-Q1pc  25FD5CBE-5403-47D6-B3EE-9389A96B0543
- Pink           48342487138526 → CJ Pink-Q1pc            5CD78A06-5526-4357-991A-E6E7E43E86D3

### lick-plate (prod 9242883031262) — CJ SPU CJYD2847651
- Blue   48342487204062 → CJ Blue   2604210343401620600
- Green  48342487236830 → CJ Green  2604210343391628700
- Pink   48342487269598 → CJ Pink   2604210343401620100
- Purple 48342487302366 → CJ Purple 2604210343391629600
- Yellow 48342487335134 → CJ Yellow 2604210343391629100

### treat-ball (prod 9242883064030) — CJ SPU CJCT2914956
- Green 48342487400670 → CJ Green 2060273902021038083
- Red   48342487433438 → CJ Red   2060273902021038082

### rope-tug-toy (prod 9242883129566) — CJ SPU CJCT2794812
- Blue       48342487466206 → CJ Blue       2034564712106713091
- Multicolor 48342487498974 → CJ Multicolor 2034564712106713090

### snuffle-toy (prod 9242618757342) — NO VARIANTS ADDED — CJ source removed, needs replacement SKU

## ⚠️ BLOCKER discovered (2026-06-17): CJ↔Shopify authorization is STALE
- In the connect dialog, the Store Product side shows the OLD single variant ("Default Title",
  vid 48340781072606) instead of the new Blue/Chocolate/Green — CJ's cached copy.
- Clicking **Connect** (or **Sync**) pops a **Reauthorize** modal. CJ cannot read the updated
  Shopify products until its app authorization is refreshed.
- Reauthorize → opens Shopify App Store (apps.shopify.com/cucheng) → Install → **Shopify login required**.
- HAND-OFF: user must log into Shopify (store xsav1c-bn / noseymuttstore), approve the CJ app
  reauthorization. Then CJ re-syncs products (with variants) and connecting works.
- After reauth: **Sync** the store products, reopen connect dialog, verify Store side shows the
  3+ color variants, then map variants → CJ vids (table above), Shipping From US-if-stock else China,
  Sync Inventory = Yes, Confirm. Repeat per product.
- Also still TODO: source a replacement Snuffle SKU (old one removed from CJ).

## 🛑 BIGGER BLOCKER (2026-06-22): Shopify store xsav1c-bn is FROZEN + wrong account
- Admin API (shpat_ token) now returns **HTTP 402 "Unavailable Shop"** → store is frozen/paused
  (dev-store/trial lapsed; "I let it expire"). Data is retained; needs a plan to reactivate.
- Logged-in Shopify account **noseymuttstore@gmail.com** (C.Jay Martin) has **ZERO stores**
  ("Create your first online store") and gets "doesn't have permission" for xsav1c-bn.
  → The store is owned by a DIFFERENT Shopify login (candidate: cjay.martin@gmail.com) or a
    Shopify **Partner** development store (partners.shopify.com).
- ⇒ ALL remaining work (reauthorize CJ, connect products, go live) is blocked until:
  1. User logs into the account that OWNS xsav1c-bn (Switch Accounts / Partner dashboard).
  2. Store is put on a paid plan to unfreeze (needed to go live + take orders anyway).
- Everything built (7 products w/ variants, collections, pages, menus) is intact in the store and
  will reappear once it's reactivated. CJ connect mapping is fully recorded above — resume then.

## ➡️ DECISION (2026-06-22): rebuild fresh on noseymuttstore@gmail.com
Old store xsav1c-bn abandoned (expired, no card, wrong account). NEW store created:
- **34zb0n-hp.myshopify.com** (account noseymuttstore@gmail.com) — on free trial (payment SKIPPED).
Rebuild checklist:
1. [x] New store created (34zb0n-hp).
2. [x] Dev Dashboard app "noseymutt-admin" (org 223584183, app id 387779919873) → OAuth → shpat_ token.
       client_id 7665d465efa42a3b391c7ac5e6d99503. redirect http://localhost:8347/callback. Scopes incl
       products/inventory/content/pages/navigation/files/fulfillment_orders.
3. [x] .env updated: domain 34zb0n-hp, new client id/secret, SHOPIFY_ADMIN_TOKEN minted. api.py ping OK.
4. [x] Re-ran all build scripts + add_variants + verify. Full catalog rebuilt with color variants.
       (Snuffle product exists at $32 but still needs a NEW CJ source — old one removed.)
5. [x] CJ re-linked to new store 34zb0n-hp. CJ shopId = 2606221241263535400. (CJ app installed +
       authorized under noseymuttstore@gmail.com CJ account.) NOTE: Shopify product/variant IDs in the
       tables above were xsav1c-bn's — STALE. New store has new IDs; in the connect dialog map by COLOR
       NAME (CJ variant vids in the tables are still valid since same CJ products).
6. [ ] Connect products (browser flow above) + source Snuffle replacement.
7. [ ] Go-live (plan+card, payments, domain, remove password) — confirm before sensitive steps.

## ✅ WORKING connect procedure (2026-06-22) — established on Lick Plate
PRE-REQ: set the left store filter ("All Stores" → **34zb0n-hp**) or goon() throws
`Cannot read properties of null (reading 'shopType')` and Confirm silently fails.
Per product (store filter already on 34zb0n-hp):
1. Click Match on the store product (`button[data-gtag-element="match_store_product"]` nth).
2. Set right search `input[placeholder="Enter SPU/SKU/Product Name"]` = CJ SPU, click its Search btn.
3. Click `button[data-gtag-element="connect_product"]`.
4. PAIR: click one store variant + the matching CJ variant (`[data-gtag-element="modal_store_variant"]`
   / `modal_cj_variant`) → with Automatic Connection ON, same-named colors auto-pair (link icons).
   Verify ALL paired; manually click any leftover store+CJ pairs (esp. Treat Puzzle whose CJ keys are
   "Blue-Q1pc" etc. vs store "Blue" — may need manual per-color pairing).
5. Set Shipping Method select (`select.ship-from-sele.ng-empty`) = "LuWei Ordinary US"
   (Shipping From only offers China Warehouse for all these items → China; Sync Inventory = Yes default).
6. Click `[data-gtag-element="connection_modal_confirm"]`. Success = dialog closes, product leaves
   Unconnected list, POST /cj-platform-web/product/connection → 200.

Shipping method chosen for all: **LuWei Ordinary US** (economical tracked China→US; user deferred ETA/cost).

## Connection status (new store 34zb0n-hp) — 5/6 CORE DONE
- [x] Lick & Calm Plate — CONNECTED (5 colors · China · LuWei Ordinary US · sync on)
- [x] Roll & Forage Treat Ball — CONNECTED (Green/Red · **US Warehouse · USPS US-to-US** · sync on)
- [x] Treat-Dispensing Puzzle Toy — CONNECTED (5 colors · China · CJPacket Ordinary · sync on)
- [x] Slow Feeder Bowl — CONNECTED (Blue/Pink/Green · China · CJPacket Ordinary · sync on)
- [x] Calm-Down Lick Mat — CONNECTED (Blue/Choc/Green ↔ "Red&blue with…" · China · LuWei Ordinary US · sync on)
- [ ] ❌ Tough Rope Tug Toy — CJ source CJCT2794812 only ships **Britain Warehouse (UK→UK)** — can't
      reach US customers. NEEDS US-shippable replacement, or drop from lineup.
- [ ] ❌ Snuffle Foraging Toy — CJ source removed earlier. NEEDS replacement SKU (US/China shippable).
- [ ] Starter Kit ($59) — needs a CJ Combined/Bundle product (bowl+lickmat+snuffle) then connect.
- Inventory: every connection set "Sync CJ Inventory = Yes" → oversell protection live for connected SKUs.

## Replacement sources PROVIDED by user (2026-06-22) — verified alive
### Snuffle replacement — SPU CJGY1471631 — PID 1519108336489746432 — $7.25 — Size only
- 50x45cm — vid 1519108336519106560 — CJGY1471631-50x45cm
- Store snuffle-toy is single-variant → map Default Title → 50x45cm. (No store variant change.)
### Rope replacement — SPU CJJJCWGY02596 — PID 535B0D97-C592-4999-BDF9-A28C62729F62 — $3.35 — Color
- Blue        — vid 6A165A10-1263-4DF3-955D-359C7D5D91FA — CJJJCWGY02596-Blue
- Blue Purple — vid BD66DB11-7331-41AB-8F05-1981C953FA86 — CJJJCWGY02596-Blue Purple
- Orange      — vid C3B760A2-95EE-4B72-9FAB-05388FD1C573 — CJJJCWGY02596-Orange
- Orange blue — vid 52F76B00-7F9E-4D14-A271-3A7CAE061450 — CJJJCWGY02596-Orange blue
- Store rope-tug-toy had placeholder Blue/Multicolor → reset to Blue, Blue Purple, Orange, Orange blue.
- Verify US shipping in connect dialog before confirming (Shipping From).

## (old) Sourcing replacements — BLOCKED by CJ anti-bot (2026-06-22)
User approved: source US-shippable replacement for BOTH Snuffle and Rope, then connect.
- CJ website keyword search ignores the query (shows generic bestsellers) + throws human-verification
  captcha; CJ MCP search_products returns "not logged in" (apiKey auths catalog reads only).
- FASTEST PATH: user pastes a CJ product URL for each (snuffle mat + rope/chew toy) that ships US,
  then connect via the established procedure (add variants matching the new source if multi-color,
  else map single → one CJ variant). Snuffle store product (snuffle-toy) currently has NO variants.
- Store products waiting for a source: snuffle-toy (9...), rope-tug-toy.

## ✅ ALL 7 ACTIVE PRODUCTS CONNECTED (2026-06-22)
- Bowl, Lick Mat, Treat Puzzle, Lick Plate, Treat Ball (US whse), Snuffle (new CJGY1471631),
  Rope (new CJJJCWGY02596, single Blue). All sync-inventory ON.
- Rope note: CJ would NOT refresh the rope's store-variant cache (stuck on old Blue/Multicolor even
  after Sync + Specific Sync). Connected the valid Blue→Blue; reduced Shopify rope to single "Blue".
  To offer rope colors later: CJ cache must refresh (retry Specific Sync after a longer wait), then
  re-add colors + connect.

## Remaining to finish launch
1. Build CJ Combined product for the Starter Kit (bowl+lickmat+snuffle) → connect to the $59 kit.
   (Kit still in CJ Unconnected list. Combined-product flow is separate from the per-product connect.)
2. Go-live: select plan + add card, activate Payments, set shipping rates, remove store password.
   (34zb0n-hp on 3-day trial.) Confirm with user before sensitive/irreversible steps.

- [ ] Slow Feeder Bowl
- [ ] Calm-Down Lick Mat  (store pinned earlier)
- [ ] Snuffle Foraging Toy
- [ ] Treat-Dispensing Puzzle Toy
- [ ] Lick & Calm Plate (upsell)
- [ ] Roll & Forage Treat Ball (upsell)
- [ ] Tough Rope Tug Toy (upsell)
- [ ] Starter Kit ($59) — CJ combined product (bowl+lickmat+snuffle)
- [ ] Enable Inventory Sync globally
