#!/usr/bin/python3
"""returns information about his/her CSV file. """

if __name__ == "__main__":
    import requests
    import sys
    import json

    USER = f"https://jsonplaceholder.typicode.com/users"

    ureq = requests.get(USER).json()

    data = {}
    for y in ureq:
        todo = f"https://jsonplaceholder.typicode.com/users/{y['id']}/todos"
        treq = requests.get(todo).json()
        ll = []
        for x in treq:
            del x['userId']
            del x['id']
            x['task'] = x.pop('title')
            x['completed'] = x.pop('completed')
            x['username'] = y['username']
            ll.append(x)
        data[f"{y['id']}"] = ll
    with open(f'todo_all_employees.json', 'w') as file:
        json.dump(data, file)
