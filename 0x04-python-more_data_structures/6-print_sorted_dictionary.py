#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordlist = list(a_dictionary.keys())
    ordlist.sort()
    for i in ordlist:
        print("{}: {}".format(i, a_dictionary.get(i)))
