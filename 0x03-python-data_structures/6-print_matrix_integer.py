#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list1 in matrix:
        for list2 in list1:
            if list1.index(list2) != 0:
                print(" ", end='')
            print("{:d}".format(list2), end='')
        print()
