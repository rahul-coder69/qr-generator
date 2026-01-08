import qrcode

# Take input from user
data = input("Enter text or URL to generate QR code: ")

# Create QR code
qr = qrcode.make(data)

# Save QR code as PNG
qr.save("qrcode.png")

print("QR code generated and saved as qrcode.png")
