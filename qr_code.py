import qrcode

img_qr = qrcode.make(input("Enter phone number to generate QR Code : "))
type(img_qr)
img_qr.save("Your_QR.png")