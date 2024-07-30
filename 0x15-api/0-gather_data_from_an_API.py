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
    completed_tasks = list(
                           filter(lambda t: t.get("completed") is True,
                                  response)
                          )
    tt_task = len(response)
    noc = len(completed_tasks)
    print(f"Employee {user_data['name']} is done with tasks({noc}/{tt_task}):")
    for task in completed_tasks:
        print(f"\t{task.get('title')}")
