import time

from Tools.i18n.msgfmt import make
from django.conf import settings
from django.shortcuts import render, redirect



# Create your views here.

def admin_view(request):
    return render(request,'admin/admin.html')

def ceo_view(request):
    return render(request,'admin/ceo.html')

def manager_view(request):
    return render(request,'admin/manager.html')

def meeting_view(request):
    return render(request,'admin/meet.html')

def store_view(request):
    return render(request,'admin/store.html')

def mess_view(request):
    return render(request,'admin/mess.html')

def toilet_view(request):
    return render(request,'admin/toilet.html')


import qrcode

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

# Add data to the QR code
data = "  http://127.0.0.1:8000/ceo_view/"
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image file
img.save("qrcode.png")
