Here’s a complete `README.md` file for your **QR Code Screen Scanner** project. It includes description, features, setup, packaging, and installer info.

---

### 📄 `README.md`

````markdown
# 📸 QRScanner - Screen QR Code Scanner

QRScanner is a lightweight Python desktop application that scans the screen for QR codes and automatically opens the URL (if any) in the default browser. It features a simple and intuitive Tkinter GUI and is built for convenience — no webcam or mobile device needed!

---

## 🚀 Features

- 🖥️ Scans QR codes directly from your screen
- 🌐 Opens URL automatically in the default browser
- 🧑‍💻 Easy-to-use GUI built with Tkinter
- 🔒 Runs offline with no data tracking
- 🪟 Bundled as a Windows `.msi` installer

---

## 🛠 Requirements

- Python 3.8 to 3.12 (✅ Recommended: avoid 3.13 due to `cx_Freeze` limitations)
- Required Python packages:

```bash
pip install pyzbar pillow pyautogui
````

> Note: Windows users may need to place `zbar.dll` in the same folder or in the system PATH.

---

## 📦 Running the App

```bash
python qr_gui_scanner.py
```

A GUI window will appear. Click the “Scan” button to capture your screen and detect any visible QR codes.

---

## 🔧 Building the Executable

### 1. Package as `.exe` using cx\_Freeze:

```bash
pip install cx-Freeze
python setup.py build
```

### 2. Build `.msi` Installer:

```bash
python setup.py bdist_msi
```

> Output will be in the `dist/` folder:
> `dist/QRScanner-1.0.win-amd64.msi`

---

## 🔴 Windows Defender SmartScreen Warning?

You may see a red warning when running the `.msi` installer for the first time:

* Click **"More info"**
* Then click **"Run anyway"**

> This is a normal SmartScreen response to unsigned apps. To eliminate this, sign the installer using a digital certificate.

---

## 📁 Project Structure

```
📦 qr_scanner/
├── qr_gui_scanner.py       # Main application script
├── setup.py                # Installer builder with cx_Freeze
├── README.md               # Project documentation
├── icon.ico                # (Optional) App icon
├── dist/                   # Output folder for installer
```

---

## 🧑‍💻 Author

**Jayasimma Mahadev**
\[Your GitHub or LinkedIn URL here]

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

```

---

Would you like me to also generate:
- A `setup.py` with icon and shortcut support?
- A GitHub-style project structure?
- A `.spec` file for `pyinstaller` instead of `cx_Freeze`?

Let me know how far you'd like to take this!
```
