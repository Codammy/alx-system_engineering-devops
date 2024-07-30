#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


url = "https://jsonplaceholder.typicode.com/"
response = requests.get(url + "users", params={"id": sys.argv[1]})
if response.ok:
    user_data = response.json()[0]
    response = requests.get(url + "todos", params={"userId": sys.argv[1]})
    response = response.json()
    with open(f"{user_data.get('id')}.csv", "w") as fp:
        for task in response:
            fp.writelines('"{}","{}","{}","{}"\n'.format(
                task.get('userId'), user_data.get('username'),
                task.get('completed'), task.get('title')))
