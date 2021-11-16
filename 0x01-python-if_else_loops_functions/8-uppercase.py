#!/usr/bin/python3
def uppercase(str):
    for string in str:
        if ord(string) > 32:
            print("{:c}".format(ord(string) - 32))
        else:
            print("{:c}".format(ord(string) - 0))
