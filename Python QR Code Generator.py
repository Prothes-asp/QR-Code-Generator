# pip install pycode
# pip install qrcode
# pip install PyQRCode

import pyqrcode


# String which represent the QR code
Text = "Name : Prothes Barai \nChannel Name  : Developer Prothes\n" \
    "Channel Url : https://www.youtube.com/channel/UC034wUXk2-EOvbqpg_X_JWw\nProjects Name : Python Projects(QR Code Genarator)"

# Generate QR code
Create_Qr = pyqrcode.create(Text)

# Create and save the png file naming "myqr.png"
Create_Qr.svg("myyoutube.svg", scale=8)
print("Successfully Genarator Your QR Code")