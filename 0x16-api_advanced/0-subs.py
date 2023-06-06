#!/usr/bin/python3
"""Advanced Apis Module for task 0"""
import requests


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
