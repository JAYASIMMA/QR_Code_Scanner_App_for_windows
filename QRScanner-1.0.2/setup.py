import sys
from cx_Freeze import setup, Executable

# Define shortcut (MSI only)
shortcut_table = [
    (
        "DesktopShortcut",           # Shortcut
        "DesktopFolder",             # Location
        "QR Scanner",                # Shortcut name
        "TARGETDIR",                 # Directory where exe is installed
        "[TARGETDIR]QRScanner.exe",  # Target path
        None,                        # Arguments
        "QR Code Screen Scanner",    # Description
        None,                        # Hotkey
        "icon.ico",                  # Icon file
        None, None, "[TARGETDIR]"    # Working directory
    )
]

# MSI data configuration
msi_data = {
    "Shortcut": shortcut_table
}

# MSI options
bdist_msi_options = {
    "data": msi_data,
    "add_to_path": False,
    "initial_target_dir": r"[ProgramFilesFolder]\QRScanner"
}

# EXE build options
build_exe_options = {
    "packages": ["pyautogui", "pyzbar", "PIL", "io", "webbrowser"],
    "include_files": ["icon.ico"]
}

# Use GUI base on Windows
base = "Win32GUI" if sys.platform == "win32" else None

# Setup configuration
setup(
    name="QRScanner",
    version="1.0",
    description="Screen QR Scanner with wxPython",
    options={
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options
    },
    executables=[
        Executable(
            script="qr_scanner_wx.py",
            base=base,
            target_name="QRScanner.exe",
            icon="icon.ico"
        )
    ]
)
