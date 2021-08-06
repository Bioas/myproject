import cv2
import numpy as np


def convert_margin(input_margin):
    margin = 0
    if float(input_margin) == 1.0:
        margin = 300
    elif float(input_margin) == 1.5:
        margin = 450
    elif float(input_margin) == 2.0:
        margin = 600
    elif float(input_margin) == 2.5:
        margin = 750

    return int(margin)


def convert_size_text(input_txt):
    thai = 0
    if int(input_txt) == 16:
        thai = 26
    elif int(input_txt) == 18:
        thai = 29
    elif int(input_txt) == 20:
        thai = 33
    elif int(input_txt) == 22:
        thai = 36

    return int(thai)


def convert_line_spacing(input_line):
    line_head = 0
    line_content = 0
    if float(input_line) == 1.0:
        line_content = 61
        line_head = 156
    elif float(input_line) == 1.15:
        line_content = 74
        line_head = 253
    elif float(input_line) == 1.5:
        line_content = 105
        line_head = 322
    elif float(input_line) == 2.0:
        line_content = 148
        line_head = 419

    return int(line_content), int(line_head)


def convert_text_english_s(input_text_s):
    text_eng_s = 0
    if int(input_text_s) == 16:
        text_eng_s = 22
    elif int(input_text_s) == 18:
        text_eng_s = 25
    elif int(input_text_s) == 20:
        text_eng_s = 28
    elif int(input_text_s) == 22:
        text_eng_s = 30

    return int(text_eng_s)


def convert_text_english_b(input_text_b):
    text_eng_s = 0
    if int(input_text_b) == 16:
        text_eng_s = 29
    elif int(input_text_b) == 18:
        text_eng_s = 35
    elif int(input_text_b) == 20:
        text_eng_s = 39
    elif int(input_text_b) == 22:
        text_eng_s = 42

    return int(text_eng_s)


def convert_paragraph(input_paragraph):
    paragraph = 0
    if float(input_paragraph) == 1.3:
        paragraph = 154
    elif float(input_paragraph) == 1.5:
        paragraph = 177
    return int(paragraph)


def covert_number(input_number):
    num = 0
    if int(input_number) == 16:
        num = 31
    elif int(input_number) == 18:
        num = 36
    elif int(input_number) == 20:
        num = 39
    elif int(input_number) == 22:
        num = 43

    return int(num)


def w_img(w_input):
    img_w = cv2.cvtColor(w_input, cv2.COLOR_RGB2BGR)
    gray_w = cv2.cvtColor(img_w, cv2.COLOR_BGR2GRAY)
    th_w, threshed_w = cv2.threshold(gray_w, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_TRIANGLE)
    pts_w = cv2.findNonZero(threshed_w)
    x_pic, y_pic, w_pic, h_pic = cv2.boundingRect(pts_w)
    width_symbol_w = format(w_pic / 300, '.1f')

    return float(width_symbol_w)


def h_img(h_input):
    img_w = cv2.cvtColor(h_input, cv2.COLOR_RGB2BGR)
    gray_w = cv2.cvtColor(img_w, cv2.COLOR_BGR2GRAY)
    th_w, threshed_w = cv2.threshold(gray_w, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_TRIANGLE)
    pts_w = cv2.findNonZero(threshed_w)
    x_pic, y_pic, w_pic, h_pic = cv2.boundingRect(pts_w)
    height_symbol_h = format(h_pic / 300, '.1f')

    return float(height_symbol_h)


def img_point_center(center_input):
    img_text_point = cv2.cvtColor(center_input, cv2.COLOR_RGB2BGR)
    height, width = img_text_point.shape[:2]
    gray_center = cv2.cvtColor(img_text_point, cv2.COLOR_BGR2GRAY)
    th_center, threshed_center = cv2.threshold(gray_center, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_TRIANGLE)
    pts_center = cv2.findNonZero(threshed_center)
    x_center, y_center, w_center, h_center = cv2.boundingRect(pts_center)
    point_img_text_center = x_center - (width - (x_center + w_center))

    return point_img_text_center


def check_point(img_point_text):
    img_text_point = cv2.cvtColor(np.array(img_point_text), cv2.COLOR_RGB2BGR)
    height, width = img_text_point.shape[:2]
    gray_text = cv2.cvtColor(img_text_point, cv2.COLOR_BGR2GRAY)
    th_text, threshed_text = cv2.threshold(gray_text, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_TRIANGLE)
    pts_text = cv2.findNonZero(threshed_text)
    x_text, y_text, w_text, h_text = cv2.boundingRect(pts_text)
    left = x_text
    center = x_text - (width - (x_text + w_text))
    right = x_text + w_text
    return int(left), int(center), int(right)



