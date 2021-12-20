#!/usr/bin/python3
"""
Contains the lookup function
"""


def lookup(obj):
    """ Function that returns the list of
        available attributes and methods of
        an object

    Args:
        obj: Instance of the class

    Returns:
        List of attributes
    """

    return dir(obj)
