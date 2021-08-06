import numpy as np
import cv2
import Memmory
from Convert import Convert
import Sub_function
import Marking
import sys

class SendValue:

    pro_path_file = Memmory.PathFile('')
    add_sub = Sub_function

    def __init__(self, category, top, bottom, left, right, heading, content, first_para,
                 line, image_point, image_explanation, table, number_top, number_right, symbol_w, symbol_h, path_save):
        self.set_mark = int(category)
        self.set_top = self.add_sub.convert_margin(top)
        self.set_bottom = self.add_sub.convert_margin(bottom)
        self.set_left = self.add_sub.convert_margin(left)
        self.set_right = self.add_sub.convert_margin(right)
        self.set_heading = self.add_sub.convert_size_text(heading)
        self.set_content = self.add_sub.convert_size_text(content)
        self.set_heading_eng = self.add_sub.convert_text_english_b(heading)
        self.set_content_eng = self.add_sub.convert_text_english_s(content)
        self.set_first_para = self.add_sub.convert_paragraph(first_para)
        self.set_line_content, self.set_line_head = self.add_sub.convert_line_spacing(line)
        self.set_point = image_point
        self.set_explanation = image_explanation
        self.set_table = table
        self.set_number_top = self.add_sub.convert_margin(number_top)
        self.set_number_right = self.add_sub.convert_margin(number_right)
        self.set_symbol_w = symbol_w
        self.set_symbol_h = symbol_h
        self.path_to_save = path_save

    def set_marking_sum(self):
        name = ''
        arr_img_output = []
        convert = Convert()
        convert.set_pdf_to_png(self.pro_path_file.get_file())
        img_convert = convert.get_pdf_to_png()
        for c in range(img_convert.__len__()):
            img = cv2.cvtColor(np.array(img_convert[c]), cv2.COLOR_RGB2BGR)
            h, w = img.shape[:2]
            # print('w', w)
            # print('h', h)
            set_margin_right = round(int(w) - self.set_right)
            set_margin_bottom = round(int(h) - self.set_bottom)
            set_right_number = round(w - int(self.set_number_right))
            mark = Marking.Mark(img)
            mark.set_clone_img_main()
            mark.set_arr_up_lo()
            mark.set_img_margin(self.set_number_top, set_right_number)
            mark.set_size_txt()
            mark.set_mark_margin(self.set_mark, self.set_top, set_margin_bottom, self.set_left, set_margin_right)

            if self.set_mark == 0:
                # print('Mark cover')
                name = 'Cover'
                mark.square_paragraph()
                mark.img_symbol(self.set_top, self.set_left, set_margin_right, self.set_symbol_w, self.set_symbol_h)
                mark.set_text(int(self.set_heading), int(self.set_content))
                mark.set_check_point(self.set_left, set_margin_right)
                mark.set_line_equal()
                mark.set_mark_symbol()
                mark.set_mark_text()
                mark.set_mark_point()
                mark.set_mark_lines_equal()
                marking_cover = mark.get_mark_img()
                arr_img_output.append(marking_cover)
                # cv2.imwrite('000.png', marking_cover)
            elif self.set_mark == 1:
                # print('Mark title')
                name = 'Title-page'
                mark.square_paragraph()
                mark.set_text_title(self.set_content)
                mark.set_check_point(self.set_left, set_margin_right)
                mark.set_line_equal()
                mark.set_mark_text_title()
                mark.set_mark_point()
                mark.set_mark_lines_equal()
                marking_title = mark.get_mark_img()
                arr_img_output.append(marking_title)
                # cv2.imwrite('100.png', marking_title)
            elif self.set_mark == 2:
                # print('Mark thesis')
                name = 'Thesis-certificate'
                mark.square_paragraph()
                mark.set_text(self.set_heading, self.set_content)
                mark.set_symbol_center(self.set_left, set_margin_right)
                mark.set_head_content_center(self.set_left, set_margin_right)
                mark.set_line_content(self.set_line_content, self.set_line_head)
                mark.set_mark_text()
                mark.set_mark_symbol_thesis()
                mark.set_mark_head_thesis()
                mark.set_mark_content_thesis()
                mark.set_mark_line_wrong()
                marking_thesis = mark.get_mark_img()
                arr_img_output.append(marking_thesis)
                # cv2.imwrite('200.png', marking_thesis)
            elif self.set_mark == 3:
                # print('Mark Abt')
                name = 'Abstract-thai'
                mark.square_paragraph()
                mark.set_mark_number(self.set_number_top, set_right_number)
                mark.set_text(self.set_heading, self.set_content)
                mark.set_line_head_abt(self.set_left, set_margin_right)
                mark.set_line_content(self.set_line_content, self.set_line_head)
                mark.square_paragraph()
                mark.paragraph(self.set_first_para, self.set_left)
                mark.paragraph_1()
                mark.paragraph_2()
                mark.mark_paragraph()
                mark.set_mark_text()
                mark.set_mark_head_abt()
                mark.set_mark_line_wrong()
                marking_abt = mark.get_mark_img()
                arr_img_output.append(marking_abt)
                # cv2.imwrite('300.png', marking_abt)
            elif self.set_mark == 4:
                # print('Mark Abe')
                name = 'Abstract-english'
                mark.square_paragraph()
                mark.set_mark_number(self.set_number_top, set_right_number)
                mark.set_text(self.set_heading_eng, self.set_content_eng)
                mark.set_line_head_abt(self.set_left, set_margin_right)
                mark.set_line_content(self.set_line_content, self.set_line_head)
                mark.square_paragraph()
                mark.paragraph(self.set_first_para, self.set_left)
                mark.paragraph_1()
                mark.paragraph_2()
                mark.mark_paragraph()
                mark.set_mark_text()
                mark.set_mark_head_abt()
                mark.set_mark_line_wrong()
                marking_abe = mark.get_mark_img()
                arr_img_output.append(marking_abe)
            elif self.set_mark == 5:
                # print('Mark Ack')
                name = 'Acknowledgements'
                mark.square_paragraph()
                mark.set_mark_number(self.set_number_top, set_right_number)
                mark.set_text(self.set_heading, self.set_content)
                mark.set_mark_text()
                mark.set_line_content(self.set_line_content, self.set_line_head)
                mark.square_paragraph()
                mark.paragraph(self.set_first_para, self.set_left)
                mark.paragraph_1()
                mark.paragraph_2()
                mark.mark_paragraph()
                mark.set_mark_line_wrong()
                mark_ack = mark.get_mark_img()
                arr_img_output.append(mark_ack)
                # cv2.imwrite('500.png', mark_ack)
            elif self.set_mark == 6:
                # print('Mark Table')
                name = 'Table-of-contents'
                mark.square_paragraph()
                mark.set_mark_number(self.set_number_top, set_right_number)
                mark.set_text(self.set_heading, self.set_content)
                mark.set_line_content(self.set_line_content, self.set_line_head)
                mark.square_paragraph()
                mark.paragraph(self.set_first_para, self.set_left)
                mark.paragraph_1()
                mark.paragraph_2()
                mark.mark_paragraph()
                mark.set_mark_text()
                mark.set_mark_line_wrong()
                mark_table = mark.get_mark_img()
                arr_img_output.append(mark_table)
                # cv2.imwrite('600.png', mark_table)
            elif self.set_mark == 7:
                # print('.....................................................................', c)
                # print('Mark Content')
                name = 'Chapter1-5'
                mark.square_paragraph()
                mark.set_mark_number(self.set_number_top, set_right_number)
                mark.set_text(self.set_heading, self.set_content)
                mark.set_category_table_img()
                mark.set_check_center_head(self.set_left, set_margin_right)
                mark.set_line_content(self.set_line_content, self.set_line_head)
                mark.set_check_point_img(self.set_point, self.set_left, set_margin_right)
                mark.set_check_img_explanation(self.set_explanation, self.set_left, set_margin_right)
                mark.set_check_table_explanation(self.set_table, self.set_left, set_margin_right)
                mark.not_number_heading(c, self.set_mark)
                mark.paragraph(self.set_first_para, self.set_left)
                mark.paragraph_1()
                mark.paragraph_2()
                mark.mark_paragraph()
                mark.set_mark_head()
                mark.set_mark_line_wrong()
                mark.set_mark_point_img()
                mark.set_mark_img_explanation()
                mark.set_mark_table()
                mark.set_mark_text()
                mark_content = mark.get_mark_img()
                arr_img_output.append(mark_content)
            elif self.set_mark == 8:
                # print('Mark Bibliography')
                name = 'Bibliography'
                mark.square_paragraph()
                mark.set_text(self.set_heading, self.set_content)
                mark.set_check_center_head(self.set_left, set_margin_right)
                mark.set_line_content(self.set_line_content, self.set_line_head)
                mark.set_mark_head()
                mark.set_mark_text()
                mark.set_mark_line_wrong()
                mark_bibliography = mark.get_mark_img()
                arr_img_output.append(mark_bibliography)
            elif self.set_mark == 9:
                # print('Mark Appendix')
                name = 'Appendix'
                mark.square_paragraph()
                mark.set_mark_number(self.set_number_top, set_right_number)
                mark.set_text(self.set_heading, self.set_content)
                mark.set_category_table_img()
                mark.set_check_center_head(self.set_left, set_margin_right)
                mark.set_line_content(self.set_line_content, self.set_line_head)
                mark.set_check_point_img(self.set_point, self.set_left, set_margin_right)
                mark.set_check_img_explanation(self.set_explanation, self.set_left, set_margin_right)
                mark.set_check_table_explanation(self.set_table, self.set_left, set_margin_right)
                mark.square_paragraph()
                mark.paragraph(self.set_first_para, self.set_left)
                mark.paragraph_1()
                mark.paragraph_2()
                mark.mark_paragraph()
                mark.set_mark_head()
                mark.set_mark_line_wrong()
                mark.set_mark_point_img()
                mark.set_mark_img_explanation()
                mark.set_mark_table()
                mark.set_mark_text()
                mark_appendix = mark.get_mark_img()
                arr_img_output.append(mark_appendix)
                # print('..........................................................................',c)
            elif self.set_mark == 10:
                # print('Provider-history')
                name = 'Provider-history'
                mark.square_paragraph()
                mark.set_mark_number(self.set_number_top, set_right_number)
                mark.set_text(self.set_heading, self.set_content)
                mark.set_check_center_head(self.set_left, set_margin_right)
                mark.set_mark_head()
                mark.set_mark_text()
                mark_history = mark.get_mark_img()
                arr_img_output.append(mark_history)

        convert.set_png_to_pdf(arr_img_output, name, self.path_to_save)

for arg in sys.argv:
    func = sys.argv[2]
    top = sys.argv[3]
    bottom = sys.argv[4]
    left = sys.argv[5]
    right = sys.argv[6]
    heading = sys.argv[7]
    content = sys.argv[8]
    fist = sys.argv[9]
    line = sys.argv[10]
    image_point = sys.argv[11]
    image_explanation = sys.argv[12]
    table = sys.argv[13]
    numpagetop = sys.argv[14]
    numpagebottom = sys.argv[15]
    symbol_w = sys.argv[16]
    symbol_h = sys.argv[17]
    
print('Start')
send_to_mark_table = SendValue(func, top, bottom, left, right, heading,
                             content, fist, line, image_point, image_explanation, 
                             table, numpagetop, numpagebottom, symbol_w, symbol_h, 0)
send_to_mark_table.set_marking_sum()