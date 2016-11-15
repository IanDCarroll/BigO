import nose.tools
import big_o 

test_of_1 = big_o.BigO_of_1()
test_of_N = big_o.BigO_of_N()
test_of_N_Squared = big_o.BigO_of_N_Squared()
test_of_N_Cubed = big_o.BigO_of_N_Cubed()
test_of_N_Four = big_o.BigO_of_N_to_the_Fourth()
test_of_2_N = big_o.BigO_of_2_to_the_N()

test_list = []
for i in range(0, 100):
    test_list.append(i)


def test_O_of_1_tells_truth():
    assert test_of_1.check_index_0_is_int(test_list) == True

def test_O_of_N_Doubles_lists():
    returned_list = test_of_N.double_values(test_list)
    assert returned_list[88] == 176
 
def test_O_of_N_Squared_makes_a_spam_field():
    returned_list = test_of_N_Squared.create_spam_field(test_list)
    assert len(returned_list) == 100
    assert len(returned_list[88]) == 100
    assert returned_list[88][88] == 'spam'

def test_O_of_N_Cubed_makes_a_spam_space():
    returned_list = test_of_N_Cubed.create_spam_space(test_list)
    assert len(returned_list) == 100
    assert len(returned_list[88]) == 100
    assert len(returned_list[88][88]) == 100
    assert returned_list[88][88][88] == 'spam'

def test_O_of_N_Four_Makes_a_spam_hyperspace():
    returned_list = test_of_N_Four.create_spam_hyperspace(test_list)
    assert len(returned_list) == 100
    assert len(returned_list[88]) == 100
    assert len(returned_list[88][88]) == 100
    assert len(returned_list[88][88][88]) == 100
    assert returned_list[88][88][88][88] == 'spam'

def test_O_of_2_N_Gives_the_right_factorial():
    result = test_of_2_N.get_factorial(8)
    assert result == 40320
