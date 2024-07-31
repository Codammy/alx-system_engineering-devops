#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys
url = "https://jsonplaceholder.typicode.com/"


def fetch_user_tasks(userid, username):
    response = requests.get(url + "todos", params={"userId": userid})
    response = response.json()
    tasks = list(map(lambda obj: {"username": username,
                                  "task": obj["title"],
                                  "completed": obj["completed"]}, response))
    return tasks


if __name__ == "__main__":
    response = requests.get(url + "users")
    if response.ok:
        user_data = response.json()
        all_user_tasks = dict()

        for info in user_data:
            user_id = info.get('id')
            user_tasks = fetch_user_tasks(user_id, info.get('username'))
            all_user_tasks[user_id] = user_tasks

        with open("todo_all_employees.json", "w") as fp:
            json.dump(all_user_tasks, fp)
