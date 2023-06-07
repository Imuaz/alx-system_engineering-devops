#!/usr/bin/python3
"""
Task 3 of Advanced APIs Module
"""
import requests
import sys


def recurse(subreddit, hot_list=[], after=None,):
    """Queries Reddit API, parses the titles of all hot articles, and prints a
    sorted count of given keywords (case-insensitive, delimited by spaces."""

    headers = {"User-Agent": "My-User-Agent"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {}
    params.update({"limit": 100, "after": after})

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']
        posts = data['children']
        hot_list.extend([post['data']['title']
                         for post in posts])
        next_page = response.json()['data']['after']
        if not next_page:
            word_counts = {}
            search_str = " ".join(hot_list)
            for word in word_list:
                count = search_str.lower().count(word.lower())
                if count != 0:
                    word_counts[word.lower()] = count
            sorted_word_counts = dict(sorted(
                word_counts.items(), key=lambda item: (-item[1], item[0])))
            for key, value in sorted_word_counts.items():
                print("{}: {}".format(key, value))
            return 0
        else:
            return count_words(subreddit, word_list, hot_list, next_page)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        subreddit = sys.argv[1]
        if len(sys.argv) > 2:
            word_list = sys.argv[2].split()
        else:
            word_list = []
        count_words(subreddit, word_list, [])
