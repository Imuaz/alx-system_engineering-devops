#!/usr/bin/python3
"""
Task 3 of Advanced APIs Module
"""
import re
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Sorts and prints the word counts in descending order
    based on count and alphabetically if counts are equal
    for a given subreddit."""
    if counts is None:
        counts = {word: 0 for word in word_list}

    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]

        for child in children:
            title = child["data"]["title"].lower().split()
            for word in word_list:
                counts[word] += sum(1 for w in title if
                                    re.match(f'^{re.escape(word)}$', w, re.I))

        after = data["data"]["after"]
        if after is None:
            sorted_counts = sorted(counts.items(),
                                   key=lambda item: (-item[1], item[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")
        else:
            count_words(subreddit, word_list, after, counts)
