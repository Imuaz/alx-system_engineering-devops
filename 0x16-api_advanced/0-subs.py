#!/usr/bin/python3
"""Module for task 0"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers to
    the subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers to the subreddit.
        Returns 0 if the subreddit doesn't exist
            or an error occurs while making the API request.

    """
    try:
        headers = {"User-Agent": "My-User-Agent"}
        url = f"https://www.reddit.com/r/{subreddit}/about.json"

        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        subscribers = response.json().get("data").get("subscribers")
        return subscribers
    except (requests.RequestException, KeyError):
        return 0
