# setup.py
import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["tkinter", "pyzbar", "PIL", "pyautogui", "webbrowser"],
    "include_files": ["screenshot.png"],  # optional
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # for GUI apps

setup(
    name="QRScanner",
    version="1.0",
    description="Screen QR Code Scanner App",
    author="Jayasimma D",
    options={"build_exe": build_exe_options},
    executables=[Executable("qr_gui.py", base=base, target_name="QRScanner.exe")]
)

