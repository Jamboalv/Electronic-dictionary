#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkMessageBox
import time
from modeltest import modelHelper


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


#翻译按钮响应事件 显示查询结果
def on_click():
    start = time.clock()  # 测试在线查询的时间
    word = edit.get()  #获取单词
    len = lbword.size()
    for row in range(len):
       str=lbword.get(row)
       list_str = str.split(':', 1)
       if list_str[0] == word:
           lbword.itemconfigure(row,bg='yellow')
    end = time.clock()
    print "在线查询时间为=%s秒" % (end - start)  # 显示运行时间

#查询我添加的单词本内容
def myWordWork():
    md = modelHelper()
    mywords=md.SelectMyWordBook()
    for row in mywords:
        strs=str(row[0]+":"+row[1])
        print strs
        lbword.insert(END,strs)
        print "%s,%s" % (row[0], row[1])

#删除单词记录
def on_click_delete():
    md = modelHelper()
    str=lbword.get(lbword.curselection())
    list_str=str.split(':',1)
    print list_str[0]
    print list_str[1]
    count=md.deleteFromMyWordBook(list_str[0])
    if count==1:
        tkMessageBox.showinfo(title='提示：', message='删除成功！')
        #刷新结果显示信息
        lbword.delete(0,END)
        myWordWork()
    elif count==0:
        tkMessageBox.showinfo(title='提示：', message='该信息不存在！')
    else:
        tkMessageBox.showinfo(title='提示：', message='删除失败！')

    # md.deleteFromMyWordBook()




###主程序入口###
# 创建主窗口
root = Tk()     # Tk()是一个Tkinter库之中的函数
root.title("电子词典系统-我的单词本")   # root = Tk(className='电子词典系统')
CenterWindow(root, 400, 400)

# 创建一个顶层菜单
menubar = Menu(root)
menubar.add_command(label="离线词典",command=LiXianCiDian)
menubar.add_command(label="在线词典", command=ZaiXianCiDian)
menubar.add_command(label="句子翻译", command=JuZiFanYi)
menubar.add_command(label="我的单词本", command=WodedanCiBen)
menubar.add_command(label="退出", command=root.quit)
root['menu'] = menubar  # root.config(menu=menubar)


# 在根窗口的顶部，从左到右放置标签、单行输入文本框、按钮
fram = Frame(root)
Label(fram,text='输入英文：'.decode('utf8').encode('utf8'), font=('Helvetica', '10', 'bold')).pack(side=LEFT)
#单行输入文本框
inout_text = StringVar()
inout_text.set('')
edit = Entry(fram ,font=('Helvetica', '10', 'bold'),width=35,foreground = 'red',highlightbackground = 'blue', relief = 'sunken',background='lightyellow')
edit.pack(side=LEFT,fill=BOTH,expand=1)
edit['textvariable'] = inout_text
edit.pack()
#翻译按钮
butt = Button(fram, text='查询',background='lightgreen')
butt['command'] = on_click
butt.pack(side=LEFT)

#删除按钮
butt_delete = Button(fram, text='删除',background='lightblue')
butt_delete['command'] = on_click_delete
butt_delete.pack(side=RIGHT)
fram.pack(side=TOP)


#显示单词本信息 添加滚动条
word_var = StringVar()
sl=Scrollbar(root)
sl.pack(side=RIGHT,fill=Y)
sb=Scrollbar(root,orient = 'horizontal')
sb.pack(side=BOTTOM,fill=X)
lbword=Listbox(root,listvariable=word_var,width=55,height=22,bg='lightgray',selectmode="browse",yscrollcommand = sl.set,xscrollcommand = sb.set)
myWordWork()
lbword.selection_set(0)
lbword.pack(side=TOP)
sl.config(command = lbword.yview)
sb.config(command = lbword.xview)

root.mainloop()
