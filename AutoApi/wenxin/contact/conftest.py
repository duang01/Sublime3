
import pytest

from AutoApi.wenxin.contact.token import Weixin


@pytest.fixture(scope="session")
def token():
    return Weixin.get_token_new()
