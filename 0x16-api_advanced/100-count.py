#!/usr/bin/python3
"""
Task 3 Advanced API Module
"""
import requests
import re


def count_words(subreddit, word_list, after=None, count_dict=None):
    """Queries Reddit API, parses the titles of all hot articles, and prints a
    sorted count of given keywords (case-insensitive, delimited by spaces."""
    if count_dict is None:
        count_dict = {}
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()["data"]
    after = data.get("after")
    children = data.get("children")

    for child in children:
        title = child["data"]["title"].lower()
        for word in word_list:
            if word.lower() in title and not re.search(
                    r"\b{}\b".format(word), title):
                count_dict[word] = count_dict.get(word, 0) + title.count(
                    word.lower())

    if after:
        return count_words(subreddit, word_list, after, count_dict)

    sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_counts:
        print(f"{word}: {count}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(
            sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2:]
        count_words(subreddit, word_list)
