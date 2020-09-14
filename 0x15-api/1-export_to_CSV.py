#!/usr/bin/python3
"""
    extend your Python script to export data in the CSV format

"""


import requests
from sys import argv


if __name__ == "__main__":

    v2 = {'userId': argv[1]}
    v = {'id': argv[1]}
    s = ""

    req1 = (requests.get('https://jsonplaceholder.typicode.com/users',
                         params=v)).json()
    req = (requests.get('https://jsonplaceholder.typicode.com/todos',
                        params=v2)).json()

    for r in req:
        s += '"{}","{}","{}","{}"\n'.format(argv[1], req1[0].get('username'),
                                            r.get('completed'), r.get('title'))

    with open(argv[1] + '.csv', "w") as f:
        f.write(s)
