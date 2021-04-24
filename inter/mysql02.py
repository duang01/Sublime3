from pymysql import connect


class JD(object):
    def __init__(self):
        # 创建Connection对象,包含数据库主机地址，端口，用户名及密码，相对应的数据编码格式
        self.conn = connect(host="localhost", port=3306, user='root', password='mysql', database='jin_dong',
                            charset='utf8')
        # 获取游标对象Cursor
        self.cursor = self.conn.cursor()

    def __del__(self):
        # 关闭Cursor 对象
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_cate(self):
        sql = "select name from goods_cate;"
        self.execute_sql(sql)

    def show_all_items(self):
        """显示所有的商品"""
        sql = "select * form goods;"
        self.execute_sql(sql)

    def show_brands(self):
        sql = "select name from goods_brands;"
        self.execute_sql(sql)

    @staticmethod
    def print_menu():
        print("------->京东<-------")
        print("1: 所有的商品")
        print("2：所有的商品分类")
        print("3.所有的商品品牌分类")
        num = input("请输入相应的数字：")
        return num

    def run(self):
        while True:
            num = self.print_menu()
            if num == "1":
                # 查询所有的商品
                self.show_all_items()

            elif num == "2":
                # 查询商品分类
                self.show_cate()

            elif num == "3":
                # 查询品牌分类
                self.show_brands()

            else:
                print("输入有误，请重新输入---")


def main():
    # 1. 创建一个京东商城对象
    jd = JD()

    # 2.调用这个对象的run方法，让其运行
    jd.run()


if __name__ == "__main__":
    main()