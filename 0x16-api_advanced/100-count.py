#!/usr/bin/python3
""" Module """


import requests


def count_words(subreddit, word_list, after="", word_dict={}):
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

    if not word_dict:
        word_dict = {k: 0 for k in word_list}

    if res.status_code == 404:
        print()

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
            d = {k: v for k, v in sorted(word_dict.items(),
                                         key=lambda item: item[1],
                                         reverse=True)}

            for k, v in d.items():
                if v != 0:
                    print("{}: {}".format(k, v))

            return

        return count_words(subreddit, word_list, after, word_dict)
