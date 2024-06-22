#!/usr/bin/python3
"""
Queries reddit api and returns number of subscribers for a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """queries number of subscribers for a given subreddit"""
    url = f"http://api.reddit.com/r/{subreddit}/about"

    res = requests.get(url)
    if res.ok:
        return res.json()['data'].get('subscribers')
    return 0
