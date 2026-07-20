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
9. [Decryption & Reverse Engineering Method](#decryption--reverse-engineering-method)
10. [Indicators of Compromise](#indicators-of-compromise)
11. [Defensive Recommendations](#defensive-recommendations)
12. [Source Files Index](#source-files-index)

---

## Executive Summary

**SilentNet** is a sophisticated multi-stage Windows infostealer targeting the gaming community, primarily distributed through malicious Minecraft mods, resource packs, and modpacks. It combines a Java-based dropper with a Nuitka-compiled Python 3.12 stealer backend, using a Polygon blockchain smart contract for censorship-resistant C2 domain rotation.

| Property | Value |
|---|---|
| **Type** | Multi-stage infostealer |
| **Primary target** | Windows (x86-64), gaming community |
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
        ↓
Java .jar executes mypyc-compiled stage-1
        ↓
Stage-1 beacons to Polygon contract → resolves C2 domain
        ↓
Downloads encrypted stage-2 ZIP from /cdn/e/<id>
        ↓
Decrypts (AES-128-CBC), extracts portable Python 3.12 runtime
        ↓
Launches app.pyd (Nuitka stealer) with victim session args
        ↓
Steals credentials, exfiltrates via HTTPS POST to C2
```

### Key Differentiators

- **Blockchain C2**: Polygon smart contract stores current domain — cannot be seized or sinkholed
- **DLL injection**: Injects into live browser processes to steal credentials without killing them
- **DNS-over-HTTPS**: All DNS patched at socket level via Cloudflare DoH — bypasses corporate DNS monitoring
- **Nuitka compilation**: Python source compiled to native x64 PE — defeats all Python decompilers
- **Custom cipher**: Constant pool encrypted with rolling XOR + 256-byte substitution table
- **Self-staging**: Downloads and installs its own portable Python 3.12 runtime
- **C2 deception**: Domain deliberately named `thisisafalsepositive.st` to fool security analysts

---

## Stage 1 — Java Launcher

### Properties

| Property | Value |
|---|---|
| Format | Java JAR (mypyc-compiled) |
| Entry | Main class triggers beacon |
| C2 resolver | Queries Polygon RPC endpoints |
| Auth | HMAC-based prefireId generation |
| Args passed to stage-2 | `--env`, `--tag`, `--mcInfo`, `--prefireId`, `--user-id` |

### Stage-1 Capabilities

- Reads victim Minecraft session (`mcUsername`, `mcUuid`, `accessToken`)
- Beacon: `POST /shard/prefireMc` with victim JSON
- Receives `prefireId` session token from C2
- Downloads stage-2 payload from `/cdn/e/<id>`
- Decrypts with AES-128-CBC key `207570de60034b19d76df8e7aefc69b7`
- Extracts ZIP, launches `python.exe AppHost/main.py` with full args

### Stage-1 Arguments to Stage-2

```
python.exe -u AppHost/main.py
  --env <Fabric|DoubleClick>     # campaign environment tag
  --tag <campaign_tag>           # operator tracking tag
  --mcInfo <json>                # MC username/uuid/accessToken
  --prefireId <session_id>       # C2 session correlation ID
  --user-id <victim_id>          # C2 victim identifier
```

---

## Stage 2 — Python Stealer

### Properties

| Property | Value |
|---|---|
| File | `AppHost/app.pyd` |
| Format | PE32+ DLL (x86-64) |
| Compiler | Nuitka 2.x (Python → native) |
| Python version | 3.12 (CPython ABI) |
| Size | 1,848,832 bytes (1.76 MB) |
| Entry | `PyInit_app()` → `app.run()` |
| Constant pool | `.rsrc` section, 237,128 bytes, entropy 7.99/8.0 |
| Constant cipher | Rolling XOR + 256-byte S-box (custom, from disassembly) |

### Bundled Dependencies

```
requests + certifi + charset_normalizer  # Full HTTPS client
adodbapi                                  # Chrome/Edge SQLite via ADO/COM
pythoncom + wmi                          # Windows WMI interface
pycryptodome                             # AES-GCM, PBKDF2, 3DES
Pillow (PIL)                             # Screenshot capture
psutil                                   # RAM/process information
Python 3.12 stdlib (506 modules)         # Full stdlib including ctypes, sqlite3
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
| Total transactions | 13 (purpose-built operational wallet) |
| ABI function | `getDomain() returns (string)` |

### Domain Rotation History

| Date (UTC) | Domain | Status |
|---|---|---|
| 2026-01-18 13:19 | *Contract deployed* | — |
| 2026-01-18 13:27 | `sltnnt.ru` | NXDOMAIN |
| 2026-05-09 22:18 | `thisisafalsepositive.ru` | NXDOMAIN |
| 2026-05-30 08:54 | `v4.thisisafalsepositive.ru` | NXDOMAIN |
| 2026-05-31 11:23 | `v5.thisisafalsepositive.ru` | NXDOMAIN |
| 2026-06-07 15:36 | `v6.thisisafalsepositive.ru` | NXDOMAIN |
| 2026-06-07 16:41 | `qasrgaovaf7m.thisisafalsepositive.ru` | NXDOMAIN |
| 2026-06-07 17:24 | `v7.thisisafalsepositive.ru` | NXDOMAIN |
| 2026-06-07 17:46 | `sltnnt.ru` (reverted) | NXDOMAIN |
| **2026-06-17 13:30** | **`thisisafalsepositive.st`** | **LIVE ✓** |

> The June 7th cluster (5 domain changes in 2 hours) indicates a rapid evasion response to takedown/detection of the `.ru` infrastructure.

### C2 API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/shard/prefireMc` | POST | Stage-1 victim beacon, receives prefireId |
| `/shard/submitMinecraftLog` | POST | Minecraft session data submission |
| `/cdn/e/<id>` | GET | Encrypted stage-2 payload download |
| `/submitData` | POST | Stolen credential JSON upload |
| `/submitFile` | POST | File upload (multipart) |
| `/submitLogs` | POST | Trace/debug log upload |

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
https://polygon-mainnet.rpcfast.com?api_key=xbhWBI1Wkguk8SNMu1bvvLurPGLXmgwYeC4S6g2H7WdwFigZSmPWVZRxrskEQwIf
https://go.getblock.io/02667b699f05444ab2c64f9bff28f027
```

> **Exposed API key**: `xbhWBI1Wkguk8SNMu1bvvLurPGLXmgwYeC4S6g2H7WdwFigZSmPWVZRxrskEQwIf`
> Submit to rpcfast.com abuse team for revocation.

---

## Complete Module Architecture

```
app/
├── __init__.py              Entry point, arg parser, orchestration
├── config.py                Configuration, argument validation
├── contract.py              Polygon smart contract C2 resolver
├── crypto.py                AES-GCM, DPAPI, PBKDF2 decryption
├── http.py                  HTTP session + DoH patch + retry
├── staging.py               Self-installer, Python runtime, persistence
├── trace.py                 Debug trace → svchost_d.log
├── logging/
│   └── __init__.py          HitLog, LoggingManager classes
├── handlers/
│   ├── __init__.py
│   ├── browser.py           Chromium credential extraction (17 browsers)
│   ├── browser_extensions.py  Wallet extension file collection
│   ├── credentials.py       Non-browser credentials (20+ applications)
│   ├── discord.py           Discord token extraction + validation
│   ├── files.py             HitFile / FileManager upload classes
│   ├── firefox.py           Firefox credential extraction
│   ├── keywords.py          Keyword-based document search
│   ├── minecraft.py         Minecraft accounts (8 launchers)
│   ├── screenshot.py        Screen capture (PIL → base64 JPEG)
│   ├── system_info.py       WMI + psutil system fingerprint
│   └── wallets.py           Desktop crypto wallets (13)
├── resources/
│   ├── __init__.py
│   └── browser_module.py    XOR-encoded injected DLL payload
└── util/
    ├── __init__.py
    ├── crypto.py            Low-level DPAPI / AES-GCM
    ├── dll_injection.py     CreateRemoteThread + LoadLibraryA
    ├── file.py              File utilities, zip helpers
    ├── handle_copy.py       Handle duplication (bypass file locks)
    ├── pipe.py              Named pipe IPC with injected DLL
    ├── process.py           SuspendedProcess, kill helpers
    └── registry.py         Windows registry read wrappers
```

---

## Capability Deep-Dive

### Browser Credential Theft (`handlers/browser.py`, `handlers/firefox.py`)

**17 Chromium browsers targeted:**
```
Google Chrome       Microsoft Edge      Brave Browser
Opera Stable        Opera GX            Vivaldi
Yandex Browser      7Star               CentBrowser
Chedot              CocCoc              Comodo Dragon
Epic Privacy        Iridium             Slimjet
Torch               Chromium
```

**Data extracted per browser profile:**

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

-- History (last 5000 entries)
SELECT url, title, visit_count, last_visit_time FROM urls
       ORDER BY last_visit_time DESC LIMIT 5000

-- Google OAuth tokens
SELECT service, encrypted_token FROM token_service
```

**Decryption chain:**
- `v10` values → Windows DPAPI (`CryptUnprotectData` via ctypes)
- `v20` values → ABE key from `Local State` → AES-256-GCM decrypt
- Cookie values: 32-byte nonce header stripped, then AES-GCM

**File lock bypass strategies (4 fallbacks):**
1. Direct file copy (browser not running)
2. `DuplicateHandle` from all browser PIDs (handle duplication)
3. DLL injection → named pipe IPC → receive decrypted key from inside browser
4. Kill browser → post-kill copy

**Firefox specific (key4.db PBKDF2 attack):**
```sql
SELECT a11 FROM nssPrivate WHERE a11 IS NOT NULL ORDER BY length(a11) DESC
SELECT item1 FROM metadata WHERE id = 'password'
SELECT fieldname, value FROM moz_formhistory
SELECT host, name, value, path, expiry FROM moz_cookies
```
Uses `Crypto.Protocol.KDF` (PBKDF2), `Crypto.Hash` (SHA256), PBES2/3DES decryption.

---

### Discord Token Theft (`handlers/discord.py`)

**Clients:** Discord, Discord Canary, Discord PTB

**Path:** `%APPDATA%\discord\Local Storage\leveldb\`

**Token regex:** `[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}`

**Validation:** `GET https://discord.com/api/v9/users/@me` with `Authorization: <token>`

Filters duplicates, invalid, and expired tokens. Returns user info dict for valid tokens.

---

### Crypto Wallet Theft (`handlers/wallets.py`)

| Wallet | Path | Output |
|---|---|---|
| Exodus | `%APPDATA%\Exodus\exodus.wallet\` | `Exodus.zip` |
| Atomic | `%APPDATA%tomic\` | `Atomic.zip` |
| Electrum | `%APPDATA%\Electrum\wallets\` | `Electrum.zip` |
| Electrum-LTC | `%APPDATA%\Electrum-LTC\wallets\` | `Electrum-LTC.zip` |
| Zcash | `%APPDATA%\Zcash\` | `Zcash.zip` |
| Armory | `%APPDATA%\Armory\` | `Armory.zip` |
| Bytecoin | `%APPDATA%\Bytecoin\` | `Bytecoin.zip` |
| Jaxx | `com.liberty.jaxxile__0.indexeddb.leveldb` | `Jaxx.zip` |
| Ethereum | `%APPDATA%\Ethereum\` | `Ethereum.zip` |
| Guarda | `%APPDATA%\Guarda\` | `Guarda.zip` |
| Coinomi | `%APPDATA%\Coinomi\` | `Coinomi.zip` |
| CakeWallet | `com.cakewallet.cake_wallet` | `CakeWallet.zip` |
| Monero | `%APPDATA%\Monero\` | `Monero.zip` + `Monero_AppData.zip` |

Browser wallet extensions: all `Local Extension Settings` directories zipped.

---

### Credential File Theft (`handlers/credentials.py`)

| Application | Files Stolen | Output |
|---|---|---|
| Git | `.git-credentials` | `Git_Credentials.txt` |
| SSH | `.ssh/` directory | `SSH_Keys.zip` |
| FileZilla | `recentservers.xml`, `sitemanager.xml` | `FileZilla_RecentServers.xml`, `FileZilla_SiteManager.xml` |
| WinSCP | `WinSCP.ini`, `WinSCP_Config.ini` | Same names |
| Riot Games | `RiotGamesPrivateSettings.yaml`, `RiotGames_Settings.yaml` | Same names |
| Thunderbird | All profiles | `Thunderbird_Profiles.zip` |
| Claude AI | `.claude/.credentials.json` | `Claude_Credentials.json` |
| Telegram | `tdata/` (excl. media_cache) | `Telegram_Data.zip` |
| Roblox | DPAPI-decrypted session cookies | `RobloxCookies.dat`, `Roblox_Cookies.txt` |
| OBS Studio | Stream keys from all profiles | `_StreamKey.json` |
| Mullvad VPN | CLI account query | `Mullvad_Account.txt` |
| Steam | `loginusers.vdf`, `local.vdf` DPAPI tokens | `Steam_Tokens.txt` |

---

### Minecraft Handler (`handlers/minecraft.py`)

**8 launchers targeted:**

| Launcher | File |
|---|---|
| Vanilla | `.minecraft/` directory |
| Lunar Client | `lunar_accounts.json` |
| Feather Launcher | `account.txt` (DPAPI encrypted), `feather_accounts.txt` |
| GG Essential | `essential_accounts.json` |
| Microsoft | `microsoft_accounts.json` |
| Prism Launcher | `prismlauncher_accounts.json` |
| Modrinth | `app.db` SQLite (`SELECT username, uuid, access_token FROM minecraft_users`) |

Also parses `servers.dat` (NBT format) → `Minecraft_Server_List.txt`

---

### Staging & Persistence (`staging.py`)

```
1. Check persistence: local HTTP status server on 127.0.0.1
   → If already running: skip (UUID: 4015d0e9-4cab-4ac1-8dfd-5ee8f283bca1)
2. Download Python 3.12.7:
   https://www.python.org/ftp/python/3.12.7/python-3.12.7-embed-amd64.zip
3. Patch python312._pth: uncomment 'import site'
4. Download pip: https://bootstrap.pypa.io/get-pip.py
5. Install pip, then install requirements.txt from C2
6. Download main.py + app.pyd from C2 /cdn/e/<id>
7. Decrypt (AES-128-CBC), write to disk
8. Launch in background thread (staging-worker)
9. Log all activity to svchost_d.log
```

---

### HTTP / Network Layer (`http.py`)

**User-Agent (fake, detectable):**
```
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36
```
> Chrome/142 does not exist as of analysis date — anomalous and detectable.

**DNS-over-HTTPS patch:**
All DNS resolution monkey-patched at `socket.getaddrinfo` level.
All hostnames resolved via `https://cloudflare-dns.com/dns-query` (application/dns-json).
Exception: `cloudflare-dns.com` itself uses native resolution.

**Custom C2 headers:**
```
X-Runtime-Env:           <--env argument value>
X-Tracking-ID:           <--prefireId value>
X-Edge-Cache-Revalidate: (present on all requests)
```

**Retry policy:** urllib3 with status_forcelist backoff.

---

### System Fingerprinting (`handlers/system_info.py`)

| Data | Method |
|---|---|
| CPU model | WMI `Win32_Processor` |
| GPU model | WMI `Win32_VideoController` |
| RAM size | psutil `virtual_memory` |
| Windows version | Registry `SOFTWARE\Microsoft\Windows NT\CurrentVersion` |
| Username | Windows API |
| Computer name | Windows API |
| All ops | 3-second timeout protection |

---

## DLL Injection Mechanism

The `resources/browser_module.py` module contains an XOR-encoded Windows DLL
that is injected into live browser processes to steal credentials without killing
or suspending the browser (avoiding user notification).

```
app_resources_browser_module.py: XOR decode DLL bytes
         ↓
Write DLL to %TEMP%\<random>.tmp
         ↓
Get all PIDs for target browser (chrome.exe, msedge.exe, brave.exe...)
         ↓
For each PID:
  VirtualAllocEx(pid, NULL, dll_path_len, MEM_COMMIT, PAGE_READWRITE)
  WriteProcessMemory(pid, alloc_addr, dll_path_bytes)
  CreateRemoteThread(pid, NULL, 0, LoadLibraryA, alloc_addr, 0, NULL)
         ↓
CreateNamedPipe(\\.\pipe\<pid_derived_tag>)
ConnectNamedPipe() → wait for DLL to connect
WriteFile(pipe, aes_key)         → send browser Local State encryption key
ReadFile(pipe) → decrypted_key   → receive master key from inside browser
```

**PID-to-pipe-tag algorithm:** `rotl32` function (matches Java stage-1 implementation for cross-language IPC).

---

## Decryption & Reverse Engineering Method

### Challenge

`app.pyd` is a Nuitka-compiled native Windows DLL. All Python source, string literals, and constants are stored in the `.rsrc` section (237KB, entropy 7.99/8.0 — maximum encryption) and decrypted at runtime via `FindResourceA` / `LoadResource` / `LockResource`.

### Method

1. **Identified decryption function** by finding `FindResourceA` IAT reference in `.text`, then disassembling the enclosing function with Capstone
2. **Reverse engineered the cipher** from the disassembly:
   - Input: raw `.rsrc` resource bytes
   - `movzx eax, [rdi+rdx]` — load byte
   - `lea ecx, [rdx-8]; add cl, bl` — accumulator update
   - `xor rbx, rax` — XOR with accumulator
   - `movzx ebx, [rbx+r9+0x174450]` — 256-byte S-box substitution
   - 8-case jump table at `0x16cc34` — modify accumulator (`add`/`sub` deltas: `-98, -59, -105, +88, +21, +13, +6, +79`)
   - Output written from offset `rdx-0x10` starting at `rdx=0x18`
   - Loop runs `rdx` from 8 to `0x39E48` (237,128 bytes)
3. **Reimplemented in Python** — decrypted full 237KB constant pool
4. **Parsed Nuitka constant pool format**: named records (`<module_name> ` + 4-byte size + type-prefixed string pool)
5. **Extracted all 30 modules** with their complete string constants

### Cipher Implementation

```python
table_rva = 0x174450   # 256-byte substitution S-box
case_deltas = [-98, -59, -105, +88, +21, +13, +6, +79]  # jump table

bl = 0                 # accumulator
rdx = 8                # byte index
while rdx < 0x39E48:
    eax = rsrc[rdx]
    cl  = ((rdx - 8) + bl) & 0xFF
    ebx = (cl ^ eax) & 0xFF
    ebx = table[ebx]           # S-box lookup
    bl  = ebx
    if rdx >= 0x18:
        output[rdx - 0x10] = bl
    bl = (bl + case_deltas[rdx & 7]) & 0xFF
    rdx += 1
```

---

## Indicators of Compromise

### Network IOCs

| Type | Value | Status |
|---|---|---|
| IP | `185.178.208.191` | **LIVE** (DDoS-Guard RU) |
| Domain | `thisisafalsepositive.st` | **LIVE** |
| Domain | `thisisafalsepositive.ru` | NXDOMAIN |
| Domain | `sltnnt.ru` | NXDOMAIN (fallback) |
| Domain | `v3-v7.thisisafalsepositive.ru` | NXDOMAIN |
| Domain | `qasrgaovaf7m.thisisafalsepositive.ru` | NXDOMAIN |
| User-Agent | `...Chrome/142.0.0.0 Safari/537.36` | Anomalous |
| HTTP Header | `X-Runtime-Env` | C2 beacon |
| HTTP Header | `X-Tracking-ID` | C2 session |
| HTTP Header | `X-Edge-Cache-Revalidate` | C2 marker |
| URL pattern | `/cdn/e/[a-z0-9]+` | Payload download |
| DNS | All via `cloudflare-dns.com/dns-query` | DoH evasion |

### Blockchain IOCs

| Type | Value |
|---|---|
| Polygon contract | `0x9c0a507300fd902787bb193d80fca5ce6e1bff9a` |
| Operator wallet | `0x6767c6496541b530a5d1d0eb9b80bd5c7bf56767` |
| Exposed API key | `xbhWBI1Wkguk8SNMu1bvvLurPGLXmgwYeC4S6g2H7WdwFigZSmPWVZRxrskEQwIf` |

### Cryptographic IOCs

| Type | Value |
|---|---|
| Stage-2 AES key | `207570de60034b19d76df8e7aefc69b7` (AES-128-CBC) |
| Staging UUID | `4015d0e9-4cab-4ac1-8dfd-5ee8f283bca1` |

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
SOFTWARE\Valve\Steam
SOFTWARE\Wow6432Node\Valve\Steam
SOFTWARE\Microsoft\Windows NT\CurrentVersion
SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths
SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\App Paths
```

### Process / Pipe IOCs

| Type | Value |
|---|---|
| Named pipe pattern | `\\.\pipe\[0-9a-f]{8}` |
| Chrome injection | `CreateRemoteThread` into `chrome.exe` / `msedge.exe` / `brave.exe` |
| Staging UUID check | Local HTTP server on `127.0.0.1` |

### Regex IOCs

```
Discord token:  [\w-]{24}\.[\w-]{6}\.[\w-]{25,110}
Browser profile: ^(Default|Profile\s+\d+)$
Telegram exclude: user_data[^/\]*[/\](media_cache|cache)($|[/\])
```

---

## Anti-Analysis & Evasion Techniques

| ID | Technique | Detail |
|---|---|---|
| E-01 | DNS-over-HTTPS | All DNS via Cloudflare DoH at socket level |
| E-02 | Blockchain C2 | Polygon smart contract — cannot be seized |
| E-03 | Nuitka compilation | Python → native x64 PE, defeats decompilers |
| E-04 | Custom cipher | Rolling XOR + 256-byte S-box on constant pool |
| E-05 | DLL injection | Bypasses browser file locks without termination |
| E-06 | Handle duplication | Secondary file lock bypass via DuplicateHandle |
| E-07 | SetErrorMode | Suppresses all error dialogs (silent) |
| E-08 | C2 domain naming | `thisisafalsepositive.st` — social engineering |
| E-09 | Log disguise | `svchost_d.log` mimics Windows service log |
| E-10 | Socket monkey-patch | `getaddrinfo` replaced at Python level |
| E-11 | Fake Chrome version | `Chrome/142.0.0.0` (non-existent) |
| E-12 | Persistence check | Local HTTP server before re-staging |
| E-13 | Size limits | Telegram excludes media_cache to avoid detection |
| E-14 | Timeout protection | All ops wrapped in 3-second timeout |

---

## Defensive Recommendations

### Immediate Actions

1. **Block `185.178.208.191`** at perimeter firewall
2. **Block `thisisafalsepositive.st`** DNS resolution (and `sltnnt.ru` fallback)
3. **Report API key** `xbhWBI1Wkguk8SNMu1...` to rpcfast.com abuse team for revocation
4. **Block Polygon RPC endpoints** in outbound firewall if not operationally required
5. **Submit Polygon contract** `0x9c0a507300fd902787bb193d80fca5ce6e1bff9a` to Polygon ecosystem abuse contacts

### Detection Rules (SIEM/EDR)

```yaml
# Anomalous Chrome User-Agent
rule: HTTP User-Agent contains "Chrome/142"

# C2 beacon headers
rule: Outbound HTTP contains header "X-Tracking-ID" OR "X-Runtime-Env"

# DNS-over-HTTPS evasion
rule: Outbound HTTPS to cloudflare-dns.com/dns-query from endpoint (not browser)

# DLL injection into browser
rule: CreateRemoteThread source=non-browser target=chrome.exe|msedge.exe|brave.exe

# Named pipe IPC
rule: Named pipe created matching \.\pipe\[0-9a-f]{8}

# Python staging
rule: python.exe OR pip.exe created in %LOCALAPPDATA% OR %TEMP%

# Stealer log
rule: File created matching *\svchost_d.log in user profile directories

# Payload download pattern
rule: HTTP GET to */cdn/e/* with response size > 10MB

# Staging UUID
rule: Network connection from process with UUID 4015d0e9-4cab-4ac1-8dfd-5ee8f283bca1
```

### Hunting Queries

```
# Proxy/firewall logs
dest_domain IN [thisisafalsepositive.st, sltnnt.ru] OR dest_ip=185.178.208.191

# Polygon RPC outbound (endpoint workstations should not query blockchain)
dest_domain IN [polygon-rpc.com, rpc-mainnet.matic.quiknode.pro,
                polygon-public.nodies.app, polygon-bor-rpc.publicnode.com,
                1rpc.io, endpoints.omniatech.io, api.zan.top]

# Python embedded zip download from python.org (unusual on endpoints)
url CONTAINS "python-3.12.7-embed-amd64.zip"

# GetPip download (unusual on endpoints)
url CONTAINS "bootstrap.pypa.io/get-pip.py"
```

---

## Source Files Index

The `source/` directory contains 30 reconstructed Python module files.
Each file contains all string literals, SQL queries, file paths, class names,
function names, and identifiers extracted directly from the compiled binary
constant pool — these are the authentic strings from the original Python source code.

| File | Module | Description |
|---|---|---|
| `app.py` | `app` | Entry point, orchestration, arg parser |
| `app_config.py` | `app.config` | Configuration, validation |
| `app_contract.py` | `app.contract` | Polygon C2 domain resolver |
| `app_crypto.py` | `app.crypto` | Crypto wrapper (AES/DPAPI/PBKDF2) |
| `app_handlers.py` | `app.handlers` | Handler package init |
| `app_handlers_browser.py` | `app.handlers.browser` | Chromium credential theft |
| `app_handlers_browser_extensions.py` | `app.handlers.browser_extensions` | Wallet extension collection |
| `app_handlers_credentials.py` | `app.handlers.credentials` | Non-browser credential theft |
| `app_handlers_discord.py` | `app.handlers.discord` | Discord token theft |
| `app_handlers_files.py` | `app.handlers.files` | File/upload management |
| `app_handlers_firefox.py` | `app.handlers.firefox` | Firefox credential theft |
| `app_handlers_keywords.py` | `app.handlers.keywords` | Document keyword search |
| `app_handlers_minecraft.py` | `app.handlers.minecraft` | Minecraft account theft |
| `app_handlers_screenshot.py` | `app.handlers.screenshot` | Screen capture |
| `app_handlers_system_info.py` | `app.handlers.system_info` | System fingerprinting |
| `app_handlers_wallets.py` | `app.handlers.wallets` | Crypto wallet theft |
| `app_http.py` | `app.http` | HTTP + DoH + C2 headers |
| `app_logging.py` | `app.logging` | Logging classes |
| `app_resources.py` | `app.resources` | Resources package init |
| `app_resources_browser_module.py` | `app.resources.browser_module` | XOR-encoded DLL payload |
| `app_staging.py` | `app.staging` | Self-install, persistence |
| `app_trace.py` | `app.trace` | Debug tracer |
| `app_util.py` | `app.util` | Util package init |
| `app_util_crypto.py` | `app.util.crypto` | Low-level crypto wrappers |
| `app_util_dll_injection.py` | `app.util.dll_injection` | DLL injector |
| `app_util_file.py` | `app.util.file` | File helpers |
| `app_util_handle_copy.py` | `app.util.handle_copy` | Handle duplication |
| `app_util_pipe.py` | `app.util.pipe` | Named pipe IPC |
| `app_util_process.py` | `app.util.process` | Process management |
| `app_util_registry.py` | `app.util.registry` | Registry access |

---

## Timeline

| Date | Event |
|---|---|
| 2026-01-18 | Polygon smart contract deployed, `sltnnt.ru` set as C2 |
| 2026-05-09 | Domain rotated to `thisisafalsepositive.ru` (infrastructure upgrade) |
| 2026-06-07 | Rapid domain rotation (5 changes in 2 hours) — likely takedown response |
| 2026-06-17 | Moved to `.st` TLD — `thisisafalsepositive.st` (current, live) |
| 2026-07-20 | Full malware analysis and decryption completed |

---

## Research Notes

### What we could NOT fully recover

- **Full Python bytecode**: Nuitka compiles Python to native C code — bytecode is not stored in the binary. The constant pool contains string literals and identifiers but not executable bytecode.
- **The injected DLL source**: `browser_module.py` contains ~157KB of XOR-encoded DLL bytes. The DLL itself is a native Windows PE that communicates via named pipe. Full DLL analysis would require a separate reverse engineering pass.
- **C2 server-side logic**: The admin panel at `/auth/login` requires authentication. Server-side data aggregation, operator tooling, and buyer infrastructure are unknown.
- **Full victim count**: On-chain data shows operator wallet with only 13 transactions suggesting either early-stage operation or use of a separate payment wallet.

### Decryption Key Recovery

The Nuitka constant pool cipher was fully reversed via static disassembly:
- `FindResourceA` call site located at `.text+0x16BA0B`
- Decryption function at `0x18016C9B7`
- S-box at file offset `0x173250` (256 bytes)
- Jump table at RVA `0x16CC34` (8 entries × 4 bytes)
- Full cipher reimplemented in Python, all 237,128 bytes decrypted

---

*Analysis performed: 2026-07-20*
*Platform: Parrot OS Linux (static + dynamic analysis)*
*Tools: pefile, capstone, unicorn, Frida, objdump, radare2, Python 3.12*

---

## Live C2 Infrastructure Scan (2026-07-20)

> Active reconnaissance performed against `thisisafalsepositive.st` / `185.178.208.191`

### Server Fingerprint

| Property | Value |
|---|---|
| Real IP | `185.178.208.191` |
| Hosting | DDoS-Guard (Russia) — bulletproof proxy |
| DNS | Cloudflare nameservers (`dean.ns.cloudflare.com`, `luciane.ns.cloudflare.com`) |
| Backend framework | **Python Flask** (confirmed via 403 error page HTML) |
| TLS issuer | Let's Encrypt / `CN=YR1` |
| TLS issued | 2026-06-17 12:36 UTC (matches on-chain domain rotation date exactly) |
| TLS SHA1 fingerprint | `57:FA:98:59:74:BF:A8:FA:91:48:F0:10:D1:99:DB:05:1A:48:4A:84` |
| TLS expires | 2026-09-15 |
| DNS records | A: `185.178.208.191`, MX: none, TXT: none |

### Endpoint Map (Active Probing)

| Endpoint | Method | Status | Notes |
|---|---|---|---|
| `/` | GET | 302 → `/auth/login` | Default redirect |
| `/auth/login` | GET | **403** | Admin panel — IP-blocked |
| `/dashboard` | GET | 308 → `/auth/login` | Permanent redirect |
| `/favicon.ico` | GET | **200** | 270KB Windows ICO (BMP format) |
| `/shard/prefireMc` | GET | **405** | Endpoint EXISTS, expects POST |
| `/shard/prefireMc` | POST | 403 | IP-blocked but endpoint confirmed |
| `/shard/submitMinecraftLog` | POST | 403 | Endpoint confirmed |
| `/cdn/e/3b8f6d2a9c1e` | GET | **200** | **LIVE PAYLOAD — actively serving** |
| All other `/cdn/e/*` | GET | 404 | ID-gated access |
| `/api/*`, `/admin/*`, `/debug/*` | GET | 404 | Not exposed |

> **Note:** DDoS-Guard blocks non-victim IPs from accessing authenticated endpoints.
> The `/shard/prefireMc` 405 response (Method Not Allowed on GET) confirms the
> endpoint exists and expects POST — consistent with Stage-1 beacon behaviour.

### Live Payload Analysis — V2 (Downloaded 2026-07-20)

The CDN endpoint `/cdn/e/3b8f6d2a9c1e` was actively serving a **22MB encrypted payload**
re-encrypted with Python Fernet within minutes of our analysis beginning — indicating
the operator monitors payload access patterns.

| Property | V1 (original sample) | V2 (live, 2026-07-20) |
|---|---|---|
| Encryption | AES-128-CBC (raw) | **Python Fernet** (AES-128-CBC + HMAC-SHA256) |
| Encryption key | `207570de60034b19d76df8e7aefc69b7` | `74af664f79d1ef1436a4bf301788c7eb207570de60034b19d76df8e7aefc69b7` |
| Key relationship | Original AES-128 key | **Old AES key = last 16 bytes of Fernet key** |
| Fernet token timestamp | N/A | `1784588729` = 2026-07-20 18:05 UTC |
| `AppHost/app.pyd` SHA256 | `1280ff5f2c4a59e8a9301d8e2eb7c2e9...` | **IDENTICAL** — stealer core unchanged |
| `AppHost/main.py` | N/A | **Plain Python, 353 bytes, unobfuscated** |
| mypyc Stage-1 component | `81d243bd2c585b0f4821__mypyc...` | `52056f4b964f1bc0419064a374a32e56...` **(updated)** |
| Bundle file count | 736 | 736 |
| Total bundle size | 22MB | 22MB |

**`main.py` full source (recovered from live payload):**

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

**Key finding:** The Fernet key was pre-embedded in the v1 constant pool as
`dK9mT3nR7xQ2pL8wF4jH6yB1cN5gA0sZ12345678abc=` — the operator hardcoded future
encryption credentials into the deployed binary.

### Operator Behaviour Assessment

| Observation | Assessment |
|---|---|
| Re-encrypted payload within hours of analysis | Operator monitors CDN access logs in near real-time |
| Upgraded AES-CBC → Fernet (adds HMAC integrity) | Response to known decryption — attempted to harden |
| Stealer `app.pyd` unchanged | Operator prioritised speed over updating stealer logic |
| mypyc Stage-1 updated | New campaign build or bug fix to Java launcher |
| DDoS-Guard IP allowlisting on `/auth/login` | Admin panel restricted to operator IP range |
| Fernet key pre-embedded in v1 binary | OPSEC failure — full key rotation not performed |

### New IOCs (Live Scan)

| Type | Value |
|---|---|
| TLS SHA1 fingerprint | `57:FA:98:59:74:BF:A8:FA:91:48:F0:10:D1:99:DB:05:1A:48:4A:84` |
| Fernet encryption key (v2) | `74af664f79d1ef1436a4bf301788c7eb207570de60034b19d76df8e7aefc69b7` |
| V2 payload SHA256 | `69a74db222b5c001ce0f25b93e4a1f5ab591fb263c9499c62b79f9ff3d633ee3` |
| mypyc Stage-1 v2 SHA256 | `52056f4b964f1bc0419064a374a32e56ef85ccb161166971d26f46a7490bd238` |
| Active CDN payload ID | `3b8f6d2a9c1e` |
| Flask 403 signature | `<h1>Forbidden</h1><p>You don&#39;t have` |
| DDoS-Guard cookie names | `__ddg1_`, `__ddg8_`, `__ddg9_`, `__ddg10_` |
