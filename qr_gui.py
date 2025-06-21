import tkinter as tk
from tkinter import messagebox
from pyzbar.pyzbar import decode
from PIL import Image
import pyautogui
import webbrowser

def scan_qr():
    # Take screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    img = Image.open("screenshot.png")

    # Decode QR code
    decoded_objects = decode(img)

    if decoded_objects:
        for obj in decoded_objects:
            data = obj.data.decode("utf-8")
            result_label.config(text=f"QR Code Data:\n{data}")

            if data.startswith("http://") or data.startswith("https://"):
                webbrowser.open(data)
                messagebox.showinfo("URL Detected", f"Opening URL:\n{data}")
            else:
                messagebox.showinfo("QR Found", f"Data: {data}")
    else:
        result_label.config(text="❌ No QR code found on screen.")
        messagebox.showwarning("No QR", "No QR code found on the screen.")

# Create main window
root = tk.Tk()
root.title("Screen QR Code Scanner")
root.geometry("400x300")
root.config(bg="#f0f4f7")

# Title
title_label = tk.Label(root, text="📸 Screen QR Code Scanner", font=("Helvetica", 16, "bold"), bg="#f0f4f7")
title_label.pack(pady=20)

# Scan button
scan_button = tk.Button(root, text="🔍 Scan Screen for QR", command=scan_qr, font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
scan_button.pack()

# Result label
result_label = tk.Label(root, text="", wraplength=350, font=("Helvetica", 11), bg="#f0f4f7", fg="#333")
result_label.pack(pady=20)

# Run the app
root.mainloop()
