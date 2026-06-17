#!/usr/bin/env python3
"""Minimal CJdropshipping API client (stdlib). Reads CJ_ACCESS_TOKEN from wesale/.env.

Respects CJ's 1 request/second QPS limit (throttles internally). Never prints the token.
"""
import json
import time
import urllib.request
import urllib.error
import urllib.parse
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
ENV_PATH = ROOT / ".env"
BASE = "https://developers.cjdropshipping.com/api2.0/v1"
_last = [0.0]


def _token():
    for line in ENV_PATH.read_text().splitlines():
        s = line.strip()
        if s.startswith("CJ_ACCESS_TOKEN="):
            return s.split("=", 1)[1].strip()
    raise SystemExit("CJ_ACCESS_TOKEN not set in .env")


def _throttle():
    dt = time.time() - _last[0]
    if dt < 1.2:
        time.sleep(1.2 - dt)
    _last[0] = time.time()


def get(path, params=None, retries=3):
    tok = _token()
    qs = ("?" + urllib.parse.urlencode(params)) if params else ""
    url = f"{BASE}{path}{qs}"
    for attempt in range(retries):
        _throttle()
        req = urllib.request.Request(url, headers={"CJ-Access-Token": tok})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            body = e.read().decode()
            if e.code == 429 and attempt < retries - 1:
                time.sleep(1.5)
                continue
            return {"code": e.code, "result": False, "message": body[:200]}
    return {"code": 0, "result": False, "message": "exhausted retries"}


def search(name, page_size=8):
    return get("/product/list", {"pageNum": 1, "pageSize": page_size, "productNameEn": name})


def detail(pid):
    return get("/product/query", {"pid": pid})


if __name__ == "__main__":
    import sys
    d = search(sys.argv[1] if len(sys.argv) > 1 else "dog lick mat")
    print(json.dumps(d, indent=2)[:1500])
