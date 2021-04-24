import pytest
import time
import random


def add(x, y):
    return x+y


# @pytest.mark.parametrize("x, y", [(4+3, 7), (4+5, 8), (4*4, 16), ('test'+'home', 'testhome')])
# def test_add(x, y):
#     assert x == y

@pytest.mark.run(order=1)
def test_add1():
    #time.sleep(random.randint(2, 6))
    pytest.assume(add(4, 2) == 6)
    pytest.assume(add(4, 3) == 7)
    pytest.assume(add(4, 2) == 6)
    pytest.assume(add('test', 'home') == 'testhome')

