import pytest
import allure


# 当前路径：D:\Atools\Sublime3\TK_GUI\gui_12.py
# 执行alluer报告  pytest 脚本  --alluredir=存放路径
# 1--用浏览器查看  allure serve 存放路径
# 2-- 生产测试报告随时打开  allure  generate  存放路径  -o  html报告路径  (覆盖路径：加 --clean)
# 3-- allure  open -h 127.0.0.1 -p 8883 html报告路径
# 4--运行指定功能模块即类/方法    pytest 脚本路径 --allure-features '模块名称'/ --allure-stories '方法名称'


def test_success():
    """this  test is succeeds"""
    assert True


def test_failure():
    """this test is  fails"""
    assert False


def test_skip():
    """this  test is  skipped"""
    pytest.skip('for a reason')


def test_broken():
    raise Exception('oops')


@allure.feature("登录-功能")
class TestLogin():

    @allure.story("子功能-账号密码登录成功")
    def test_login_success(self):
        with allure.step("输入账号："):
            print("输入账号:")
        with allure.step("输入密码："):
            print("输入密码：")
        print("这是登录测试用例，账号密码测试用例   测试成功")
        with allure.step("点击登录"):
            assert 1 == 1
            print("登录成功")

    @allure.story("子功能-微信二维码登录成功")
    def test_login_success_a(self):
        print("这是登录用例 微信测试用例a 登录成功")

    @allure.story("子功能-qq登录成功")
    def test_login_success_b(self):
        print("这是登录用例 qq测试用例b 登录成功")

    @allure.story("子功能-账号错误用例")
    def test_login_fail_a(self):
        print("这是登录失败用例-账号错误")

    @allure.story("子功能-密码错误用例")
    def test_login_fail_a(self):
        print("这是登录失败用例-密码错误")

    @allure.story("子功能-二维码错误用例")
    def test_login_fail_a(self):
        print("这是登录失败用例-二维码错误")

    @allure.story("子功能-qq错误用例")
    def test_login_fail_a(self):
        print("这是登录失败用例-qq账号错误")

    @allure.story("子功能-qq密码错误用例")
    def test_login_fail_a(self):
        print("这是登录失败用例-qq密码错误")


@pytest.mark.parametrize("test_input, test_expect", [("9+8", 17), ("6+5", 11), ("5-3", 3)])
def test_eval(test_input, test_expect):
    # eval 将字符串str当成有效的表达式来求值，并返回结果
    assert eval(test_input) == test_expect

