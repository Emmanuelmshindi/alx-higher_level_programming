#!/usr/bin/python3
"""
    Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        content_type = type(body)
        content_bytes = body
        content_utf8 = content_bytes.decode('utf-8')
        
        print("Body response:")
        print("  - type: {}".format(content_type))
        print("  - content: {}".format(content_bytes))
        print("  - utf8 content: {}".format(content_utf8))
