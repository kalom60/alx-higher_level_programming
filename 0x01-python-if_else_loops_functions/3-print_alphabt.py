#!/usr/bin/python3
for string in range(97, 123):
    if string != 101 and string != 113:
        print("{:c}".format(string), end='')
