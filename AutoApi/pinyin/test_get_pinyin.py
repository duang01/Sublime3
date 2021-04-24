import pytest

from AutoApi.xpinyin import Pinyin


class TestDefaultValue:
    @pytest.fixture(scope='module', autouse=True)
    def test_all_default(self):
        assert Pinyin().get_pinyin(u"上海") == "shanghai"
