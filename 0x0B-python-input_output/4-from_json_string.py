#!/usr/bin/python3
"""
Contains the "from_json_string" function
"""


import json


def from_json_string(my_str):
    """ Function that returns an object by a JSON representation

    Args:
        my_str: JSON representation

    Raises:
        Exception: when the string can't be decoded
    """
    return json.loads(my_str)
