#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_num = my_list[0]
        for val in my_list:
            if val > max_num:
                max_num = val
        return max_num
