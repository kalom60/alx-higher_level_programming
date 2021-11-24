#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for val in new_dic.keys():
        new_dic[val] *= 2
    return new_dic
