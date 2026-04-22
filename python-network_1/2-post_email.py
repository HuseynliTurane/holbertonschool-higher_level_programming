#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a POST request
with the email as a parameter, and displays the response body.
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Məlumatı hazırlayırıq
    values = {'email': email}

    # Məlumatı encode edirik (79 simvol limitini gözləyərək)
    data = urllib.parse.urlencode(values).encode('ascii')

    # POST sorğusunu yaradırıq
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
