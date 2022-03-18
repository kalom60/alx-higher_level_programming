#!/usr/bin/python3
"""
a python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response
"""
if __name__ == "__main__":
    from urllib import request, parse
    import sys
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = parse.urlencode(value)
    data = data.encode("utf-8")
    req = request.Request(url, data)
    with request.urlopen(req) as resp:
        new = resp.read()
        print(new.decode("utf-8"))
