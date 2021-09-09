import os
from django.shortcuts import render
from django.http import HttpResponse, request


def Delete(request):
    folder = (r'webs/static/pdf_export')
    test = os.listdir(folder)
    for images in test:
        if images.endswith('.pdf'):
            os.remove(os.path.join(folder, images))

    folder = (r'webs/static/pdf_import')
    test = os.listdir(folder)
    for images in test:
        if images.endswith('.pdf'):
            os.remove(os.path.join(folder, images))

    folder = (r'webs/static/pdf_import')
    test = os.listdir(folder)
    for images in test:
        if images.endswith('.csv'):
            os.remove(os.path.join(folder, images))             
    return render(request,'Home.html')