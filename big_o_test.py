import nose.tools
from big_o import O_of_1

test1 = O_of_1()
test2 = O_of_N()

test_list = []
for i in range(1, 10000):
    test_list.append(i)


def test_O_of_1_tells_truth():
    assert test1.run(test_list) == True

def test_O_of_N():
    returned_list = test2.run(test_list)
    assert returned_list[880] == test_list[880] * 2
 
