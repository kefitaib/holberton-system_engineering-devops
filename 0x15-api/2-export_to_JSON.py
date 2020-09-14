#!/usr/bin/python3
"""
    extend your Python script to export data in the JSON format

"""


import json
import requests
from sys import argv


if __name__ == "__main__":

    v2 = {'userId': argv[1]}
    v = {'id': argv[1]}
    l = []
    res = {argv[1]: ""}

    req1 = (requests.get('https://jsonplaceholder.typicode.com/users',
                         params=v)).json()
    req = (requests.get('https://jsonplaceholder.typicode.com/todos',
                        params=v2)).json()

    for r in req:
        d = {}
        d['task'] = r.get('title')
        d['completed'] = r.get('completed')
        d['username'] = req1[0].get('username')
        l.append(d)

    res[argv[1]] = l

    with open("{}.json".format(argv[1]), "w") as f:
        json.dump(res, f)
