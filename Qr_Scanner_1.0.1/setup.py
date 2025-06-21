import sys
from cx_Freeze import setup, Executable

# -----------------------------
# Basic Configuration
# -----------------------------
app_name = "QR Scanner"
app_version = "1.0.1"
app_description = "Screen QR Code Scanner with GUI"
main_script = "qr_gui.py"
icon_file = "icon.ico"

# -----------------------------
# Shortcut Table (12 fields)
# -----------------------------
shortcut_table = [
    (
        "DesktopShortcut",        # 1 - Shortcut ID
        "DesktopFolder",          # 2 - Directory_
        app_name,                 # 3 - Shortcut name
        "TARGETDIR",              # 4 - Component_
        f"[TARGETDIR]{app_name}.exe",  # 5 - Target
        None,                     # 6 - Arguments
        app_description,          # 7 - Description
        None,                     # 8 - Hotkey
        icon_file,                # 9 - Icon file (must be included)
        None,                     # 10 - IconIndex
        None,                     # 11 - ShowCmd (None = normal window)
        "[TARGETDIR]"             # 12 - WorkingDir
    ),
    (
        "StartMenuShortcut",
        "ProgramMenuFolder",
        app_name,
        "TARGETDIR",
        f"[TARGETDIR]{app_name}.exe",
        None,
        app_description,
        None,
        icon_file,
        None,
        None,
        "[TARGETDIR]"
    )
]

# -----------------------------
# MSI Data (shortcuts)
# -----------------------------
msi_data = {
    "Shortcut": shortcut_table
}

# -----------------------------
# Build Options
# -----------------------------
build_exe_options = {
    "packages": ["tkinter", "pyzbar", "PIL", "pyautogui", "webbrowser"],
    "include_files": [icon_file],
    "include_msvcr": True  # Include Microsoft C Runtime libraries (safer for compatibility)
}

# -----------------------------
# Base config for GUI app
# -----------------------------
base = "Win32GUI" if sys.platform == "win32" else None

# -----------------------------
# Executable Definition
# -----------------------------
executables = [
    Executable(
        script=main_script,
        base=base,
        target_name=f"{app_name}.exe",
        icon=icon_file
    )
]

# -----------------------------
# Setup Function
# -----------------------------
setup(
    name=app_name,
    version=app_version,
    description=app_description,
    author="Jayasimma D",
    options={
        "build_exe": build_exe_options,
        "bdist_msi": {
            "data": msi_data
        }
    },
    executables=executables
)
