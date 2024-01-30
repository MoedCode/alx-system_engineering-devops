#!/usr/bin/python3

import  requests

def fitch_url(url):
    REQ = requests.get(url)
    if REQ.status_code == 200:
        print(REQ.__dict__)
    else:
        print(f"Failed to fetch data. Status code: {REQ.status_code}")
        return None

if __name__ == "__main__":
    fitch_url("https://jsonplaceholder.typicode.com/toos/1")