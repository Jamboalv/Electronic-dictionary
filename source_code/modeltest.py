#!/user/bin/env python
# -*- coding: utf-8 -*-

from mysqlDB import MysqldbHelper
from baiduAPI import Translation
from baiduAPI_ZhToEn import Translation_ZhToEn
from screen_shot import *
class modelHelper:
    # 离线查询单词，输入参数：单词，返回结果：一行记录（元组类型）
    def outlineSelect(self,word):
        db = MysqldbHelper()
        sql = "select * from mydict where word='%s'" % (word)
        fc= db.select(sql)
        return fc

    # 添加单词本，输入参数：单词，解释，标记，返回结果：影响行数
    def addWordbook(self,word,explain,mark):
        db = MysqldbHelper()
        #now()函数表示添加时间
        sql = "insert into word_book (word_add,explain_add,mark_add,time_add) values (%s,%s,%s,now())"
        params=(word,explain,mark)
        count = db.updateByParam(sql, params)
        print count
        return count

    # 单词本里查询该记录是否已经存在，输入参数：单词，返回结果：影响行数
    def selectFromWord_book(self,word):
        db = MysqldbHelper()
        sql = "select * from word_book where word_add='%s'" % (word)
        count = db.selectCount(sql)
        return count

    # 在线查询,输入单词,返回结果  英译中
    def onlineSelect(self,word):
        Trans = Translation()
        str = Trans.StartTrans(word)
        return str

    def deleteFromMyWordBook(self, word):
        db = MysqldbHelper()
        sql = "delete from word_book where word_add='%s'" % (word)
        count = db.update(sql)
        return count

    # 在线查询,输入单词,返回结果 中译英
    def onlineSelect_ZhToEn(self, word):
        Trans = Translation_ZhToEn()
        str = Trans.StartTrans_ZhToEn(word)
        return str

    #中文翻译为英文,输入参数为中文，输出
    def zhongYiYing(self,explain):
        db = MysqldbHelper()
        print explain
        explain = "%"+explain +"_,%"
        sql = "select * from mydict where mydict.explain LIKE '%s'" % (explain)

        print sql
        fc = db.select(sql)
        return fc
        # 查询单词本，输入参数：单词，返回结果：所有记录

    def SelectMyWordBook(self):
        db = MysqldbHelper()
        sql = "select * from word_book"
        fc = db.select(sql)
        return fc

    #调用屏幕取词接口
    def Capture_Word_on_Screen(self):
        list1=[]
        f = open('./ret.txt')
        word = f.read()
        list1.append(word)

        Trans = Translation()
        str = Trans.StartTrans(word)
        list1.append(str)

        return list1


if __name__ == "__main__":
    md=modelHelper()

    #md.Capture_Word_on_Screen()
