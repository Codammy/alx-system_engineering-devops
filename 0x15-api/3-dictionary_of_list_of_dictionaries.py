#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys
import json
url = "https://jsonplaceholder.typicode.com/"


def fetch_user_tasks(userid, username):
    response = requests.get(url + "todos", params={"userId": userid})
    response = response.json()
    tasks = list(map(lambda obj: {
        "task": obj['title'], "completed": obj["completed"],
        "username": username}, response
        ))
    with open("todo_all_employees.json", "a") as fp:
        json.dump({userid: tasks}, fp)


if __name__ == "__main__":
    response = requests.get(url + "users")
    if response.ok:
        user_data = response.json()
        for info in user_data:
            fetch_user_tasks(info.get('id'), info.get('username'))
