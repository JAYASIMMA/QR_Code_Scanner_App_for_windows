import wx
import wx.adv
import pyautogui
from pyzbar.pyzbar import decode
from PIL import Image
import webbrowser
import io

class QRScannerFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="🕶️ Dark QR Scanner", size=(500, 300),
                         style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("#1e1e1e")  # Dark background

        self.SetIcon(wx.Icon(wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_OTHER, (32, 32))))

        title_font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        text_font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        self.label = wx.StaticText(self.panel, label="Scan QR Code from your screen", style=wx.ALIGN_CENTER)
        self.label.SetFont(title_font)
        self.label.SetForegroundColour("#00ffff")

        self.scan_button = wx.Button(self.panel, label="🔍 Scan Now")
        self.scan_button.SetBackgroundColour("#007ACC")
        self.scan_button.SetForegroundColour("white")
        self.scan_button.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.result_label = wx.StaticText(self.panel, label="", style=wx.ALIGN_CENTER)
        self.result_label.SetFont(text_font)
        self.result_label.SetForegroundColour("#c0c0c0")
        self.result_label.Wrap(450)

        # Bind events
        self.scan_button.Bind(wx.EVT_BUTTON, self.on_scan_click)

        # Layout
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddStretchSpacer(1)
        vbox.Add(self.label, 0, wx.ALIGN_CENTER | wx.TOP, 20)
        vbox.Add(self.scan_button, 0, wx.ALIGN_CENTER | wx.TOP, 20)
        vbox.Add(self.result_label, 0, wx.ALIGN_CENTER | wx.ALL, 20)
        vbox.AddStretchSpacer(1)

        self.panel.SetSizer(vbox)
        self.Centre()
        self.Show()

    def on_scan_click(self, event):
        self.result_label.SetLabel("🔄 Scanning screen for QR code...")

        # Screenshot screen
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
