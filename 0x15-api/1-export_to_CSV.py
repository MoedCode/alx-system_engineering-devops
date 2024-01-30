#!/usr/bin/python3
"""returns information about his/her CSV file. """

if __name__ == "__main__":
    import requests
    import sys
    import csv

    EMPID = int(sys.argv[1])
    USER = f"https://jsonplaceholder.typicode.com/users/{EMPID}"
    TODO = f"https://jsonplaceholder.typicode.com/users/{EMPID}/todos"

    ureq = requests.get(USER).json()
    treq = requests.get(TODO).json()
    name = ureq['username']
    with open(f'{EMPID}.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for x in treq:
            writer.writerow([str(EMPID), f"{name}",
                            f"{x['completed']}", f"{x['title']}"])
