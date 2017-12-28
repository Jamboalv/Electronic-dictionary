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


#离线翻译按钮响应事件 显示查询结果
def on_click():
    start=time.clock()   #测试离线查询的时间

    global result_var   #全局变量
    global check_var

    check_var.set('')   #清空原有内容
    result_var.set('')

    md = modelHelper()
    word = edit.get()   #获取单词
    fc=md.outlineSelect(word)   #离线查询单词，返回结果
    if fc==():
        tkMessageBox.showinfo(title='提示：', message="未查到相关内容。。。")
        butt_add["state"]="disable" #添加单词本按钮设为不可用
    else:
        for row in fc:
            check_var.set(row[0])   #结果显示到界面上
            result_var.set(row[1])
            butt_add["state"] = "normal"  # 激活添加按钮
            print "%s,%s" % (row[0], row[1])
    end=time.clock()
    print "离线查询时间为=%s秒" % (end-start) #显示运行时间


# 添加到单词本响应事件
def on_click_add():
    md = modelHelper()
    # 查询是否单词本已存在该单词，已存在则无需再添加，不存在再添加
    exist = md.selectFromWord_book(check_var.get().strip())
    if exist == 0:
        mark = "N"
        count = md.addWordbook(check_var.get().strip(), result_var.get().strip(), mark)
        tkMessageBox.showinfo(title='提示：', message='添加成功！')
        print count
    else:
        alarmstr = "该单词已存在，无需再添加，记录数=%d" % (exist)
        tkMessageBox.showinfo(title='提示：', message=alarmstr)
        print alarmstr




#主程序

# 创建主窗口
root = Tk()     # Tk()是一个Tkinter库之中的函数
root.title("电子词典系统-离线翻译")   # root = Tk(className='电子词典系统')
CenterWindow(root, 400, 400)

# 创建一个顶层菜单
menubar = Menu(root)
menubar.add_command(label="离线词典", command=LiXianCiDian)
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
butt = Button(fram, text='离线翻译',background='lightgreen')
butt['command'] = on_click
butt.pack(side=RIGHT)
fram.pack(side=TOP)

#显示查询结果，单词+解释
check_var = StringVar()
check_var.set('')
check=Label(root,width=31,height=3,bg='lightblue',textvariable=check_var, relief="ridge",borderwidth=2,font=('Helvetica', '14', 'bold'),anchor="w",justify="left").pack(side=TOP)

result_var = StringVar()
result_var.set('')
text_result=Label(root,width=31,height=12,bg='lightblue',textvariable=result_var,relief="ridge",borderwidth=2, font=('Helvetica', '14', 'bold'),anchor="nw",wraplength=350,justify="left").pack(side=TOP)


#添加单词本按钮
butt_add = Button(root, text='添加到我的单词本',background='pink')
butt_add['command'] = on_click_add
butt_add.pack(side=TOP)
butt_add["state"] = "disable"  #添加单词本按钮初始化未激活状态


#mainloop则是主窗口的成员函数，也就是表示让这个root工作起来，开始接收鼠标的和键盘的操作。
root.mainloop()
