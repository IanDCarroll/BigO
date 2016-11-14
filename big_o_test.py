import nose.tools
from big_o import O_of_1

test = O_of_1()

test_list = []
for i in range(0, 10000):
    test_list.append(i)


def test_O_of_1():
    assert O_of_1.run(test_list) == True
