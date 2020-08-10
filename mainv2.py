# -*- coding: <encoding name> -*- : # -*- coding: utf-8 -*-
import addv2
import cv2
import random
import os

bgpath='./bg'
repath='./result'
filenames=os.listdir(bgpath)

for filename in filenames:        
    ip_num = random.randint(0, 3)  #range of ip_num
    x=random.randint(100, 800)     #x location 
    y=random.randint(50, 300)      #y location
    bgname=os.path.join(bgpath,filename)
    rename=os.path.join(repath,filename)
    addv2.Picture_Synthesis(mother_img=bgname,
                            son_img='./ip/' + str(ip_num)+'.jpg',
                            save_img=rename,
                            coordinate=(x,y)#指定子图位置
                            #coordinate=None#居中
                      )