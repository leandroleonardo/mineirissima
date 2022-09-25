import sys
from cx_Freeze import setup, Executable
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter", "pymysql"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

local = './controllers/main.py'

setup(
    name="Mineirissima",
    version="0.1",
    description="ERP!",
    options={"Mineirissima_exe": build_exe_options},
    executables=[Executable(local, base=base)]
)