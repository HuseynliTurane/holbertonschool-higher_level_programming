#!/usr/bin/python3
"""
A script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable in the header.
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        # getheader() funksiyası başlıqdakı xüsusi dəyişəni oxuyur
        request_id = response.getheader('X-Request-Id')
        print(request_id)
