"""
SilentNet Infostealer - Decompiled Module
Module: .app.http
Chunk size: 2342 bytes
String constants: 52 unicode, 134 identifiers

# HTTP session with DoH patch, retry policy, C2 headers
# Original path: app/http.py
"""

# ============================================================
# RECONSTRUCTED FROM NUITKA CONSTANT POOL
# Method: Rolling XOR + substitution cipher decryption
# All string literals, SQL queries, paths, and identifiers
# are authentic - extracted directly from compiled binary.
# ============================================================

# --- STRING CONSTANTS (in order of appearance) ---

# identifier: _in_doh_resolution
# identifier: _doh_cache
# identifier: trace
'r.'
# identifier: _DOH_SERVER
'?name='
'&type=A'
# identifier: urllib
# identifier: request
# identifier: Request
# identifier: headers
# identifier: Accept
'application/dns-json'
# identifier: urlopen
# identifier: timeout
# identifier: __enter__
# identifier: __exit__
# identifier: json
# identifier: loads
# identifier: read
# identifier: decode
# identifier: data
# identifier: get
# identifier: Answer
# identifier: type
# identifier: data
# identifier: doh1
'ok.'
# identifier: LoggingManager
# identifier: add
# identifier: _MODULE
'DoH resolved'
# identifier: LogType
# identifier: DEBUG
' -> '
# identifier: doh2
'no.ans'
'DoH no answer'
# identifier: WARN
'No A record for '
'DoH failed'
'Resolve hostname using Cloudflare DoH, returns first A record IP.'
# identifier: _DOH_HOSTNAME
# identifier: _resolve_via_doh
# identifier: _original_getaddrinfo
'Patched getaddrinfo that uses DoH for all hosts except cloudflare-dns.com.'
# identifier: _doh_enabled
# identifier: socket
# identifier: getaddrinfo
# identifier: _patched_getaddrinfo
'doh.en'
# identifier: global
'DoH enabled'
# identifier: INFO
'All DNS via Cloudflare DoH'
'Enable DoH resolution for all DNS lookups.'
# identifier: _session
# identifier: requests
# identifier: Session
# identifier: Retry
# identifier: total
# identifier: backoff_factor
# identifier: status_forcelist
# identifier: HTTPAdapter
# identifier: max_retries
# identifier: mount
'https://'
'http://'
'Session created'
'HTTP session initialized with retry policy'
# identifier: config
# identifier: API_HOST
'/shard'
# identifier: shard_url
# identifier: SHARD_HEADERS
# identifier: update
# identifier: replace
'/submit'
'f:'
'POST '
'url='
# identifier: get_session
# identifier: post
# identifier: headers
# identifier: data
# identifier: files
# identifier: timeout
# identifier: headers
# identifier: json
# identifier: timeout
'h.r.'
'Response '
'status='
' len='
# identifier: text
# identifier: strip
# identifier: startswith
'<html'
'h.html.'
'HTML response detected'
# identifier: ERROR
'Received HTML instead of JSON. url='
# identifier: url
# identifier: RequestException
'h.ex.'
'Request failed '
'h.g.'
'GET '
# identifier: headers
# identifier: timeout
'h.gr.'
'h.ghtml.'
'h.gex.'
# identifier: __doc__
# identifier: __file__
# identifier: origin
# identifier: has_location
# identifier: __cached__
# identifier: __annotations__
'urllib.request'
'requests.adapters'
# identifier: HTTPAdapter
'urllib3.util.retry'
# identifier: Retry
# identifier: config
# identifier: trace
# identifier: logging
# identifier: LoggingManager
# identifier: LogType
# identifier: http
'https://cloudflare-dns.com/dns-query'
'cloudflare-dns.com'
# identifier: hostname
# identifier: return
# identifier: enable_doh
'X-Edge-Cache-Revalidate'
'X-Runtime-Env'
'stale-if-error'
'jre-embedded'
# identifier: return
# identifier: endpoint
# identifier: return
# identifier: endpoint
# identifier: json_data
# identifier: files
# identifier: extra_headers
# identifier: Response
# identifier: shard_post
# identifier: shard_get
'app\\http.py'
'<module app.http>'
# identifier: host
# identifier: port
# identifier: family
# identifier: type
# identifier: proto
# identifier: flags
# identifier: ip
# identifier: hostname
# identifier: url
# identifier: req
# identifier: resp
# identifier: data
# identifier: answer
# identifier: ip
# identifier: adapter
# identifier: endpoint
# identifier: extra_headers
# identifier: url
# identifier: headers
# identifier: ep_short
# identifier: session
# identifier: resp
# identifier: json_data
# identifier: files
# identifier: extra_headers
# identifier: url
# identifier: headers
# identifier: ep_short
# identifier: session
# identifier: resp
# identifier: __spec__
