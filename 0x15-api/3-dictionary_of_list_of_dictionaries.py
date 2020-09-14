#!/usr/bin/python3
"""
    extend your Python script to export data in the JSON format

"""


import json
import requests


if __name__ == "__main__":

    res = {}

    req = (requests.get('https://jsonplaceholder.typicode.com/users')).json()

    for r in req:
        v = {'userId': r.get('id')}
        req1 = (requests.get('https://jsonplaceholder.typicode.com/todos',
                             params=v)).json()

        l = []
        for todo in req1:
            d = {}
            d['username'] = r.get('username')
            d['task'] = todo.get('title')
            d['completed'] = todo.get('completed')
            l.append(d)

        res[str(r.get('id'))] = l

    with open("todo_all_employees.json", "w") as f:
        json.dump(res, f)
