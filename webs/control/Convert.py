
import numpy as np
import cv2
from wand.image import Image as wimage
from wand.color import Color
from PIL import Image
import sys

filename = sys.argv[1]

class Convert:
    path = 'webs/static/pdf_import/'+str(filename)
    path_covert = 'webs/static/pdf_export/'
    convert_img = path
    #print(convert_img)
    def __init__(self):
        self.page_images = []
        self.count_name = ''

    def set_pdf_to_png(self, convert_img):
        all_pages = wimage(filename=self.path, resolution=300)
        for i, page in enumerate(all_pages.sequence):
            with wimage(page) as img:
                img.background_color = Color('white')
                img.alpha_channel = 'remove'
                img_buffer = np.asarray(bytearray(img.make_blob("png")), dtype=np.uint8)
                mat_color = cv2.imdecode(img_buffer, cv2.IMREAD_COLOR)
                self.page_images.append(mat_color)
        print("Number of pages :", len(self.page_images))

    def set_png_to_pdf(self, arr_img, name, path_save):
        print('start save', len(arr_img))
        print('Start test time save png to pdf')
        png_pdf = []
        file_pdf_name = 'Verified' + '.pdf'
        path_pdf_save = self.path_covert
        c = Image.fromarray(arr_img[0])
        c.convert(mode="RGB")
        for i in arr_img:
            c2 = Image.fromarray(i)
            c2.convert(mode="RGB")
            png_pdf.append(c2)

        
        c.save((path_pdf_save + file_pdf_name), "PDF", resolution=100.0, save_all=True, append_images=png_pdf[1:])
        path_file_output = path_pdf_save + file_pdf_name
        print('Path file output :', path_file_output)
        print('....................................................................')
        #open_path_folder = os.path.realpath(path_pdf_save)
        #os.startfile(open_path_folder)

    def get_pdf_to_png(self):
        return self.page_images
