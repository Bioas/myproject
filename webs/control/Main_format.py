import cv2
import numpy as np
import copy
import os

class MainFormat:

    font = cv2.FONT_HERSHEY_SIMPLEX

    def __init__(self, img):
        self.img = img
        self.clone_img = ''
        self.top_border = 0
        self.bottom_border = 0
        self.left_border = 0
        self.right_border = 0
        self.arr_uppers = []
        self.arr_lowers = []
        self.arr_size_text = []
        self.top_number_border = 0
        self.right_number_border = 0
        self.arr_x = []
        self.arr_y = []
        self.arr_x_w = []
        self.arr_y_h = []

    def set_clone_img_main(self):
        self.clone_img = copy.copy(self.img)

    def set_img_margin(self, top_num, right_num):
        if len(self.arr_uppers) >= 2:
            h, w = self.img.shape[:2]
            check_null_value = self.img[self.arr_uppers[0]:self.arr_lowers[0], 0:w]
            gray_margin = cv2.cvtColor(check_null_value, cv2.COLOR_BGR2GRAY)
            th_margin, threshold_margin = cv2.threshold(gray_margin, 127, 255,
                                                        cv2.THRESH_BINARY_INV | cv2.THRESH_TRIANGLE)
            pts_margin = cv2.findNonZero(threshold_margin)
            x_margin, y_margin, w_margin, h_margin = cv2.boundingRect(pts_margin)
            check_page = x_margin - (x_margin + w_margin)
            # print('........................................................', check_page)
            if abs(check_page) < 100:
                y1 = self.arr_uppers[1]
                check_set_number = self.img[self.arr_uppers[0]:self.arr_lowers[0], 0:w]
                gray_margin0 = cv2.cvtColor(check_set_number, cv2.COLOR_BGR2GRAY)
                gray_number = cv2.cvtColor(self.clone_img, cv2.COLOR_BGR2GRAY)
                h, w = gray_number.shape[:2]
                cv2.line(self.clone_img, (right_num - 10, 0), (right_num - 10, top_num + 10), (0, 0, 255), 2)
                cv2.line(self.clone_img, (right_num - 10, top_num + 10), (w, top_num + 10), (0, 0, 255), 2)
                cv2.rectangle(self.clone_img, (right_num - 10, top_num - 40), (right_num + 40, top_num + 10), (0, 0, 255), 2)
                th_margin0, threshold_margin0 = cv2.threshold(gray_margin0, 127, 255,
                                                              cv2.THRESH_BINARY_INV | cv2.THRESH_TRIANGLE)
                pts_margin0 = cv2.findNonZero(threshold_margin0)
                x_1, y_1, w_1, h_1 = cv2.boundingRect(pts_margin0)

                self.top_number_border = round(self.lowers[0])
                # print('1', self.top_number_border)
                self.right_number_border = round(x_1)
                # print('2', self.right_number_border)

                check_null_value2 = self.img[self.arr_uppers[1]:h, 0:w]
                gray_margin1 = cv2.cvtColor(check_null_value2, cv2.COLOR_BGR2GRAY)
                th_margin1, threshold_margin1 = cv2.threshold(gray_margin1, 127, 255,
                                                              cv2.THRESH_BINARY_INV | cv2.THRESH_TRIANGLE)
                pts_margin1 = cv2.findNonZero(threshold_margin1)
                x_margin1, y_margin1, w_margin1, h_margin1 = cv2.boundingRect(pts_margin1)
                self.top_border = round(y1)
                # self.bottom_border = round((y1 + h_margin1) - 10)
                self.bottom_border = round(self.arr_lowers[-1])
                self.left_border = round(x_margin1)
                self.right_border = round(x_margin1 + w_margin1)
                # cv2.rectangle(self.clone_img, (self.left_border, self.top_border),
                # (self.right_border, self.bottom_border),
                # (255, 0, 0), 2)
            elif abs(check_page) > 100:
                self.top_number_border = 0
                self.right_number_border = 0
                y0 = self.arr_uppers[0]
                check_1 = self.img[self.arr_uppers[0]:h, 0:w]
                gray_margin2 = cv2.cvtColor(check_1, cv2.COLOR_BGR2GRAY)
                th_margin2, threshed_margin2 = cv2.threshold(gray_margin2, 127, 255,
                                                             cv2.THRESH_BINARY_INV | cv2.THRESH_TRIANGLE)
                pts_margin2 = cv2.findNonZero(threshed_margin2)
                x_margin2, y_margin2, w_margin2, h_margin2 = cv2.boundingRect(pts_margin2)
                self.top_border = round(y0)
                # self.bottom_border = round((y0 + h_margin2) - 10)
                self.bottom_border = round(self.arr_lowers[-1])
                self.left_border = round(x_margin2)
                self.right_border = round(x_margin2 + w_margin2)
                # cv2.rectangle(self.clone_img, (self.left_border, self.top_border),
                # (self.right_border, self.bottom_border),
                # (255, 0, 0), 2)

    def set_arr_up_lo(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        th, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_TRIANGLE)
        pts = cv2.findNonZero(threshold)
        ret = cv2.boundingRect(pts)
        cx, cy, w, h = ret
        M = cv2.getRotationMatrix2D((cx, cy), 0, 1.0)
        self.rotated = cv2.warpAffine(threshold, M, (gray.shape[1], gray.shape[0]))
        hist = cv2.reduce(self.rotated, 1, cv2.REDUCE_SUM, dtype=cv2.CV_32S)
        H, W = gray.shape[:2]
        self.uppers = [y for y in range(H - 1) if hist[y] <= 0 and hist[y + 1] > 1]
        self.lowers = [y for y in range(H - 1) if hist[y] > 1 and hist[y + 1] <= 0]
        diff = np.subtract(self.lowers, self.uppers)
        usize = np.size(self.uppers)
        lsize = np.size(self.lowers)

        for up in range(usize):
            diff = self.lowers[up] - self.uppers[up]
            if diff > 100:
                self.arr_uppers.append(self.uppers[up])
            elif diff < 100:
                if diff > 20:
                    cc_up = 0
                    max = np.max(hist[self.uppers[up]:self.lowers[up]])
                    for j_up in range(np.size(hist[self.uppers[up]:self.lowers[up]])):
                        percent = (hist[self.uppers[up]:self.lowers[up]] * 120) / max
                        if percent[j_up] > 65:
                            top_line = self.uppers[up] + j_up
                            self.arr_uppers.append(top_line)
                            cc_up += 1
                            if cc_up == 1:
                                break

        for lo in range(lsize):
            diff = self.lowers[lo] - self.uppers[lo]
            if diff > 100:
                self.arr_lowers.append(self.lowers[lo])
            elif diff < 100:
                if diff > 20:
                    cc_lo = 0
                    max = np.max(hist[self.uppers[lo]:self.lowers[lo]])
                    for j_lo in range(self.lowers[lo], self.uppers[lo], -1):
                        percent = (hist[j_lo] * 100) / max
                        if percent > 42:
                            bottom_line = j_lo
                            cc_lo += 1
                            self.arr_lowers.append(bottom_line)
                            if cc_lo == 1:
                                break

    def set_size_txt(self):
        # print('arr  -> :', self.arr_uppers)
        set_size_up = np.size(self.arr_uppers)
        for t in range(set_size_up):
            sum_size_text = self.arr_lowers[t] - self.arr_uppers[t]
            self.arr_size_text.append(sum_size_text)

        # print('Test :', self.arr_size_text)

    def square_paragraph(self):
        u_check = np.size(self.arr_uppers)
        for m in range(u_check):
            h, w = self.img.shape[:2]
            img1 = self.img[self.arr_uppers[m]:self.arr_lowers[m], 0:w]
            gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_TRIANGLE)
            pts = cv2.findNonZero(threshed)
            x, y, w, h = cv2.boundingRect(pts);
            self.arr_x.append(x)
            self.arr_y.append(y)
            self.arr_x_w.append(x + w)
            self.arr_y_h.append(y + h)
        # print('arr x :', self.arr_x)

    def get_mark_img(self):
        return self.clone_img

















