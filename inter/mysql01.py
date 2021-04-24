from pymysql import *


def main():
    # 创建Connection对象,包含数据库主机地址，端口，用户名及密码，相对应的数据编码格式
    conn = connect(host='localhost', port=3306, user='root', password='mysql', database='jin_dong', charset='utf-8')

    # 获取游标对象Cursor
    cs1 = conn.cursor()

    # 执行SQL语句，返回受影响的行数，打印相对应的数据
    count = cs1.execute('select id,name from goods where id>+4')

    # 打印受影响的行数
    print("查询到%d条数据："%count)

    for i in range(count):
        # 获取查询到的数据;fetchall 表示所有，fetchone 表示一条；fetchmany(5)表示多条
        result = cs1.fetchall()
        print(result)

    # 若是增删改需要commit提交,查询是不需要提交的，切记-！！！
    conn.commit()
    # 若是反悔了不提交了可以用rollback 进行撤销
    conn.rollback()
    # 先关闭游标再关闭连接
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()