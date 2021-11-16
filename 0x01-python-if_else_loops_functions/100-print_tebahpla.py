#!/usr/bin/python3
for string in reversed(range(97, 123)):
    if string % 2 != 0:
        string = string - 32
    print("{:c}".format(string), end='')
