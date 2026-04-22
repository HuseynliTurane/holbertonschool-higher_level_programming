#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable in the response header.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)

    # headers lüğətindən .get() metodu ilə dəyəri götürürük
    request_id = r.headers.get('X-Request-Id')
    print(request_id)
