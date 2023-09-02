#!/usr/bin/python3
"""
    Send request to a url and ndisplay value of X-Request-Id variable
    in the response header
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        id = response.headers.get('X-Request-Id')
        print(id)
