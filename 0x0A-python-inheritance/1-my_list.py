#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """ Class that inherits the attributes references of class list

    Args:
        list: class list

    """

    def print_sorted(self):
        list_sorted = self.copy()
        list_sorted.sort()
        print(list_sorted)
