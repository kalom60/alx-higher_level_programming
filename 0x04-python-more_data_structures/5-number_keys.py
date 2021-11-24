#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    keylist = list(a_dictionary.keys())
    for i in keylist:
        count += 1
    return count
