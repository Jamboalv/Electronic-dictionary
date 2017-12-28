#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pyHook
import pythoncom

def write_position1_to_txt(position):
    f = open('./txt/monitor_p1.txt','w')
    f.write(position+'\n')
    f.close()

def write_position2_to_txt(position):
        f = open('./txt/monitor_p2.txt', 'w')
        f.write(position + '\n')
        f.close()

#获取点击鼠标时的坐标
def onMouse_leftdown(event):
    p1 = event.Position
    #print  p1
    write_position1_to_txt(p1.__str__())
    return True

#获取松开鼠标点时的坐标
def onMouse_leftup(event):
    p2 = event.Position
    #print p2
    write_position2_to_txt(p2.__str__())
    return True

#挂鼠标钩子
def mousehook_run():
    hm = pyHook.HookManager()
    hm.SubscribeMouseLeftDown(onMouse_leftdown)
    hm.SubscribeMouseLeftUp(onMouse_leftup)
    hm.HookMouse()
    pythoncom.PumpMessages(1)