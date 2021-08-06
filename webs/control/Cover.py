
from Main_format import MainFormat
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import Sub_function


class Cover(MainFormat):

    def __init__(self, img):
        MainFormat.__init__(self, img)
        self.w_symbol = ''
        self.h_symbol = ''
        self.img_cover = ''
        self.category = []
        self.wrong_w = ''
        self.wrong_h = ''
        self.not_symbol = ''
        self.check_point = []
        self.set_check_point_cover = ''
        self.lines_equal_wrong = []

    def img_symbol(self, set_top, set_left, set_right, set_symbol_w, set_symbol_h):
        u_size = np.size(self.arr_uppers)
        for s in range(u_size):
            symbol = self.arr_lowers[s] - self.arr_uppers[s]
            if symbol > 100:
                img_symbol = self.img[self.arr_uppers[s]:self.arr_lowers[s], set_left:set_right]
                h, w = img_symbol.shape[:2]
                img_w_sym = round(int(w) / 2)
                set_w_sym = round((float(set_symbol_w) * 300) / 2)
                draw_sym = round(img_w_sym - set_w_sym)
                w_sym = round(float(set_symbol_w) * 300)
                h_sym = round(float(set_symbol_h) * 300)
                cv2.rectangle(self.clone_img, (int(set_left) + draw_sym, int(set_top)),
                              (int(set_left) + draw_sym + int(w_sym), int(set_top) + int(h_sym)), (0, 0, 255), 2)
                self.w_symbol = Sub_function.w_img(img_symbol)
                self.h_symbol = Sub_function.h_img(img_symbol)
                break
            else:
                self.not_symbol = 1
                self.w_symbol = ''
                self.h_symbol = ''

        if self.w_symbol != '':
            if float(self.w_symbol) != float(set_symbol_w):
                self.wrong_w = 1
            if float(self.h_symbol) != float(set_symbol_h):
                self.wrong_h = 1

    def set_text(self, text_heading, text_content):
        u_size = np.size(self.arr_size_text)
        # print('Text 20 :', text_heading)
        # print('Text 16 :', text_content)

        for x in range(u_size):
            # arr_sum = self.arr_size_text[x]
            # head_size = text_heading - arr_sum
            # content_size = text_content - arr_sum
            if x == 0:
                if self.arr_size_text[x] < 100:
                    if int(self.arr_x[x]) < 1500:
                        if (text_heading - self.arr_size_text[x]) >= -2 and (text_heading - self.arr_size_text[x]) <= 2:
                            # print('number1 :', text_heading - self.arr_size_text[x])
                            con = 2
                            self.category.append(con)
                        else:
                            # print('number2 :', text_heading - self.arr_size_text[x])
                            self.category.append(self.arr_uppers[x])
                    elif int(self.arr_x[x]) > 1500:
                        if (text_content - (self.lowers[x] - self.uppers[x])) >= -11 and (
                                text_content - (self.lowers[x] - self.uppers[x])) <= 11:
                            # print('number1.1 :', text_content - self.arr_size_text[x])
                            con = 1
                            self.category.append(con)
                        else:
                            # print('number2.1 :', text_content - self.arr_size_text[x])
                            self.category.append(self.arr_uppers[x])
                elif self.arr_size_text[x] > 100:
                    con = 0
                    self.category.append(con)
            # elif content_size >= -2 and content_size <= 2:
            elif (text_content - self.arr_size_text[x]) >= -2 and (text_content - self.arr_size_text[x]) <= 2:
                con = 1
                self.category.append(con)
            # elif head_size >= -2 and head_size <= 2:
            elif (text_heading - self.arr_size_text[x]) >= -2 and (text_heading - self.arr_size_text[x]) <= 2:
                head = 2
                self.category.append(head)
            # elif arr_sum > 100:
            elif self.arr_size_text[x] > 100:
                img_num = 3
                self.category.append(img_num)
            else:
                self.category.append(self.arr_uppers[x])
        # print(self.category)

    def set_check_point(self, set_left, set_margin_right):
        c_size = np.size(self.arr_uppers)
        for c in range(c_size):
            img_point = self.img[self.arr_uppers[c]:self.arr_lowers[c], set_left:set_margin_right]
            center_cover = Sub_function.img_point_center(img_point)
            if center_cover < -10 or center_cover > 10:
                print(self.arr_uppers[c])
                self.check_point.append(self.arr_uppers[c])

    def set_line_equal(self):
        point_line_spacing = []
        lines_spacing = []
        line_set_size_up = np.size(self.arr_uppers)
        for i in range(line_set_size_up):
            if i + 1 < line_set_size_up:
                point_line = self.arr_lowers[i] - self.arr_uppers[i + 1]
                if abs(point_line) > 300:
                    lines_spacing.append(self.arr_lowers[i])
                    point_line_spacing.append(abs(point_line))

        line_spacing_check = np.size(point_line_spacing)
        for j in range(line_spacing_check):
            if j + 1 < line_spacing_check:
                point_line2 = point_line_spacing[j] - point_line_spacing[j + 1]
                if point_line2 < -50 or point_line2 > 50:
                    self.lines_equal_wrong = lines_spacing
                    # print('value line spacing1', point_line2)
                    # print('value line spacing2', self.lines_equal_wrong)

    def set_mark_symbol(self):
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        if len(self.arr_x) >= 2:
            if self.not_symbol == 1:
                # cv2.putText(self.clone_img, 'Symbol not found.',
                # (1500, 450), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                draw.text((1500, 450), "ไม่พบตราสัญลักษณ์", font=font, fill=(255, 0, 0, 0))
            if self.wrong_w == 1:
                # cv2.putText(self.clone_img, 'Wrong image width.', (self.arr_x[0] + 10, self.arr_lowers[0] + 50),
                # self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                draw.text((self.arr_x[0] - 20, self.arr_lowers[0] + 50), "ความกว้างรูปตราสัญลักษณ์ผิด", font=font, fill=(255, 0, 0, 0))
            if self.wrong_h == 1:
                draw.text((1550, 750), "ความสูงรูปตราสัญลักษณ์ผิด", font=font, fill=(255, 0, 0, 0))
                # cv2.line(self.clone_img, (self.arr_x_w[0] + 30, self.arr_uppers[0] + 5),
                # (self.arr_x_w[0] + 30, self.arr_lowers[0] - 10), (255, 0, 0), 2)
                # cv2.line(self.clone_img, (self.arr_x_w[0] + 10,
                # self.arr_uppers[0] + 5), (self.arr_x_w[0] + 50, self.arr_uppers[0] + 5), (255, 0, 0), 2)
                # cv2.line(self.clone_img, (self.arr_x_w[0] + 10, self.arr_lowers[0] - 10),
                # (self.arr_x_w[0] + 50, self.arr_lowers[0] - 10), (255, 0, 0), 2)
                # cv2.putText(self.clone_img, 'Wrong image height.', (1550, 750), self.font, 1, (255, 0, 0), 2,
                # cv2.LINE_AA);
        self.clone_img = np.array(p_img)

    def set_mark_text(self):
        wrong_size = np.size(self.category)
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        for w in range(wrong_size):
            if self.category[w] > 10:
                draw.text((2200, self.category[w]), "ขนาดตัวอักษรผิด", font=font, fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, '* ', (400, self.category[w] + 30),
                # self.font, 2, (255, 0, 0), 2, cv2.LINE_AA);
                # cv2.putText(self.clone_img, '* = Wrong text size ',
                # (100, 3400), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                # draw.text((100, 3400), "* คือ ขนาดตัวอักษรผิด", font=font, fill=(255, 0, 0, 0))
        self.clone_img = np.array(p_img)

    def set_mark_point(self):
        wrong_point = np.size(self.check_point)
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        for p in range(wrong_point):
            draw.text((300, self.check_point[p]), "เนื้อหาต้องจัดกลาง", font=font, fill=(255, 0, 0, 0))
            # cv2.putText(self.clone_img, '+', (2250, self.check_point[p] + 50),
            # self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
            # cv2.putText(self.clone_img, '+ = Wrong not center.',
            # (100, 3300), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
            # draw.text((100, 3300), "+ คือ เนื้อหาต้องจัดกลาง", font=font, fill=(255, 0, 0, 0))
        self.clone_img = np.array(p_img)

    def set_mark_lines_equal(self):
        lines_equal = np.size(self.lines_equal_wrong)
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        for l_equal in range(lines_equal):
            draw.text((1420, self.lines_equal_wrong[l_equal] + 300), "ระยะห่างระหว่างบรรทัดไม่เท่ากัน", font=font, fill=(255, 0, 0, 0))
            # cv2.line(self.clone_img, (1400, self.lines_equal_wrong[l_equal] + 100),
            # (1400, self.lines_equal_wrong[l_equal] + 500), (255, 0, 0), 2)
            # cv2.line(self.clone_img, (1350, self.lines_equal_wrong[l_equal] + 100),
            # (1450, self.lines_equal_wrong[l_equal] + 100), (255, 0, 0), 2)
            # cv2.line(self.clone_img, (1350, self.lines_equal_wrong[l_equal] + 500),
            # (1450, self.lines_equal_wrong[l_equal] + 500), (255, 0, 0), 2)
            # cv2.putText(self.clone_img, 'Line spacing is not equal.', (1420, self.lines_equal_wrong[l_equal] + 300),
            # self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
            # cv2.putText(self.clone_img, '<|>', (1400, self.lines_equal_wrong[l_equal] + 230), self.font, 1,
            # (255, 0, 0), 2, cv2.LINE_AA);
            # cv2.putText(self.clone_img, '<|> = Line spacing is not equal.', (1400, 3480), self.font, 1,
            # (255, 0, 0), 2, cv2.LINE_AA);
        self.clone_img = np.array(p_img)



