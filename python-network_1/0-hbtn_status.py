#!/usr/bin/python3
"""
Bu modul urllib istifadə edərək statusu yoxlayır.
Buraya yazılan mətn 'documentation' (sənədləşdirmə) adlanır.
Bu hissə olmazsa, yoxlama sistemi xəta verəcək.
"""
import urllib.request


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
