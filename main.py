# -*- coding: <encoding name> -*- : # -*- coding: utf-8 -*-
import add
import cv2
import random

bgpath='./bg'
repath='./result'
filenames=os.listdir(bgpath)

for filename in filenames:                
    ip_num = random.randint(0, 3)  #range of ip_num
    path_bg = os.path.join(bgpath,filename)
    path_ip = './ip/' + str(ip_num)+'.jpg'
    print(path_ip)
    img_fuse = add.pic_superpose(path_bg, path_ip)
    cv2.imwrite(os.path.join(repath,filename), img_fuse)

