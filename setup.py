import sys, os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Users\M.2\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\M.2\AppData\Local\Programs\Python\Python36\tcl\tk8.6'

build_exe_options = {"packages": ["os", "_tkinter"],
                     "excludes": [],
                     "includes": ["string", "math", "csv", "datetime"],
                     }
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "_enigma",
        version = "0.1",
        description = "M3 Enigma Simulator",
        options = {"build_exe": build_exe_options},
        executables = [Executable("_enigma.py", base=base)])
