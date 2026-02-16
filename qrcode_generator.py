import os
import sys
import qrcode
import easygui
from datetime import datetime

inputData = easygui.enterbox("Enter data for QR code:")
if not inputData:
    sys.exit("No input provided.")

default_name = datetime.now().strftime("qrcode_%Y%m%d_%H%M%S.png")

outputPath = easygui.filesavebox(
    title="Save QR Code to...",
    default=default_name,
    filetypes=["*.png"]
)

if not outputPath:
    sys.exit("No output selected.")

root, ext = os.path.splitext(outputPath)
if not ext:
    outputPath = root + ".png"

qr = qrcode.QRCode()
qr.add_data(inputData)
img = qr.make_image()
img.save(outputPath)

easygui.msgbox(f"Finished – saved to:\n{outputPath}")