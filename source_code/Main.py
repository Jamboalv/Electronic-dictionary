#!/usr/bin/python
# -*- coding: utf-8 -*-

# ======================
# imports
# ======================
import Tkinter as tk
import ttk
import ScrolledText
from Tkinter import Menu
from Tkinter import Spinbox
import tkMessageBox as mBox

import PIL
import Image
import time
from PIL import ImageTk
import threading
import sys
import time
from modeltest import modelHelper

# 由于tkinter中没有ToolTip功能，所以自定义这个功能如下
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))

        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


# ===================================================================
def createToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

def CenterWindow(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    root.geometry(size)

def HideWindow(root):
    root.withdraw()

def ShowWindow(root):
    root.update()
    root.deiconify()

# Create instance
win = tk.Tk()

# Add a title
win.title("电子词典系统")
CenterWindow(win, 400, 480)

# Tab Control introduced here --------------------------------------
tabControl = ttk.Notebook(win)  # Create Tab Control

tab1 = ttk.Frame(tabControl)  # Create a tab
tabControl.add(tab1, text='主页')  # Add the tab

tab2 = ttk.Frame(tabControl)  # Add a second tab
tabControl.add(tab2, text='离线词典')  # Make second tab visible

tab3 = ttk.Frame(tabControl)  # Add a third tab
tabControl.add(tab3, text='在线词典')  # Make second tab visible

tab4 = ttk.Frame(tabControl)  # Add a third tab
tabControl.add(tab4, text='句子翻译')  # Make second tab visible

tab7 = ttk.Frame(tabControl)  # Add a third tab
tabControl.add(tab7, text='屏幕取词')  # Make second tab visible

tab5 = ttk.Frame(tabControl)  # Add a third tab
tabControl.add(tab5, text='我的单词本')  # Make second tab visible

tab6 = ttk.Frame(tabControl)  # Add a third tab
tabControl.add(tab6, text='退出')  # Make second tab visible



tabControl.pack(expand=1, fill="both")  # Pack to make visible
# -- Tab Control introduced here -----------------------------------------

# ---------------Tab1控件介绍------------------#
# 主界面
monty = ttk.LabelFrame(tab1, text='')
monty.grid(column=0, row=0, padx=8, pady=4)

def func1():
    imgs = [ImageTk.PhotoImage(file='./images/' + str(i) + '.jpg') for i in range(3)]
    count=1
    strs=["For the ideal that I hold near to my heart,\nI'd not regret a thousand times to die.\n亦余心之所善兮，虽九死其尤未悔！",
          "No matter how high the mountain is,\none can always ascend to its top.\n华山再高，顶有过路！",
          "My conscience stays untainted in spite of rumors\n and slanders from the outside.\n 人或加讪，心无疵兮！"]
    while count<=3:
        for img in imgs:
            label1.config(image=img)
            texts1.set(strs[count-1])
            time.sleep(2)
            count = count + 1
            if count==3:
                count=0

#-------------------主页面--------------
texts1 = tk.StringVar()
texts1.set('My conscience stays untainted in spite of rumors\n and slanders from the outside.\n 人或加讪，心无疵兮！')
filename1 = './images/2.jpg'
img1 = ImageTk.PhotoImage(Image.open(filename1))
label1 = tk.Label(monty,
               padx = 10,
               pady = 30,
               borderwidth = 2,
               textvariable=texts1,
               foreground = "HotPink",underline = 4,anchor = "ne",image=img1,compound="top")
label1.pack()
timer=threading.Timer(3,func1)
timer.setDaemon(True)
timer.start()
# ---------------Tab1控件介绍------------------#


# ---------------Tab2控件介绍------------------#
# 离线词典页面
monty2 = ttk.LabelFrame(tab2, text='')
monty2.grid(column=0, row=0, padx=8, pady=4)

def on_click_ZhToEn2():
    start = time.clock()  # 测试离线查询的时间

    global result_var2  # 全局变量
    global check_var2

    check_var2.set('')  # 清空原有内容
    result_var2.set('')

    md = modelHelper()
    word = edit2.get()  # 获取单词
    fc = md.zhongYiYing(word)  # 离线查询单词，返回结果
    if fc == ():
        mBox.showinfo(title='提示：', message="未查到相关内容。。。")
        butt_add2["state"] = "disable"  # 添加单词本按钮设为不可用
    else:
        check_var2.set(word)
        str = ""
        for row in fc:
            # 结果显示到界面上
            str += row[0] + '\n'

        result_var2.set(str)
        butt_add2["state"] = "normal"  # 激活添加按钮
        print "%s" % (str)
    end = time.clock()
    print "离线查询时间为=%s秒" % (end - start)  # 显示运行时间

#离线翻译按钮响应事件 显示查询结果
def on_click_EnToZh2():
    start=time.clock()   #测试离线查询的时间
    global result_var2   #全局变量
    global check_var2
    check_var2.set('')   #清空原有内容
    result_var2.set('')
    md = modelHelper()
    word = edit2.get()   #获取单词
    fc=md.outlineSelect(word)   #离线查询单词，返回结果
    if fc==():
        mBox.showinfo(title='提示：', message="未查到相关内容。。。")
        butt_add2["state"]="disable" #添加单词本按钮设为不可用
    else:
        for row in fc:
            check_var2.set(row[0])   #结果显示到界面上
            result_var2.set(row[1])
            butt_add2["state"] = "normal"  # 激活添加按钮
            print "%s,%s" % (row[0], row[1])
    end=time.clock()
    print "离线查询时间为=%s秒" % (end-start) #显示运行时间


# 添加到单词本响应事件
def on_click_add2():
    md = modelHelper()
    # 查询是否单词本已存在该单词，已存在则无需再添加，不存在再添加
    exist = md.selectFromWord_book(check_var2.get().strip())
    if exist == 0:
        mark = "N"
        count = md.addWordbook(check_var2.get().strip(), result_var2.get().strip(), mark)
        mBox.showinfo(title='提示：', message='添加成功！')
        print count
    else:
        alarmstr = "该单词已存在，无需再添加，记录数=%d" % (exist)
        mBox.showinfo(title='提示：', message=alarmstr)
        print alarmstr

#-------------# #离线词典页面----------------------
labeltxt2=tk.Label(monty2,text='输入英文：'.decode('utf8').encode('utf8'), font=('Helvetica', '10', 'bold'))
labeltxt2.grid(column=0, row=0, sticky=tk.W)
# #单行输入文本框
inout_text2 = tk.StringVar()
inout_text2.set('')
edit2 = tk.Entry(monty2 ,font=('Helvetica', '10', 'bold'),width=35,foreground = 'red',highlightbackground = 'blue', relief = 'sunken',background='lightyellow')
edit2['textvariable'] = inout_text2
edit2.grid(column=1, row=0, sticky=tk.W,columnspan=4)

#翻译按钮
butt2 = tk.Button(monty2, text='英译中',background='lightgreen')
butt2['command'] = on_click_EnToZh2
butt2.grid(column=3, row=1, sticky=tk.W)

#翻译按钮英译中
butt2 = tk.Button(monty2, text='中译英',background='lightgreen')
butt2['command'] = on_click_ZhToEn2
butt2.grid(column=4, row=1, sticky=tk.W)

##显示查询结果，单词+解释
check_var2 = tk.StringVar()
check_var2.set('')
check2=tk.Label(monty2,width=31,height=3,bg='lightgray',textvariable=check_var2, relief="ridge",borderwidth=2,font=('Helvetica', '14', 'bold'),anchor="w",justify="left")
check2.grid(column=0, row=2, sticky=tk.W,columnspan=5)

result_var2 = tk.StringVar()
result_var2.set('')
text_result2=tk.Label(monty2,width=31,height=12,bg='lightgray',textvariable=result_var2,relief="ridge",borderwidth=2, font=('Helvetica', '14', 'bold'),anchor="nw",wraplength=350,justify="left")
text_result2.grid(column=0, row=3, sticky=tk.W,columnspan=5)

# #添加单词本按钮
butt_add2 = tk.Button(monty2, text='添加到我的单词本',background='pink')
butt_add2['command'] = on_click_add2
butt_add2.grid(column=2, row=4, sticky=tk.W,columnspan=1)
butt_add2["state"] = "disable"  #添加单词本按钮初始化未激活状态
# ---------------Tab2控件介绍------------------#


# ---------------Tab3控件介绍----在线翻译词典--------------#
monty3 = ttk.LabelFrame(tab3, text='')
monty3.grid(column=0, row=0, padx=8, pady=4)


def on_click_Online_ZhToEn3():
    start = time.clock()  # 测试离线查询的时间

    global result_var3  # 全局变量
    global check_var3

    check_var3.set('')  # 清空原有内容
    result_var3.set('')

    md = modelHelper()
    word = edit3.get()  # 获取单词

    str = md.onlineSelect_ZhToEn(word)  # 在线查询，返回查询结果
    check_var3.set(word)  # 结果显示到界面上
    result_var3.set(str)
    butt_add3["state"] = "normal"  # 激活添加按钮
    print "%s,%s" % (word, str)

    end = time.clock()
    print "离线查询时间为=%s秒" % (end - start)  # 显示运行时间

#在线翻译按钮响应事件 显示查询结果
def on_click_Online_EnToEn3():
    start = time.clock()  # 测试在线查询的时间

    global result_var3  # 全局变量
    global check_var3

    check_var3.set('')  # 清空原有内容
    result_var3.set('')

    md = modelHelper()
    word = edit3.get()  # 获取单词

    str = md.onlineSelect(word)  # 在线查询，返回查询结果
    check_var3.set(word)  # 结果显示到界面上
    result_var3.set(str)
    butt_add3["state"] = "normal"  # 激活添加按钮
    print "%s,%s" % (word, str)

    end = time.clock()
    print "在线查询时间为=%s秒" % (end - start)  # 显示运行时间


# 添加到单词本响应事件
def on_click_add_Online3():
    md = modelHelper()
    # 查询是否单词本已存在该单词，已存在则无需再添加，不存在再添加
    exist = md.selectFromWord_book(check_var3.get().strip())
    if exist == 0:
        mark = "N"
        count = md.addWordbook(check_var3.get().strip(), result_var3.get().strip(), mark)
        mBox.showinfo(title='提示：', message='添加成功！')
        print count
    else:
        alarmstr = "该单词已存在，无需再添加，记录数=%d" % (exist)
        mBox.showinfo(title='提示：', message=alarmstr)
        print alarmstr
        print "on_click_add!"

#------------- #在线词典页面----------------------
labeltxt3=tk.Label(monty3,text='输入：'.decode('utf8').encode('utf8'), font=('Helvetica', '10', 'bold'))
labeltxt3.grid(column=0, row=0, sticky=tk.W)
# #单行输入文本框
inout_text3 = tk.StringVar()
inout_text3.set('')

edit3 = tk.Entry(monty3 ,font=('Helvetica', '10', 'bold'),width=40,foreground = 'red',highlightbackground = 'blue', relief = 'sunken',background='lightyellow')
edit3['textvariable'] = inout_text3
edit3.grid(column=1, row=0, sticky=tk.W,columnspan=4)

#翻译按钮中译英
butt3 = tk.Button(monty3, text='英译中',background='lightgreen')
butt3['command'] = on_click_Online_EnToEn3
butt3.grid(column=3, row=1, sticky=tk.W)


#翻译按钮英译中
butt31 = tk.Button(monty3, text='中译英',background='lightgreen')
butt31['command'] = on_click_Online_ZhToEn3
butt31.grid(column=4, row=1, sticky=tk.W)


##显示查询结果，单词+解释
check_var3 = tk.StringVar()
check_var3.set('')
check3=tk.Label(monty3,width=31,height=3,bg='lightblue',textvariable=check_var3, relief="ridge",borderwidth=2,font=('Helvetica', '14', 'bold'),anchor="w",justify="left")
check3.grid(column=0, row=2, sticky=tk.W,columnspan=5)

result_var3 = tk.StringVar()
result_var3.set('')
text_result3=tk.Label(monty3,width=31,height=12,bg='lightblue',textvariable=result_var3,relief="ridge",borderwidth=2, font=('Helvetica', '14', 'bold'),anchor="nw",wraplength=350,justify="left")
text_result3.grid(column=0, row=3, sticky=tk.W,columnspan=5)

# #添加单词本按钮
butt_add3 = tk.Button(monty3, text='添加到我的单词本',background='pink')
butt_add3['command'] = on_click_add_Online3
butt_add3.grid(column=2, row=4, sticky=tk.W,columnspan=1)
butt_add3["state"] = "disable"  #添加单词本按钮初始化未激活状态
# ---------------Tab3控件介绍------------------#


# ---------------Tab4控件介绍-句子翻译---中英互译--------------#
monty4 = ttk.LabelFrame(tab4, text='')
monty4.grid(column=0, row=0, padx=8, pady=4)

#在线翻译按钮响应事件 显示查询结果
def on_click_Online_ZhToEn4():
    start = time.clock()  # 测试离线查询的时间

    global result_var4  # 全局变量
    global check_var4

    check_var4.set('')  # 清空原有内容
    result_var4.set('')

    md = modelHelper()
    word = edit4.get("0.0","end").strip()  # 获取单词
    print "word=%s" % (word)
    str = md.onlineSelect_ZhToEn(word)  # 在线查询，返回查询结果
    check_var4.set(word)  # 结果显示到界面上
    result_var4.set(str)
    butt_add4["state"] = "normal"  # 激活添加按钮
    print "%s,%s" % (word, str)

    end = time.clock()
    print "离线查询时间为=%s秒" % (end - start)  # 显示运行时间

#在线翻译按钮响应事件 显示查询结果
def on_click_Online_EnToEn4():
    start = time.clock()  # 测试在线查询的时间

    global result_var4  # 全局变量
    global check_var4

    check_var4.set('')  # 清空原有内容
    result_var4.set('')

    md = modelHelper()
    word = edit4.get("0.0","end").strip()  # 获取单词
    print "word=%s" % (word)
    str = md.onlineSelect(word)  # 在线查询，返回查询结果
    check_var4.set(word)  # 结果显示到界面上
    result_var4.set(str)
    butt_add4["state"] = "normal"  # 激活添加按钮
    print "%s,%s" % (word, str)

    end = time.clock()
    print "在线查询时间为=%s秒" % (end - start)  # 显示运行时间

# 添加到单词本响应事件
def on_click_add_Online4():
    md = modelHelper()
    # 查询是否单词本已存在该单词，已存在则无需再添加，不存在再添加
    exist = md.selectFromWord_book(check_var4.get().strip())
    if exist == 0:
        mark = "N"
        count = md.addWordbook(check_var4.get().strip(), result_var4.get().strip(), mark)
        mBox.showinfo(title='提示：', message='添加成功！')
        print count
    else:
        alarmstr = "该单词已存在，无需再添加，记录数=%d" % (exist)
        mBox.showinfo(title='提示：', message=alarmstr)
        print alarmstr
        print "on_click_add!"

#-------------
#在线翻译页面
labeltxt4=tk.Label(monty4,text='输入：'.decode('utf8').encode('utf8'), font=('Helvetica', '10', 'bold'))
labeltxt4.grid(column=0, row=0, sticky=tk.W)
#单行输入文本框
inout_text4 = tk.StringVar()
inout_text4.set('')
edit4=tk.Text(monty4,width=40,height=10,font=('Helvetica', '10', 'bold'))
edit4.grid(column=1, row=0, sticky=tk.W,columnspan=4)

#翻译按钮中译英
butt4 = tk.Button(monty4, text='英译中',background='lightgreen')
butt4['command'] = on_click_Online_EnToEn4
butt4.grid(column=3, row=4, sticky=tk.W)


#翻译按钮英译中
butt4 = tk.Button(monty4, text='中译英',background='lightgreen')
butt4['command'] = on_click_Online_ZhToEn4
butt4.grid(column=4, row=4, sticky=tk.W)


#显示查询结果，单词+解释
check_var4 = tk.StringVar()
check_var4.set('')

result_var4 = tk.StringVar()
result_var4.set('')
text_result4=tk.Label(monty4,width=31,height=8,bg='lightblue',textvariable=result_var4,relief="ridge",borderwidth=2, font=('Helvetica', '14', 'bold'),anchor="nw",wraplength=350,justify="left")
text_result4.grid(column=0, row=5, sticky=tk.W,columnspan=5)

#添加单词本按钮
butt_add4 = tk.Button(monty4, text='添加到我的单词本',background='pink')
butt_add4['command'] = on_click_add_Online4
butt_add4.grid(column=2, row=6, sticky=tk.W,columnspan=1)
butt_add4["state"] = "disable"  #添加单词本按钮初始化未激活状态
# ---------------Tab4控件介绍------------------#


# ---------------Tab5控件介绍--屏幕取词--------------#
monty7 = ttk.LabelFrame(tab7, text='')
monty7.grid(column=0, row=0, padx=8, pady=4)
#屏幕取词按钮响应事件
def Capture_Word_on_Screen_h():
    #start = time.clock()  # 测试在线查询的时间
    global result_var7  # 全局变量
    global check_var7

    check_var7.set('')  # 清空原有内容
    result_var7.set('')

    # 隐藏当前界面
    #HideWindow(win)

    md = modelHelper()
    list1 =[]
    list1 = md.Capture_Word_on_Screen()

    #重新显示界面
    #ShowWindow(win)

    #返回单词及意思，在此需要进一步分离
    # 获取单词
    # 意思
    check_var7.set(list1[0])  # 结果显示到界面上
    result_var7.set(list1[1])
    butt_add7["state"] = "normal"  # 激活添加按钮

    #nd = time.clock()
    #print "在线查询时间为=%s秒" % (end - start)  # 显示运行时间

# 添加到单词本响应事件
def on_click_add_Online7():
    md = modelHelper()
    # 查询是否单词本已存在该单词，已存在则无需再添加，不存在再添加
    exist = md.selectFromWord_book(check_var7.get().strip())
    if exist == 0:
        mark = "N"
        count = md.addWordbook(check_var7.get().strip(), result_var7.get().strip(), mark)
        mBox.showinfo(title='提示：', message='添加成功！')
        print count
    else:
        alarmstr = "该单词已存在，无需再添加，记录数=%d" % (exist)
        mBox.showinfo(title='提示：', message=alarmstr)
        print alarmstr
        print "on_click_add!"


#-------------
# #屏幕取词页面
#屏幕取词按钮
butt7 = tk.Button(monty7, text='开始屏幕取词',background='lightgreen')
butt7['command'] = Capture_Word_on_Screen_h
butt7.grid(column=4, row=0, sticky=tk.W)


# ##显示查询结果，单词+解释
check_var7 = tk.StringVar()
check_var7.set('')
text_word7=tk.Label(monty7,width=31,height=6,bg='lightblue',textvariable=check_var7,relief="ridge",borderwidth=2, font=('Helvetica', '14', 'bold'),anchor="nw",wraplength=350,justify="left")
text_word7.grid(column=0, row=1, sticky=tk.W,columnspan=5)


result_var7 = tk.StringVar()
result_var7.set('')
text_result7=tk.Label(monty7,width=31,height=10,bg='lightblue',textvariable=result_var7,relief="ridge",borderwidth=2, font=('Helvetica', '14', 'bold'),anchor="nw",wraplength=350,justify="left")
text_result7.grid(column=0, row=2, sticky=tk.W,columnspan=5)

# #添加单词本按钮
butt_add7 = tk.Button(monty7, text='添加到我的单词本',background='pink')
butt_add7['command'] = on_click_add_Online7
butt_add7.grid(column=4, row=6, sticky=tk.W,columnspan=1)
butt_add7["state"] = "disable"  #添加单词本按钮初始化未激活状态
# ---------------Tab5控件介绍------------------#





# ---------------Tab6控件介绍-我的单词本-----------------#
monty5 = ttk.LabelFrame(tab5, text='')
monty5.grid(column=0, row=0, padx=8, pady=4)

#翻译按钮响应事件 显示查询结果
def on_click5():
    lbword.config(bg='black')
    start = time.clock()  # 测试在线查询的时间
    word = edit5.get()  # 获取单词
    len = lbword.size()
    lbword.select_clear(first=0, last=len) # 清空原来选中内容
    for row in range(len):
        str = lbword.get(row)
        list_str = str.split(':', 1)
        if list_str[0] == word:
            lbword.selection_set(row)

    end = time.clock()
    print "在线查询时间为=%s秒" % (end - start)  # 显示运行时间

#查询我添加的单词本内容
def myWordWork():
    md = modelHelper()
    mywords = md.SelectMyWordBook()
    for row in mywords:
        strs = str(row[0] + ":" + row[1])
        print strs
        lbword.insert(0, strs)
        print "%s,%s" % (row[0], row[1])

#删除单词记录
def on_click_delete5():
    md = modelHelper()
    size=lbword.size()
    print "lbword.curselection()=%s" % (lbword.curselection())
    str=lbword.get(lbword.curselection())
    print "str=%s" % str
    list_str=str.split(':',1)
    print list_str[0]
    print list_str[1]
    count=md.deleteFromMyWordBook(list_str[0])
    if count==1:
        mBox.showinfo(title='提示：', message='删除成功！')
        #刷新结果显示信息
        lbword.delete(0,size)
        myWordWork()
    elif count==0:
        mBox.showinfo(title='提示：', message='该信息不存在！')
    else:
        mBox.showinfo(title='提示：', message='删除失败！')

# ---------------Tab6控件介绍我的单词本-----------------#
label5=tk.Label(monty5,text='输入英文：'.decode('utf8').encode('utf8'), font=('Helvetica', '10', 'bold'))
label5.grid(column=0, row=0, sticky=tk.W)
# #单行输入文本框
inout_text5 = tk.StringVar()
inout_text5.set('')
edit5 = tk.Entry(monty5 ,font=('Helvetica', '10', 'bold'),width=30,foreground = 'red',highlightbackground = 'blue', relief = 'sunken',background='lightyellow')
edit5['textvariable'] = inout_text5
edit5.grid(column=1, row=0, sticky=tk.W,columnspan=2)

#翻译按钮
butt5 = tk.Button(monty5, text='查询',background='lightgreen')
butt5['command'] = on_click5
butt5.grid(column=3, row=0, sticky=tk.W)

#删除按钮
butt_delete5 = tk.Button(monty5, text='删除',background='lightblue')
butt_delete5['command'] = on_click_delete5
butt_delete5.grid(column=4, row=0, sticky=tk.W)

# #显示单词本信息 添加滚动条
word_var = tk.StringVar()
sl=tk.Scrollbar(monty5)
sl.grid(column=5, row=1, rowspan=1,sticky='ns')
sb=tk.Scrollbar(monty5,orient = 'horizontal')
sb.grid(column=0, row=2, columnspan=4,sticky='ew')

scrolW = 35;
scrolH = 17
lbword=tk.Listbox(monty5,font=('Courier New',13),fg='yellow', width=scrolW, height=scrolH,bg='black',listvariable=word_var,selectmode="browse",yscrollcommand = sl.set,xscrollcommand = sb.set)
myWordWork()
lbword.selection_set(0)
lbword.grid(column=0, row=1, sticky=tk.W, columnspan=5, rowspan=1)
sl.configure(command = lbword.yview)
sb.configure(command = lbword.xview)
# ---------------Tab6控件介绍------------------#


# ---------------Tab7控件介绍----退出--------------#
monty6 = ttk.LabelFrame(tab6,text='')
monty6.grid(column=0, row=0, padx=100, pady=100)

def Quits():
    win.quit()
    win.destroy()
    exit()
    sys.exit()

label6=tk.Label(monty6,text='确定退出电子词典系统？'.decode('utf8').encode('utf8'),font=('Helvetica', '10', 'bold'))
label6.grid(column=3, row=4)

buttok6 = tk.Button(monty6, text='YES',background='yellow')
buttok6['command'] = Quits
buttok6.grid(column=3, row=6,sticky=tk.S)
# ---------------Tab7控件介绍------------------#

edit2.focus()
edit3.focus()
# edit4.focus()
edit5.focus()
# ======================
# Start GUI
# ======================
win.mainloop()