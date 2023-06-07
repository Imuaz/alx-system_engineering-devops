#!/usr/bin/python3
"""
Task 3 of Advanced APIs Module
"""
import re
import requests
import sys


def add_title(dictionary, hot_posts):
    """Queries Reddit API,"""
    if not hot_posts:
        return

    title = hot_posts.pop(0)['data']['title'].split()
    for word in title:
        for key in dictionary:
            if re.search(rf"\b{re.escape(key)}\b", word, re.I):
                dictionary[key] += 1

    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """ Queries the Reddit API """
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    params = {
        'after': after
    }
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    hot_posts = data['data']['children']
    add_title(dictionary, hot_posts)
    after = data['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after)


def count_words(subreddit, word_list):
    """ Initializes the function """
    dictionary = {word: 0 for word in word_list}

    recurse(subreddit, dictionary)

    sorted_dict = sorted(
        dictionary.items(), key=lambda kv: kv[1], reverse=True)

    for word, count in sorted_dict:
        if count != 0:
            print(f"{word}: {count}")

    print("")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        subreddit = sys.argv[1]
        word_list = sys.argv[2:] if len(sys.argv) > 2 else []
        count_words(subreddit, word_list)
