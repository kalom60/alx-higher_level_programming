#!/usr/bin/python3
def uppercase(str):
    num = 0
    for string in str:
        if ord(string) >= 97 and ord(string) <= 122:
            num = 32
        else:
            num = 0
        print("{:c}".format(string), end='')
    print()
