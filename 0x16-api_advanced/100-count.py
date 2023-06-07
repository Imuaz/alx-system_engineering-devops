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

    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if word not in instances:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return

        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        for k, v in instances:
            print("{}: {}".format(k, v))
    else:
        count_words(subreddit, word_list, instances, after, count)
