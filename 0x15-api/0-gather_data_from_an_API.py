#!/usr/bin/python3
"""0-gather_data_from_an_API module"""

import requests
import sys


def emp_info():
    """for a given ID, returns information about progress"""
    api_url = 'https://jsonplaceholder.typicode.com/users'
    usr_id = sys.argv[1]
    response = requests.get(f'{api_url}/{usr_id}')
    data = response.json()
    name = data.get('name')

    response = requests.get(f'{api_url}/{usr_id}/todos')
    data = response.json()

    tasks = []
    num_tasks = 0
    num_com_tasks = 0

    for task in data:
        num_tasks += 1
        if task.get('completed'):
            tasks.append(task.get('title'))
            num_com_tasks += 1

    print(f'Employee {name} is done with tasks\
({num_com_tasks}/{num_tasks}):')

    for task in tasks:
        print('\t {}'.format(task))


if __name__ == '__main__':
    emp_info()
