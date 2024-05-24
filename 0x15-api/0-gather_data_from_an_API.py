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
    EMPLOYEE_NAME = res.json().get('name')

    res = requests.get(URL + '/todos')
    tasks = list(filter(lambda task: task.get('userId') == int(EMPLOYEE_ID),
                 res.json()))
    completed_tasks = list(filter(lambda task: task.get('completed') is True,
                           tasks))

    print('Employee {} is done with tasks({}/{}):'.format(EMPLOYEE_NAME,
          len(completed_tasks), len(tasks)))
    for t in completed_tasks:
        print('\t {}'.format(t['title']))
