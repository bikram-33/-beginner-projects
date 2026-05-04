# qrcode version == 7.4.2
import qrcode
import os

data = input("Enter the text or URL you want to make qrcode:").strip()
filename = input("Enter the final name you want to save:").strip()
qr = qrcode.QRCode(box_size=20, border=5)
qr.add_data(data)
im = qr.make_image()
im.save(filename,"PNG")
print("Your qr code is ready")
