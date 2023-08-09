#!/usr/bin/python3
"""
Task 3 of Advanced APIs Module
"""
import sys
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Sorts and prints the word counts in descending order
    based on count and alphabetically if counts are equal
    for a given subreddit."""
    if not counts:
        counts = {word: 0 for word in word_list}

    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after} if after else {}

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
                word = word.lower()
                counts[word] += title.count(word)

        after = data['data']['after']

        if after is None:
            sorted_counts = sorted(counts.items(), key=lambda item:
                                   (-item[1], item[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")
        else:
            count_words(subreddit, word_list, after, counts)


if __name__ == '__main__':
    if len(sys.argv) > 0:
        subred = sys.argv[1]
        if (len(sys.argv) > 1):
            word_list = sys.argv[2].split()
        count_words(subred, word_list)
