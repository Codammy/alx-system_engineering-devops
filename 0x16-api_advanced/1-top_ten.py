#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""
import requests
import sys


def top_ten(subreddit):
    """function that queries the reddit api"""
    response = requests.get(f'https://api.reddit.com/r/{subreddit}',
                            headers={'User-Agent': 'Windows'})
    if response.ok and not response.is_redirect:
        data = response.json().get('data').get('children')
        for d in data[:10]:
            print(d['data']['title'])
    else:
        print(None)
