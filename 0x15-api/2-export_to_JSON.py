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


if __name__ == "__main__":
    response = requests.get(url + "users", params={"id": sys.argv[1]})
    if response.ok:
        user_data = response.json()[0]
        response = requests.get(url + "todos", params={"userId": sys.argv[1]})
        response = response.json()
        tasks = list(map(lambda obj: {
                    "task": obj['title'], "completed": obj["completed"],
                    "username": user_data["username"]}, response
                    ))
        with open(f"{user_data.get('id')}.json", "w") as fp:
            json.dump({user_data['id']: tasks}, fp)
