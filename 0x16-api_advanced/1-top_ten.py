#!/usr/bin/python3
"""
Module task 1
"""
import requests
import sys


def top_ten(subreddit):
    """Function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}  # User-Agent header

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for request errors

        data = response.json()
        children = data["data"]["children"]
        for child in children:
            title = child["data"]["title"]
            print(title)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        subreddit = sys.argv[1]
        top_ten(subreddit)
