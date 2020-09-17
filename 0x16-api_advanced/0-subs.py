#!/usr/bin/python3
""" Module """


import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given
    """

    user_agent = {'User-agent': 'Mozilla/5.0 (Macintosh; \
Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/39.0.2171.95 Safari/537.36'}

    res = requests.get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers=user_agent)

    if res.status_code == 404:
        return 0

    return res.json().get("data").get("subscribers")
