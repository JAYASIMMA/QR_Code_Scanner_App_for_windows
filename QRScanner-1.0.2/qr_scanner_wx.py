import wx
import wx.adv
import pyautogui
from pyzbar.pyzbar import decode
from PIL import Image
import webbrowser
import io

class QRScannerFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="🕶️ Dark QR Scanner", size=(600, 350),
                         style=wx.DEFAULT_FRAME_STYLE)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("#1e1e1e")  # Dark background

        # ✅ Custom icon
        self.SetIcon(wx.Icon("icon.ico", wx.BITMAP_TYPE_ICO))

        # Fonts
        title_font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        text_font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        # UI Elements
        self.label = wx.StaticText(self.panel, label="Scan QR Code from your screen")
        self.label.SetFont(title_font)
        self.label.SetForegroundColour("#00ffff")

        self.scan_button = wx.Button(self.panel, label="🔍 Scan Now", size=(150, 40))
        self.scan_button.SetBackgroundColour("#007ACC")
        self.scan_button.SetForegroundColour("white")
        self.scan_button.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.result_label = wx.StaticText(self.panel, label="")
        self.result_label.SetFont(text_font)
        self.result_label.SetForegroundColour("#c0c0c0")
        self.result_label.Wrap(560)

        # Bind button event
        self.scan_button.Bind(wx.EVT_BUTTON, self.on_scan_click)

        # Layout
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.AddStretchSpacer(1)
        main_sizer.Add(self.label, 0, wx.ALIGN_CENTER | wx.TOP, 10)
        main_sizer.Add(self.scan_button, 0, wx.ALIGN_CENTER | wx.TOP, 20)
        main_sizer.Add(self.result_label, 0, wx.ALIGN_CENTER | wx.ALL, 20)
        main_sizer.AddStretchSpacer(1)

        self.panel.SetSizer(main_sizer)

        # Resize handling
        self.Bind(wx.EVT_SIZE, self.on_resize)

        self.Centre()
        self.Show()

    def on_resize(self, event):
        # Re-wrap text based on new width
        width = self.GetSize()[0] - 40
        self.result_label.Wrap(width)
        event.Skip()

    def on_scan_click(self, event):
        self.result_label.SetLabel("🔄 Scanning screen for QR code...")

        # Screenshot
        screenshot = pyautogui.screenshot()
        buffer = io.BytesIO()
        screenshot.save(buffer, format='PNG')
        buffer.seek(0)

        image = Image.open(buffer)
        qr_codes = decode(image)

        if qr_codes:
            data = qr_codes[0].data.decode('utf-8')
            self.result_label.SetLabel(f"✅ QR Code Found:\n{data}")
            if data.startswith("http"):
                webbrowser.open(data)
        else:
            self.result_label.SetLabel("❌ No QR Code found on screen.")

if __name__ == "__main__":
    app = wx.App(False)
    frame = QRScannerFrame()
    app.MainLoop()
