#!/usr/bin/python3
"""
Task 3 Advanced API Module
"""
import requests
import sys


def count_words(subreddit, wordlist, hot_list=[], after=None,):
    """Queries Reddit API, parses the titles of all hot articles, and prints a
    sorted count of given keywords (case-insensitive, delimited by spaces."""
    headers = {"User-Agent": "user_agent"}
    url = "https://www.reddit.com/r/{}/hot.json".format(
        subreddit)
    params = {"limit": 100, "after": after}

    response = requests.get(
        url=url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']
        children = data['children']
        hot_list.extend([child['data']['title']
                         for child in children])
        after = response.json()['data']['after']
        if not after:
            wordcounts = {}
            search_str = " ".join(hot_list)
            wordcounts = {word.lower(): search_str.lower().count(
                word.lower()) for word in wordlist}
            sorted_wordcounts = dict(
                sorted(wordcounts.items(),
                       key=lambda item: (-item[1], item[0])))
            for key, value in sorted_wordcounts.items():
                if value != 0:
                    print("{}: {}".format(key, value))
            return (0)
        return count_words(subreddit, wordlist, hot_list, after)
    else:
        return None


if __name__ == '__main__':
    if len(sys.argv) > 0:
        subred = sys.argv[1]
        if (len(sys.argv) > 1):
            wordlist = sys.argv[2].split()
        count_words(subred, wordlist, [])
