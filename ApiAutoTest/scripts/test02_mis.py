import pytest

from ApiAutoTest.api.api_mis import ApiMis
from ApiAutoTest.tools.get_log import GetLog
from ApiAutoTest.tools.read_yaml import read_yaml
from ApiAutoTest.tools.tools import Tools

log = GetLog.get_logger()


class TestMis:
    # 1、初始化
    def setup_class(self):
        log.info("获取后台mis登录对象")
        # 获取ApiMis登录对象
        self.mis = ApiMis()

    # 2、登录
    @pytest.mark.parametrize("account,password", read_yaml("mis_login.yaml"))
    def test01_mis_login(self, account, password):
        # 1、调用登录接口
        r = self.mis.api_mis_login(account, password)
        try:
            # 2、提取token
            Tools.common_token(r)
            # 3、登录断言
            Tools.common_assert(r)
        except Exception as e:
            # 1、日志
            log.error(e)
            # 2、抛异常
            raise

    # 3、查询文章
    def test02_mis_search(self):
        # 1、调用查询接口
        r = self.mis.api_mis_search()
        try:
            # 2、断言
            Tools.common_assert(r, status_code=200)
        except Exception as e:
            log.error(e)
            raise

    # 4、审核文章
    def test03_mis_audit(self):
        r = self.mis.api_mis_audit()
        try:
            Tools.common_assert(r)
        except Exception as e:
            log.error(e)
            raise
