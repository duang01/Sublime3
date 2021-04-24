import logging


class BaseTestCase(object):
    logging.basicConfig()
    _log = logging.getLogger("loglog")  # 生成自己的log日志，指定级别
    _log.setLevel(logging.DEBUG)

    @property       # 表示属性
    def log(self):
        return self._log