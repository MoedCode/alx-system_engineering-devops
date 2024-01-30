#!/usr/bin/python3
"""returns information about his/her CSV file. """

if __name__ == "__main__":
    import requests
    import sys
    import csv

    ID = int(sys.argv[1])
    Em_url = f"https://jsonplaceholder.typicode.com/users/{ID}"
    TODO = f"https://jsonplaceholder.typicode.com/users/{ID}/todos"

    REQ = requests.get(Em_url).json()
    treq = requests.get(TODO).json()
    name = REQ['username']
    with open(f'{ID}.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for x in treq:
            writer.writerow([str(ID), f"{name}",
                            f"{x['completed']}", f"{x['title']}"])
