# Shopify Admin API tooling

Lets Claude build the store directly (products, collections, pages, menus, theme settings) via the Admin GraphQL API. Stdlib Python only — nothing to install.

## One-time setup (you do this)
1. In Shopify admin: **Settings → Apps and sales channels → Develop apps → Create an app**. Name it `wesale-builder`.
2. **Configure Admin API scopes** — check the writes below (search the list if needed):
   - `write_products` — products, variants, media
   - `write_publications` — publish products to the Online Store
   - `write_content` — pages, blogs/articles, menus
   - `write_online_store_pages` and `write_online_store_navigation` — *if listed separately*, check them too
   - `write_themes` — theme settings (colors/fonts/sections) *(optional)*
   - `write_files` — image/logo uploads
3. **Install app** → **API credentials** → **Reveal Admin API access token** (starts `shpat_`). You only see it once.
4. `cp .env.example .env` and paste the token + your `*.myshopify.com` domain into `.env`.
5. Tell Claude it's ready.

## Verify the connection
```bash
python3 scripts/shopify/api.py ping
```
Prints the store name/plan/URL if it works. **Never prints the token.**

## Security
- `.env` is gitignored — the token is never committed.
- Token is scoped to writes only; delete the `wesale-builder` app when the build is done to revoke it.
- The ping/build scripts never echo the token to logs.

## What runs after connection (Claude drives these)
1. `ping` → confirm access.
2. Create 7 products from `storefront/catalog.md` (idempotent — safe to re-run).
3. Create 3 collections; assign products.
4. Create pages + policies from `storefront/pages/`.
5. Build header/footer menus.
6. (Optional) apply brand colors/fonts + homepage sections via theme files.
