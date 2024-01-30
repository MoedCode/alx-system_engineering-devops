#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    from sys import argv
    import csv
    ID = argv[1]
    URL = "https://jsonplaceholder.typicode.com/"
    Employee = requests.get(URL + f"users/{ID}").json()
    NAME = Employee.get("username")
    TODO = requests.get(URL + "todos", params={"userId": ID}).json()

    with open("{}.csv".format(ID), "w", newline="") as FILE:
        writer = csv.writer(FILE, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [ID, NAME, t.get("completed"), t.get("title")]
        ) for t in TODO]
