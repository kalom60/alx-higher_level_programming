#!/usr/bin/python3
"""
Contains the "to_json_string" fundtion
"""


import json


def to_json_string(my_obj):
    """ Function that returns the JSON representation of an object

    Args:
        my_obj: object

    Raises:
        Exception: when the object can't be encoded
    """
    return json.dumps(my_obj)
