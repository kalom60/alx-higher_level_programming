#!/usr/bin/python3
def common_elements(set_1, set_2):
    c_set = []
    for string in set_1:
        if string in set_2:
            c_set.append(string)
    return c_set
