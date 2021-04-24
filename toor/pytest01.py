import pytest
import random


class Test_ABC:
    def setup(self):
        print("---------->setup_method")

    def teardown(self):
        print("**********>teardown_method")

    def test_a(self):
        print("-------->test_a")
        assert 1

    def test_b(self):
        print("--------->test_b")

#
# if __name__ == '__main__':
#     pytest.main(['-s', 'pytest01.py'])


data1 = ['linda', 'swag']


@pytest.fixture(params=data1)
def data(request):
    print("数据准备--->")
    a = request.param
    #print(a)
    return a


@pytest.mark.parametrize('data', data1, indirect=True)
def test_data(data):
    print(data)


@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_simple_assume(x, y):
    pytest.assume(x == y)
    pytest.assume(True)
    pytest.assume(False)


if __name__ == '__main__':
    pytest.main(['-s', 'pytest01.py'])
