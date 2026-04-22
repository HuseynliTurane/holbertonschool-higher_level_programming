#!/usr/bin/python3
"""
A script that takes in a URL, sends a request and displays the response body.
If the status code is >= 400, it prints the error code.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)

    # Status kodu 400-ə bərabər və ya ondan böyükdürsə xəta çap edirik
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
