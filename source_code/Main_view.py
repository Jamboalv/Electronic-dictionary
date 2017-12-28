#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkMessageBox
import PIL
import Image
import time
from PIL import ImageTk
import threading
import sys



# 调整窗口位置及大小
def CenterWindow(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    root.geometry(size)

#离线单词 菜单选项响应事件
def LiXianCiDian():
    print "LiXianCiDian!"


#在线单词 菜单选项响应事件
def ZaiXianCiDian():
    print "ZaiXianCiDian!"

#句子翻译 菜单选项响应事件
def JuZiFanYi():
    print "JuZiFanYi!"

#我的单词本 菜单选项响应事件
def WodedanCiBen():
    print "WodedanCiBen!"

def Quits():
    sys.exit()
    # root.quit


def func():
    imgs = [ImageTk.PhotoImage(file='./images/' + str(i) + '.jpg') for i in range(3)]
    count=1
    strs=["For the ideal that I hold near to my heart,\nI'd not regret a thousand times to die.\n亦余心之所善兮，虽九死其尤未悔！",
          "No matter how high the mountain is,\none can always ascend to its top.\n华山再高，顶有过路！",
          "My conscience stays untainted in spite of rumors\n and slanders from the outside.\n 人或加讪，心无疵兮！"]
    while count<=3:
        for img in imgs:
            label1.config(image=img)
            texts.set(strs[count-1])
            time.sleep(2)
            count = count + 1
            if count==3:
                count=0

# 创建主窗口
root = Tk()     # Tk()是一个Tkinter库之中的函数
root.title("电子词典系统")   # root = Tk(className='电子词典系统')
CenterWindow(root, 400, 400)

# 创建一个顶层菜单
menubar = Menu(root)
menubar.add_command(label="离线词典", command=LiXianCiDian)
menubar.add_command(label="在线词典", command=ZaiXianCiDian)
menubar.add_command(label="句子翻译", command=JuZiFanYi)
menubar.add_command(label="我的单词本", command=WodedanCiBen)
menubar.add_command(label="退出", command=Quits)
root['menu'] = menubar  # root.config(menu=menubar)


texts = StringVar()
texts.set('My conscience stays untainted in spite of rumors\n and slanders from the outside.\n 人或加讪，心无疵兮！')
filename1 = './images/2.jpg'
img1 = ImageTk.PhotoImage(Image.open(filename1))
label1 = Label(root,
               padx = 10,
               pady = 30,
               borderwidth = 2,
               textvariable=texts,
               foreground = "HotPink",underline = 4,anchor = "ne",image=img1,compound="top")
label1.pack()
timer=threading.Timer(3,func)
timer.setDaemon(True)
timer.start()
root.mainloop()
