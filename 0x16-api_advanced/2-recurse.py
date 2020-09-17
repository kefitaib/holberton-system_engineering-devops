#!/usr/bin/python3
""" Module """


import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    unction that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit
    """

    params = {'after': after}

    user_agent = {'User-agent': 'Mozilla/5.0 (Macintosh; \
Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/39.0.2171.95 Safari/537.36'}

    res = requests.get('https://www.reddit.com/r/{}/hot.json'.format(
        subreddit), headers=user_agent, params=params)

    if res.status_code == 404:
        return None

    for sub in res.json().get("data").get("children"):
        hot_list.append(sub.get("data").get("title"))

    after = res.json().get("data").get("after")
    if not after:
        return hot_list

    return recurse(subreddit, hot_list, after)
