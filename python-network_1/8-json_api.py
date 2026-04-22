#!/usr/bin/python3
"""
A script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    # Əgər arqument verilməyibsə q="", verilibsə birinci arqumenti götürürük
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    payload = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'

    try:
        r = requests.post(url, data=payload)
        # Cavabı JSON formatında oxumağa çalışırıq
        response_json = r.json()

        if response_json == {}:
            print("No result")
        else:
            # JSON dolu olduqda ID və Name məlumatlarını çap edirik
            print("[{}] {}".format(response_json.get('id'),
                                   response_json.get('name')))
    except ValueError:
        # Əgər gələn cavab JSON formatında deyilsə ValueError fırlanır
        print("Not a valid JSON")
