#-*-coding:utf8-*-

import numpy as np
import cv2
import os
width = 32
hight = 32
classes = 52
mark = 0
mark_label = 0
read_path = '../dataset'
allfolders = os.listdir(read_path)
newLabel = []
for tempfolder in allfolders:
    templabel = tempfolder[ len(tempfolder) - 2:len(tempfolder) ]
    templabel = int(templabel)-11
    allfiles = os.listdir(read_path+'/'+tempfolder)
    numbers = len(allfiles)
    sublabel = np.zeros( (numbers, classes) )
    sublabel[:, templabel] = 1
    if mark_label == 0:
        label = sublabel
    else:
        label = np.vstack( (label, sublabel) )
    mark_label = 1
    for tempfile in allfiles:
        newLabel.append(templabel)
        tempDir = read_path + '/' +tempfolder+'/'+tempfile
        raw_image=cv2.imread(tempDir,0)
        image = cv2.GaussianBlur(raw_image,(5,5),0)
        res = cv2.resize(image, (width, hight),interpolation=cv2.INTER_CUBIC)
        #print res.shape
        
        if mark == 0:
            array = np.reshape(res, width*hight)
        else:
            tempArray = np.reshape(res, width*hight)
            array = np.vstack( (array, tempArray) )

        mark = 1
savepath = '../data/'
np.save(savepath + 'array.npy', array)
np.save(savepath + 'label.npy', label)
np.save(savepath + 'newLabel.npy', newLabel)