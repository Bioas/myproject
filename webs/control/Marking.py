from Titlepage import Title
from Abstractthai import Abt
from Content import Content
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np


class Mark(Title, Abt, Content):
    def __init__(self, img):
        Title.__init__(self, img)
        Abt.__init__(self, img)
        Content.__init__(self, img)

    def set_mark_number(self, top_num, right_num):
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        if self.top_number_border != 0:
            if (int(top_num) - int(self.top_number_border)) < -30 or (int(top_num) - int(self.top_number_border)) > 30:
                # print(int(top_num) - int(self.top_number_border))
                # cv2.putText(self.clone_img, 'Wrong top number.',
                # (1830, 250), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                draw.text((1830, 200), "ระยะขอบบนเลขหน้าผิด", font=font, fill=(255, 0, 0, 0))
        if self.right_number_border != 0:
            if (int(right_num) - int(self.right_number_border)) < -30 or (int(right_num) - int(self.right_number_border)) > 30:
                # print(int(right_num) - int(self.right_number_border))
                # cv2.putText(self.clone_img, 'Wrong right number ',
                # (2150, 350), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                draw.text((2100, 350), "ระยะขอบบนขวาเลขหน้าผิด", font=font, fill=(255, 0, 0, 0))

        self.clone_img = np.array(p_img)

    def set_mark_margin(self, set_mark1, top, bottom, left, right):
        cv2.rectangle(self.clone_img, (left, top), (right, bottom), (0, 0, 255), 2)
        # cv2.putText(self.clone_img, 'line blue = Correct structure style',
        # (1200, 3350), self.font, 1, (0, 0, 255), 2, cv2.LINE_AA);
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        draw.text((1200, 3350), "กรอบสีน้ำเงิน คือ รูปแบบโครงสร้างที่ถูกต้อง", font=font, fill=(0, 0, 255, 0))

        # cv2.putText(self.clone_img, 'line red = Content area',
        # (1200, 3400), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
        if int(set_mark1) == 0 or int(set_mark1) == 1:
            # Mark cover and title
            # print('Mark margin cover and title')
            if (int(top) - int(self.top_border)) < -5 or (int(top) - int(self.top_border)) > 5:
                # cv2.putText(self.clone_img, 'Wrong top Margin.',
                # (1200, 350), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                draw.text((1000, 350), "ระยะขอบบนผิด", font=font, fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, '*Top* = Invalid top Margin.', (100, 100), self.font, 1,
                # (255, 0, 0), 2, cv2.LINE_AA);

            if (int(bottom) - int(self.bottom_border)) < -25 or (int(bottom) - int(self.bottom_border)) > 30:
                # cv2.putText(self.clone_img, 'Wrong bottom Margin.'
                # , (1200, 3300), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                draw.text((1200, 3300), "ระยะขอบล่างผิด", font=font, fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, '*Bottom* = Invalid bottom Margin.', (100, 150),
                # self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
            if (int(left) - int(self.left_border)) < -85 or (int(left) - int(self.left_border)) > 85:
                # cv2.putText(self.clone_img, 'Wrong left Margin.',
                # (50, 1800), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                draw.text((50, 1800), "ระยะขอบซ้ายผิด", font=font, fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, '*Left* = Invalid left Margin.', (100, 200), self.font, 1, (255, 0, 0), 2,
                # cv2.LINE_AA);
            if (int(right) - int(self.right_border)) < -85 or (int(right) - int(self.right_border)) > 85:
                # cv2.putText(self.clone_img, 'Wrong right Margin.',
                # (2100, 3000), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                draw.text((2100, 3200), "ระยะขอบขวาผิด", font=font, fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, '*Right* = Invalid right Margin.', (100, 250), self.font, 1,
                # (255, 0, 0), 2, cv2.LINE_AA);
        else:
            # Mark thesis > 2 - 10
            if (int(top) - int(self.top_border)) < -5 or (int(top) - int(self.top_border)) > 5:
                # cv2.putText(self.clone_img, 'Wrong top Margin.',
                # (1200, 420), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);

                draw.text((1000, 350), "ระยะขอบบนผิด", font=font, fill=(255, 0, 0, 0))

                # cv2.putText(self.clone_img, '*Top* = Invalid top Margin.',
                # (100, 100), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);

            if (int(bottom) - int(self.bottom_border)) < -25 or (int(bottom) - int(self.bottom_border)) > 1400:

                # cv2.putText(self.clone_img, 'Wrong bottom Margin.',
                # (1200, 3300), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                draw.text((1200, 3300), "ระยะขอบล่างผิด", font=font, fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, '*Bottom* = Invalid bottom Margin.',
                # (100, 150), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);

            if (int(left) - int(self.left_border)) < -10 or (int(left) - int(self.left_border)) > 10:
                draw.text((50, 1800), "ระยะขอบซ้ายผิด", font=font, fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, 'Wrong left Margin.',
                # (50, 1800), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                # cv2.putText(self.clone_img, '*Left* = Invalid left Margin.',
                # (100, 200), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
            if (int(right) - int(self.right_border)) < -15 or (int(right) - int(self.right_border)) > 15:
                draw.text((2100, 3200), "ระยะขอบขวาผิด", font=font, fill=(255, 0, 0, 0))
                # cv2.putText(self.clone_img, 'Wrong right Margin.', (2100, 3000)
                # , self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
                # cv2.putText(self.clone_img, '*Right* = Invalid right Margin.',
                # (100, 250), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);

        self.clone_img = np.array(p_img)
