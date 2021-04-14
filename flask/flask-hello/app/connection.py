import pymysql


def db_conn():
    conn = pymysql.connect(host="127.0.0.1", user="qiong",
                           password="qiong", database="qiongblog", charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    sql="select * from `users` " # SQL语句
    cursor.execute(sql) # 执行SQL语句
    data = cursor.fetchall() # 通过fetchall方法获得数据
    for i in data: # 打印输出前2条数据
        print (i)
    #关闭光标对象
    cursor.close
    #关闭数据库
    conn.close()

db_conn()