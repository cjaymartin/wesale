#!/usr/bin/env python3
"""Minimal Shopify Admin GraphQL client (stdlib only).

Reads credentials from wesale/.env. Never prints the token.

Usage:
    python3 scripts/shopify/api.py ping     # verify connection, print shop info
"""
import json
import os
import sys
import urllib.request
import urllib.error
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
ENV_PATH = ROOT / ".env"


def load_env():
    if not ENV_PATH.exists():
        sys.exit(f"ERROR: {ENV_PATH} not found. Copy .env.example -> .env and fill it in.")
    env = {}
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip().strip('"').strip("'")
    domain = env.get("SHOPIFY_STORE_DOMAIN", "")
    token = env.get("SHOPIFY_ADMIN_TOKEN", "")
    version = env.get("SHOPIFY_API_VERSION", "2026-04")
    missing = [k for k, v in {"SHOPIFY_STORE_DOMAIN": domain, "SHOPIFY_ADMIN_TOKEN": token}.items()
               if not v or "xxxx" in v or v.startswith("your-")]
    if missing:
        sys.exit(f"ERROR: fill these in .env: {', '.join(missing)}")
    return domain, token, version


def gql(query, variables=None):
    domain, token, version = load_env()
    url = f"https://{domain}/admin/api/{version}/graphql.json"
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(
        url, data=body, method="POST",
        headers={"Content-Type": "application/json", "X-Shopify-Access-Token": token},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        detail = e.read().decode()[:500]
        sys.exit(f"HTTP {e.code} from Shopify ({version}). Check token/scopes/version.\n{detail}")
    except urllib.error.URLError as e:
        sys.exit(f"Network/URL error: {e}. Check SHOPIFY_STORE_DOMAIN (use the *.myshopify.com host).")
    if "errors" in data and data["errors"]:
        # surface GraphQL errors (e.g. missing scope) without dumping the whole payload
        sys.exit("GraphQL errors:\n" + json.dumps(data["errors"], indent=2)[:1500])
    return data["data"]


PING_QUERY = """
{
  shop {
    name
    myshopifyDomain
    primaryDomain { url }
    plan { displayName partnerDevelopment }
    currencyCode
  }
}
"""


def ping():
    data = gql(PING_QUERY)
    s = data["shop"]
    print("✅ Connected to Shopify Admin API")
    print(f"   Store name : {s['name']}")
    print(f"   Backend    : {s['myshopifyDomain']}")
    print(f"   Live URL   : {s['primaryDomain']['url']}")
    print(f"   Plan       : {s['plan']['displayName']}")
    print(f"   Currency   : {s['currencyCode']}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "ping"
    if cmd == "ping":
        ping()
    else:
        sys.exit(f"Unknown command: {cmd}. Try: ping")
