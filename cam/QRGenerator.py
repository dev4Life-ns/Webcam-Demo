import qrcode
import png
from pyqrcode import QRCode
import qr_data.dataA
import qrcode

""" 
creates a qrcode based on data from dataA class 
then stores results to images folder in project
"""
qr_data = qr_data.dataA.DataA.qr_profile

qr = qrcode.QRCode(version=1,
                   box_size=10,
                   border=5)
qr.add_data(qr_data)
qr.make(fit=True)
img = qr.make_image(fill_color='teal',
                    back_color='black')
img.save('../images/baby blue_qrcode.png')
