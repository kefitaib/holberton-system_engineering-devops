#!/usr/bin/python3
"""
    using a REST API, for a given employee ID, returns information
    about his/her TODO list progress

"""


import requests
from sys import argv


if __name__ == "__main__":

    v2 = {'userId': argv[1]}
    v = {'id': argv[1]}

    req1 = requests.get('https://jsonplaceholder.typicode.com/users', params=v)
    req = requests.get('https://jsonplaceholder.typicode.com/todos', params=v2)

    done = 0
    for r in req.json():
        if r.get('completed') is True:
            done += 1

    print(req1.json())
    print('Employee {} is done with tasks({}/{}):'.
          format(req1.json()[0].get('name'), done, len(req.json())))

    for r in req.json():
        if r.get('completed') is True:
            print("\t {}".format(r.get('title')))
