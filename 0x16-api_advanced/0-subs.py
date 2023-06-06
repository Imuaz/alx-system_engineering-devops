#!/usr/bin/python3
"""Advanced Apis Module for task 0"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers to the subreddit.
        Returns 0 if the subreddit is invalid
            or an error occurs during the API request.
    """
    headers = {"User-Agent": "user_agent"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        subscribers = data.get('subscribers')
        return subscribers
    else:
        return 0


if __name__ == '__main__':
    if len(sys.argv) > 1:
        subreddit = sys.argv[1]
        num_subscribers = number_of_subscribers(subreddit)
        print(
            f"The subreddit '{subreddit}' has {num_subscribers} subscribers.")
