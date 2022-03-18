#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
"""

if __name__ == "__main__":

    from urllib.request import urlopen
    import sys

    with urlopen(sys.argv[1]) as res:
        print(res.getheader("X-Request-Id"))
