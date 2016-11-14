import nose.tools
from big_o import O_of_1

test = O_of_1()

test_list = []
for i in range(1, 10000):
    test_list.append(i)


def test_O_of_1():
    assert test.run(test_list) == True
