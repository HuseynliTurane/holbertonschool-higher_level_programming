#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a POST request
with the email as a parameter, and displays the body of the response.
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Məlumatı lüğət (dictionary) şəklində hazırlayırıq
    values = {'email': email}

    # Məlumatı URL formatına (email=test@test.com) salırıq və baytlara çeviririk
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    # POST sorğusunu göndəririk
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
