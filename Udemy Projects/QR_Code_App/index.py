import pyqrcode

url = input("Enter a Url to Generate QR Code")

QR = pyqrcode.create(url)

QR.png("webqr.png", scale=8)