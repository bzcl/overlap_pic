# -*- coding: <encoding name> -*- : # -*- coding: utf-8 -*-
import cv2
def pic_superpose(path_img_bg, path_img_ip):
    img1 = cv2.imread(path_img_bg)#背景图的读取
    img2 = cv2.imread(path_img_ip)#需要插入图的读取
    rows, cols = img2.shape[:2]
    roi = img1[:rows, :cols]
    # 创建掩膜
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 150, 255, cv2.THRESH_BINARY)#将灰度图150-255之间的设为黑色，其余为白色，用于制作背景(根据你想要扣的图，设置灰度图的颜色)
    mask_inv = cv2.bitwise_not(mask)#用于抠图

    # # 保留除logo外的背景
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask)#背景处理，将目标位置的数字扣掉
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)#目标图案的背景扣掉
    dst = cv2.add(img1_bg, img2_fg)  # 进行融合
    img1[:rows, :cols] = dst  # 融合后放在原图上
    return img1
