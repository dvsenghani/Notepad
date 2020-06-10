import cx_Freeze
import sys
import os 
base = None








if sys.platform == "win32":
    base = "Win32GUI"

includes = ["atexit","re"]
executables = [cx_Freeze.Executable("dspad.py", base=base, icon='icon.ico')]

cx_Freeze.setup(
        name = 'DS Text Editor',
        version = "0.1",
        description = "Sample cx_Freeze PyQt4 script",
        options = {"build.exe": {"packages":["tkinter", "os"], "include_files": ["icon.ico", "tcl86t.dll","tk86t.dll", "icons2"]}},
        executables = executables )