# Proof-of-Concept Scripts — SilentNet C2

> **Legal notice:** These scripts are provided for **defensive security research only**.
> They document confirmed vulnerabilities in a live criminal C2 infrastructure.
> Do not use against systems you do not own or have explicit written authorization to test.

## Scripts

| File | VULN | Title | Impact |
|---|---|---|---|
| `poc_01_ip_bypass.py` | VULN-01 | Flask IP Allowlist Bypass | Unauthenticated access to all `/shard/*` endpoints |
| `poc_02_db_write.py` | VULN-02 | Unauthenticated DB Write | Arbitrary data injection into victim database |
| `poc_03_submitlogs_dos.py` | VULN-03 | submitLogs DoS | Persistent HTTP 500 crash on log submission handler |
| `poc_04_fernet_decrypt.py` | VULN-05 | Fernet Key Decryption | Full plaintext recovery of live CDN payload |
| `poc_05_static_bypass.py` | VULN-04 | nginx Static File Exposure | Read all panel CSS/JS without authentication |
| `poc_06_blockchain_resolver.py` | VULN-06 | Blockchain C2 Resolver | Real-time C2 domain monitoring via Polygon RPC |

## Requirements

```bash
pip install pycryptodome requests
```

## Usage

```bash
# Confirm IP bypass
python3 poc_01_ip_bypass.py

# Demonstrate DB write
python3 poc_02_db_write.py

# Test DoS (10 requests)
python3 poc_03_submitlogs_dos.py 10

# Decrypt live payload (requires pycryptodome)
python3 poc_04_fernet_decrypt.py

# Confirm nginx static bypass
python3 poc_05_static_bypass.py

# Query blockchain C2 domain
python3 poc_06_blockchain_resolver.py
```
