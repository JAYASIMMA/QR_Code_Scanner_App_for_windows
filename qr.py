from pyzbar.pyzbar import decode
from PIL import Image
import pyautogui
import time

def scan_qr_from_screen():
    print("Scanning the screen for QR codes...")

    # Capture screenshot
    screenshot = pyautogui.screenshot()

    # Convert screenshot to image
    screenshot.save("screenshot.png")
    img = Image.open("screenshot.png")

    # Decode the QR code
    decoded_objects = decode(img)

    if decoded_objects:
        for obj in decoded_objects:
            print("✅ QR Code Detected:")
            print(f"Type: {obj.type}")
            print(f"Data: {obj.data.decode('utf-8')}")
    else:
        print("❌ No QR Code found on the screen.")

if __name__ == "__main__":
    time.sleep(2)  # Delay to allow you to open the QR code
    scan_qr_from_screen()