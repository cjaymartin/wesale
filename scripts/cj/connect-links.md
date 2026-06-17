# CJ → Shopify connect deep-links (NoseyMutt)

Each link opens the CJ product with the **Connect** dialog auto-triggered (`?connect=1`).
In the dialog: match to the Shopify product, map the variant, pick **CJ US warehouse**, Confirm.

| # | CJ PID | Shopify product to select | Connect link |
|---|---|---|---|
| 1 | 1834432475368935424 | Slow-Feeder Enrichment Bowl | https://www.cjdropshipping.com/product/slow-feeder-dog-bowls-silicone-dog-puzzle-feeder-bowl-for-healthy-eating-puppy-slow-feeder-bowl-anti-choking-dog-slow-feeder-bowls-p-1834432475368935424.html?connect=1 |
| 2 | 1402533508353757184 | Calm-Down Lick Mat | https://www.cjdropshipping.com/product/dog-licking-mat-slow-feeder-peanut-lick-pad-with-suction-p-1402533508353757184.html?connect=1 |
| 3 | 2020069592964943873 | Snuffle Foraging Toy | https://www.cjdropshipping.com/product/pet-dog-snuffle-mat-sniffing-treat-foraging-puzzle-feeder-toy-nose-training-pad-p-2020069592964943873.html?connect=1 |
| 4 | 1574CAB1-85D2-4B0E-9B53-FD1B23763674 | Treat-Dispensing Puzzle Toy | https://www.cjdropshipping.com/product/pet-puzzle-toys-increase-interactive-slow-dispensing-feeding-training-games-feeder-p-1574CAB1-85D2-4B0E-9B53-FD1B23763674.html?connect=1 |
| 5 | 2604210343391628100 | Lick & Calm Plate (upsell) | https://www.cjdropshipping.com/product/slow-food-bowl-silicone-licking-mat-licking-plate-p-2604210343391628100.html?connect=1 |
| 6 | 2060273901891014657 | Roll & Forage Treat Ball (upsell) | https://www.cjdropshipping.com/product/dog-puzzle-toy-adjustable-treat-dispensing-ball-food-dispenser-p-2060273901891014657.html?connect=1 |
| 7 | 2034564711125245954 | Tough Rope Tug Toy (upsell) | https://www.cjdropshipping.com/product/dog-rope-toys-large-xxl-rope-toys-for-large-dogs-teeth-cleaning-tug-of-war-p-2034564711125245954.html?connect=1 |

**Starter Kit ($59):** assemble a CJ Combined/Bundle product (bowl + lick mat + snuffle), then connect that to the kit. Not a single-link connect.

**After connecting all:** CJ → My Stores → enable **Inventory Sync** (feeds stock to Shopify; with `inventoryPolicy=DENY` already set, prevents overselling).

## Browser automation (Playwright MCP)
Registered in user config (`npx @playwright/mcp@latest`, headed, DISPLAY=:1). Loads after a Claude Code restart. Post-restart flow: open browser → user logs into CJ + Shopify (persistent profile) → drive connect dialogs + go-live steps.
