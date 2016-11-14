class O_of_1(object):
    def run(self, value_list):
        if value_list[0]:
           return True

class O_of_N(object):
    def run(self, value_list):
        finished_list = []
        for i in value_list:
            finished_list.append(i * 2)
        return finished_list
