#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a POST request
with the email as a parameter, and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Göndəriləcək məlumatı lüğət (dictionary) şəklində hazırlayırıq
    payload = {'email': email}

    # POST sorğusunu göndəririk. 'data' arqumenti məlumatı
    # 'application/x-www-form-urlencoded' formatında göndərir.
    r = requests.post(url, data=payload)

    # Cavabın mətnini çap edirik
    print(r.text)
