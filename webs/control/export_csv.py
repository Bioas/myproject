import csv
import sys

func = sys.argv[1]
top = sys.argv[2]
bottom = sys.argv[3]
left = sys.argv[4]
right = sys.argv[5]
heading = sys.argv[6]
content = sys.argv[7]
fist = sys.argv[8]
line = sys.argv[9]
image_point = sys.argv[10]
image_explanation = sys.argv[11]
table = sys.argv[12]
numpagetop = sys.argv[13]
numpagebottom = sys.argv[14]
symbol_w = sys.argv[15]
symbol_h = sys.argv[16]


with open('webs/static/csvfile/my_config.csv','w',newline='') as f:
    
    thewriter = csv.writer(f)
    
    thewriter.writerow([func,top,bottom,left,right,heading,content,
                        fist,line,image_point,image_explanation,table,
                        numpagetop,numpagebottom,symbol_w,symbol_h])


