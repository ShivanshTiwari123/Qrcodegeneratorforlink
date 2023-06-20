import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L)

qr.add_data("https://www.youtube.com")    #plz input the webiste or url to make the Qr code within "" plz

img = qr.make_image()
img.save("qrcode.png")    #You can also change the name of the Qrcode.png to your prefered name but ends with .png
