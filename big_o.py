class BigO_of_1(object):
    def check_index_0_is_int(self, value_list):
        if value_list[0] == int(value_list[0]):
           return True

class BigO_of_N(object):
    def double_values(self, value_list):
        for i in range(0, len(value_list)):
            value_list[i] *= 2
        return value_list

class BigO_of_N_Squared(object):
    def create_spam_field(self, value_list):
        for i in range(0, len(value_list)):
            value_list[i] = []
            for j in range(0, len(value_list)):
                value_list[i].append('spam')
        return value_list

class BigO_of_N_Cubed(object):
    def create_spam_space(self, value_list):
        for i in range(0, len(value_list)):
            value_list[i] = []
            for j in range(0, len(value_list)):
                value_list[i].append([])
                for k in range (0, len(value_list)):
                    value_list[i][j].append('spam')
        return value_list
