#!/usr/bin/python3
"""
Task 3 Advanced API Module
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Queries Reddit API, parses the titles of all hot articles, and prints a
    sorted count of given keywords (case-insensitive, delimited by spaces."""
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after} if after else {}

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(
        url,
        params=params,
        headers=headers,
        allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()["data"]
    after = data.get("after")
    children = data.get("children")

    for child in children:
        title = child["data"]["title"].lower()
        for word in word_list:
            word_count = title.count(word.lower())
            if word_count > 0:
                counts[word] = counts.get(word, 0) + word_count

    if after:
        return count_words(subreddit, word_list, after, counts)

    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_counts:
        print(f"{word.lower()}: {count}")


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
