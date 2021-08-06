from django.shortcuts import render
from django.http import HttpResponse, request
from django.core.files.storage import FileSystemStorage
from subprocess import run, PIPE
import sys
import csv

def home(request):
    return render(request,'Home.html')

def index(request) :
    return render(request,'Home.html')

def contact(request):
    return render(request,'Contact.html')

def start(request):
    return render(request,'Start.html')

def recommend(request):
    return render(request,'Recommend.html')

def custom(request):
    return render(request,'Custom.html')

def setting_congig(request):
    return render(request,'Setting_Config.html')

def download(request):
    return render(request,'Download.html')

def download_config(request):
    return render(request,'Download_Config.html')

def input(request):
    function = request.POST["function"]
    top = request.POST["top"]
    bottom = request.POST["bottom"]
    left = request.POST["left"]
    right = request.POST["right"]
    heading = request.POST["heading"]
    content = request.POST["content"]
    fist = request.POST["fist"]
    line = request.POST["line"]
    image_point = request.POST["image_point"]
    image_explanation = request.POST["image_explanation"]
    table1 = request.POST["table1"]
    numpagetop = request.POST["numpagetop"]
    numpagebottom = request.POST["numpagebottom"]
    symbol_w = request.POST["symbol_w"]
    symbol_h = request.POST["symbol_h"]
    f = request.FILES['file']

    fs = FileSystemStorage()
    filename, ext = str(f).split('.')
    file1 = fs.save(str(f), f)
    fileurl = fs.url(file1)
    fileSize = fs.size(file1)

    run([sys.executable, 'webs//control//Format_management.py',
    file1,function,top,bottom,left,right,heading,content,fist,
    line,image_point,image_explanation,table1,numpagetop,
    numpagebottom,symbol_w,symbol_h])
    return render(request,'Download.html')

def input_csv(request):
    function_csv = request.POST["function"]
    top_csv = request.POST["top"]
    bottom_csv = request.POST["bottom"]
    left_csv = request.POST["left"]
    right_csv = request.POST["right"]
    heading_csv = request.POST["heading"]
    content_csv = request.POST["content"]
    fist_csv = request.POST["fist"]
    line_csv = request.POST["line"]
    image_point_csv = request.POST["image_point"]
    image_explanation_csv = request.POST["image_explanation"]
    table1_csv = request.POST["table1"]
    numpagetop_csv = request.POST["numpagetop"]
    numpagebottom_csv = request.POST["numpagebottom"]
    symbol_w_csv = request.POST["symbol_w"]
    symbol_h_csv = request.POST["symbol_h"]

    run([sys.executable, 'webs//control//export_csv.py',
    function_csv,top_csv,bottom_csv,left_csv,right_csv,
    heading_csv,content_csv,fist_csv,line_csv,image_point_csv,image_explanation_csv,
    table1_csv,numpagetop_csv,numpagebottom_csv,symbol_w_csv,symbol_h_csv])

    return render(request,'Download_Config.html')

def upload_csv(request):
    csv_f = request.FILES['csv-file']
    f = request.FILES['file']

    fs = FileSystemStorage()
    file1 = fs.save(str(f), f)
    file2 = fs.save(str(csv_f), csv_f)

    with open('webs/static/pdf_import/'+str(file2),'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)
            function = line[0]
            top = line[1]
            bottom = line[2]
            left = line[3]
            right = line[4]
            heading = line[5]
            content = line[6]
            fist = line[7]
            linee = line[8]
            image_point = line[9]
            image_explanation = line[10]
            table1 = line[11]
            numpagetop = line[12]
            numpagebottom = line[13]
            symbol_w = line[14]
            symbol_h = line[15]

    run([sys.executable, 'webs//control//Format_management.py',
    file1,function,top,bottom,left,right,heading,content,fist,
    linee,image_point,image_explanation,table1,numpagetop,
    numpagebottom,symbol_w,symbol_h])
    return render(request,'Download.html')