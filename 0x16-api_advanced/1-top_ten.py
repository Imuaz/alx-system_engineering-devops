#!/usr/bin/python3
"""
Task 1 Advanced APIs Module
"""
import requests
import sys


def top_ten(subreddit):
    """Queries Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit."""

    headers = {"User-Agent": "My-User-Agent"}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        children = data.get('children', [])
        titles = [child.get('data', {}).get('title') for child in children]
        print(*titles, sep='\n')
    else:
        print("None")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        subred = sys.argv[1]
        top_ten(subred)
