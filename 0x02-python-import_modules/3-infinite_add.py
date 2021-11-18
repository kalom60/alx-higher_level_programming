#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    num = 0
    for arg in range(1, len(sys.argv)):
        num += int(sys.argv[arg])
    print(num)
