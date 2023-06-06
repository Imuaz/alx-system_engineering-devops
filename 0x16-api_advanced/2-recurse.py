#!/usr/bin/python3
"""
Task 2 of Advanced APIs Module
"""
import requests
import sys


def recurse(subreddit, hot_list=[], after=None,):
    """Queries Reddit API and prints the titles of all hot posts listed
    for a given subreddit."""

    headers = {"User-Agent": "My-User-Agent"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    reqst_params = {"limit": 100, "after": after}

    response = requests.get(
        url, headers=headers, reqst_params, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json()
        data = json_data['data']
        children = data['children']
        hot_list.extend(child['data']['title'] for child in children)
        after = data['after']
        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None


if __name__ == '__main__':
    if len(sys.argv) > 1:
        subred = sys.argv[1]
        recurse(subred, [])
