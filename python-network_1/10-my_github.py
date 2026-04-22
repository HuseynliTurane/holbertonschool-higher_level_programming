#!/usr/bin/python3
"""
A script that takes GitHub credentials (username and password)
and uses the GitHub API to display the user id.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    # Basic Authentication üçün auth parametrindən istifadə edirik
    r = requests.get(url, auth=(username, password))

    try:
        # Cavabı JSON formatına çeviririk
        response_json = r.json()
        # 'id' açarını götürürük, əgər yoxdursa None çap olunacaq
        print(response_json.get('id'))
    except ValueError:
        # Əgər cavab JSON deyilsə
        print("None")
