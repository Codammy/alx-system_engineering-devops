#!/usr/bin/python3
"""
Python script that, uses REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import json
from datetime import datetime


if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com'
    print('Consuming all tasks @' + str(datetime.now()))
    all_tasks = requests.get(URL + '/todos').json()
    u_tasks = []
    all_users_tasks = dict()
    for task in all_tasks:
        userId = task.get('userId')
        res = requests.get(URL + '/users/' + str(userId))
        EMPLOYEE_NAME = res.json().get('username')
        data = {
                "username": EMPLOYEE_NAME,
                "task": task['title'],
                "completed": task["completed"]
               }
        u_tasks.append(data)
        all_users_tasks[userId] = u_tasks

    with open('todo_all_employees.json', 'w') as fp:
        json.dump(all_users_tasks, fp)
