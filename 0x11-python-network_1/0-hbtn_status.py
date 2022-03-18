#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """

if __name__ == "__main__":
    from urllib.request import urlopen

    with urlopen('https://alx-intranet.hbtn.io/status') as res:
        result = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(result)))
        print("\t- content: {}".format(result))
        print("\t- utf8 content: {}".format(result.decode("utf-8")))
