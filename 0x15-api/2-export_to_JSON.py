#!/usr/bin/python3
#!/usr/bin/python3
"""returns information about his/her CSV file. """

if __name__ == "__main__":
    import requests
    import sys
    import json

    EMPID = int(sys.argv[1])
    USER = f"https://jsonplaceholder.typicode.com/users/{EMPID}"
    TODO = f"https://jsonplaceholder.typicode.com/users/{EMPID}/todos"

    ureq = requests.get(USER).json()
    treq = requests.get(TODO).json()

    data = {}
    ll = []
    for x in treq:
        del x['userId']
        del x['id']
        x['task'] = x.pop('title')
        x['completed'] = x.pop('completed')
        x['username'] = ureq['username']
        ll.append(x)
    data[f"{EMPID}"] = ll
    with open(f'{EMPID}.json', 'w') as file:
        json.dump(data, file)
