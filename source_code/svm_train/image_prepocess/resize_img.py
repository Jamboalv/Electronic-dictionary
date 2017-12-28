#-*-coding:utf8-*-

import cv2
import numpy as cv
import os
import os.path

count = 0

for f in os.listdir("./splited_images"):
    count += 1

for i in range(1,count+1):
    img = cv2.imread('./splited_images/' + str(i) + '.png', 0)   #read images
    res = cv2.resize(img,(32, 32), interpolation=cv2.INTER_CUBIC)
    print type(res), res.shape
