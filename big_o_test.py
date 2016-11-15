import nose.tools
from big_o import BigO_of_1, BigO_of_N

test_of_1 = BigO_of_1()
test_of_N = BigO_of_N()

test_list = []
for i in range(1, 10000):
    test_list.append(i)


def test_O_of_1_tells_truth():
    assert test_of_1.check_index_0(test_list) == True

def test_O_of_N():
    returned_list = test_of_N.double_values(test_list)
    assert returned_list[880] == test_list[880] * 2
 
