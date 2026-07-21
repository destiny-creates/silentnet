#!/usr/bin/env python3
"""
POC-04: Hardcoded Fernet Key — Live C2 Payload Decryption
==========================================================
Target:  https://thisisafalsepositive.st/cdn/e/3b8f6d2a9c1e
Vuln:    The Fernet symmetric encryption key is hardcoded in the Nuitka
         compiled binary constant pool (resource section type 10, id 3).
         Any version of the payload encrypted with this key can be
         decrypted, providing full access to the malware bundle.
Key:     74af664f79d1ef1436a4bf301788c7eb207570de60034b19d76df8e7aefc69b7
Impact:  Full plaintext recovery of all payload versions served from CDN.
         Confirms all malware modules, C2 URLs, and stealer logic.
Author:  Security Research — 2026-07-20
"""
import urllib.request, ssl, base64, struct, time, hashlib, zipfile, io, sys

TARGET_IP    = "185.178.208.191"
HOST          = "thisisafalsepositive.st"
UA            = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
FERNET_KEY    = bytes.fromhex("74af664f79d1ef1436a4bf301788c7eb207570de60034b19d76df8e7aefc69b7")
PAYLOAD_ID   = "3b8f6d2a9c1e"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode    = ssl.CERT_NONE

print("=== STEP 1: Download live C2 payload ===")
req = urllib.request.Request(
    f"https://{TARGET_IP}/cdn/e/{PAYLOAD_ID}",
    headers={"Host": HOST, "User-Agent": UA}
)
with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
    encrypted = r.read()
print(f"  Downloaded: {len(encrypted):,} bytes")
print(f"  SHA256: {hashlib.sha256(encrypted).hexdigest()}")

print()
print("=== STEP 2: Verify Fernet format ===")
try:
    raw = base64.urlsafe_b64decode(encrypted + b"==")
except Exception:
    raw = base64.urlsafe_b64decode(encrypted.strip() + b"==")
assert raw[0] == 0x80, f"Not a Fernet token (first byte 0x{raw[0]:02x})"
ts = struct.unpack(">Q", raw[1:9])[0]
ts_str = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime(ts))
print(f"  Fernet magic: 0x80 [OK]")
print(f"  Encrypted at: {ts_str}")
print(f"  Ciphertext:   {len(raw)-57:,} bytes")

print()
print("=== STEP 3: Decrypt with hardcoded key ===")
try:
    from Crypto.Cipher import AES
    from Crypto.Hash import HMAC, SHA256
    signing_key    = FERNET_KEY[:16]
    encryption_key = FERNET_KEY[16:]
    iv  = raw[9:25]
    ct  = raw[25:-32]
    mac = raw[-32:]
    h = HMAC.new(signing_key, digestmod=SHA256)
    h.update(raw[:-32])
    computed = h.digest()
    assert computed == mac, "HMAC verification FAILED — key may have rotated"
    print("  HMAC verification: VALID")
    cipher = AES.new(encryption_key, AES.MODE_CBC, iv)
    pt = cipher.decrypt(ct)
    pt = pt[:-pt[-1]]  # PKCS7 unpad
    print(f"  Decryption: SUCCESS")
    print(f"  Plaintext:  {len(pt):,} bytes")
except ImportError:
    print("  pycryptodome not available — install with: pip install pycryptodome")
    sys.exit(1)

print()
print("=== STEP 4: Parse ZIP and list contents ===")
assert pt[:2] == b"PK", "Plaintext is not a ZIP file"
with zipfile.ZipFile(io.BytesIO(pt)) as z:
    names = z.namelist()
    total_size = sum(info.file_size for info in z.infolist())
    print(f"  Files in bundle: {len(names)}")
    print(f"  Extracted size:  {total_size:,} bytes")
    print()
    print("  Key files:")
    key_files = [n for n in names if any(k in n for k in
        ["app.pyd", "main.py", "mypyc", "python312.zip",
         "requests", "Crypto", "psutil", "PIL", "win32"])]
    for f in key_files[:20]:
        info = z.getinfo(f)
        print(f"    {f:60s} {info.file_size:>10,} bytes")
    if len(names) > 20:
        print(f"    ... and {len(names)-len(key_files)} more files")

print()
print("[+] POC-04 complete. Live C2 payload decrypted successfully.")
print(f"[+] Fernet key 74af664f79d1ef1436a4bf301788c7eb207570de60034b19d76df8e7aefc69b7 confirmed valid")
