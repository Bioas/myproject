
from Cover import Cover
import Sub_function
import numpy as np
from PIL import ImageFont, ImageDraw, Image


class Thesis(Cover):
    def __init__(self, img):
        Cover.__init__(self, img)
        self.center_symbol = 0
        self.center_head = 0
        self.center_content = 0
        self.line_wrong = []

    def set_symbol_center(self, set_left, set_margin_right):
        # print('symbol')
        s_size = np.size(self.arr_uppers)
        for s in range(s_size):
            sum_symbol = self.arr_lowers[s] - self.arr_uppers[s]
            if sum_symbol > 100:
                # print('1')
                center_symbol_head = self.img[self.arr_uppers[s]:self.arr_lowers[s], set_left:set_margin_right]
                center_value = Sub_function.img_point_center(center_symbol_head)
                # print('c1 :', center_value)
                if center_value < -10 or center_value > 10:
                    self.center_symbol = self.arr_uppers[s]
                    # print('center symbol', self.center_head)
                break
            else:
                self.center_symbol = ''
                break

    def set_head_content_center(self, set_left, set_margin_right):
        h_size = np.size(self.category)
        # print(h_size)
        # print('2')
        for h in range(h_size):
            if self.category[h] == 2:
                # print('2.1')
                center_head = self.img[self.arr_uppers[h]:self.arr_lowers[h], set_left:set_margin_right]
                center_value_head = Sub_function.img_point_center(center_head)
                # print('c2 :', center_value_head)
                if center_value_head < -10 or center_value_head > 10:
                    self.center_head = self.arr_uppers[h]
                if self.category[h + 1] == 1:
                    center_content = self.img[self.arr_uppers[h + 1]:self.arr_lowers[h + 1], set_left:set_margin_right]
                    center_value_content = Sub_function.img_point_center(center_content)
                    # print('c3 :', center_value_content)
                    if center_value_content < -1 or center_value_content > 1:
                        self.center_content = self.arr_uppers[h + 1]
                else:
                    self.center_content = 0
                break

    def set_line_content(self, line_con, line_head):
        # print(self.arr_size_text)
        # print('..................', line_con)
        # print('..................', line_head)
        c_size = np.size(self.category)
        for i in range(1, c_size):
            if i + 1 < c_size:
                if int(self.category[i]) == 1:
                    a_line = self.arr_lowers[i] - self.arr_uppers[i + 1]
                    # print('a line :', a_line)
                    if abs(a_line) > 35:
                        sum_line_value = line_con - abs(a_line)
                        if sum_line_value < -10 or sum_line_value > 10:
                            # print('5555', sum_line_value, self.arr_lowers[i])
                            self.line_wrong.append(self.arr_lowers[i])

                elif int(self.category[i]) == 2 and int(self.category[i + 1]) == 2:
                    a_line_1 = self.arr_lowers[i] - self.arr_uppers[i + 1]
                    sum_line_value_1 = line_con - abs(a_line_1)
                    if sum_line_value_1 < -20 or sum_line_value_1 > 20:
                        # print('6666', sum_line_value_1, self.arr_lowers[i])
                        self.line_wrong.append(self.arr_lowers[i])

                elif (self.category[i]) == 2 and int(self.category[i + 1]) == 1:
                    a_line_2 = self.arr_lowers[i] - self.arr_uppers[i + 1]
                    sum_line_value_2 = line_head - abs(a_line_2)
                    if sum_line_value_2 < -10 or sum_line_value_2 > 10:
                        # print('6666', sum_line_value_2, self.arr_lowers[i])
                        self.line_wrong.append(self.arr_lowers[i])
        # print('line :', self.line_wrong)

    def set_mark_symbol_thesis(self):
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        if self.center_symbol == '':
            draw.text((1500, 500), "ไม่พบตราสัญลักษณ์", font=font, fill=(255, 0, 0, 0))
            # cv2.putText(self.clone_img, 'Logo not found',
            # (1500, 500), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
        elif self.center_symbol != 0:
            # cv2.putText(self.clone_img, '+Logo', (1000, self.center_symbol),
            # self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
            # cv2.putText(self.clone_img, 'Wrong logo not center.',
            # (1400, self.center_symbol), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
            draw.text((1400, self.center_symbol), "ตราสัญลักษณ์ต้องจัดกลาง", font=font, fill=(255, 0, 0, 0))
        self.clone_img = np.array(p_img)

    def set_mark_head_thesis(self):
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        if self.center_head != 0:
            draw.text((1400, self.center_head), "หัวข้อต้องจัดกลาง", font=font, fill=(255, 0, 0, 0))
            # cv2.putText(self.clone_img, '+H', (600, self.center_head), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
            # cv2.putText(self.clone_img, 'Wrong title not center.',
            # (1400, self.center_head + 40), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
        self.clone_img = np.array(p_img)

    def set_mark_content_thesis(self):
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        if self.center_content != 0:
            # cv2.putText(self.clone_img, '+CH', (450, self.center_content), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
            # cv2.putText(self.clone_img, 'Wrong content not center.', (1400,
            # self.center_content), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
            draw.text((1400, self.center_content), "หัวข้อต้องจัดกลาง", font=font, fill=(255, 0, 0, 0))
        self.clone_img = np.array(p_img)

    def set_mark_line_wrong(self):
        l_size = np.size(self.line_wrong)
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        for l in range(l_size):
            # cv2.putText(self.clone_img, '| ', (2330, self.line_wrong[l] + 40),
            # self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
            # cv2.putText(self.clone_img, 'Wrong line spacing ',
            # (1000, self.line_wrong[l] + 40), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
            draw.text((1000, self.line_wrong[l] + 40), "ระยะห่างบรรทัดมากเกินไป", font=font, fill=(255, 0, 0, 0))
        self.clone_img = np.array(p_img)

