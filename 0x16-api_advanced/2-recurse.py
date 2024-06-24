#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, after=None, count=0, hot_list=[]):
    """recursive function that makes requeet to reddit api"""
    url = f'https://api.reddit.com/r/{subreddit}'
    res = requests.get(url, params={'after': after},
                       headers={'User-Agent': 'github.com/codammy'})
    if res.ok and not res.is_redirect:
        count += 1
        data_all = res.json()
        after = data_all.get('data').get('after')
        data = data_all.get('data').get('children')
        for d in data:
            hot_list.append(d['data']['title'])
        if after is None:
            return hot_list
        return recurse(subreddit, after, count, hot_list)
    return None
