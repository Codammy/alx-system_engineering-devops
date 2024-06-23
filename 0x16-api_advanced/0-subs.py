#!/usr/bin/python3
"""
Queries reddit api and returns number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """queries number of subscribers for a given subreddit"""

    if type(subreddit) is not str:
        return 0
    url = f"https://api.reddit.com/r/{subreddit}/about"

    res = requests.get(url, headers={'User-Agent': 'Laptop'})
    #if res.ok and not res.is_redirect:
    return res.json().get('data', {}).get('subscribers', 0)
    return 0
