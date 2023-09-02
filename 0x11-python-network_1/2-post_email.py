#!/usr/bin/python3
"""
    Takes in a url and an email. Sned POST request to URL with
    the email as a parameter.Displays response body in utf-8.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    data = {"Your email is": sys.argv[2]}
    request = urllib.parse.urlencode(data).encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        response_data = response.read()
        decoded_data = response_data.decode('utf-8')

        print(decoded_data)
