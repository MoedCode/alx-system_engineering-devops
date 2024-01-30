#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

if __name__ == "__main__":
    import requests
    from sys import argv

    URL = "https://jsonplaceholder.typicode.com/"
    ID = argv[1]
    Employee = requests.get(URL + f"users/{ID}").json()
    NAME = Employee.get("name")

    TODO = requests.get(URL + "todos", params={"userId": ID}).json()
    lnT = len(TODO)

    DONE = [t.get("title") for t in TODO if t.get("completed") is True]
    lnD = len(DONE)

    print(f"Employee {NAME} is done with tasks({lnD}/{lnT}):")
    [print("\t {}".format(unDifTxt)) for unDifTxt in DONE]
