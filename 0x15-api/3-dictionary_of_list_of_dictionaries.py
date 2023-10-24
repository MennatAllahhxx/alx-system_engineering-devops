#!/usr/bin/python3
"""3-dictionary_of_list_of_dictionaries module"""

import json
import requests


def emp_info_json_dict():
    """for a given users, returns information about progress"""
    api_url = 'https://jsonplaceholder.typicode.com'
    usrs = requests.get(f'{api_url}/users').json()
    usrs_tasks = {}

    for usr in usrs:
        usr_id = usr.get('id')
        usr_name = usr.get('username')
        tasks = requests.get(f'{api_url}/users/{usr_id}/todos').json()
        tasks_dict = []

        for task in tasks:
            tasks_dict.append({'username': usr_name,
                               'task': task.get('title'),
                               'completed': task.get('completed')
                               })

        usrs_tasks[usr_id] = tasks_dict

    filename = f'todo_all_employees.json'

    with open(filename, mode='w') as f:
        json.dump(usrs_tasks, f)


if __name__ == '__main__':
    emp_info_json_dict()
