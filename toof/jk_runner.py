import unittest
from BSTestRunner import BSTestRunner
import time


test_dir = './test_case'
report_dir = './reports'


# 加载测试用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_weather01.py')


# 定义测试报告的文件格式
now = time.strftime("%Y-%m-%d %H-%M-%S")
report_name = report_dir + '/' + now + 'test_report.html'

# 运行测试用例并生成测试报告
with open(report_name, "wb") as f:
    runner = BSTestRunner(stream=f, title="Weather api Test Report", description="中国城市天气预报")
    runner.run(discover)

