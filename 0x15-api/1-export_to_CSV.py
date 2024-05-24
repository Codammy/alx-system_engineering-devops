#!/usr/bin/python3
"""
Python script that, uses REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == '__main__':
    EMPLOYEE_ID = sys.argv[1]

    URL = 'https://jsonplaceholder.typicode.com'
    res = requests.get(URL + '/users/' + EMPLOYEE_ID)
    USERNAME = res.json().get('username')

    res = requests.get(URL + '/todos')
    tasks = list(filter(lambda task: task.get('userId') == int(EMPLOYEE_ID),
                 res.json()))
    csv_str = ''
    for task in tasks:
        t_status = task['completed']
        t_title = task['title']
        csv_str += f'"{EMPLOYEE_ID}","{USERNAME}","{t_status}","{t_title}"\n'

    filename = EMPLOYEE_ID + '.csv'
    with open(filename, 'w') as fs:
        fs.write(csv_str)
