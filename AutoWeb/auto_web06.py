"""使用unittest 测试框架"""
import unittest


class Test(unittest.TestCase):

    def setUp(self):  # 初始化测试用例
        print("每个测试用例开始执行前执行")

    def tearDown(self):
        print("每个测试用例执行后执行")

    def test_001(self):
        print("测试用例001")
        try:
            self.assertEqual('1', '2', msg="1 不等于 2，测试错误")
        except Exception:
            print("不得了了啊")

    def test_002(self):
        print("测试用例002")
        self.assertEqual('1', '1', msg="1 等于 1，测试欧克")

    def test_003(self):
        print("测试用例003")


if __name__ == '__main__':
    # unittest.main()
    # 创建测试套件
    suit = unittest.TestSuite()
    # 向测试套件中加载测试用例
    case_list = ['test_001', 'test_002', 'test_003']
    for case in case_list:
        suit.addTest(case)

    # 运行测试用例，verbosity2为每一个测试用例输出报告，run=的参数是测试套件
    unittest.TextTestRunner(verbosity=2).run(suit)
