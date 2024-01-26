#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the url,
and display the value od X-request-id variavble found
in the header of the response
"""


import urllib.request
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        request_id = response.getheader('X-Request-Id')
        print(request_id)
