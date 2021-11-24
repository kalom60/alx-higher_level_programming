#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    over = 0

    for val in my_list:
        num += val[0] * val[1]
        over += val[1]

    return (num / over)
