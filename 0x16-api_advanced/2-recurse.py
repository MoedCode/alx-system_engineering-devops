#!/usr/bin/python3
#!/usr/bin/python3
"""file"""


def recurse(subreddit, hot_list=[], after=""):
    """Tasks Reddit user name and returns the subscribers number."""
    import requests
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after}
    header = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=header, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    data = response.json()
    data_after = data.get('data').get("after")
    for child in data.get('data').get("children"):
        hot_list.append(child.get("data").get("title"))
    if data_after is not None:
        return recurse(subreddit, hot_list, data_after)
    return hot_list