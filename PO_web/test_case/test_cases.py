import unittest
from PO_web.pageObject.seach_page import SearchPage
from selenium import webdriver
from time import sleep
from ddt import ddt, data, unpack


@ddt
class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        drive = webdriver.Firefox()
        self.sp = SearchPage(drive)

    def tearDown(self) -> None:
        self.sp.quit_browser()

    @data(['http://www.baidu.com', '光头强', '光头强_百度搜索'], ['http://www.baidu.com', '霍格沃兹', '霍格沃兹_百度搜索'])
    @unpack
    def test_1(self, url, input_text, err):
        self.sp.check(url, input_text)
        sleep(3)
        self.assertEqual(self.sp.get_title(), err, msg='对不起，你还不知道呢')


if __name__ == '__main__':
    unittest.main()