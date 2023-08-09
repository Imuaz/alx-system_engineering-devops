#!/usr/bin/python3
"""
Task 3 of Advanced APIs Module
"""
import re
import sys
import requests


def count_words(subreddit, word_list, sort_list=[], after=None):
    """Sorts and prints the word counts in descending order
    based on count and alphabetically if counts are equal
    for a given subreddit."""
    params = {"limit": 100, "after": after}
    headers = {"User-Agent": "User-Agent"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']
        children = data['children']
        sort_list.extend([child['data']['title']
                          for child in children])
        after = response.json()['data']['after']
        if not after:
            word_counts = {}
            find_str = " ".join(sort_list)
            word_counts = {word.lower(): find_str.lower().count(
                word.lower()) for word in word_list}
            sorted_word_counts = dict(
                sorted(word_counts.items(),
                       key=lambda item: (-item[1], item[0])))
            for word, count in sorted_word_counts.items():
                if count != 0:
                    print("{}: {}".format(word, count))
            return (0)
        return count_words(subreddit, word_list, sort_list, after)
    else:
        return None


if __name__ == '__main__':
    if len(sys.argv) > 0:
        subred = sys.argv[1]
        if (len(sys.argv) > 1):
            word_list = sys.argv[2].split()
        count_words(subred, word_list, [])
