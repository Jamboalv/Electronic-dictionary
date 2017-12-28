# -*- coding: utf-8 -*-
import pythoncom
import pyHook
from PIL import ImageGrab
from mouse_click import *
from picture_reconize import *

def readFile(filename):
    fopen = open(filename, 'r')
    s = fopen.readline()
    fopen.close()
    return s

def str_to_intx(str):
    s=''
    for i in range(1,len(str)):
        if(str[i] != ","):
            s += str[i]
        else:
            break
    return int(s)

def str_to_inty(str):
    s=""
    count = 0
    while(str[count] != ","):
        count +=1
    count += 1
    for i in range(count,len(str)-2):
        s +=str[i]
    return int(s)

def compare_max(x,y):
    if(x>y):
        max_number = x
    else:
        max_number = y
    return max_number

def compare_min(x,y):
    if(x<y):
        min_number = x
    else:
        min_number = y
    return min_number
#获取坐标截图
def screen_shot():
    s1 = readFile('./txt/monitor_p1.txt')
    s2 = readFile('./txt/monitor_p2.txt')
    x0 = str_to_intx(s1)
    y0 = str_to_inty(s1)
    x1 = str_to_intx(s2)
    y1 = str_to_inty(s2)
    maxX = compare_max(x0,x1)
    minX = compare_min(x0,x1)
    maxY = compare_max(y0,y1)
    minY = compare_min(y0,y1)
    box = (minX, minY, maxX, maxY)
    im = ImageGrab.grab(box)
    im.save('./picture\os.jpg')

#监听键盘事件
def onKeyboardEvent(event):
    if str(event.Key) == 'Snapshot':
          mousehook_run()
    screen_shot()
    txt = image_tess('./picture/os.jpg')
    print txt
    if(txt!=''):
        fopen = open('ret.txt', 'w')
        fopen.write(txt)
        fopen.close()
    return True
#挂键盘钩子
def keyboardhook_run():
    hm = pyHook.HookManager()
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages(10000)

if __name__ == '__main__':
    keyboardhook_run()
