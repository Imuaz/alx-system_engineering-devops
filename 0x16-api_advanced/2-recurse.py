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
    params = {}
    params.update({"limit": 100, "after": after})

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']
        posts = data['children']
        hot_list.extend([post['data']['title']
                         for post in posts])
        next_page = response.json()['data']['next_page']
        if not next_page:
            return hot_list
        return recurse(subreddit, hot_list, next_page)
    else:
        return None


if __name__ == '__main__':
    if len(sys.argv) > 1:
        subred = sys.argv[1]
        recurse(subred, [])
