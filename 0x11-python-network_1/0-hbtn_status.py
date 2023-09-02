#!/usr/bin/python3
"""
    Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content_type = type(response.read())
        content_bytes = response.read()
        content_utf8 = content_bytes.decode('utf-8')
        
        print("Body response:")
        print("  - type: {}".format(content_type))
        print("  - content: {}".format(content_bytes))
        if content_utf8:
            print("  - utf8 content: {}".format(content_utf8))
