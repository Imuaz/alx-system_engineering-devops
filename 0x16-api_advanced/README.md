# 0x16. API advanced

**Background Context**

Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.

A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.

**Introduction**

The project encompassed a variety of topics related to working with APIs. It covered techniques such as reading API documentation to locate specific endpoints, utilizing pagination in API requests, parsing JSON results received from an API, implementing recursive API calls, and sorting a dictionary based on its values. These concepts provided a comprehensive understanding of API utilization, enabling effective data retrieval and manipulation within programming applications.

## Resources:books:
***Read or watch:***
- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Query String](https://en.m.wikipedia.org/wiki/Query_string)

## Requirements:round_pushpin:
- [General](../0x15-api/README.md#Requirements)

## Tasks:page_with_curl:
**0. How many subs?**
- [0-subs.py](./0-subs.py): A function that queries the `Reddit API` and returns the number of subscribers (not active users, total subscribers) for a given subreddit.
  - Prototype: `def number_of_subscribers(subreddit)`
  - If not a valid subreddit, it returns 0.
  - **NOTE**: Invalid subreddits may return a redirect to search results. Thus, it must be ensured that redirects shouldn't be followed.

**1. Top Ten**
- [1-top_ten.py](./1-top_ten.py): A function that queries the `Reddit API` and prints the titles of the first 10 hot posts listed for a given subreddit.
  - Prototype: `def top_ten(subreddit)`
  - If not a valid subreddit, it prints None.

**2. Recurse it!**
- [2-recurse.py](./2-recurse.py): A recursive function that queries the `Reddit API` and returns a list containing the titles of all hot articles for a given subreddit.
  - Prototype: `def recurse(subreddit, hot_list=[])`
  - If not a valid subreddit, it returns None
  - Note: the prototype could be changed, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.
  - It uses a recursive function instead of a loop as required.

**3. Count it!**
- [100-count.py](./100-count.py): A recursive function that queries the `Reddit API`, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces.(`Javascript` counts as `javascript`, but `java` does not).
  - Prototype: `def count_words(subreddit, word_list)`
  - Note: the prototype could be changed, but it must be able to be called with just a subreddit supplied and a list of keywords. AKA you can add a counter or anything else, but the function must work without supplying a starting value in the main.
  - If `word_list` contains the same word (case-insensitive), the final count will be the sum of each duplicate.
  - Results will be printed in descending order, by the count, and if the count is the same for separate keywords, they will then be sorted alphabetically (ascending, from A to Z). Words with no matches will be skipped and not printed. Words are printed in lowercase.
  - Results are based on the number of times a keyword appears, not titles it appears in. `java` `java` `java` counts as 3 separate occurrences of `java`.
  - for easy implementation, `java.` or `java!` or `java_` should not count as `java`
  - If no posts match or the subreddit is invalid, it prints nothing.

:tired_face:
