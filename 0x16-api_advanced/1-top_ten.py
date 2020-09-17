#!/usr/bin/python3
""" Module """


import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit
    """

    user_agent = {'User-agent': 'Mozilla/5.0 (Macintosh; \
Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/39.0.2171.95 Safari/537.36'}

    res = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'.format(
        subreddit), headers=user_agent)

    if res.status_code == 404:
        print(None)

    else:
        for sub in res.json().get("data").get("children"):
            print(sub.get("data").get("title"))
