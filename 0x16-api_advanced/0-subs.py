#!/usr/bin/python3


from fake_useragent import UserAgent
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given
    """

    ua = UserAgent()
    user_agent = {'User-agent': str(ua.chrome)}
    res = requests.get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers=user_agent)

    if res.status_code == 404:
        return 0

    return res.json().get("data").get("subscribers")
