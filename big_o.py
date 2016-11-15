class BigO_of_1(object):
    def check_index_0_is_int(self, value_list):
        if value_list[0] == int(value_list[0]):
           return True

class BigO_of_N(object):
    def double_values(self, value_list):
        finished_list = []
        for i in value_list:
            finished_list.append(i * 2)
        return finished_list
