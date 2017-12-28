#-*-coding:utf8-*-

import numpy as np
import cv2

raw_image=cv2.imread('./shrimp.png',0)
gray = cv2.cvtColor(raw_image,cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(gray,(5,5),0)
t,image=cv2.threshold(image,100,255,cv2.THRESH_BINARY)
image[image==0] = 1
image[image==255] = 0

hit_x = sum(image)

list = []
head = 0
end = 0
n = 0
savepath = '/home/computer/code/splited_images/'
for i in range(hit_x.shape[0]):
    if i+1 < hit_x.shape[0]:
        if hit_x[i] == 0 and hit_x[i+1] != 0:
            head = i
        if hit_x[i] != 0 and hit_x[i+1] == 0:
            end = i
    if head != 0 and end != 0:
        list.append([head,end])
        head = 0
        end = 0
s = raw_image[:,list[0][0]:list[0][1]]

for i in range(len(list)):
    cv2.imshow('window',raw_image[:,list[i][0]:list[i][1]])
    cv2.imwrite(savepath+'{0}'.format(n+1)+'.png',raw_image[:,list[i][0]:list[i][1]])
    cv2.waitKey(1000)
    n = n + 1
    
