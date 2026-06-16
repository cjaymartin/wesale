#!/usr/bin/env python3
"""One-time OAuth install to mint a real Admin API token for a Dev Dashboard app.

Flow:
  1. Reads CLIENT_ID / CLIENT_SECRET / STORE_DOMAIN / SCOPES from wesale/.env
  2. Starts a local listener on http://localhost:3456/callback
  3. Prints an authorize URL — you open it, approve the install
  4. Shopify redirects to the local listener with a code; we exchange it for an
     access token and write it to .env as SHOPIFY_ADMIN_TOKEN
  5. Exits

Stdlib only. The token is written to .env (gitignored) and never printed in full.
"""
import http.server
import json
import sys
import urllib.parse
import urllib.request
import urllib.error
import secrets
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
ENV_PATH = ROOT / ".env"
PORT = 3456
REDIRECT = f"http://localhost:{PORT}/callback"
DEFAULT_SCOPES = ",".join([
    "write_products", "read_products",
    "write_publications", "read_publications",
    "write_content", "read_content",
    "write_online_store_pages", "read_online_store_pages",
    "write_online_store_navigation", "read_online_store_navigation",
    "write_files", "read_files",
])


def read_env():
    env = {}
    for line in ENV_PATH.read_text().splitlines():
        s = line.strip()
        if s and not s.startswith("#") and "=" in s:
            k, v = s.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def write_token(token):
    lines = ENV_PATH.read_text().splitlines()
    out, found = [], False
    for line in lines:
        if line.strip().startswith("SHOPIFY_ADMIN_TOKEN="):
            out.append(f"SHOPIFY_ADMIN_TOKEN={token}")
            found = True
        else:
            out.append(line)
    if not found:
        out.append(f"SHOPIFY_ADMIN_TOKEN={token}")
    ENV_PATH.write_text("\n".join(out) + "\n")


def exchange(shop, client_id, client_secret, code):
    url = f"https://{shop}/admin/oauth/access_token"
    body = json.dumps({"client_id": client_id, "client_secret": client_secret, "code": code}).encode()
    req = urllib.request.Request(url, data=body, method="POST",
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def main():
    env = read_env()
    shop = env.get("SHOPIFY_STORE_DOMAIN", "")
    cid = env.get("SHOPIFY_CLIENT_ID", "")
    csecret = env.get("SHOPIFY_CLIENT_SECRET", "")
    # If SHOPIFY_SCOPES is set, request exactly those; if blank, omit `scope` so the
    # token inherits whatever scopes the app is configured with (safest with Dev Dashboard).
    scopes = env.get("SHOPIFY_SCOPES", "").strip()
    bad = [k for k, v in {"SHOPIFY_STORE_DOMAIN": shop, "SHOPIFY_CLIENT_ID": cid,
                          "SHOPIFY_CLIENT_SECRET": csecret}.items()
           if not v or "PASTE" in v or v.startswith("your-")]
    if bad:
        sys.exit(f"ERROR: fill these in .env first: {', '.join(bad)}")

    state = secrets.token_hex(16)
    auth_url = (f"https://{shop}/admin/oauth/authorize?client_id={cid}"
                f"&redirect_uri={urllib.parse.quote(REDIRECT)}&state={state}")
    if scopes:
        auth_url += f"&scope={urllib.parse.quote(scopes)}"

    result = {}

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            parsed = urllib.parse.urlparse(self.path)
            if parsed.path != "/callback":
                self.send_response(404); self.end_headers(); return
            qs = urllib.parse.parse_qs(parsed.query)
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            if qs.get("state", [""])[0] != state:
                self.wfile.write(b"<h2>State mismatch - aborted. Re-run the script.</h2>")
                result["error"] = "state_mismatch"; return
            code = qs.get("code", [""])[0]
            if not code:
                self.wfile.write(b"<h2>No code returned. Check app config.</h2>")
                result["error"] = "no_code"; return
            try:
                tok = exchange(shop, cid, csecret, code)
                result["token"] = tok.get("access_token", "")
                result["scope"] = tok.get("scope", "")
                self.wfile.write(b"<h2>NoseyMutt connected. You can close this tab and return to Claude.</h2>")
            except urllib.error.HTTPError as e:
                result["error"] = f"exchange_http_{e.code}: {e.read().decode()[:300]}"
                self.wfile.write(b"<h2>Token exchange failed - see terminal.</h2>")

        def log_message(self, *a):
            pass

    httpd = http.server.HTTPServer(("localhost", PORT), Handler)
    print("=" * 70)
    print("STEP 1 — open this URL in your browser (logged into the store) and")
    print("         click Install / Approve:\n")
    print(auth_url)
    print("\nWaiting for approval on http://localhost:%d ..." % PORT)
    print("=" * 70, flush=True)

    while "token" not in result and "error" not in result:
        httpd.handle_request()

    if result.get("token"):
        write_token(result["token"])
        masked = result["token"][:9] + "…" + result["token"][-4:]
        print(f"\n✅ Access token saved to .env ({masked}).")
        print(f"   Granted scopes: {result.get('scope','(none returned)')}")
        print("   Next: python3 scripts/shopify/api.py ping")
    else:
        sys.exit(f"\n❌ OAuth failed: {result.get('error')}")


if __name__ == "__main__":
    main()
