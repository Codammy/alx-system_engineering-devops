#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit.
"""
import requests
import time


def recurse(subreddit, hot_list=[]):
    """recursive function that makes requeet to reddit api"""
    url = f'https://api.reddit.com/r/{subreddit}'
    res = requests.get(url, params=hot_list)
    after = [res.json().get('data').get('after')]
    print(after)
    if res.ok and not res.is_redirect:
        data = res.json().get('data').get('children')
        for d in data:
            print(d['data']['title'])
        time.sleep(2)
        print()
        recurse(subreddit, after)

recurse('programming')
