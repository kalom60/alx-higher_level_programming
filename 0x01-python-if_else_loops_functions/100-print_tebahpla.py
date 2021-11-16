#!/usr/bin/python3
for string in reversed(range(97, 123)):
    print("{:c}".format(string if string % 2 == 0 else string - 32), end='')
