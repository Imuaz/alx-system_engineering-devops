
import requests
import sys

def count_words(subreddit, word_list, after=None, counts=None):
    """Sorts and prints the word counts in descending order
    based on count and alphabetically if counts are equal
    for a given subreddit."""
    if not counts:
        counts = {}

    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "after": after} if after else {}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code == 200:
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
    else:
        return


if __name__ == '__main__':
    if len(sys.argv) > 0:
        subred = sys.argv[1]
        if (len(sys.argv) > 1):
            wordlist = sys.argv[2].split()
        count_words(subred, wordlist, [])
