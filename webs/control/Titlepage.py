from Cover import Cover
import numpy as np
from PIL import ImageFont, ImageDraw, Image


class Title(Cover):

    def __init__(self, img):
        Cover.__init__(self, img)
        self.txt_wrong_title = []

    def set_text_title(self, text_content):
        t_size_title = np.size(self.arr_uppers)
        for x in range(t_size_title):
            if self.arr_size_text[x] < 100:
                arr_sum = self.arr_size_text[x]
                content_size = text_content - arr_sum
                if content_size >= -2 and content_size <= 2:
                    # print('content title :', content_size)
                    continue
                else:
                    # print('content title :', content_size)
                    self.txt_wrong_title.append(self.arr_uppers[x])

    def set_mark_text_title(self):
        wrong_text_title = np.size(self.txt_wrong_title)
        # print(self.txt_wrong_title)
        font = ImageFont.truetype("webs/control/font/THSarabun Bold.ttf", 45)
        p_img = Image.fromarray(self.clone_img)
        draw = ImageDraw.Draw(p_img)
        for w_title in range(wrong_text_title):
            # cv2.putText(self.clone_img, '* ', (2200, self.txt_wrong_title[w_title]),
            # self.font, 2, (255, 0, 0), 2, cv2.LINE_AA);
            # cv2.putText(self.clone_img, '* = Wrong text size ',
            # (100, 3400), self.font, 1, (255, 0, 0), 2, cv2.LINE_AA);
            draw.text((2200, self.txt_wrong_title[w_title]), "*", font=font, fill=(255, 0, 0, 0))
        draw.text((100, 3400), "* คือ ขนาดตัวอักษรผิด", font=font, fill=(255, 0, 0, 0))
        self.clone_img = np.array(p_img)






