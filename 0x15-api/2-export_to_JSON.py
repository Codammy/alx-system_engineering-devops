#!/usr/bin/python3
"""
Python script that, uses REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


if __name__ == '__main__':
    import json
    import requests
    import sys

    EMPLOYEE_ID = sys.argv[1]

    URL = 'https://jsonplaceholder.typicode.com'
    res = requests.get(URL + '/users/' + EMPLOYEE_ID)
    EMPLOYEE_NAME = res.json().get('username')

    res = requests.get(URL + '/todos')
    tasks = list(filter(lambda task: task.get('userId') == int(EMPLOYEE_ID),
                 res.json()))

    u_tasks = []
    for task in tasks:
        data = {
                "task": task['title'],
                "completed": task["completed"],
                "username": EMPLOYEE_NAME
               }
        u_tasks.append(data)
    user_tasks = {EMPLOYEE_ID: u_tasks}

    filename = EMPLOYEE_ID + '.json'
    with open(filename, 'w') as fp:
        json.dump(user_tasks, fp)
