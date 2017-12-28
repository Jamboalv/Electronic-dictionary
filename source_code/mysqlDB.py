#!/user/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')

class MysqldbHelper:
    # 获取数据库连接-MYSQL数据库
    def getCon(self):
        try:
            reload(sys)
            sys.setdefaultencoding('utf8')

            conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', port=3306, charset='utf8')
            conn.select_db('dictionary')
            return conn
        except MySQLdb.Error, e:
            print "Mysqldb Error:%s" % e

    # 查询方法，返回元组类型数据，若使用con.cursor(MySQLdb.cursors.DictCursor),返回结果为(字典)
    def select(self, sql):
        try:
            con = self.getCon()
            print con
            # cur = con.cursor(MySQLdb.cursors.DictCursor)
            cur = con.cursor()
            cur.execute('SET NAMES UTF8')
            count = cur.execute(sql)
            fc = cur.fetchall()
            return fc
        except MySQLdb.Error, e:
            print "Mysqldb Error:%s" % e
        finally:
            cur.close()
            con.close()




     # 查询，返回结果为影响行数，判断是否存在该记录
    def selectCount(self, sql):
        try:
            con = self.getCon()
            print con
            # cur = con.cursor(MySQLdb.cursors.DictCursor)
            cur = con.cursor()
            cur.execute('SET NAMES UTF8')
            count = cur.execute(sql)
            # fc = cur.fetchall()
            return count
        except MySQLdb.Error, e:
            print "Mysqldb Error:%s" % e
        finally:
            cur.close()
            con.close()

    # 带参数的更新方法,可执行插入、更新操作，返回影响行数
    def updateByParam(self, sql, params):
        try:
            con = self.getCon()
            cur = con.cursor()
            count = cur.execute(sql, params)
            con.commit()        #提交事务
            return count
        except MySQLdb.Error, e:
            con.rollback()
            print "Mysqldb Error:%s" % e
        finally:
            cur.close()
            con.close()

    # 不带参数的更新方法，，返回影响行数
    def update(self, sql):
        try:
            con = self.getCon()
            cur = con.cursor()
            count = cur.execute(sql)
            con.commit()
            return count
        except MySQLdb.Error, e:
            con.rollback()
            print "Mysqldb Error:%s" % e
        finally:
            cur.close()
            con.close()


if __name__ == "__main__":
    db=MysqldbHelper()
    word="book"
    sql="select * from mydict where word='%s'" % (word)
    dict1=db.select(sql)
    print dict1
    # j=json.dumps(dict1)
    # dict2=j.decode("unicode-escape").decode("unicode-escape")
    # print dict2
    db.addWordbook('like', '喜欢', 'N')


    def get():
        sql = "select * from pythontest"
        fc = db.select(sql)
        for row in fc:
            print row["ptime"]


    def ins():
        sql = "insert into pythontest values(5,'数据结构','this is a big book',now())"
        count = db.update(sql)
        print count


    def insparam():
        sql = "insert into pythontest values(%s,%s,%s,now())"
        params = (6, 'C#', 'good book')
        count = db.updateByParam(sql, params)
        print count


    def delop():
        sql = "delete from pythontest where pid=4"
        count = db.update(sql)
        print "the：" + str(count)


    def change():
        sql = "update pythontest set pcontent='c# is a good book' where pid=6"
        count = db.update(sql)
        print count

        # get()
        # ins()
        # insparam()
        # delop()
        # change()




