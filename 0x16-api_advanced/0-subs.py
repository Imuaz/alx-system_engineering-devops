#!/usr/bin/python3
"""
Function that query subscribers on a givensubreddit of Redit API.
"""

import requests
"""Module for task 0"""

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    headers = {"User-Agent": "My-User-Agent"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        subscribers = response.json()["data"]["subscribers"]
        return subscribers
    except (requests.RequestException, KeyError):
        return 0
