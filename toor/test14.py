#数据库的连接和使用

import pymysql

#1.打开数据库连接  主机地址 端口号3306 用户名 密码

db = pymysql.Connect(host="localhost",port=3306,user="root",password="",db="数据库名",charset="utf-8")

#创建一个游标对象 cursor()
cursor = db.cursor()

#定义sql语句  创建一个表
sql = """create table  student(id int not null ,name varchar (20),age int )"""

#定义sql语句 向表增加数据
sql = """insert into student(id,name,age) values (1,"zhangsan",12)"""

cursor.execute(sql)  #执行插入语句
db.commit()          #提交数据至数据库

# 查询数据
sql = """ select * from student where id=1"""
cursor.execute(sql)
data1 = cursor.fetchone()       #获取单个对象（单行数据）
print(data1[1])

data2 = cursor.fetchall()       #获取多行数据及所有，所获数据都是元祖
print(data2)
db.close()

#数据库的更新和删除操作
sql = """update student set age=age+1"""    #更新数据
cursor.execute(sql)
db.commit()
db.close()

#删除操作
sql = """ delete from student where name='lisi'"""
cursor.execute()
db.commit()
cursor.close(sql)   #执行关闭表
db.close()         #关闭数据库

#异常事务的处理

try:
    cursor.execute(sql)
    db.commit()
except Exception as E:
    db.rollback()    #回滚,所有操作都不提交
    print("执行错误！")