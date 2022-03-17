#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ Function that find a peak """
    if list_of_integers == []:
        return None
    size = len(list_of_integers)
    middle = int(size / 2)
    lint = list_of_integers

    if middle - 1 < 0 and middle + 1 >= size:
        return lint[middle]
    elif middle - 1 < 0:
        if lint[middle] > lint[middle + 1]:
            return lint[middle]
        else:
            return lint[middle + 1]
    elif middle + 1 >= size:
        if lint[middle] > lint[middle - 1]:
            return lint[middle]
        else:
            return lint[middle - 1]
    elif lint[middle - 1] < lint[middle] > lint[middle + 1]:
        return lint[middle]
    elif lint[middle + 1] > lint[middle - 1]:
        return find_peak(lint[middle:])
    return find_peak(lint[:middle])
