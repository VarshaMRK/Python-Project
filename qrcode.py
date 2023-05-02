import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("Varsha Ramkumar")
qr.png("myqr.png", scale=8)

d = decode(Image.open('myqr.png'))
print(d[0].data.decode("ascii"))
