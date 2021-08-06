from Cover import Cover
import Sub_function
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


class Content(Cover):

    def __init__(self, img):
        Cover.__init__(self, img)
        self.category_table_img = []
        self.not_head_center = []
        self.check_table = 0
        self.arr_point_table = []
        self.check_img = 0
        self.arr_point_img_explanation = []
        self.check_img_point = 0
        self.arr_point_img = []

    def set_check_center_head(self, set_left, set_margin_right):
        u_size = np.size(self.category)
        for u in range(u_size):
            if u + 1 < u_size:
                if self.category[u] == 2:
                    center_head_1 = self.img[self.arr_uppers[u]:self.arr_lowers[u], set_left:set_margin_right]
                    center_value_head = Sub_function.img_point_center(center_head_1)
                    # print('H :', center_value_head)
                    if center_value_head < -10 or center_value_head > 10:
                        self.not_head_center.append(self.arr_uppers[u])

    def set_category_table_img(self):
        ti_size = np.size(self.arr_size_text)
        # print('ก่อนตาราง', self.arr_size_text)
        for s in range(ti_size):
            if self.arr_size_text[s] < 100:
                find_not = 0
                self.category_table_img.append(find_not)
            elif self.arr_size_text[s] > 100:
                h, w = self.img.shape[:2]
                img = self.img[self.arr_uppers[s]:self.arr_lowers[s], 0:w]
                height, width = img.shape[:2]
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
                pts = cv2.findNonZero(threshed)
                ret = cv2.boundingRect(pts)
                cx, cy, w, h = ret
                M = cv2.getRotationMatrix2D((cx, cy), 0, 1.0)
                rotated = cv2.warpAffine(threshed, M, (img.shape[1], img.shape[0]))
                hist = cv2.reduce(rotated, 1, cv2.REDUCE_SUM, dtype=cv2.CV_32S)
                max01 = max(hist)
                count = 0
                for a in range(height):
                    if hist[a] == max01:
                        count += 1
                # print('......................................................................................', s)
                # print('count', count)
                # print('......................................................................................')
                if count <= 9:
                    img_1 = 4
                    self.category_table_img.append(img_1)
                elif count >= 10:
                    # img_3 = self.img[self.arr_uppers[s]:self.arr_lowers[s], set_left:set_right]
                    # l1, c1, r1 = Sub_function.check_point(img_3)
                    # print('ค่าซ้ายตาราง :', l1)
                    # print('ค่าซ้ายตาราง :', c1)
                    # print('ค่าซ้ายตาราง :', r1)
                    # if l1 == 0 or l1 == 1 or l1 == 2:
                    table = 3
                    self.category_table_img.append(table)
                    # else:
                    # img_12 = 4
                    # self.category_table_img.append(img_12)
        # print('ประเภทตาราง', self.category_table_img)

    def set_check_table_explanation(self, set_point, set_left, set_margin_right):
        self.check_table = int(set_point)
        c_size = np.size(self.arr_uppers)
        for c_list in range(c_size):
            if c_list <= c_size:
                if int(self.category_table_img[c_list]) == 3:
                    t_up = self.arr_uppers[c_list - 1]
                    t_lo = self.arr_lowers[c_list - 1]
                    img_point = self.img[t_up:t_lo, set_left:set_margin_right]
                    l, c, r = Sub_function.check_point(img_point)
                    if self.check_table == 1:
                        if l > 5:
                            self.arr_point_table.append(t_up)
                    elif self.check_table == 2:
                        if c < -5 or c > 5:
                            self.arr_point_table.append(t_up)
                    elif self.check_table == 3:
                        if r != set_margin_right:
                            self.arr_point_table.append(t_up)

                    # print('l', l)
                    # print('c', c)
                    # print('r', r)
        # print('table arr', self.arr_point_table)

    def set_check_img_explanation(self, set_point, set_left, set_margin_right):
        # print('img........................img')
        self.check_img = int(set_point)
        c_size = np.size(self.arr_uppers)
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        for c in range(c_size):
            if c + 1 <= c_size:
                if int(self.category_table_img[c]) == 4:
                    if c + 1 != c_size:
                        up_p = self.arr_uppers[c + 1]
                        lo_p = self.arr_lowers[c + 1]
                        img_point = self.img[up_p:lo_p, set_left:set_margin_right]
                        l, c, r = Sub_function.check_point(img_point)
                        # print('l img', l)
                        # print('c img', c)
                        # print('r img', r)
                        if self.check_img == 1:
                            if l > 5:
                                self.arr_point_img_explanation.append(up_p)
                        elif self.check_img == 2:
                            if c < -5 or c > 5:
                                self.arr_point_img_explanation.append(up_p)
                        elif self.check_img == 3:
                            if r != set_margin_right:
                                self.arr_point_img_explanation.append(up_p)
                    elif c + 1 == c_size:
                        draw.text((1700, self.arr_lowers[c] + 30), "ต้องมีคำอธิบายรูปภาพ", font=font,
                                  fill=(255, 0, 0, 0))
                        # cv2.putText(self.clone_img, 'Not found explanation image.',
                        # (1700, self.arr_lowers[c] + 30), self.font, 1, (255, 0, 0), 2,
                        # cv2.LINE_AA);
        self.clone_img = np.array(p_img)
        # print('arr img exp', self.arr_point_img_explanation)

    def set_check_point_img(self, set_point, set_left, set_margin_right):
        self.check_img_point = int(set_point)
        i_size = np.size(self.arr_uppers)
        for i in range(i_size):
            if i + 1 < i_size:
                if int(self.category_table_img[i]) == 4:
                    up_i = self.arr_uppers[i]
                    lo_i = self.arr_lowers[i]
                    img_point = self.img[up_i:lo_i, set_left:set_margin_right]
                    l, c, r = Sub_function.check_point(img_point)
                    if self.check_img_point == 1:
                        if l > 7:
                            self.arr_point_img.append(up_i)
                    elif self.check_img_point == 2:
                        if c < -5 or c > 5:
                            self.arr_point_img.append(up_i)
                    elif self.check_img_point == 3:
                        if r != set_margin_right:
                            self.arr_point_img.append(up_i)
                    # print('l img_point', l)
                    # print('c img_point', c)
                    # print('r img_point', r)
        # print('a l', self.arr_point_img)

    def set_mark_table(self):
        t_size = np.size(self.arr_point_table)
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        if self.check_table == 1:
            for l in range(t_size):
                draw.text((1600, self.arr_point_table[l] - 30), "คำอธิบายตารางต้องจัดชิดซ้าย", font=font, fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, 'Wrong explanation table not left.',
                # (1600, self.arr_point_table[t] - 30), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                # cv2.putText(self.clone_img, '*TL* = Wrong explanation table not left.',
                # (1800, 3400), self.font, 1, (255, 0, 0), 2,
                # cv2.LINE_AA);
        elif self.check_table == 2:
            for c in range(t_size):
                draw.text((1600, self.arr_point_table[c] - 30), "คำอธิบายตารางต้องจัดกึ่งกลาง", font=font, fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, 'Wrong explanation table not center.',
                # (1600, self.arr_point_table[t] - 30), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                # cv2.putText(self.clone_img, '*TC* = Wrong explanation table not center.',
                # (1800, 3400), self.font, 1, (255, 0, 0), 2,
                # cv2.LINE_AA);
        elif self.check_table == 3:
            for r in range(t_size):
                draw.text((1600, self.arr_point_table[r] - 30), "คำอธิบายตารางต้องจัดชิดขวา", font=font, fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, 'Wrong explanation table not right.',
                # (1600, self.arr_point_table[t] - 30), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                # cv2.putText(self.clone_img, '*TR* = Wrong explanation table not right.',
                # (1800, 3400), self.font, 1, (255, 0, 0), 2,
                # cv2.LINE_AA);
        self.clone_img = np.array(p_img)

    def set_mark_img_explanation(self):
        # print('img_explanation :', self.arr_point_img_explanation)
        ex_size = np.size(self.arr_point_img_explanation)
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        if self.check_img == 1:
            for l in range(ex_size):
                draw.text((1700, self.arr_point_img_explanation[l] - 20), "คำอธิบายรูปภาพต้องจัดชิดซ้าย", font=font,
                          fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, 'Wrong explanation image not left.',
                # (1700, self.arr_point_img_explanation[t] - 15), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                # cv2.putText(self.clone_img, '*eL* = Wrong explanation not left.',
                # (1800, 3350), self.font, 1, (255, 0, 0), 2,
                # cv2.LINE_AA);
        elif self.check_img == 2:
            for c in range(ex_size):
                draw.text((1700, self.arr_point_img_explanation[c] - 20), "คำอธิบายรูปภาพต้องจัดกึ่งกลาง", font=font,
                          fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, 'Wrong explanation image not center.',
                # (1700, self.arr_point_img_explanation[t] - 15), self.font, 1,
                # (255, 0, 0), 2, cv2.LINE_AA);
                # cv2.putText(self.clone_img, '*eC* = Wrong explanation not center.',
                # (1800, 3350), self.font, 1, (255, 0, 0), 2,
                # cv2.LINE_AA);
        elif self.check_img == 3:
            for r in range(ex_size):
                draw.text((1700, self.arr_point_img_explanation[r] - 20), "คำอธิบายรูปภาพต้องจัดชิดขวา", font=font,
                          fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, 'Wrong explanation image not right.',
                # (1700, self.arr_point_img_explanation[t] - 15),
                # self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                # cv2.putText(self.clone_img, '*eR* = Wrong explanation not right.',
                # (1800, 3350), self.font, 1, (255, 0, 0), 2,
                # cv2.LINE_AA);
        self.clone_img = np.array(p_img)

    def set_mark_point_img(self):
        # print('img_ :', self.arr_point_img)
        ei_size = np.size(self.arr_point_img)
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        if self.check_img_point == 1:
            for l in range(ei_size):
                draw.text((1700, self.arr_point_img[l] + 50), "รูปภาพต้องจัดชิดขวา", font=font,
                          fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, 'Wrong point image not left.',
                # (1500, self.arr_point_img[t] + 50), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                # cv2.putText(self.clone_img, '*iL* = Wrong point image not left.', (1800, 3300), self.font, 1,
                # (255, 0, 0), 2, cv2.LINE_AA);
        elif self.check_img_point == 2:
            for c in range(ei_size):
                draw.text((1700, self.arr_point_img[c] + 50), "รูปภาพต้องจัดกึ่งกลาง", font=font,
                          fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, 'Wrong point image not center.',
                # (1500, self.arr_point_img[t] + 50), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                # cv2.putText(self.clone_img, '*iC* = Wrong point image not center.', (1800, 3300), self.font, 1,
                # (255, 0, 0), 2, cv2.LINE_AA);
        elif self.check_img_point == 3:
            for r in range(ei_size):
                draw.text((1700, self.arr_point_img[r] + 50), "รูปภาพต้องจัดชิดขวา", font=font,
                          fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, 'Wrong point image not right.',
                # (1500, self.arr_point_img[t] + 50), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                # cv2.putText(self.clone_img, '*iR* = Wrong point image not right.', (1800, 3300), self.font, 1,
                # (255, 0, 0), 2, cv2.LINE_AA);
        self.clone_img = np.array(p_img)

    def set_mark_head(self):
        h_size = np.size(self.not_head_center)
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        # print('m h :', self.not_head_center)
        for h in range(h_size):
            draw.text((1700, self.not_head_center[h] + 30), "หัวข้อต้องจัดกลาง", font=font,
                      fill=(255, 0, 0, 0))
            # cv2.putText(self.clone_img, 'Wrong head not center.',
            # (1700, self.not_head_center[h] + 30), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
            # cv2.putText(self.clone_img, '+H = Wrong head not center.',
            # (100, 3200), self.font, 1, (255, 0, 0), 2,
            # cv2.LINE_AA);
        self.clone_img = np.array(p_img)
