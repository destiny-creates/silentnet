# SilentNet Infostealer — Complete Malware Analysis

> **For educational and defensive research purposes only.**  
> All findings documented here are intended to help defenders detect, block, and remediate this threat.

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Threat Overview](#threat-overview)
3. [Stage 1 — Java Launcher](#stage-1--java-launcher)
4. [Stage 2 — Python Stealer](#stage-2--python-stealer)
5. [Blockchain C2 Infrastructure](#blockchain-c2-infrastructure)
6. [Complete Module Architecture](#complete-module-architecture)
7. [Capability Deep-Dive](#capability-deep-dive)
8. [DLL Injection Mechanism](#dll-injection-mechanism)
9. [Decryption and Reverse Engineering Method](#decryption-and-reverse-engineering-method)
10. [Live C2 Scan Results](#live-c2-scan-results)
11. [Indicators of Compromise](#indicators-of-compromise)
12. [Defensive Recommendations](#defensive-recommendations)
13. [Source Files Index](#source-files-index)

---

## Executive Summary

**SilentNet** is a sophisticated multi-stage Windows infostealer targeting the gaming community, primarily distributed through malicious Minecraft mods, resource packs, and modpacks. It combines a Java-based dropper with a Nuitka-compiled Python 3.12 stealer backend, using a Polygon blockchain smart contract for censorship-resistant C2 domain rotation.

| Property | Value |
|---|---|
| **Type** | Multi-stage infostealer |
| **Primary target** | Windows x86-64, gaming community |
| **Distribution** | Minecraft mods, modpacks, Discord |
| **Stage 1** | mypyc-compiled Java launcher |
| **Stage 2** | Nuitka-compiled Python 3.12 extension (`.pyd`) |
| **C2 mechanism** | Polygon smart contract (blockchain) |
| **Current C2** | `thisisafalsepositive.st` → `185.178.208.191` |
| **Hosting** | DDoS-Guard (Russia) — bulletproof |
| **First seen** | 2026-01-18 (contract deployment) |
| **Browsers targeted** | 17 Chromium-family + Firefox |
| **Crypto wallets targeted** | 13 desktop wallets + all browser extensions |
| **Other targets** | Discord, Steam, Telegram, Roblox, OBS, Mullvad VPN, FileZilla, WinSCP, Riot Games, Claude AI, SSH keys |

---

## Threat Overview

### Distribution Chain

```
Victim downloads malicious Minecraft mod/pack
        |
        v
Java .jar executes mypyc-compiled stage-1
        |
        v
Stage-1 beacons to Polygon contract -> resolves C2 domain
        |
        v
Downloads encrypted stage-2 ZIP from /cdn/e/<id>
        |
        v
Decrypts (AES-128-CBC / Fernet), extracts portable Python 3.12 runtime
        |
        v
Launches app.pyd (Nuitka stealer) with victim session args
        |
        v
Steals credentials, exfiltrates via HTTPS POST to C2
```

### Key Differentiators

- **Blockchain C2**: Polygon smart contract stores current domain — cannot be seized or sinkholed
- **DLL injection**: Injects into live browser processes to steal credentials without killing them
- **DNS-over-HTTPS**: All DNS patched at socket level via Cloudflare DoH — bypasses corporate DNS monitoring
- **Nuitka compilation**: Python source compiled to native x64 PE — defeats all Python decompilers
- **Custom cipher**: Constant pool encrypted with rolling XOR + 256-byte substitution table
- **Self-staging**: Downloads and installs its own portable Python 3.12 runtime
- **C2 deception**: Domain deliberately named `thisisafalsepositive.st` to fool analysts

---

## Stage 1 — Java Launcher

| Property | Value |
|---|---|
| Format | Java JAR (mypyc-compiled) |
| C2 resolver | Queries Polygon RPC endpoints |
| Auth | HMAC-based prefireId generation |
| Args passed to stage-2 | `--env`, `--tag`, `--mcInfo`, `--prefireId`, `--user-id` |

### Stage-1 Capabilities

- Reads victim Minecraft session (`mcUsername`, `mcUuid`, `accessToken`)
- Beacon: `POST /shard/prefireMc` with victim JSON
- Receives `prefireId` session token from C2
- Downloads stage-2 payload from `/cdn/e/<id>`
- Decrypts with AES-128-CBC key: `207570de60034b19d76df8e7aefc69b7`
- Extracts ZIP, launches `python.exe AppHost/main.py` with full args

### main.py — Recovered Plaintext Loader

`main.py` is **unobfuscated plain Python** (353 bytes) recovered directly from the live C2 payload:

```python
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util
spec = importlib.util.spec_from_file_location("app", os.path.join(os.path.dirname(__file__), "app.pyd"))
app = importlib.util.module_from_spec(spec)
sys.modules["app"] = app
spec.loader.exec_module(app)
if __name__ == "__main__":
    app.run()
```

---

## Stage 2 — Python Stealer

| Property | Value |
|---|---|
| File | `AppHost/app.pyd` |
| Format | PE32+ DLL (x86-64) |
| Compiler | Nuitka 2.x (Python to native) |
| Python version | 3.12 (CPython ABI) |
| Size | 1,848,832 bytes (1.76 MB) |
| Entry | `PyInit_app()` → `app.run()` |
| Constant pool | `.rsrc` section, 237,128 bytes, entropy 7.99/8.0 |
| Constant cipher | Rolling XOR + 256-byte S-box (custom) |

### Bundled Dependencies

```
requests + certifi + charset_normalizer  # HTTPS client
adodbapi                                  # Chrome/Edge SQLite via ADO/COM
pythoncom + wmi                          # Windows WMI interface
pycryptodome                             # AES-GCM, PBKDF2, 3DES
Pillow (PIL)                             # Screenshot capture
psutil                                   # RAM/process information
vdf                                      # Steam VDF file parser
Python 3.12 stdlib                       # Full stdlib including ctypes, sqlite3
```

---

## Blockchain C2 Infrastructure

### Smart Contract

| Property | Value |
|---|---|
| Network | Polygon (MATIC) mainnet |
| Contract | `0x9c0a507300fd902787bb193d80fca5ce6e1bff9a` |
| Owner wallet | `0x6767c6496541b530a5d1d0eb9b80bd5c7bf56767` |
| Wallet balance | 77.49 MATIC (~$50 USD) |
| ABI function | `getDomain() returns (string)` |

### Domain Rotation History

| Date (UTC) | Domain | Status |
|---|---|---|
| 2026-01-18 13:19 | Contract deployed | — |
| 2026-01-18 13:27 | `sltnnt.ru` | NXDOMAIN |
| 2026-05-09 22:18 | `thisisafalsepositive.ru` | NXDOMAIN |
| 2026-05-30 — 2026-06-07 | `v3` through `v7.thisisafalsepositive.ru` | NXDOMAIN |
| 2026-06-07 17:24 | `qasrgaovaf7m.thisisafalsepositive.ru` | NXDOMAIN |
| **2026-06-17 13:30** | **`thisisafalsepositive.st`** | **LIVE** |

> The June 7th cluster (5 domain changes in 2 hours) indicates rapid evasion response to takedown of `.ru` infrastructure.

### C2 API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/shard/prefireMc` | POST | Stage-1 victim beacon, receives prefireId |
| `/shard/submitMinecraftLog` | POST | Minecraft session data submission |
| `/cdn/e/<id>` | GET | Encrypted stage-2 payload download |
| `/submitData` | POST | Stolen credential JSON upload |
| `/submitFile` | POST | File upload (multipart) |
| `/submitLogs` | POST | Trace/debug log upload |
| `/auth/login` | GET/POST | Operator admin panel |
| `/auth/logout` | GET | Operator session logout |

### Polygon RPC Fallback List (hardcoded)

```
https://polygon-rpc.com
https://rpc-mainnet.matic.quiknode.pro
https://polygon-public.nodies.app
https://polygon-bor-rpc.publicnode.com
https://1rpc.io/matic
https://endpoints.omniatech.io/v1/matic/mainnet/public
https://polygon.rpc.subquery.network/public
https://api.zan.top/polygon-mainnet
https://go.getblock.io/02667b699f05444ab2c64f9bff28f027
https://polygon-mainnet.rpcfast.com?api_key=xbhWBI1Wkguk8SNMu1bvvLurPGLXmgwYeC4S6g2H7WdwFigZSmPWVZRxrskEQwIf
```

> **Exposed API key**: `xbhWBI1Wkguk8SNMu1bvvLurPGLXmgwYeC4S6g2H7WdwFigZSmPWVZRxrskEQwIf`  
> Submit to rpcfast.com abuse team for revocation.

---

## Complete Module Architecture

```
app/
|-- __init__.py              Entry point, arg parser, orchestration
|-- config.py                Configuration, argument validation
|-- contract.py              Polygon smart contract C2 resolver
|-- crypto.py                AES-GCM, DPAPI, PBKDF2 decryption
|-- http.py                  HTTP session + DoH patch + retry
|-- staging.py               Self-installer, Python runtime, persistence
|-- trace.py                 Debug trace -> svchost_d.log
|-- logging/
|   |-- __init__.py          HitLog, LoggingManager classes
|-- handlers/
|   |-- __init__.py
|   |-- browser.py           Chromium credential extraction (17 browsers)
|   |-- browser_extensions.py  Wallet extension file collection
|   |-- credentials.py       Non-browser credentials (20+ applications)
|   |-- discord.py           Discord token extraction + validation
|   |-- files.py             HitFile / FileManager upload classes
|   |-- firefox.py           Firefox credential extraction
|   |-- keywords.py          Keyword-based document search
|   |-- minecraft.py         Minecraft accounts (8 launchers)
|   |-- screenshot.py        Screen capture (PIL -> base64 JPEG)
|   |-- system_info.py       WMI + psutil system fingerprint
|   |-- wallets.py           Desktop crypto wallets (13)
|-- resources/
|   |-- __init__.py
|   |-- browser_module.py    XOR-encoded injected DLL payload
|-- util/
    |-- __init__.py
    |-- crypto.py            Low-level DPAPI / AES-GCM
    |-- dll_injection.py     CreateRemoteThread + LoadLibraryA
    |-- file.py              File utilities, zip helpers
    |-- handle_copy.py       Handle duplication (bypass file locks)
    |-- pipe.py              Named pipe IPC with injected DLL
    |-- process.py           SuspendedProcess, kill helpers
    |-- registry.py          Windows registry read wrappers
```

---

## Capability Deep-Dive

### Browser Credential Theft

**17 Chromium browsers targeted:**

```
Google Chrome       Microsoft Edge      Brave Browser
Opera Stable        Opera GX            Vivaldi
Yandex Browser      7Star               CentBrowser
Chedot              CocCoc              Comodo Dragon
Epic Privacy        Iridium             Slimjet
Torch               Chromium
```

**SQL queries executed per browser profile:**

```sql
-- Passwords
SELECT origin_url, username_value, password_value FROM logins

-- Cookies
SELECT host_key, name, path, is_secure, is_httponly,
       expires_utc, encrypted_value FROM cookies

-- Credit cards
SELECT guid, name_on_card, expiration_month, expiration_year,
       card_number_encrypted FROM credit_cards
SELECT guid, value_encrypted FROM local_stored_cvc

-- Autofill
SELECT name, value FROM autofill

-- Browsing history (last 5000 entries)
SELECT url, title, visit_count, last_visit_time FROM urls
       ORDER BY last_visit_time DESC LIMIT 5000

-- Google OAuth tokens
SELECT service, encrypted_token FROM token_service
```

**Decryption chain:**

- `v10` values: Windows DPAPI via `CryptUnprotectData` (ctypes)
- `v20` values: ABE key from `Local State` file, then AES-256-GCM
- Cookie values: 32-byte nonce header stripped before AES-GCM

**File lock bypass (4 strategies, in order):**

1. Direct copy if browser is not running
2. `DuplicateHandle` from all browser process IDs
3. DLL injection into browser process, named pipe IPC to receive decrypted key
4. Kill browser, then post-kill copy

**Firefox key derivation:**

```sql
SELECT a11 FROM nssPrivate WHERE a11 IS NOT NULL ORDER BY length(a11) DESC
SELECT item1 FROM metadata WHERE id = 'password'
SELECT fieldname, value FROM moz_formhistory
SELECT host, name, value, path, expiry FROM moz_cookies
```

Uses PBKDF2 (SHA256) + PBES2/3DES for master key decryption from `key4.db`.

### Discord Token Theft

- **Clients:** Discord, Discord Canary, Discord PTB
- **Path:** `%APPDATA%/discord/Local Storage/leveldb/`
- **Token regex:** `[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}`
- **Validation:** `GET https://discord.com/api/v9/users/@me` with `Authorization: <token>`
- Filters duplicates, invalid, and expired tokens

### Crypto Wallet Theft

| Wallet | Path | Output |
|---|---|---|
| Exodus | `%APPDATA%/Exodus/exodus.wallet/` | `Exodus.zip` |
| Atomic | `%APPDATA%/atomic/` | `Atomic.zip` |
| Electrum | `%APPDATA%/Electrum/wallets/` | `Electrum.zip` |
| Electrum-LTC | `%APPDATA%/Electrum-LTC/wallets/` | `Electrum-LTC.zip` |
| Zcash | `%APPDATA%/Zcash/` | `Zcash.zip` |
| Armory | `%APPDATA%/Armory/` | `Armory.zip` |
| Bytecoin | `%APPDATA%/Bytecoin/` | `Bytecoin.zip` |
| Jaxx | `com.liberty.jaxx/file__0.indexeddb.leveldb` | `Jaxx.zip` |
| Ethereum | `%APPDATA%/Ethereum/` | `Ethereum.zip` |
| Guarda | `%APPDATA%/Guarda/` | `Guarda.zip` |
| Coinomi | `%APPDATA%/Coinomi/` | `Coinomi.zip` |
| CakeWallet | `com.cakewallet.cake_wallet` | `CakeWallet.zip` |
| Monero | `%APPDATA%/Monero/` | `Monero.zip` + `Monero_AppData.zip` |

Browser wallet extensions: all `Local Extension Settings` directories are zipped and uploaded.

### Credential File Theft

| Application | Files Stolen | Output |
|---|---|---|
| Git | `.git-credentials` | `Git_Credentials.txt` |
| SSH | `.ssh/` directory | `SSH_Keys.zip` |
| FileZilla | `recentservers.xml`, `sitemanager.xml` | `FileZilla_RecentServers.xml`, `FileZilla_SiteManager.xml` |
| WinSCP | `WinSCP.ini`, `WinSCP_Config.ini` | Same names |
| Riot Games | `RiotGamesPrivateSettings.yaml`, `RiotGames_Settings.yaml` | Same names |
| Thunderbird | All profiles | `Thunderbird_Profiles.zip` |
| Claude AI | `.claude/.credentials.json` | `Claude_Credentials.json` |
| Telegram | `tdata/` (excludes media_cache) | `Telegram_Data.zip` |
| Roblox | DPAPI-decrypted session cookies | `RobloxCookies.dat`, `Roblox_Cookies.txt` |
| OBS Studio | Stream keys from all profiles | `_StreamKey.json` |
| Mullvad VPN | CLI account query | `Mullvad_Account.txt` |
| Steam | `loginusers.vdf`, `local.vdf` DPAPI tokens | `Steam_Tokens.txt` |

### Minecraft Handler

**8 launchers targeted:**

| Launcher | File |
|---|---|
| Vanilla | `.minecraft/` |
| Lunar Client | `lunar_accounts.json` |
| Feather Launcher | `account.txt` (DPAPI encrypted), `feather_accounts.txt` |
| GG Essential | `essential_accounts.json` |
| Microsoft | `microsoft_accounts.json` |
| Prism Launcher | `prismlauncher_accounts.json` |
| Modrinth | `app.db` SQLite |

```sql
SELECT username, uuid, access_token FROM minecraft_users
```

Also parses `servers.dat` (NBT format) and extracts server list as `Minecraft_Server_List.txt`.

### Staging and Persistence

```
1. Check persistence via local HTTP server on 127.0.0.1
   -> If already running: skip (UUID: 4015d0e9-4cab-4ac1-8dfd-5ee8f283bca1)
2. Download Python 3.12.7:
   https://www.python.org/ftp/python/3.12.7/python-3.12.7-embed-amd64.zip
3. Patch python312._pth: uncomment 'import site'
4. Download pip: https://bootstrap.pypa.io/get-pip.py
5. Install pip, then install requirements.txt from C2
6. Download main.py + app.pyd from C2 /cdn/e/<id>
7. Decrypt (Fernet/AES), write to disk
8. Launch in background thread (staging-worker)
9. Log all activity to svchost_d.log
```

### HTTP and Network Layer

**User-Agent (fake, detectable):**

```
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36
```

> `Chrome/142` does not exist — anomalous and detectable in proxy logs.

**DNS-over-HTTPS patch:**  
All DNS resolution monkey-patched at `socket.getaddrinfo` level.  
All hostnames resolved via `https://cloudflare-dns.com/dns-query`.  
Exception: `cloudflare-dns.com` itself uses native resolution.

**Custom C2 headers present on every request:**

```
X-Runtime-Env:           <--env argument value>
X-Tracking-ID:           <--prefireId value>
X-Edge-Cache-Revalidate: (always present)
```

---

## DLL Injection Mechanism

The `resources/browser_module.py` contains an XOR-encoded Windows DLL injected into live browser processes to steal credentials without terminating the browser.

```
1. XOR-decode DLL bytes from browser_module.py constant pool
2. Write DLL to %TEMP%\<random>.tmp
3. Get all PIDs for target browser (chrome.exe, msedge.exe, brave.exe...)
4. VirtualAllocEx(pid, NULL, dll_path_len, MEM_COMMIT, PAGE_READWRITE)
5. WriteProcessMemory(pid, alloc_addr, dll_path_bytes)
6. CreateRemoteThread(pid, NULL, 0, LoadLibraryA, alloc_addr, 0, NULL)
7. CreateNamedPipe(\\.\pipe\<pid_derived_tag>)
8. ConnectNamedPipe() -> wait for injected DLL to connect
9. WriteFile(pipe, aes_key)    -> send browser Local State AES key
10. ReadFile(pipe) -> master_key -> receive decrypted master key
```

**PID-to-pipe-tag:** `rotl32` function — matches Java stage-1 implementation for cross-language IPC.

---

## Decryption and Reverse Engineering Method

### Challenge

`app.pyd` is a Nuitka-compiled native Windows DLL. All Python source, string literals, and constants are stored in the `.rsrc` section (237 KB, entropy 7.99/8.0) and decrypted at runtime via `FindResourceA` / `LoadResource` / `LockResource`.

### Cipher (Reversed from Disassembly)

```python
# S-box at file offset 0x173250 (256 bytes)
# Jump table at RVA 0x16CC34 (8 entries)
case_deltas = [-98, -59, -105, +88, +21, +13, +6, +79]

bl  = 0      # accumulator
rdx = 8      # byte index
while rdx < 0x39E48:  # 237,128 bytes
    eax = rsrc[rdx]
    cl  = ((rdx - 8) + bl) & 0xFF
    ebx = (cl ^ eax) & 0xFF
    ebx = sbox[ebx]            # S-box substitution
    bl  = ebx
    if rdx >= 0x18:
        output[rdx - 0x10] = bl
    bl  = (bl + case_deltas[rdx & 7]) & 0xFF
    rdx += 1
```

Successfully decrypted all 237,128 bytes, exposing 30 Python modules with 5,000+ string constants.

---

## Live C2 Scan Results

> Active reconnaissance performed against `thisisafalsepositive.st` on 2026-07-20

### Server Fingerprint

| Property | Value |
|---|---|
| Real IP | `185.178.208.191` |
| Architecture | DDoS-Guard (proxy) -> nginx -> Python Flask |
| Hosting | DDoS-Guard (Russia) — bulletproof |
| DNS NS | `dean.ns.cloudflare.com`, `luciane.ns.cloudflare.com` |
| TLS issuer | Let's Encrypt / CN=YR1 |
| TLS issued | 2026-06-17 12:36 UTC (matches on-chain domain rotation date) |
| TLS SHA1 fingerprint | `57:FA:98:59:74:BF:A8:FA:91:48:F0:10:D1:99:DB:05:1A:48:4A:84` |
| TLS expires | 2026-09-15 |
| nginx leaked via | TRACE method 405 response body |

### Endpoint Map

| Endpoint | Method | Status | Notes |
|---|---|---|---|
| `/` | GET | 302 | Redirects to `/auth/login` |
| `/auth/login` | GET | **403** | Admin panel — IP-allowlisted |
| `/auth/login` | OPTIONS | **200** | CORS preflight succeeds — allowed methods: GET, POST, OPTIONS, HEAD |
| `/auth/login` | PUT/PATCH/DELETE | 405 | Flask method not allowed |
| `/auth/logout` | GET | **403** | Endpoint confirmed (not 404) |
| `/dashboard` | GET | 308 | Permanent redirect to `/auth/login` |
| `/favicon.ico` | GET | **200** | 270 KB Windows BMP ICO |
| `/shard/prefireMc` | GET | **405** | Endpoint EXISTS, expects POST |
| `/shard/prefireMc` | POST | 403 | IP-blocked |
| `/shard/submitMinecraftLog` | POST | 403 | Endpoint confirmed |
| `/cdn/e/3b8f6d2a9c1e` | GET | **200** | **LIVE PAYLOAD — actively serving** |

### 403 Bypass Attempts

| Technique | Result |
|---|---|
| X-Forwarded-For spoofing (127.0.0.1, 192.168.x.x) | 403 — not bypassed |
| Path normalisation variants (`/auth//login`, `/./auth/login`, `/%61uth/login`) | 403 or 404 |
| HTTP method switching (PUT, PATCH, DELETE) | 405 — methods rejected |
| Host header injection (127.0.0.1, localhost) | **503** — reveals DDoS-Guard backend detection |
| OPTIONS method | **200** — CORS misconfiguration; no `Access-Control-Allow-Origin` returned |

> **Assessment:** The `/auth/login` 403 is enforced by DDoS-Guard IP allowlisting at the proxy layer, not by Flask itself. Bypassing it requires either a source IP in the operator's allowlist or a DDoS-Guard bypass technique.

### Live Payload — V2 (Downloaded 2026-07-20 18:05 UTC)

| Property | V1 (original sample) | V2 (live) |
|---|---|---|
| Encryption | AES-128-CBC (raw) | Python Fernet (AES-128-CBC + HMAC-SHA256) |
| Encryption key | `207570de60034b19d76df8e7aefc69b7` | `74af664f79d1ef1436a4bf301788c7eb207570de60034b19d76df8e7aefc69b7` |
| Key relationship | Original AES-128 key | Old AES key = last 16 bytes of new Fernet key |
| Fernet timestamp | N/A | 2026-07-20 18:05 UTC (re-encrypted during our analysis) |
| `app.pyd` SHA256 | `1280ff5f2c4a59e8a9...` | **IDENTICAL** |
| Stage-1 mypyc component | `81d243bd2c585b0f...` | `52056f4b964f1bc0...` (updated) |
| Bundle files | 736 | 736 |

### Operator Behaviour Assessment

| Observation | Assessment |
|---|---|
| Payload re-encrypted within hours of our analysis | Operator monitors CDN access logs in near real-time |
| Upgraded AES-CBC to Fernet (adds HMAC integrity) | Response to known decryption — attempted to harden |
| Stealer `app.pyd` unchanged | Operator prioritised speed over updating stealer logic |
| Stage-1 mypyc component updated | New campaign build or launcher bug fix |
| Admin panel restricted to operator IP range | DDoS-Guard allowlisting in use |
| Fernet key pre-embedded in v1 binary | OPSEC failure — full key rotation not performed |

---

## Indicators of Compromise

### Network IOCs

| Type | Value | Status |
|---|---|---|
| IP | `185.178.208.191` | **LIVE** |
| Domain | `thisisafalsepositive.st` | **LIVE** |
| Domain | `thisisafalsepositive.ru` | NXDOMAIN |
| Domain | `sltnnt.ru` | NXDOMAIN (fallback) |
| Domain | `v3` through `v7.thisisafalsepositive.ru` | NXDOMAIN |
| User-Agent | `...Chrome/142.0.0.0 Safari/537.36` | Anomalous |
| HTTP Header | `X-Runtime-Env` | C2 beacon marker |
| HTTP Header | `X-Tracking-ID` | C2 session marker |
| HTTP Header | `X-Edge-Cache-Revalidate` | C2 marker |
| URL pattern | `/cdn/e/[a-z0-9]+` | Payload download |
| TLS SHA1 | `57:FA:98:59:74:BF:A8:FA:91:48:F0:10:D1:99:DB:05:1A:48:4A:84` | C2 cert |

### Blockchain IOCs

| Type | Value |
|---|---|
| Polygon contract | `0x9c0a507300fd902787bb193d80fca5ce6e1bff9a` |
| Operator wallet | `0x6767c6496541b530a5d1d0eb9b80bd5c7bf56767` |
| Exposed RPC API key | `xbhWBI1Wkguk8SNMu1bvvLurPGLXmgwYeC4S6g2H7WdwFigZSmPWVZRxrskEQwIf` |

### Cryptographic IOCs

| Type | Value |
|---|---|
| Stage-1 AES-128 key | `207570de60034b19d76df8e7aefc69b7` |
| Stage-2 Fernet key (v2) | `74af664f79d1ef1436a4bf301788c7eb207570de60034b19d76df8e7aefc69b7` |
| Staging UUID | `4015d0e9-4cab-4ac1-8dfd-5ee8f283bca1` |
| V1 payload SHA256 | `23ab6a5d46f20bc8fe23800195558cb99caacf43e2ecd80f7090f74fe0fe1068` |
| V2 payload SHA256 | `69a74db222b5c001ce0f25b93e4a1f5ab591fb263c9499c62b79f9ff3d633ee3` |
| `app.pyd` SHA256 | `1280ff5f2c4a59e8a9301d8e2eb7c2e9774ec6026a48905c52d23fb1974438bf` |

### File System IOCs

| Path | Purpose |
|---|---|
| `%TEMP%\svchost_d.log` | Stealer debug log |
| `%TEMP%\*.tmp` | Injected DLL (temporary) |
| `%LOCALAPPDATA%\python.exe` | Staged Python runtime |
| `%LOCALAPPDATA%\python312._pth` | Modified to enable site-packages |
| `%LOCALAPPDATA%\pip.exe` | Staged pip |

### Registry IOCs

```
HKLM\SOFTWARE\Valve\Steam
HKLM\SOFTWARE\Wow6432Node\Valve\Steam
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion
HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths
HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\App Paths
```

### Process and Pipe IOCs

| Type | Value |
|---|---|
| Named pipe pattern | `\\.\pipe\[0-9a-f]{8}` |
| Staging UUID check | Local HTTP server on `127.0.0.1` |
| DLL injection target | `chrome.exe`, `msedge.exe`, `brave.exe` (via `CreateRemoteThread`) |

### Regex IOCs

```
Discord token:    [\w-]{24}\.[\w-]{6}\.[\w-]{25,110}
Browser profile:  ^(Default|Profile\s+\d+)$
Telegram exclude: user_data[^/\\]*[/\\](media_cache|cache)($|[/\\])
```

---

## Anti-Analysis and Evasion Techniques

| ID | Technique | Detail |
|---|---|---|
| E-01 | DNS-over-HTTPS | All DNS via Cloudflare DoH at socket level |
| E-02 | Blockchain C2 | Polygon smart contract — cannot be seized |
| E-03 | Nuitka compilation | Python compiled to native x64 PE |
| E-04 | Custom cipher | Rolling XOR + 256-byte S-box on constant pool |
| E-05 | DLL injection | Bypasses browser file locks without termination |
| E-06 | Handle duplication | Secondary file lock bypass via `DuplicateHandle` |
| E-07 | Silent errors | `SetErrorMode` suppresses all error dialogs |
| E-08 | C2 domain naming | `thisisafalsepositive.st` — social engineering |
| E-09 | Log disguise | `svchost_d.log` mimics Windows service log |
| E-10 | Socket patch | `getaddrinfo` replaced at Python level |
| E-11 | Fake Chrome version | `Chrome/142.0.0.0` does not exist |
| E-12 | Persistence check | Local HTTP server prevents double-staging |
| E-13 | Size limits | Telegram excludes large cache directories |
| E-14 | Timeout protection | All operations wrapped in 3-second timeout |

---

## Defensive Recommendations

### Immediate Actions

1. Block `185.178.208.191` at perimeter firewall
2. Block DNS resolution for `thisisafalsepositive.st` and `sltnnt.ru`
3. Report API key `xbhWBI1Wkguk8SNMu1...` to rpcfast.com abuse team for revocation
4. Block Polygon RPC endpoints in outbound firewall if not operationally required
5. Submit contract `0x9c0a507300fd902787bb193d80fca5ce6e1bff9a` to Polygon ecosystem abuse contacts

### SIEM / EDR Detection Rules

```yaml
# Anomalous Chrome version (Chrome/142 does not exist)
- rule: HTTP User-Agent contains "Chrome/142"

# C2 beacon headers
- rule: Outbound HTTP request contains header "X-Tracking-ID" or "X-Runtime-Env"

# DNS-over-HTTPS evasion from non-browser process
- rule: Outbound HTTPS to cloudflare-dns.com/dns-query NOT from browser process

# DLL injection into browser
- rule: CreateRemoteThread where source != chrome.exe AND target IN [chrome.exe, msedge.exe, brave.exe]

# Named pipe IPC pattern
- rule: Named pipe created matching pattern [0-9a-f]{8}

# Python staging in user directories
- rule: python.exe or pip.exe created in %LOCALAPPDATA% or %TEMP%

# Stealer log file
- rule: File created matching svchost_d.log in user profile directories

# Payload download
- rule: HTTP GET to */cdn/e/* with response size > 10 MB
```

### Threat Hunting Queries

```
# Proxy / firewall logs
dest_domain IN [thisisafalsepositive.st, sltnnt.ru]
OR dest_ip = 185.178.208.191

# Polygon RPC outbound (endpoints should not query blockchain)
dest_domain IN [
  polygon-rpc.com, rpc-mainnet.matic.quiknode.pro,
  polygon-public.nodies.app, polygon-bor-rpc.publicnode.com,
  1rpc.io, endpoints.omniatech.io, api.zan.top
]

# Unusual Python downloads from endpoints
url CONTAINS "python-3.12.7-embed-amd64.zip"
OR url CONTAINS "bootstrap.pypa.io/get-pip.py"
```

---

## Source Files Index

The `source/` directory contains 30 reconstructed Python module files. Each file contains all string literals, SQL queries, file paths, class names, function names, and identifiers extracted directly from the compiled binary constant pool — authentic strings from the original Python source code.

| File | Module | Description |
|---|---|---|
| `app.py` | `app` | Entry point, orchestration, arg parser |
| `app_config.py` | `app.config` | Configuration, validation |
| `app_contract.py` | `app.contract` | Polygon C2 domain resolver |
| `app_crypto.py` | `app.crypto` | Crypto wrappers (AES/DPAPI/PBKDF2) |
| `app_handlers.py` | `app.handlers` | Handler package init |
| `app_handlers_browser.py` | `app.handlers.browser` | Chromium credential theft (17 browsers) |
| `app_handlers_browser_extensions.py` | `app.handlers.browser_extensions` | Wallet extension collection |
| `app_handlers_credentials.py` | `app.handlers.credentials` | Non-browser credential theft (20+ apps) |
| `app_handlers_discord.py` | `app.handlers.discord` | Discord token theft |
| `app_handlers_files.py` | `app.handlers.files` | File and upload management |
| `app_handlers_firefox.py` | `app.handlers.firefox` | Firefox credential theft |
| `app_handlers_keywords.py` | `app.handlers.keywords` | Document keyword search |
| `app_handlers_minecraft.py` | `app.handlers.minecraft` | Minecraft account theft (8 launchers) |
| `app_handlers_screenshot.py` | `app.handlers.screenshot` | Screen capture |
| `app_handlers_system_info.py` | `app.handlers.system_info` | WMI system fingerprinting |
| `app_handlers_wallets.py` | `app.handlers.wallets` | Crypto wallet theft (13 wallets) |
| `app_http.py` | `app.http` | HTTP + DoH + C2 headers |
| `app_logging.py` | `app.logging` | Logging classes |
| `app_resources.py` | `app.resources` | Resources package init |
| `app_resources_browser_module.py` | `app.resources.browser_module` | XOR-encoded DLL payload |
| `app_staging.py` | `app.staging` | Self-installer, persistence |
| `app_trace.py` | `app.trace` | Debug tracer |
| `app_util.py` | `app.util` | Util package init |
| `app_util_crypto.py` | `app.util.crypto` | Low-level crypto wrappers |
| `app_util_dll_injection.py` | `app.util.dll_injection` | Browser DLL injector |
| `app_util_file.py` | `app.util.file` | File helpers |
| `app_util_handle_copy.py` | `app.util.handle_copy` | File lock bypass via handle duplication |
| `app_util_pipe.py` | `app.util.pipe` | Named pipe IPC |
| `app_util_process.py` | `app.util.process` | Process management |
| `app_util_registry.py` | `app.util.registry` | Registry access |

---

## Timeline

| Date | Event |
|---|---|
| 2026-01-18 | Polygon smart contract deployed, `sltnnt.ru` set as C2 |
| 2026-05-09 | Domain rotated to `thisisafalsepositive.ru` |
| 2026-06-07 | Rapid domain rotation — 5 changes in 2 hours (takedown response) |
| 2026-06-17 | Moved to `.st` TLD — `thisisafalsepositive.st` (current, live) |
| 2026-07-20 | Full malware analysis completed; live C2 scanned; V2 payload downloaded and decrypted |

---

*Analysis performed: 2026-07-20*  
*Platform: Parrot OS Linux (static + dynamic analysis)*  
*Tools: pefile, capstone, unicorn, Frida, objdump, Python 3.12*
