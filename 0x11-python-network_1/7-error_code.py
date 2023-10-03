#!/usr/bin/python3
"""
Python script that takes in URL, sends request to it
and displays the body of the response.
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    retrieved = requests.get(url)
    if retrieved.status_code >= 400:
        print("Error code: {}".format(retrieved.status_code))
    else:
        print(retrieved.text)