#!/usr/bin/env python3
"""
POC-06: Blockchain C2 Domain Resolver
======================================
Target:  Polygon mainnet contract 0x9c0a507300fd902787bb193d80fca5ce6e1bff9a
Vuln:    The malware resolves its C2 domain via a public Ethereum smart
         contract on Polygon mainnet. The contract stores the operator's
         C2 domain as a plain string, readable by anyone with access to
         any Polygon RPC endpoint. This enables defenders to:
           1. Monitor the contract for domain changes
           2. Proactively block new C2 domains before malware updates
           3. Track operator wallet for identity attribution
Function: getDomain() -> selector 0xce6d41de
Wallet:   0x6767c6496541b530a5d1d0eb9b80bd5c7bf56767
Author:   Security Research — 2026-07-20
"""
import urllib.request, json, sys

CONTRACT = "0x9c0a507300fd902787bb193d80fca5ce6e1bff9a"
WALLET   = "0x6767c6496541b530a5d1d0eb9b80bd5c7bf56767"
SELECTOR = "0xce6d41de"  # getDomain()
RPC_ENDPOINTS = [
    "https://polygon-public.nodies.app",
    "https://polygon-bor-rpc.publicnode.com",
    "https://1rpc.io/matic",
    "https://polygon.drpc.org",
]

def eth_call(rpc, to, data):
    payload = json.dumps({
        "jsonrpc": "2.0", "method": "eth_call",
        "params": [{"to": to, "data": data}, "latest"], "id": 1
    }).encode()
    req = urllib.request.Request(
        rpc, data=payload,
        headers={"Content-Type": "application/json",
                 "User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.loads(r.read())

def decode_string_result(hex_result):
    # ABI decode: offset(32) + length(32) + data
    data = bytes.fromhex(hex_result[2:] if hex_result.startswith("0x") else hex_result)
    if len(data) < 64: return None
    length = int.from_bytes(data[32:64], "big")
    return data[64:64+length].decode("utf-8", errors="replace")

print("=== BLOCKCHAIN C2 DOMAIN RESOLVER ===")
print(f"Contract: {CONTRACT}")
print(f"Function: getDomain() [selector {SELECTOR}]")
print(f"Network:  Polygon mainnet")
print()

current_domain = None
for rpc in RPC_ENDPOINTS:
    try:
        result = eth_call(rpc, CONTRACT, SELECTOR)
        if "result" in result and result["result"] != "0x":
            domain = decode_string_result(result["result"])
            if domain:
                current_domain = domain
                print(f"  [OK] {rpc}")
                print(f"       Current C2 domain: {domain}")
                break
        else:
            print(f"  [ERR] {rpc}: {result.get('error', 'empty result')}")
    except Exception as e:
        print(f"  [ERR] {rpc}: {e}")

if current_domain:
    print()
    print(f"[+] CONFIRMED C2 domain: {current_domain}")
    print(f"[+] Operator wallet:     {WALLET}")
    print()
    print("[+] Defender action: Block this domain and monitor contract for updates")
    print(f"[+] Monitor URL (Polygonscan):")
    print(f"    https://polygonscan.com/address/{CONTRACT}")
    print(f"[+] Wallet history:")
    print(f"    https://polygonscan.com/address/{WALLET}")
else:
    print("[-] Could not resolve domain from any RPC endpoint")
