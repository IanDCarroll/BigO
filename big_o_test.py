import nose.tools
from big_o import BigO_of_1, BigO_of_N, BigO_of_N_Squared

test_of_1 = BigO_of_1()
test_of_N = BigO_of_N()
test_of_N_Squared = BigO_of_N_Squared()

test_list = []
for i in range(0, 10000):
    test_list.append(i)


def test_O_of_1_tells_truth():
    assert test_of_1.check_index_0_is_int(test_list) == True

def test_O_of_N_Doubles_lists():
    returned_list = test_of_N.double_values(test_list)
    assert returned_list[880] == 1760
 
def test_O_of_N_Squared():
    returned_list = test_of_N_Squared.field_of_spam(test_list)
    assert len(returned_list[880]) == 10000
    assert returned_list[880][880] == 'spam'
