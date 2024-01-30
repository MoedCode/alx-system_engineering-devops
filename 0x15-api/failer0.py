#!/usr/bin/python3
"Doc Str"

if __name__ == "__main__":
    import requests
    from sys import argv
    URL = "https://jsonplaceholder.typicode.com/"
    emp_ID = argv[1]
    emp_url = f"{URL}users/{emp_ID}"

    emp_json = requests.get(emp_url).json()
    TODO_json = requests.get(URL + "todos", params={"UserId": emp_ID}).json()

    DONE = [t.get("title") for t in TODO_json if t.get("completed") is True]
    NAME = emp_json.get("name")
    L1, L2 = len(DONE), len(TODO_json)

    print(f"Employee {NAME} is done with tasks({L1}/{L2}):")
