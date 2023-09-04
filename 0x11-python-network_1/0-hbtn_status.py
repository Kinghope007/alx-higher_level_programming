#!/usr/bin/python3
""" A Script that
     fetches https://alx-intranet.hbtn.io/status
     use the package urllib
     The body of the response must be displayed like the following example (tabulation before -)
"""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
