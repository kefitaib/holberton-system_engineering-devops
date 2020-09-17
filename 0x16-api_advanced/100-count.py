#!/usr/bin/python3
""" Module """


import requests


def count_words(subreddit, word_list):
    """ retuen to main """

    res = count(subreddit, {k: 0 for k in word_list}, after="")
    for k, v in res.items():
        if v != 0:
            print("{}: {}".format(k, v))


def count(subreddit, word_dict, after=""):
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
        pass

    else:
        for sub in res.json().get("data").get("children"):
            l = [x for x in sub.get("data").get("title").split()]
            for x in l:
                for k, v in word_dict.items():
                    if x.lower() == k.lower():
                        word_dict[k] += 1
                        continue

        after = res.json().get("data").get("after")
        if not after:
            return word_dict

        return count(subreddit, word_dict, after)
