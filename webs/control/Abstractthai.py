
from Thesis_certificate import Thesis
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import Sub_function


class Abt(Thesis):
    def __init__(self, img):
        Thesis.__init__(self, img)
        self.head = []

        self.arr_para_1 = []
        self.arr_para_2 = []
        self.arr_point = []
        self.arr_point2 = []
        self.arr_point_1 = []
        self.arr_point1 = []
        self.arr_point1_1 = []
        self.arr_point2_1 = []

    def not_number_heading(self, loop_c, select_check):
        loop = int(loop_c)
        sc = int(select_check)
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        if len(self.arr_x_w) >= 2:
            if sc == 7:
                if loop == 0:
                    if int(self.arr_x_w[0]) - int(self.arr_x[0]) < 100:
                        draw.text((2200, 220), "หน้านี้ไม่ต้องใส่เลขหน้า", font=font, fill=(255, 0, 0, 0))

                        # cv2.putText(self.clone_img, 'page not number.',
                        # (2200, 220), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
        self.clone_img = np.array(p_img)

    def paragraph(self, paragraph, margin):
        paragraph = int(paragraph)
        margin = int(margin)
        u_check = np.size(self.arr_uppers)
        for o in range(u_check):
            if o - 1 < u_check:
                if  self.arr_x[o] > (paragraph+margin)-5 and self.arr_x[o] < (paragraph+margin) +5 :
                    if self.arr_lowers[o-1] - self.arr_uppers[o-1] < 100 and self.arr_lowers[o] - self.arr_uppers[o] < 100:
                        if o+1 < u_check:
                            self.arr_point.append(o)
                            white_pixels = np.array(np.where(self.rotated[self.arr_lowers[o]] == 255))
                            w_dist = 0
                            for ww in range(0, np.size(white_pixels)):
                                if ww + 1 < np.size(white_pixels):
                                    jj = white_pixels[:, ww + 1] - white_pixels[:, ww]
                                    if jj >= 20:
                                        w_dist = white_pixels[:, ww]
                                        img1 = self.img[self.arr_uppers[o]:self.arr_lowers[o], w_dist[0] + 15:2481]
                                        gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                                        th, threshed = cv2.threshold(gray, 127, 255,
                                                                     cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
                                        pts = cv2.findNonZero(threshed)
                                        x, y, w, h = cv2.boundingRect(pts);
                                        self.arr_para_1.append(w_dist[0] + 15 + x)
                                        break
                elif  self.arr_x[o] < (paragraph+margin)-5 and self.arr_x[o] > margin+20:
                    if self.arr_lowers[o-1] - self.arr_uppers[o-1] < 100 and self.arr_lowers[o] - self.arr_uppers[o] < 100:
                        self.arr_point_1.append(self.arr_uppers[o])

    def paragraph_1(self):
        u_size_a = np.size(self.arr_uppers)
        size_point = np.size(self.arr_point)
        if size_point != 0:
            for p in range(size_point):
                if size_point == 1:
                    for a in range(u_size_a):
                        if self.arr_x[a] > self.arr_x[int(self.arr_point[p])] and a > int(self.arr_point[p]):
                            if self.arr_lowers[a - 1] - self.arr_uppers[a - 1] < 100 and self.arr_lowers[a] - self.arr_uppers[a] < 100:
                                x_1 = self.arr_x[a] - self.arr_para_1[p]
                                if abs(x_1) >= -5 and (x_1) <= 15:
                                    # print("ย่อหน้าแรกถูก4444", a)
                                    self.arr_point1.append(a)
                                    white_pixels = np.array(np.where(self.rotated[self.arr_lowers[a]] == 255))
                                    w_dist = 0
                                    for ww in range(0, np.size(white_pixels)):
                                        if ww + 1 < np.size(white_pixels):
                                            jj = white_pixels[:, ww + 1] - white_pixels[:, ww]
                                            if jj >= 20:
                                                w_dist = white_pixels[:, ww]
                                                img1 = self.img[self.arr_uppers[a]:self.arr_lowers[a],
                                                       w_dist[0] + 15:2481]
                                                gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                                                th, threshed = cv2.threshold(gray, 127, 255,
                                                                             cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
                                                pts = cv2.findNonZero(threshed)
                                                x, y, w, h = cv2.boundingRect(pts);
                                                self.arr_para_2.append(w_dist[0] + 15 + x)
                                                break
                                elif abs(x_1) >= 15 and abs(x_1) <= 40:
                                    # print("ย่อหน้าแรกผิด", a)
                                    self.arr_point1_1.append(self.arr_uppers[a])
                elif size_point > 1:
                    if p+1 < size_point:
                        for l in range(self.arr_point[p], self.arr_point[p + 1]):
                            if self.arr_x[l] > self.arr_x[int(self.arr_point[p])]and l > int(self.arr_point[p]) and l < int(self.arr_point[p + 1]):
                                if self.arr_lowers[l - 1] - self.arr_uppers[l - 1] < 100 and self.arr_lowers[l] - self.arr_uppers[l] < 100:
                                    x_1 = self.arr_x[l] - self.arr_para_1[p]
                                    if abs(x_1) >= -5 and abs(x_1) <= 15:
                                        # print("ย่อหน้าแรกถูก666", l)
                                        self.arr_point1.append(l)
                                        white_pixels = np.array(np.where(self.rotated[self.arr_lowers[l]] == 255))
                                        w_dist = 0
                                        for ww in range(0, np.size(white_pixels)):
                                            if ww + 1 < np.size(white_pixels):
                                                jj = white_pixels[:, ww + 1] - white_pixels[:, ww]
                                                if jj >= 20:
                                                    w_dist = white_pixels[:, ww]
                                                    img1 = self.img[self.arr_uppers[l]:self.arr_lowers[l],
                                                           w_dist[0] + 15:2481]
                                                    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                                                    th, threshed = cv2.threshold(gray, 127, 255,
                                                                                 cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
                                                    pts = cv2.findNonZero(threshed)
                                                    x, y, w, h = cv2.boundingRect(pts);
                                                    self.arr_para_2.append(w_dist[0] + 15 + x)
                                                    break
                                    elif abs(x_1) >= 15 and abs(x_1) <= 40:
                                        # print("ย่อหน้าแรกผิด", l)
                                        self.arr_point1_1.append(self.arr_uppers[l])

                        for k in range(self.arr_point[size_point - 1], u_size_a):
                            if self.arr_x[k] > self.arr_x[self.arr_point[size_point - 1]]and k > int(self.arr_point[size_point - 1]) and k < u_size_a:
                                if self.arr_lowers[k - 1] - self.arr_uppers[k - 1] < 100 and self.arr_lowers[k] - self.arr_uppers[k] < 100:
                                    x_1 = self.arr_x[k] - self.arr_para_1[size_point - 1]
                                    if abs(x_1) >= -5 and abs(x_1) <= 15:
                                        # print("ย่อหน้าแรกถูก555", k)
                                        self.arr_point1.append(k)
                                        white_pixels = np.array(np.where(self.rotated[self.arr_lowers[k]] == 255))
                                        w_dist = 0
                                        for ww in range(0, np.size(white_pixels)):
                                            if ww + 1 < np.size(white_pixels):
                                                jj = white_pixels[:, ww + 1] - white_pixels[:, ww]
                                                if jj >= 20:
                                                    w_dist = white_pixels[:, ww]
                                                    img1 = self.img[self.arr_uppers[k]:self.arr_lowers[k],
                                                           w_dist[0] + 15:2481]
                                                    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                                                    th, threshed = cv2.threshold(gray, 127, 255,
                                                                                 cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
                                                    pts = cv2.findNonZero(threshed)
                                                    x, y, w, h = cv2.boundingRect(pts);
                                                    self.arr_para_2.append(w_dist[0] + 15 + x)
                                                    break
                                    elif abs(x_1) >= 15 and abs(x_1) <= 40:
                                        # print("ย่อหน้าแรกผิด", k)
                                        self.arr_point1_1.append(self.arr_uppers[k])

    def paragraph_2(self):
        u_size_2 = np.size(self.arr_uppers)
        size_point_2 = np.size(self.arr_point1)
        if size_point_2 != 0:
            for p in range(size_point_2):
                if size_point_2 == 1:
                    for a in range(u_size_2):
                        if self.arr_x[a] > self.arr_x[int(self.arr_point1[p])] and a > int(self.arr_point1[p]):
                            if self.arr_lowers[a - 1] - self.arr_uppers[a - 1] < 100 and self.arr_lowers[a] - self.arr_uppers[a] < 100:
                                x_1 = self.arr_x[a] - self.arr_para_2[p]
                                if abs(x_1) >= -5 and abs(x_1) <= 15:
                                    # print("ย่อหน้าที่ 2 ถูก :", a)
                                    self.arr_point2.append(a)
                                elif abs(x_1) >= 15 and abs(x_1) <= 40:
                                    # print("ย่อหน้าที่ 2 ผิด:", a)
                                    self.arr_point2_1.append(self.arr_uppers[a])
                elif size_point_2 > 1:
                    if p+1 < size_point_2:
                        for l in range(self.arr_point1[p], self.arr_point1[p + 1]):
                            if self.arr_x[l] > self.arr_x[int(self.arr_point1[p])]and l > int(self.arr_point1[p]) and l < int(self.arr_point1[p + 1]):
                                if self.arr_lowers[l - 1] - self.arr_uppers[l - 1] < 100 and self.arr_lowers[l] - self.arr_uppers[l] < 100:
                                    x_1 = self.arr_x[l] - self.arr_para_2[p]
                                    if abs(x_1) >= -5 and abs(x_1) <= 15:
                                        # print("ย่อหน้าที่ 2 ถูก :", l)
                                        self.arr_point2.append(l)
                                    elif abs(x_1) >= 15 and abs(x_1) <= 40:
                                        # print("ย่อหน้าที่ 2 ผิด:", l)
                                        self.arr_point2_1.append(self.arr_uppers[l])
                        for k in range(self.arr_point1[size_point_2 - 1], u_size_2):
                            if self.arr_x[k] > self.arr_x[self.arr_point1[size_point_2 - 1]]and k > int(self.arr_point1[size_point_2 - 1]) and k < u_size_2:
                                if self.arr_lowers[k - 1] - self.arr_uppers[k - 1] < 100 and self.arr_lowers[k] - self.arr_uppers[k] < 100:
                                    x_1 = self.arr_x[k] - self.arr_para_2[size_point_2 - 1]
                                    if abs(x_1) >= -5 and abs(x_1) <= 15:
                                        # print("ย่อหน้าที่ 2 ถูก :", k)
                                        self.arr_point2.append(k)
                                    elif abs(x_1) >= 10 and abs(x_1) <= 40:
                                        # print("ย่อหน้าที่ 2 ผิด:", k)
                                        self.arr_point2_1.append(self.arr_uppers[k])

    def set_line_head_abt(self, set_left, set_margin_right):
        a_size = np.size(self.category)
        for a in range(a_size):
            if a + 1 < a_size:
                if self.category[a] == 2:
                    if self.category[a - 1] == 1 and self.category[a + 1] == 1:
                        center_head = self.img[self.arr_uppers[a]:self.arr_lowers[a], set_left:set_margin_right]
                        center_value_head = Sub_function.img_point_center(center_head)
                        # print('10', center_value_head)
                        if center_value_head < - 10 or center_value_head > 10:
                            self.head.append(self.arr_uppers[a])
                            # print('in', self.head)

    def set_mark_head_abt(self):
        h_size = np.size(self.head)
        # print('m h :', self.head)
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        for h in range(h_size):
            # cv2.putText(self.clone_img, 'Wrong head not center.',
            # (2000, self.head[h]), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
            # cv2.putText(self.clone_img, 'Wrong head not center.',
            # (100, 3300), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
            draw.text((2000, self.head[h]), "หัวข้อต้องจัดกลาง", font=font, fill=(255, 0, 0, 0))
        self.clone_img = np.array(p_img)

    def mark_paragraph(self):
        size_point_1 = np.size(self.arr_point_1)
        size_point1_1 = np.size(self.arr_point1_1)
        size_point2_1 = np.size(self.arr_point2_1)
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        if size_point_1 != 0:
            for a in range(size_point_1):
                # cv2.putText(self.clone_img, 'Wrong first paragraph. ',
                # (200, self.arr_point_1[a]), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                draw.text((200, self.arr_point_1[a]), "ย่อหน้าแรกผิด", font=font, fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, '->1 =  Wrong first paragraph ',
                # (100, 3300), self.font, 1, (255, 0, 0), 2,
                # cv2.LINE_AA);
        if size_point1_1 != 0:
            for d in range(size_point1_1):
                # cv2.putText(self.clone_img, 'Wrong second paragraph.',
                # (200, self.arr_point1_1[d]), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                draw.text((200, self.arr_point1_1[d]), "ย่อหน้าสองผิด", font=font, fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, '->2 =  Wrong second paragraph ',
                # (100, 3350), self.font, 1, (255, 0, 0), 2,
                # cv2.LINE_AA);
        if size_point2_1 != 0:
            for b in range(size_point2_1):
                # cv2.putText(self.clone_img, 'Wrong third paragraph.',
                # (200, self.arr_point2_1[b]), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                draw.text((200, self.arr_point2_1[b]), "ย่อหน้าสามผิด", font=font, fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, '->3  =  Wrong third paragraph',
                # (100, 3400), self.font, 1, (255, 0, 0), 2,
                # cv2.LINE_AA);

        self.clone_img = np.array(p_img)









