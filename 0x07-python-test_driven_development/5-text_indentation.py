#!/usr/bin/python3
"""

Module that prints 2 new line after ".?:" characters

"""


def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters

    Args:
        text: input string

    Returns:
        no return

    Raises:
        TypeError: If text is not a string


    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    f = 0
    for string in text:
        if f == 0:
            if string == ' ':
                continue
            else:
                f = 1
        if f == 1:
            if string == '?' or string == '.' or string == ':':
                print(string)
                print()
                f = 0
            else:
                print(string, end="")
